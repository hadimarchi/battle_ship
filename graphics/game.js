
class Game {
    constructor(size) {
        this.placementPhase = true;

        this.size = size;
        this.gap = size / 10.0;
        const length = 2;

        this.ships = []
        this.fetchPlacementShips()

        this.placementShip = this.getPlacementShip();
    }

    fetchPlacementShips() {
        $.getJSON('http://localhost:5000', data => {
            console.log(data);
        });
    }


    getPlacementShip() {
        const [size, isVertical, length]= [this.gap, 2, true];

        return new Ship(0, 0, size, isVertical, length);
    }

    draw() {
        this.drawHorizontalLines();
        this.drawVerticalLines();

        for (const ship of this.ships) {
            ship.draw();
        }

        if (this.placementPhase) {
            this.placementShip.draw();
        }
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

    movePlacementShip(key) {
        this.placementShip.move(key);
    }

    setPlacementShip() {
        this.ships.push(this.placementShip);
        const length = 2;
        this.placementShip = new Ship(0, 0, this.gap, length, true);
    }
}
