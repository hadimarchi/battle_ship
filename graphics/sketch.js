const WIDTH = 640;
const HEIGHT = 480;

class Ship {
    constructor(fore, aft, size, length, isVertical) {
        this.padding = 7;
        this.size = size;
        this.fore = fore;
        this.aft = aft;
        this.length = length;
        this.isVertical = isVertical;
    }

    draw() {
        push();
        fill(0);
        const [row, col] = [this.fore, this.aft].map(v => v * this.size + this.padding);
        let [width, height] = [this.size, this.size];

        (this.isVertical) ?
            height *= this.length :
            width *= this.length;

        const innerPadding = 2*this.padding;

        rect(
            row,
            col,
            width - innerPadding,
            height - innerPadding
        );

        pop();
    }
}

class Game {
    constructor(size) {
        this.size = size;
        this.gap = size / 10.0;
        const length = 2;

        this.ship = new Ship(1, 3, this.gap, length, true);
    }

    draw() {
        this.drawHorizontalLines();
        this.drawVerticalLines();

        this.ship.draw();
    }

    drawHorizontalLines() {
        push();
        for (let space = 0; space <=this.size; space+=this.gap) {
            line(0, 0, this.size, 0);
            translate(0, this.gap);
        }
        pop();
    }

    drawVerticalLines() {
        push();
        for (let space = 0; space <= this.size; space+=this.gap) {
            line(0, 0, 0, this.size);
            translate(this.gap, 0);
        }
        pop();
    }
}

let game;

function setup() {
    createCanvas(WIDTH, HEIGHT);
    game = new Game(400);
}

function draw() {
    background(255);
    game.draw();
}

function keyPressed() {
    switch(keyCode) {
        case RIGHT_ARROW: {
            break;
        }
        case LEFT_ARROW: {
            break;
        }
        case UP_ARROW: {
            break;
        }
        case DOWN_ARROW: {
            break;
        }
    }
}
