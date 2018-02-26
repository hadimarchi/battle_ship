
const WIDTH = 640;
const HEIGHT = 480;

let game = new Game(400);

function setup() {
    createCanvas(WIDTH, HEIGHT);
}

function draw() {
    background(255);
    game.draw();
}

function keyPressed() {
    if (!game.placementPhase) {
        return;
    }

    if (keyCode == ENTER) {
        game.setPlacementShip();
        return
    }

    const key = String.fromCharCode(keyCode);
    game.movePlacementShip(key);
}
