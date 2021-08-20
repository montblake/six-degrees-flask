# Six Degrees of Kevin Bacon
## History
While using Wikipedia as your main cited source is academically frowned upon, in this case the internet's "free encyclopedia" provides as good a description of the inspiration of this app as any I could provide:

> **_Six Degrees of Kevin Bacon_** or **_Bacon's Law_** is a parlor game where players challenge each other to arbitrarily choose an actor and then connect them to another actor via a film that both actors have appeared in together, repeating this process to try and find the shortest path that ultimately leads to prolific American actor Kevin Bacon. It rests on the assumption that anyone involved in the Hollywood film industry can be linked through their film roles to Bacon within six steps. The game's name is a reference to "six degrees of separation", a concept which posits that any two people on Earth are six or fewer acquaintance links apart.

<br>

## The App
The application I've created begins with a user entering the name of an actor into a text field and submitting it to the browser via pressing "return" or clicking a submit button. The app uses this entry as a general search term to submit to the **IMDB** through an api in order to get that database's official ID number for that actor. That ID is used to execute a second search which returns name, image, and filmography info which the app then stores in memory.

The user is presented with the name and image of an actor and is asked to confirm whether this is their desired starting point. If not, the initial search field is presented again. If this is the desired starting point, upon clicking the confirm button, the app uses an algorythm to process the full list of movie titles down to major motion picture releases only. (With a major star this generally is reducing an array of 500 titles to something in the range of 40 - 50 titles.) The app then uses each of these titles as the parameter for a new search connecting to the **OMDB** which it uses to return and store cast information for each film. 

The cast information for the actor's filmography is used to select one new actor... and the process repeats itself.
The user has six tries to successfully connect their starting point to Kevin Bacon. There is a reset button which can be used at any point to start a new game.

<br>

## Technologies Used
The app is made with HTML, CSS, JavaScript, and jQuery.

<br>

## Getting Started
As an web-based app, the interface should be straight-forward enough to use without any special instructions. However, it is perhaps not clear enough that the filmography section when it arrives can be scrolled horizontally.There have also been some issues with funcitonality of onscreen error messages; for the time being, you will find errors on the console. 

Project deployed: 05/28/21

[Six Degrees... can be found on GitHub pages](https://montblake.github.io/degrees-bacon/)

<br>

## Future Enhancements
Currently, the application's code is built to allow for the consumption of the necessary APIs and the use of jQuery to render data to the DOM for the main functions: actor ID search, full actor info and filmography search, and to obtain the cast lists of an actor's entire career of films. We switch to the OMDB from the IMDB for the final step due to current financial considerations. Eventually the app could invest in greater IMDB access to allow for full cast lists for each movie instead of just the four featured performers from each film.

More important in the short term is making sure that the actor selection and information delivery process can be looped the required number of times and that winning/losing game logic can be applied. Until that functionality is achieved, the app functions more as a way to explore a specific actors filmography than as a means to reach Kevin Bacon.

Thinking more about the gamification of the app,  I believe the design needs to shift the focus more onto the numbers: how many attemtps remain to connect to Kevin Bacon?! Also, perhaps you could choose to either begin by entering an actor (as is currently the case) or the computer could randomly choose an actor from the IMDB and present the user with a challenge. It might be fun to allow the user to change the end goal actor. So we could instead play Six Degrees of Cate Blanchett or Six Degrees of Idris Elba.

<br>

## Wire-Frames and Visual Development
Here are a visual reference and a collection of wire-frame illustrations of the app to give a sense of what it looks like and how it will function. 

![wireframe collection](readme-resources/degrees-wireframe-collection.png)

![visual reference 2](readme-resources/six-degrees-welcome.png)

![reference responsive](readme-resources/narrow-bacon.png)

![wireframe #1](readme-resources/degrees-wireframe1.png)

![wireframe #2](readme-resources/degrees-wireframe2.png)

![wireframe #3](readme-resources/degrees-wireframe3.png)

![wireframe #4](readme-resources/degrees-wireframe4.png)

![wireframe #7](readme-resources/degrees-wireframe7.png)

![wireframe #9](readme-resources/degrees-wireframe9.png)

![iPhone responsive](readme-resources/skinny-bacon.png)