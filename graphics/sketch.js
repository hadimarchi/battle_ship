
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
}

function onPlayerSwitch() {
    game.placementPhase = !game.placementPhase;
}

function draw() {
    background(0, 67, 139);
    game.draw();
}

function keyPressed() {
    const key = String.fromCharCode(keyCode);

    if (!game.placementPhase) {
        if (keyCode == ENTER) {
            game.fireShot();
            return
        }

        game.moveCrossHair(key);
        return;
    }

    if (keyCode == ENTER) {
        game.setPlacementShip();
        return
    }

    game.movePlacementShip(key);
}
