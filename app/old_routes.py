from app import app, db
from flask import render_template
from app.models import Actor, Film
import requests

IMDB_KEY = app.config['IMDB_KEY']
OMDB_KEY = app.config['OMDB_KEY']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getactor/<actor>')
def get_actor(actor):
    actor_info = search_db_for_actor(actor)
    if actor_info is None:
        actor_info = search_imdb_for_actor(actor)
    return actor_info


@app.route('/getcast/<movie_id>')
def get_cast(movie_id):
    film = Film.query.filter_by(id=movie_id).first()
    # if movie is in DB
    if film is not None:
        # if all relevant info, return info
        if film.title and film.year:
           print('title and year exist')
        else:
            print('need title or year')
        if film.image_url:
            print('image exists')
        else:
            print('sorry, no image')
        if film.featured_cast:
            return film
        else:
            # search omdb for featured cast, add to db, and return
            featured_cast = get_cast_from_api(movie_id)
            film.featured_cast = featured_cast
            db.session.add(film)
            db.session.commit()
            return film
    else:
        print('that film is not in the db')
        film = get_film_from_api(movie_id)
        db.session.add(film)
        db.session.commit()
        return film



# HELPER FUNCTIONS
def get_cast_from_api(movie_id):
    api_url = "https://www.omdbapi.com/?apikey=" + OMDB_KEY + "&i=" + movie_id
    # api_url = "https://imdb8.p.rapidapi.com/title/get-full-credits?tconst=" + movie_id
    # headers = {
    # 'x-rapidapi-host': "imdb8.p.rapidapi.com",
    # 'x-rapidapi-key': IMDB_KEY
    # }
    response = requests.get(api_url)
    response = response.json()
    featured_cast = response['Actors']
    return featured_cast





def actor_in_db(actor_name):
    actor_split = actor_name.split(' ')
    search_name = ""
    for i in range(len(actor_split)):
        search_name += (actor_split[i][0].upper() + actor_split[i][1:])
        if i != len(actor_split) - 1:
            search_name += " "
    actor = Actor.query.filter_by(name=search_name).first()
    return actor

def search_db_for_actor(actor):
    # check if actor is in db
    target = actor_in_db(actor)
    if target:
        print("ACTOR FOUND IN DATABASE!!!!!!!!!")
        actor_info = {}
               
        if target.id and target.name and target.image_url and len(target.films) > 0:
            actor_info['id'] = target.id
            actor_info['name'] = target.name
            actor_info['image_url'] = target.image_url
            actor_info['filmography'] = target.films
            return actor_info

        elif target.id and target.name and target.image_url:
            actor_info['id'] = target.id
            actor_info['name'] = target.name
            actor_info['image_url'] = target.image_url
            # search imdb for filmography
            api_url = "https://imdb8.p.rapidapi.com/actors/get-all-filmography?nconst=" + actor_info["id"]
            headers = {"x-rapidapi-key": IMDB_KEY, "x-rapidapi-host": "imdb8.p.rapidapi.com"}
            response = requests.get(api_url, headers=headers)
            response = response.json()
            actor_info["filmography"] = narrow_films(response['filmography'])

            # create films and add actor to cast
            for film in actor_info["filmography"]:
                new_film = Film.query.filter_by(id=film.id).first()
                if new_film is None:
                    new_film = Film(id=film['id'], title=film['title'], year=film['year'], image_url=film['image_url'])
                    new_film.cast.append(target)
                    db.session.add(new_film)
                    db.session.commit()
            return actor_info

        else:
            print("Not all three")
            # search imdb for actor and UPDATE db
            # set actor_info and return it
    else:
        #actor not in db at all
        print("MUST SEARCH IMDB")
        search_imdb_for_actor(actor)

def search_imdb_for_actor(actor):
    print('searching IMDB')
    actor_info = {}
    # This first search takes in a name and from the response we extract actor_id
    imdb_url = "https://imdb8.p.rapidapi.com/auto-complete?q="
    api_url = imdb_url + actor
    headers = {"x-rapidapi-key": IMDB_KEY, "x-rapidapi-host": "imdb8.p.rapidapi.com"}
    response = requests.get(api_url, headers=headers)
    response = response.json()
    if response["d"]:
        actor_info["id"] = response["d"][0]["id"]
        api_url = "https://imdb8.p.rapidapi.com/actors/get-all-filmography?nconst=" + actor_info["id"]
        response = requests.get(api_url, headers=headers)
        response = response.json()

        actor_info["name"] = response["base"]["name"]
        actor_info["image_url"] = response["base"]["image"]["url"]
        actor_info["filmography"] = narrow_films(response["filmography"])
        a = Actor(id=actor_info["id"], name=actor_info["name"], image_url=actor_info["image_url"])
        db.session.add(a)
        db.session.commit()
        
        for film in actor_info["filmography"]:
            new_film = Film(id=film['id'].split('/')[2], title=film['title'], year=film['year'], image_url=film['image_url'])
            new_film.cast.append(a)
            db.session.add(new_film)
        db.session.commit()
        return actor_info
    else:
        print('sorry, actor not found')


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
