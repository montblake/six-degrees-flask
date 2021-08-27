// URL BASE SETTINGS for DEV and PROD
// const URL_BASE = "http://localhost:5000/"
const URL_BASE = "https://six-degrees-flask.herokuapp.com/"


// Create an ACTOR OBJECT to capture all relevant data
let actorObject = [
    {
        name: "",
        image: "",
        id: "",
        filmography: [],
    },
    {
        name: "",
        image: "",
        id: "",
        filmography: [],
    },
    {
        name: "",
        image: "",
        id: "",
        filmography: [],
    },
    {
        name: "",
        image: "",
        id: "",
        filmography: [],

    },
    {
        name: "",
        image: "",
        id: "",
        filmography: [],
    },
    {
        name: "",
        image: "",
        id: "",
        filmography: [],
    },
    {
        name: "",
        image: "",
        id: "",
        filmography: [],
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

const $endpoint1 = $('#endpoint1');
const $endpoint2 = $('#endpoint2');
const $endpoint3 = $('#endpoint3');
const $bgImage = $('body')


// FUNCTIONS
function changeEndpoint(actor){
    $.ajax({url: `${URL_BASE}search/${actor}`})
    .then(response => {
        $endpoint1.text(response.name);
        $endpoint2.text(response.name);
        $endpoint3.text(response.name.split(' ')[0]);
        $bgImage.css("background-image", `url(${response.image_url})`);  
    })
}

function changeColorScheme(color){
    document.body.style.setProperty('--accent-color', color);
}



function getActorId(settings) {
    settings => $.ajax(settings);
}


function resetActorObject() {
    actorObject = [
        {
            name: "",
            image: "",
            id: "",
            filmography: [],
        },
        {
            name: "",
            image: "",
            id: "",
            filmography: [],
        },
        {
            name: "",
            image: "",
            id: "",
            filmography: [],
        },
        {
            name: "",
            image: "",
            id: "",
            filmography: [],
        },
        {
            name: "",
            image: "",
            id: "",
            filmography: [],
        },
        {
            name: "",
            image: "",
            id: "",
            filmography: [],
        },
    ];
}


function setActorInfo(response) {
    actorObject[actorIndex].image = response.image_url;
    actorObject[actorIndex].name = response.name;
    actorObject[actorIndex].filmography = response.filmography;
    actorObject[actorIndex].id = response.id;
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
// This needs to be updated with an ONSCREEN MESSAGE
function handleFailure(){
    console.log('Operation failed');
}


//  Used to reset form to initial state.
function handleReset(){
    location.reload(true);
}

function getCast(film){
    $.ajax({url: `${URL_BASE}getcast/${film.id}`})
    .then(response => {
        film.featured_cast = response.split(', ');
        renderFilm(film);
    });
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

    actorObject[actorIndex].filmography.forEach(film => {
        getCast(film);
    });
        
    $filmHdr.text(`The Films of ${actorObject[actorIndex].name} (${actorObject[actorIndex].filmography.length})`);
    $filmography.append($filmStrip);
    $filmography.append($filmHdr);
    $filmography.show(1000);  
};


// Initiates Search Process from Clicking in Cast List
function handleChoice(){
    actorIndex++;
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


// send search term to localhost:5000/search
// either add search term to address bar or include in body
// search route should not render anything, simply return json
function search(normalizedInput){
    $.ajax({url: `${URL_BASE}getactor/${normalizedInput}`})
    .then(response => {
        setActorInfo(response);
        let $pic = $(`#actor-img${actorIndex}`);
        let $nameTag = $(`#actor-card${actorIndex} h3`);
        $pic.attr('src', actorObject[actorIndex].image);
        $nameTag.text(actorObject[actorIndex].name);
        $inputForm.hide();
        $initialInstructions.hide();
        $confirmationForm.show();
        $featuredText.show(1000);
    });   
}


//  RENDER FILM CARDS TO FILMOGRAPHY SECTION
function renderFilm(film){
    let $filmCastUl = $('<ul></ul>');
    film.featured_cast.forEach(function(member) {
        let $castLi = $(`<li>${member}</li>`);
        $filmCastUl.append($castLi);
    });
    
    let $textCtr = $(`<div class="text-ctr">
                            <h4>${film.title}</h4>
                            <h5>${film.year}</h5>
                            <div class="movie-pic-frame">
                                <img class="movie-pic" src="${film.image_url}"/>
                            </div>
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