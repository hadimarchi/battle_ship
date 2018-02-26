
const [WIDTH, HEIGHT] = [480, 480];

const game = new Game(WIDTH - 1);
let button;
let apiConf;

function preload() {
    apiConf = loadJSON('./assets/api.json');
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

    createCanvas(WIDTH, HEIGHT);
    button = createButton('Switch player');
    button.position(width + 20, 10);
    button.mousePressed(onPlayerSwitch);
}

function onPlayerSwitch() {
    console.log('switching players (dummy)');
}

function draw() {
    background(0, 67, 139);
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
