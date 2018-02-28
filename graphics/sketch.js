
const [WIDTH, HEIGHT] = [480, 480];

let game;
let gearSound, splashSound, expolsionSound, chainSound, cannonSound, fogHornSound;

let apiUrl, apiConf;

let gameNameInput, player1Input, player2Input, submitButton;
let gameName, playerName;

function preload() {
    apiConf = loadJSON('./assets/api.json');

    gearSound = loadSound('./assets/gear.wav');
    splashSound = loadSound('./assets/splash.mp3')
    expolsionSound = loadSound('./assets/explosion.mp3')
    cannonSound = loadSound('./assets/cannon.wav')
    fogHornSound = loadSound('./assets/fog-horn.wav')
}

// p5js function
function setup() {
    apiUrl = apiConf['url']

    createCanvas(WIDTH, HEIGHT);

    createGameCreationForm();
}

function onPlayerSwitch() {
    game.placementPhase = !game.placementPhase;
}


// p5js function
function draw() {
    background(0, 67, 139);

    if (game) {
        game.draw();
    } else {
        drawSplash();
    }
}

function drawSplash() {
    push();
    textSize(72);
    fill(255);
    text("Battle Ship", 50, height / 2 );
    pop();
}

// p5js function
function keyPressed() {
    if (!game) {
        return;
    }

    const key = String.fromCharCode(keyCode);

    (game.placementPhase)  ?
        placementKeyPressed(key) :
        targetingKeyPressed(key);

}

function placementKeyPressed(key) {
    (keyCode == ENTER) ?
        game.setPlacementShip() :
        game.movePlacementShip(key);
}

function targetingKeyPressed(key) {
    (keyCode == ENTER) ?
        game.fireShot() :
        game.moveTargeter(key);
}

function createGameCreationForm() {
    const startingHeight = HEIGHT - 100;

    gameNameInput = createInput('testGameName').position(width + 20, startingHeight);
    player1Input = createInput('player2').position(width + 20, startingHeight + 25);
    player2Input = createInput('player1').position(width + 20, startingHeight + 50);

    submitButton = createButton('Create Game');
    submitButton.position(width + 20, startingHeight + 80);
    submitButton.mousePressed(onCreateGame);

    loadButton = createButton('Load Game');
    loadButton.position(width + 120, startingHeight + 80);
    loadButton.mousePressed(onLoadGame);
}

function onCreateGame() {
    const [gameName, active, inactive] = [
        gameNameInput,
        player1Input,
        player2Input
    ].map(input => input.value());

    $.post(`${apiUrl}/api/game/create`, {
        name: gameName,
        active_player: active,
        inactive_player: inactive
    }).done(resp => {
        console.log(resp);
        alert(`${gameName} has been created with players: ${active}, ${inactive}.`)
    });
}

function onLoadGame() {
    gameName = gameNameInput.value();
    playerName = player1Input.value();
    console.log(gameName, playerName)

    $.post(`${apiUrl}/api/player/check`, {
        game: gameName,
        player: playerName
    }).done(resp => {
        if (!resp['is_player']) {
            alert(`${playerName} is not part of the game ${gameName}`);
        }

        createGame(gameName);
    });
}

function createGame(name) {
    const [gameSize, numSpaces] = [WIDTH - 1, 10.];
    const gridSpaceSize = gameSize / numSpaces;

    const targeter = new Targeter(0, 0, gridSpaceSize, gearSound);

    game = new Game(name, WIDTH - 1, numSpaces, targeter);
}


function isControlKey(key) {
    return key == "W" ||
        key == "A" ||
        key == "S" ||
        key == "D";
}
