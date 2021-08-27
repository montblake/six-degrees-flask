from app import app, db
from flask import render_template
from app.models import Actor, Film
import requests

IMDB_KEY = app.config['IMDB_KEY']
OMDB_KEY = app.config['OMDB_KEY']


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getactor/<actor_name>')
def get_actor(actor_name):
    # actor_info will be returned to frontend
    # properties: id, name, image_url, films
    actor_info = {}

    # is actor in the db?
    actor = search_db_for_actor(actor_name)

    if actor is not None:
        # actor is in DB
        # search was done using name. name must exist and can be set on actor_info
        actor_info['name'] = actor.name

        # which db fields need info, if any?
        need_id =  False
        need_image = False
        need_films = False
        if actor.id:
            need_id = True
        if actor.image_url:
            need_image = True
        if not len(actor.films) > 0:
            need_films = True

        # if info is needed, search imdb
        if need_id or need_image or need_films:
            imdb_actor = search_imdb_for_actor(actor_name)
          
            if need_id:
                actor.id = imdb_actor['id']
                
            if need_image:
                actor.image_url = imdb_actor['image_url']
          
            if need_films:
                for film in imdb_actor['filmography']:
                    target_film = Film.query.filter_by(id=film['id']).first()
                    if target_film is not None:
                        # add actor to film.cast
                        target_film.cast.append(actor)
                    else:
                        # create film, add actor to cast, add to db.session
                        target_film = Film(title=film['title'], id=film['id'].split('/')[2], image_url=film['image_url'], year=film['year'])
                        target_film.cast.append(actor)
                        db.session.add(target_film)
            # add all objects from db.session into db
            db.session.commit()
        
        actor_info['id'] = actor.id
        actor_info['name'] = actor.name
        actor_info['image_url'] = actor.image_url
        actor_info['filmography'] = []
        # make Film objects into python objects so they can be sent with json
        for film in actor.films:
            film_obj = {'title': film.title, 'id': film.id, 'year': film.year, 'image_url': film.image_url, 'featured_cast': film.featured_cast }
            actor_info['filmography'].append(film_obj)
        return actor_info

    else:
    # the actor is not in DB at all
        actor_info = search_imdb_for_actor(actor_name)
        new_actor = Actor(id=actor_info['id'], name=actor_info['name'], image_url=actor_info['image_url'])
        db.session.add(new_actor)
        db.session.commit()
        for film in actor_info['filmography']:
            film_in_db = Film.query.filter_by(id=film['id']).first()
            if film_in_db is None:
                if 'image_url' in film:
                    new_film = Film(title=film['title'], id=film['id'], year=film['year'], image_url=film['image_url'])
                else:
                    new_film = Film(title=film['title'], id=film['id'], year=film['year'])
                new_film.cast.append(new_actor)
                db.session.add(new_film)
            else:
                # if film IS in db, we still want to add actor to cast
                film_in_db.cast.append(new_actor)
        db.session.commit()
        return actor_info


@app.route('/getcast/<movie_id>')
def get_cast(movie_id):
    # try db
    film = Film.query.filter_by(id=movie_id).first()
    # if movie is in DB
    if film is not None:
        if not film.featured_cast:
            # search omdb for featured cast, add to db, and return
            api_film = get_film_from_api(movie_id)
            print('api_film:' ,api_film)
            film.featured_cast = api_film['Actors']
            db.session.commit()
        return film.featured_cast
    else:
        response = get_film_from_api(movie_id)
        film = Film(title=response["title"], id=response["id"], year=response["year"], featured_cast = response["Actors"])
        if "image" in response:
            film.image_url = response["image"]["url"]
        db.session.add(film)
        db.session.commit()
        return film.featured_cast


def get_film_from_api(movie_id):
    api_url = "https://www.omdbapi.com/?apikey=" + OMDB_KEY + "&i=" + movie_id
    response = requests.get(api_url)
    response = response.json()
    return response


def search_db_for_actor(actor_name):
    actor_split = actor_name.split(' ')
    search_name = ""
    for i in range(len(actor_split)):
        search_name += (actor_split[i][0].upper() + actor_split[i][1:])
        if i != len(actor_split) - 1:
            search_name += " "
    actor = Actor.query.filter_by(name=search_name).first()
    # if the name matches this will return the actor
    # if not this returns false
    return actor


def search_imdb_for_actor(actor_name):
    actor_info = {}
    # search takes in a name and from the response we extract actor_id
    imdb_url = "https://imdb8.p.rapidapi.com/auto-complete?q="
    api_url = imdb_url + actor_name
    headers = {"x-rapidapi-key": IMDB_KEY, "x-rapidapi-host": "imdb8.p.rapidapi.com"}
    response = requests.get(api_url, headers=headers)
    response = response.json()

    # check the response for the data we need
    # if false... most likely mispelling?
    if "d" in response:
        actor_info["id"] = response["d"][0]["id"]
        api_url = "https://imdb8.p.rapidapi.com/actors/get-all-filmography?nconst=" + actor_info["id"]
        response = requests.get(api_url, headers=headers)
        response = response.json()

        actor_info["name"] = response["base"]["name"]
        actor_info["image_url"] = response["base"]["image"]["url"]
        actor_info['filmography'] = []

        # this can be a function
        # make Film objects into python objects so they can be sent with json
        for film in narrow_films(response["filmography"]):
            if 'image_url' in film:
                film_obj = {'title': film['title'], 'id': film['id'].split("/")[2], 'year': film['year'], 'image_url': film['image_url']}
            else: 
                film_obj = {'title': film['title'], 'id': film['id'].split("/")[2], 'year': film['year']}
            actor_info['filmography'].append(film_obj)
        return actor_info

    else:
        print('error: ' + actor_name + ' not found.', response)
        return {'error': actor_name + ' not found. Try entering name again.', 'response': response}


def narrow_films(films_all):
    films_cut1 = []
    for film in films_all:
        if "titleType" in film:
            if film["titleType"] == "movie":
                films_cut1.append(film)
    
    films_cut2 = []
    for film in films_cut1:
        if "status" in film:
            if film["status"] == "released":
                films_cut2.append(film)

    films_cut3 = []    
    for film in films_cut2:
        if "category" in film:
            if (film["category"] == "actress" or film["category"] == "actor"):
                films_cut3.append(film)

    films_cut4 = []
    for film in films_cut3:
        if "billing" in film:
            films_cut4.append(film)

    filmography = []
    for film in films_cut4:
        film_slim = {"title": film["title"], "year": film["year"], "id": film["id"]}
        if "image" in film:
            film_slim["image_url"] = film["image"]["url"]
        
        filmography.append(film_slim)

    return filmography