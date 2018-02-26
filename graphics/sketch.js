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

        if (this.isVertical) {
            rect(
                this.fore + this.padding,
                this.aft + this.padding,
                this.size*this.length - 2*this.padding,
                this.size - 2*this.padding
            );
        } else {
            rect(
                this.fore + this.padding,
                this.aft + this.padding,
                this.size - 2*this.padding,
                this.size*this.length - 2*this.padding
            )
        }

        pop();
    }
}

class Grid {
    constructor(size) {
        this.size = size;
        this.gap = size / 10.0;
        const length = 2;

        this.ship = new Ship(0, 0, this.gap, length, false);
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

let grid;

function setup() {
    createCanvas(WIDTH, HEIGHT);
    grid = new Grid(400);
}

function draw() {
    background(255);
    grid.draw();
}
