
const [WIDTH, HEIGHT] = [480, 480];

let game;
let gearSound;

let apiUrl, apiConf;

let gameNameInput, player1Input, player2Input, submitButton;

function preload() {
    apiConf = loadJSON('./assets/api.json');
    gearSound = loadSound('./assets/gear.wav');
}

function setup() {
    apiUrl = apiConf['url']

    createCanvas(WIDTH, HEIGHT);

    createGameCreationForm();

}

function onPlayerSwitch() {
    game.placementPhase = !game.placementPhase;
}


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

    gameNameInput = createInput('game name').position(width + 20, startingHeight);
    player1Input = createInput('player 1').position(width + 20, startingHeight + 25);
    player2Input = createInput('player 2').position(width + 20, startingHeight + 50);

    submitButton = createButton('Create Game');
    submitButton.position(width + 20, startingHeight + 80);
    submitButton.mousePressed(onCreateGame);
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
        createGame(resp);
    });
}

function createGame(resp) {
    const [gameSize, numSpaces] = [WIDTH - 1, 10.];
    const gridSpaceSize = gameSize / numSpaces;

    const targeter = new Targeter(0, 0, gridSpaceSize, gearSound);
    game = new Game(WIDTH - 1, numSpaces, targeter);
}

function shipTestCall() {
    $.post(`${apiUrl}/api/game/place/ship`, {
        game: "test-game",
        ship: "cool new ship"
    }).done(resp => {
        console.log(resp);
    });
}

