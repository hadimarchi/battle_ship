
const [WIDTH, HEIGHT] = [480, 480];

let game;
let gearSound;
let button;
let apiConf;

function preload() {
    apiConf = loadJSON('./assets/api.json');
    gearSound = loadSound('./assets/gear.wav');
}

function setup() {
    url = apiConf['url']
    $.post(`${url}/api/game/create`, {
        name: "test-game",
        active_player:"America",
        inactive_player:"Russia"
    }).done(resp => {
          console.log(resp);
    });

    $.post(`${url}/api/game/place/ship`, {
        game: "test-game",
        ship: "cool new ship"
    }).done(resp => {
          console.log(resp);
    });

    createCanvas(WIDTH, HEIGHT);
    button = createButton('Switch game phase');
    button.position(width + 20, 10);
    button.mousePressed(onPlayerSwitch);

    const [gameSize, numSpaces] = [WIDTH - 1, 10.];
    const gridSpaceSize = gameSize / numSpaces;

    const targeter = new Targeter(0, 0, gridSpaceSize, gearSound);
    game = new Game(WIDTH - 1, numSpaces, targeter);
    console.log(game);
}

function onPlayerSwitch() {
    game.placementPhase = !game.placementPhase;
}

function draw() {
    background(0, 67, 139);
    game.draw();
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

function keyPressed() {
    const key = String.fromCharCode(keyCode);

    (game.placementPhase)  ?
        placementKeyPressed(key) :
        targetingKeyPressed(key);

}


