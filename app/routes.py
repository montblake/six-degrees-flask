from requests.models import Response
from app import app, db
from flask import render_template
from app.models import Actor, Film
import requests
import random

IMDB_KEY = app.config['IMDB_KEY']
OMDB_KEY = app.config['OMDB_KEY']


######################################################
### ROUTES
######################################################
@app.route('/landing')
def index():
    return render_template('index.html')


@app.route('/getrandomactor')
def get_random_actor():
    print("Get random!")
    actor_info = {}
    actors = Actor.query.all()
    actor = random.choice(actors)
    print('updating actor')
    updated_actor = update_actor_object(actor)
    print('turning actor into a dictionary')
    actor_info = actor_object_into_dict(updated_actor)
    return actor_info


@app.route('/getactor/<actor_name>')
def get_actor(actor_name):
    # is actor in the db?
    print('searching db for', actor_name)
    actor = search_db_for_actor(actor_name)
   
    if actor is not None:
        print(actor.name +  " is in the db")
        updated_actor = update_actor_object(actor)
        print("updating actor object")
    else:
       print(actor_name, " NOT in db")
       new_actor = create_new_actor(actor_name)
       print('create new actor')
       updated_actor = update_actor_object(new_actor)
       print('update actor object')
    actor_info = actor_object_into_dict(updated_actor)
    print('actor object into dictionary')
    return actor_info
    


######################################################
### SUPPORTING FUNCTIONS FOR ACTOR
######################################################
def create_new_actor(actor_name):
    print("initiating imdb search")
    response = search_imdb_with_name(actor_name)
    
    if "d" in response:
        print(response)
        actor_id = response["d"][0]["id"]
        if 'name' in response["d"][0]:
             name = response["d"][0]["name"]
        else:
            name = response["d"][0]["l"]
        
        print("first search returned actor id: ", actor_id, name)

        new_actor = Actor(id=actor_id)
        db.session.add(new_actor)
        db.session.commit()
        
        actor_object = Actor.query.filter_by(id=actor_id).first()
        return actor_object

    else:
        print('Actor not found. Response: ', response)
        return({'Response': response})


def update_actor_object(actor):
    # assume nothing needs updating
    films_needed=False
    image_needed=False
    name_needed=False
    
    if actor.name:
        print('name. check.')
    else:
        name_needed = True
        print('no name')
    if actor.id:
        print('id. check.')
    else:
        print('no id')
    if actor.image_url:
        print('image. check.')
    else:
        image_needed = True
        print('no image')
    if len(actor.films) < 5:
        films_needed = True
        print('all films NEEDED')
    else:
        print('len(films). check.')
    # for film in actor.films:
    #     if not film.featured_cast:
    #         films_needed = True
    #         print('featured cast NEEDED')
    #     else:
    #         print('featured casts. check')

    # Update the simple things if needed
    if films_needed or image_needed or name_needed:
        print('addressing need')
        response = search_imdb_with_id(actor.id)
        if image_needed:
            actor.image_url = response["base"]["image"]["url"]
        if name_needed:
            actor.name = response["base"]["name"] 
        
        # all films in this actor filmography must be checked against the database
        # if they exist, they will be updated (if necessary)
        # if they don't exist, they will be created, then updated

        legit_films = narrow_films(response["filmography"])
        process_all_films(legit_films, actor)
        # for all films you must make sure actor is linked to it. it will be included...
        # also film must have featured_cast

        updated_actor = Actor.query.filter_by(id=actor.id).first()
        return updated_actor
    else:
        return actor


######################################################
### Supporting Functions for Films
######################################################
def process_all_films(films, actor):
    print('processing_all_films for', actor.name)
    for film in films:
        print("film: ", film)
        db_film = Film.query.filter_by(id=film['id']).first()
        print("processing film: db film")
        if db_film is None:
            new_film = make_film_object(film)
            updated_film = update_film_object(new_film, actor)
        else:
            updated_film = update_film_object(db_film, actor)

                
