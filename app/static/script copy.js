// const IMDB_KEY = "bffc00bf41mshb25f975275b6b40p19ecc6jsn9bced5cedcf9";
// const OMDB_KEY = "e3567fae";


// Create an ACTOR OBJECT to capture all relevant data
let actorObject = [
    {
        name: "",
        image: {url:""},
        imdbId: "",
        filmsRaw: [],
        filmsSelected: [],
        filmObjectArray: [],
    },
    {
        name: "",
        image: {url:""},
        imdbId: "",
        filmsRaw: [],
        filmsSelected: [],
        filmObjectArray: [],
    },
    {
        name: "",
        image: {url:""},
        imdbId: "",
        filmsRaw: [],
        filmsSelected: [],
        filmObjectArray: [],
    },
    {
        name: "",
        image: {url:""},
        imdbId: "",
        filmsRaw: [],
        filmsSelected: [],
        filmObjectArray: [],
    },
    {
        name: "",
        image: {url:""},
        imdbId: "",
        filmsRaw: [],
        filmsSelected: [],
        filmObjectArray: [],
    },
    {
        name: "",
        image: {url:""},
        imdbId: "",
        filmsRaw: [],
        filmsSelected: [],
        filmObjectArray: [],
    },
    {
        name: "",
        image: {url:""},
        imdbId: "",
        filmsRaw: [],
        filmsSelected: [],
        filmObjectArray: [],
    },
];

let progressArray = [
    {actorA:"", actorB:"", film:""},
    {actorA:"", actorB:"", film:""},
    {actorA:"", actorB:"", film:""},
    {actorA:"", actorB:"", film:""},
    {actorA:"", actorB:"", film:""},
    {actorA:"", actorB:"", film:""},
    {actorA:"", actorB:"", film:""},
    {actorA:"", actorB:"", film:""},
]

let userInput, normalizedInput;
let actorIndex = 0;
let currentPic, currentTag;


// CACHED OBJECTS
const $inputFld = $('#input-fld');
const $inputBtn = $('#input-btn');
const $inputForm = $('#user-input');

const $featuredText = $('#featured-text');
const $initialInstructions = $('#initial-instructions');
const $confirmationForm = $('#confirmation-form');
const $confirmationBtn = $('#confirmation-btn');
const $resetBtnBdy = $('#reset-btn-body');
const $resetBtnHdr = $('#reset-btn-hdr');

const $filmography = $('#filmography');
const $filmHdr = $("<h2 class='films-header'></h2>");
const $filmStrip = $("<div id=film-strip></div>");

const $num1 = $('#num-one');
const $num2 = $('#num-two');
const $num3 = $('#num-three');
const $num4 = $('#num-four');
const $num5 = $('#num-five');
const $num6 = $('#num-six');

const $progress = $('#degree-progress');
const $progressOl = $('#degree-progress ol');


// FUNCTIONS
function getActorId(settings) {
    settings => $.ajax(settings);
}


function resetActorObject() {
    actorObject = [
        {
            name: "",
            image: "",
            imdbId: "",
            filmsRaw: [],
            filmsSelected: [],
            filmObjectArray: [],
        },
        {
            name: "",
            image: "",
            imdbId: "",
            filmsRaw: [],
            filmsSelected: [],
            filmObjectArray: [],
        },
        {
            name: "",
            image: "",
            imdbId: "",
            filmsRaw: [],
            filmsSelected: [],
            filmObjectArray: [],
        },
        {
            name: "",
            image: "",
            imdbId: "",
            filmsRaw: [],
            filmsSelected: [],
            filmObjectArray: [],
        },
        {
            name: "",
            image: "",
            imdbId: "",
            filmsRaw: [],
            filmsSelected: [],
            filmObjectArray: [],
        },
        {
            name: "",
            image: "",
            imdbId: "",
            filmsRaw: [],
            filmsSelected: [],
            filmObjectArray: [],
        },
    ];
}


function setActorInfo(response) {
    actorObject[actorIndex].image = response.base.image;
    actorObject[actorIndex].name = response.base.name;
    actorObject[actorIndex].filmsRaw = response.filmography;
}


function displayProgress() {
    if (actorIndex === 0) return;
    let $progressLi = $(`<li>${progressArray[actorIndex].actorA} worked with ${progressArray[actorIndex].actorB} on the film <span>${progressArray[actorIndex].film}</span></li>`);
    $progressOl.append($progressLi);
    $progressOl.show(1000)
    $progress.show(1000);
    $featuredText.show(1000);
    
}

function updateProgress($actorLink) {
    progressArray[0].actorB = actorObject[0].name;
    progressArray[1].actorA = actorObject[0].name;
    if (actorIndex === 0) {
        return;
    } else {
        progressArray[actorIndex].actorB = $actorLink.text();
        progressArray[actorIndex+1].actorA = $actorLink.text();
        progressArray[actorIndex].film = $actorLink.parents('.text-ctr').children('h4').text();
    }
    
}


