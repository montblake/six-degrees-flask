from app import app
from flask import render_template
import requests

IMDB_KEY = app.config['IMDB_KEY']
OMDB_KEY = app.config['OMDB_KEY']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<actor>')
def search(actor):
    actor_info = {
        "id": "",
        "name": "",
        "image_url": "",
        "filmography": []
    }

    imdb_url = "https://imdb8.p.rapidapi.com/auto-complete?q="
    actor = actor
    api_url = imdb_url + actor
    headers = {"x-rapidapi-key": IMDB_KEY, "x-rapidapi-host": "imdb8.p.rapidapi.com"}
    response = requests.get(api_url, headers=headers)
    response = response.json()
    actor_info["id"] = response["d"][0]["id"]
    api_url = "https://imdb8.p.rapidapi.com/actors/get-all-filmography?nconst=" + actor_info["id"]
    response = requests.get(api_url, headers=headers)
    response = response.json()
    actor_info["id"] = response["base"]["id"]
    actor_info["name"] = response["base"]["name"]
    actor_info["image_url"] = response["base"]["image"]["url"]
    films_all = response["filmography"]

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

    for film in films_cut4:
        film_slim = {"title": film["title"], "year": film["year"], "id": film["id"]}
        if "image" in film:
            film_slim["image_url"] = film["image"]["url"]
        actor_info["filmography"].append(film_slim)

    return actor_info

@app.route('/getcast/<movie_id>')
def getcast(movie_id):
    api_url = "https://www.omdbapi.com/?apikey=" + OMDB_KEY + "&i=" + movie_id
    response = requests.get(api_url)
    response = response.json()
    print(response)
    return response