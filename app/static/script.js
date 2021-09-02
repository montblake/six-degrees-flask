const $gameButton = $('#btn-game');
const $projectButton = $('#btn-project');
const $techButton = $('#btn-tech');

const $gameSect = $('#the-game');
const $projectSect = $('#the-project');
const $techSect = $('#the-techs');

$projectSect.hide();
$techSect.hide();

$gameButton.on('click', handleClick);
$projectButton.on('click', handleClick);
$techButton.on('click', handleClick);

function handleClick(event) {
    if (event.target.innerHTML === "The Game") {
        $gameButton.css("border-left",'1px solid orange');
        $projectButton.css("border-left",'none');
        $techButton.css("border-left",'none');
        console.log(event.target.innerHTML);
        $gameSect.show();
        $projectSect.hide();
        $techSect.hide();
    } else if (event.target.innerHTML === "The Project") {
        $gameButton.css("border-left",'none');
        $projectButton.css("border-left",'1px solid orange');
        $techButton.css("border-left",'none');
        console.log(event.target.innerHTML);
        $gameSect.hide();
        $projectSect.show();
        $techSect.hide();
    } else {
        console.log(event.target.innerHTML);
        $gameButton.css("border-left",'none');
        $projectButton.css("border-left",'none');
        $techButton.css("border-left",'1px solid orange');
        $gameSect.hide();
        $projectSect.hide();
        $techSect.show();
    }
}
