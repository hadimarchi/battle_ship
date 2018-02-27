
const [WIDTH, HEIGHT] = [480, 480];

let game;
let gearSound;

let apiUrl, apiConf;

let gameNameInput, player1Input, player2Input, submitButton;

function preload() {
    apiConf = loadJSON('./assets/api.json');
    gearSound = loadSound('./assets/gear.wav');
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

    console.log(`${apiUrl}/api/game/create`);

    $.post(`${apiUrl}/api/game/create`, {
        name: gameName,
        active_player: active,
        inactive_player: inactive
    }).done(resp => {
        console.log(resp);
        createGame(gameName);
    });
}

function onLoadGame() {
    const gameName = gameNameInput.value();

    loadGame(gameName);
}

function loadGame(name) {
    console.log(`${apiUrl}/api/game/${name}`)
    $.get(`${apiUrl}/api/game/${name}`, gameJson => {
        console.log(gameJson);
    });
}

function createGame(name) {
    const [gameSize, numSpaces] = [WIDTH - 1, 10.];
    const gridSpaceSize = gameSize / numSpaces;

    const targeter = new Targeter(0, 0, gridSpaceSize, gearSound);

    game = new Game(name, WIDTH - 1, numSpaces, targeter);
}

function shipTestCall() {
    $.post(`${apiUrl}/api/game/place/ship`, {
        game: "test-game",
        ship: "cool new ship"
    }).done(resp => {
        console.log(resp);
    });
}