function changeNumberDisplay() {
    if (actorIndex === 0) {
        $num1.css('visibility', 'hidden');
        $num2.css('visibility', 'hidden');
        $num3.css('visibility', 'hidden');
        $num4.css('visibility', 'hidden');
        $num5.css('visibility', 'hidden');
        $num6.css('visibility', 'hidden');
    } else if (actorIndex === 1) {
        $num1.css('visibility', 'visible');
        $num2.css('visibility', 'hidden');
        $num3.css('visibility', 'hidden');
        $num4.css('visibility', 'hidden');
        $num5.css('visibility', 'hidden');
        $num6.css('visibility', 'hidden');
    } else if (actorIndex === 2) {
        $num1.css('visibility', 'visible');
        $num2.css('visibility', 'visible');
        $num3.css('visibility', 'hidden');
        $num4.css('visibility', 'hidden');
        $num5.css('visibility', 'hidden');
        $num6.css('visibility', 'hidden');
    } else if (actorIndex === 3) {
        $num1.css('visibility', 'visible');
        $num2.css('visibility', 'visible');
        $num3.css('visibility', 'visible');
        $num4.css('visibility', 'hidden');
        $num5.css('visibility', 'hidden');
        $num6.css('visibility', 'hidden');
    } else if (actorIndex === 4) {
        $num1.css('visibility', 'visible');
        $num2.css('visibility', 'visible');
        $num3.css('visibility', 'visible');
        $num4.css('visibility', 'visible');
        $num5.css('visibility', 'hidden');
        $num6.css('visibility', 'hidden');
    } else if (actorIndex === 5) {
        $num1.css('visibility', 'visible');
        $num2.css('visibility', 'visible');
        $num3.css('visibility', 'visible');
        $num4.css('visibility', 'visible');
        $num5.css('visibility', 'visible');
        $num6.css('visibility', 'hidden');
    } else {
        $num1.css('visibility', 'visible');
        $num2.css('visibility', 'visible');
        $num3.css('visibility', 'visible');
        $num4.css('visibility', 'visible');
        $num5.css('visibility', 'visible');
        $num6.css('visibility', 'visible');
    }
}


//  HANDLING FAILED OPERATION
function handleFailure(){
    console.log('Operation failed');
}


//  Used to reset form to initial state.
function handleReset(){
    location.reload(true);
}

// Confirms Name and Image refer to intended actor
// also, takes this moment to cut down initial list of films to selected ones
function handleConfirm(event){
    event.preventDefault();
    $filmography.hide(1000);
    $filmStrip.empty();
    $confirmationForm.hide(1000);
    $featuredText.hide(1000);
    $resetBtnHdr.show(1000);
    changeNumberDisplay();
    displayProgress();

    // process the list from raw to selected
    actorObject[actorIndex].filmsRaw.forEach(function(film) {
        if (film.titleType === "movie" 
        && film.status === "released" 
        && (film.category === "actor" || film.category === "actress")
        && film.billing) {
            actorObject[actorIndex].filmsSelected.push(film);
        }
    });
    // SETS ACTOROBJECT information for Filmography
    actorObject[actorIndex].filmsSelected.forEach(function(film) {
        let filmObject = {};
        filmObject.title = film.title;
        filmObject.year = film.year;
        filmObject.id = film.id;
        $.ajax({ url: `https://www.omdbapi.com/?i=tt3896198&apikey=${OMDB_KEY}&t=${filmObject.title}` })
        .then(function(response) {
            filmObject.cast = response["Actors"];
            filmObject.cast = filmObject.cast.split(', ');
            actorObject[actorIndex].filmObjectArray.push(filmObject);
            renderFilm(filmObject);
        });
    });
    $filmHdr.text(`The Films of ${actorObject[actorIndex].name}`);
    $filmography.append($filmStrip);
    $filmography.append($filmHdr);
    $filmography.show(1000);  
    actorIndex++;
}


// Initiates Search Process from Clicking in Cast List
function handleChoice(){
    let $actorLink = $(this);
    updateProgress($actorLink);
    // Update Progress
    
    // Process Clicked Name
    userInput = $actorLink.text();
    normalizedInput = userInput.toLowerCase().replace(' ', '%20');
    search(normalizedInput);
}

//  Initiates Search Process from Entering Text in Search Field
function handleInput(event) {
        // calling preventDefault() on a 'submit' event will prevent a page refresh  
        event.preventDefault();
        // getting the user input
        userInput = $inputFld.val();
        normalizedInput = userInput.toLowerCase().replace(' ', '%20');
        search(normalizedInput);
}

// Two Phase search.
//  First using general terms to get IMDB Actor Id 
//  Second using Actor ID to get Name, Image, 
function search(normalizedInput){
    // USE INPUT TO SET SEARCH SETTINGS OBJECT
    const settings = {
        "url": `http://localhost:5000/search/${normalizedInput}`,
        "method": "POST",
    };
    // DO THE ACTUAL SEARCH
    $.ajax(settings)
    .then(response => {
        setActorInfo(response);
        let $pic = $(`#actor-img${actorIndex}`);
        let $nameTag = $(`#actor-card${actorIndex} h3`);
        $pic.attr('src', actorObject[actorIndex].image.url);
        $nameTag.text(actorObject[actorIndex].name);
        $inputForm.hide();
        $initialInstructions.hide();
        $confirmationForm.show();
        $featuredText.show(1000);
    });
}


//  RENDER FILM CARDS TO FILMOGRAPHY SECTION
function renderFilm(filmObject){
    let $filmCastUl = $('<ul></ul>');
    filmObject.cast.forEach(function(member) {
        let $castLi = $(`<li>${member}</li>`);
        $filmCastUl.append($castLi);
    });
    
    let $textCtr = $(`<div class="text-ctr">
                            <h4>${filmObject.title}</h4>
                            <h5>${filmObject.year}</h5>
                        </div>`);
    $textCtr.append($filmCastUl);
    let $filmCard = $('<div class="film-card"></div>');
    $filmCard.append($textCtr);
    $filmStrip.append($filmCard);

}


// EVENT HANDLERS
$inputForm.on('submit', handleInput);
$confirmationBtn.on('click', handleConfirm);
$resetBtnBdy.on('click', handleReset);
$resetBtnHdr.on('click', handleReset);
$filmography.on('click', 'div.text-ctr li', handleChoice);


// Immediate Action
$filmography.hide();