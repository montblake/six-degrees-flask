# create <actor> with name
# imdb search with name
# imdb search with id
# make <actor>

# add <actor> to database

# turn <actor> into actor_info
# 

# info for both actor and film
# comes in two(?) forms
# from search and prepared to send off: objects (via json) or on the python end: dictionaries
# into and out of the database (which are different)
#
# info must be packaged to add to database.
# FOR ACTOR
# variable = Actor(name="some name", id="sm000012", image_url="", filmography=[list of film objects])
# when it is returned from db
# <Actor some name>
# which has .properties
# actor_info = {
#    "name": "some name",
#    "id": "sm0000012",
#    "image_url": "https://somethingsomethingsomething.com/image/lotsofcharacters123456789/here",
#    "filmography": [],
# }

# FILMs
# film_info = {
#   "title": "some title",
#   "id": "tt0003241",
#   "year": 2012,
#   "image_url": "https://somethingsomethingsomething.com/image/lotsofcharacters123456789/here",
#   "featured_cast": "Contains String, Three Actors, Sometimes Four"
# }

there is a third bit of information that you can use but also must take care to create/update
film-actor table. 
for any <film>, film.cast returns a list of <ACTORS> who are in the film
for any <ACTOR>, <ACTOR>.films returns a list of <FILMS> the <ACTOR> is in

making sure films exist in db when adding actor is important
you get filmography in second actor search...
first) narrow down filmography using algorithm
second) for each film, 
   

    (you could do a search for the film.cast at this point, but that is what is holding up game in current version)
    ( this is also what defines current database and api usage: take the time to get ALL of the information... shortest route to building up the db, but at cost of slowness when it does have to search AND and automatic vast amount of API calls to pay for)



    from two searches:
        actor_inf = {
            "name":,
            "id":,
            "image_url": "httosjasdj342j23kj34sa",
        }
    make actor object and add to database


    from 2nd search and film-algo:
        filmography = [
            {"title": "", "id": "", "image_url": "", "year": 2012 }
        ]    

    for each film in filmography:
        if film in db:
            if actor is NOT in film.cast:
            film.cast.append(actor)
        if film NOT in db:
            f = Film(title="some title", id="tt0023404", year=2012, image_url="hhtpssdlhsdj32n2.24.4")
            f.cast.append
        db.session.add(f)
        db.session.commit()

search with a name
search returns either error or an id

search with id
returns object with name, image_url, id, filmography
    filmography has everything except featured cast


you need to create the actor