def update_film_object(film, actor):
    # print('Updating Film OBJECT')
    # if not film.featured_cast:
    #     featured_cast = get_featured_cast(film.id)
    #     film.featured_cast = featured_cast
    #     db.session.commit()
    #     print('add feature cast')

    # if current actor object isn't on cast list, ADD current actor object to cast list and commit object to db????
    if actor not in film.cast:
        film.cast.append(actor)
        db.session.commit()
        print('add actor to cast')
    return film


def make_film_object(film):
    print('making FILM OBJECT', film)
    # They must be turned into python dictionaries before sending
    query_film = Film.query.filter_by(id=film['id'].split('/')[2]).first()
    if query_film is not None:
        return query_film
    else:
        film_obj = Film(title=film['title'], id=film['id'].split('/')[2], year=film['year'])
        if 'image' in film:
            film_obj['image_url'] = film['image']['url']
        db.session.add(film_obj)
        db.session.commit()
        new_film = Film.query.filter_by(id=film['id'].split('/')[2]).first()
        return new_film


    
######################################################
### Supporting Functions for ACTOR OBJECTS
######################################################
def actor_object_into_dict(actor):
    # TAKES IN A ACTOR object (the form of the db information)
    print(actor)
    print(actor.name)
    print(actor.films)
    actor_info = {}
    actor_info['name'] = actor.name
    actor_info['id'] = actor.id
    actor_info['image_url']= actor.image_url
    actor_info['filmography'] = []

    legit_films = actor.films
    for film in legit_films:
        film_obj = {'title': film.title, 'id': film.id, 'year': film.year}
        if film.image_url:
            film_obj['image_url'] = film.image_url
        if film.featured_cast:
            film_obj['featured_cast'] = film.featured_cast
        actor_info['filmography'].append(film_obj)
    # FUNCTION TURNS ACTOR object into python dictionary 
    # which when returned to frontend automatically becomes json
    return actor_info
    


##########################################################################
# LOCAL DB SEARCHES
##########################################################################
def search_db_for_actor(actor_name):
    search_name = prep_name_for_search(actor_name)
    actor = Actor.query.filter_by(name=search_name).first()
    # if the name matches this will return the actor
    # if not this returns None
    # actor is an Actor Object from DB
    return actor

# ENSURES capitalization of entry to match condition of our DB
def prep_name_for_search(actor_name):
    actor_split = actor_name.split(' ')
    search_name = ""
    for i in range(len(actor_split)):
        search_name += (actor_split[i][0].upper() + actor_split[i][1:])
        if i != len(actor_split) - 1:
            search_name += " "
    return search_name



##########################################################################
# IMDB SEARCHES
##########################################################################
def search_imdb_with_name(actor_name):
    # search takes in a name and from the response we extract actor_id
    imdb_url = "https://imdb8.p.rapidapi.com/auto-complete?q="
    api_url = imdb_url + actor_name
    headers = {"x-rapidapi-key": IMDB_KEY, "x-rapidapi-host": "imdb8.p.rapidapi.com"}
    response = requests.get(api_url, headers=headers)
    response = response.json()
    return response
    

def search_imdb_with_id(actor_id):
    api_url = "https://imdb8.p.rapidapi.com/actors/get-all-filmography?nconst=" + actor_id
    headers = {"x-rapidapi-key": IMDB_KEY, "x-rapidapi-host": "imdb8.p.rapidapi.com"}
    response = requests.get(api_url, headers=headers)
    response = response.json()
    return response



########################################################################################
#  OMDB SEARCH for FILM CASTS
########################################################################################
def get_featured_cast(movie_id):
    api_url = "https://www.omdbapi.com/?apikey=" + OMDB_KEY + "&i=" + movie_id
    response = requests.get(api_url)
    response = response.json()
    print(response)
    featured_cast = response["Actors"]
    return featured_cast


########################################################################################
# "ALGORITHM"  TO PROCESS/DISPLAY ONLY "LEGIT" FILMS
########################################################################################
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
    return films_cut4
    
def build_filmography(films_cut):
    filmography = []
    for film in films_cut:
        film_slim = {"title": film["title"], "year": film["year"], "id": film["id"]}
        if "image" in film:
            film_slim["image_url"] = film["image"]["url"]
        if "featured_cast" in film:
            film_slim["featured_cast"] = film["featured_cast"]
        filmography.append(film_slim)
    return filmography
