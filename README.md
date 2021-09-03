

---
# SIX DEGREES, an application

## History
While using Wikipedia as your main cited source is academically frowned upon, in this case the internet's "free encyclopedia" provides as good a description of the inspiration of this app as any I could provide:

> **_Six Degrees of Kevin Bacon_** or **_Bacon's Law_** is a parlor game where players challenge each other to arbitrarily choose an actor and then connect them to another actor via a film that both actors have appeared in together, repeating this process to try and find the shortest path that ultimately leads to prolific American actor Kevin Bacon. It rests on the assumption that anyone involved in the Hollywood film industry can be linked through their film roles to Bacon within six steps. The game's name is a reference to "six degrees of separation", a concept which posits that any two people on Earth are six or fewer acquaintance links apart.

<br>

## Core Functionality
This app was originally built as a project exploring the use of third-party API data to create content for a dynamic website. This current iteration involved a lot of technical developments but most imortantly it was a chance to go back and "gamify" the presentation of the data.

The process can either be started by entering in an actor's name manually or letting the app choose an actor at random. The first stage of information comes from the IMDB and is completed in two successive calls. The first uses the actor's name as a general search term and from the response the app extracts the IMDB actor id. This id allows a targeted search for the actor which includes a full filmography. The film history for a popular actor can often return many hundreds of items, most of which are not exactly what we need. The app uses an algorithm to filter down the filmography into a list of "legit" movies.

To achieve the functionality we need, the app must also provide a cast list for each movie. It is these cast lists that provide the links to actors propeling the game forward. This requires an additional call for data for each film in the filmography of an actor. For George Clooney or Julia Roberts you might need to make 40 or 50 calls for movie cast data. Our IMDB connection is limited to 4 calls/second which makes this process impossible using their public api. Instead we switch to the OMDB to query individual movies.

<br>


## Technologies Used
JavaScript, Node, React <br>
Python, Flask <br>
HTML, CSS <br>
deployed on Heroku with PostgreSql database

<br>

---
# USING THE APP
## VISIT THE LIVE DEPLOYMENT:
## [Play Six Degrees!](https://six-degrees-flask.herokuapp.com/landing)

<br>

## INSTALL THE APP LOCALLY
Frontend:
<br>
1. clone the repository onto your local machine
1. cd into the directory
1. yarn install
1. yarn start gets front-end running at localhost:3000
1. in the src/app.js file you can switch URL from remote backend to a local server running on your machine.

Note: API data (through the backend) can be overtaxed. If you're playing around, the random search button will always pull from the database so is preferable. Also, if just doing design or development adjustments, calling on actors you know are in the db will save the expense of gratuitous calls. 

Backend:
<be>
1. clone the repository on to your local machine
1. cd into directory
1. python3 -m venv venv
1. source venv/bin/activate 
<br>
(on windows machine: venv\Scripts\activate)
1. pip install -r requirements.txt
1.  flask run <br>
(starts dev server at localhost:5000)<br>
(landingpage for the app at /landing)



<br>

---
# ADDITIONAL DETAILS

## Credits

The **Six Degrees App** is developed by Blake Montgomery, a Chicago-based engineer. Blake recently finished _General Assembly's_ Software Engineering Intersive in August 2021. He got his start coding with Stanford's pandemic-inspired "Code in Place" and was proud to contribute to "Code in Place 2021" as a volunteer Section Leader. In a previous career, Blake was a theater artist and director specializing in original, ensemble-created productions. He is currently solidifying his knowledge with projects and continuing to deepen his understanding of CS fundamentals while seeking the elusive Junior Developer job. You can reach him at blakemontgomery312@gmail.com.

<br>

## Current Iteration: September 1, 2021
Beyond redesigning the user interface to amplify the "game" aspects of the app, the current iteration involved addressing some technical concerns. I had previously created a backend version of the app in order to store and protect the API keys used for data gathering. This was built in Python using the Flask micro-framework and served up a static html framework, populated by api data rendered using jQuery.

<br>
Technical Goals:<br>

    1) Build a separate front end allowing the presentation aspects to be separate from data and processing.
    
    2) Integrate a database into the backend to store actor/film data as it is received and to supply the data in a fashion that eliminates unnecessary API calls.


<br>


## Future Enhancements
All about the data! <br>
Separate the actor call and the movie calls. The separation of showing cast lists of movies from the existence of the movie card has already been achieved in the frontend; it still needs to be decoupled on the backend and a separate call from client to server put back into the code. This will slow down the rate at which movie calls are made. It also changes the game and makes the filmography browsing more of a game since cast lists are not automatically displayed.

The database is also building over time its actor-film table so the app can integrate that into the "featured cast" that we download from OMDB. Over time this should give us much deeper cast information beyond the three of four listed stars.

Further improvements to the game aspect can be expected as well as more technical work clarifying the codebase.

