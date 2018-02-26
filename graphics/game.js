
class Game {
    constructor(size) {
        this.placementPhase = false;

        this.size = size;
        this.gap = size / 10.0;
        const length = 2;

        this.ships = [];
        this.shots = [];

        this.isLoading = true;

        this.targeter = new Targeter(0, 0, this.gap);

        this.fetchPlacementShips()
    }

    fetchPlacementShips() {
        $.getJSON('http://localhost:5000/api/ships/types', ships => {
            this.placementShips = [];

            for (const shipType of ships) {
                for (let n = 0; n < shipType.amount; ++n) {
                    const [size, isVertical, length]= [this.gap, shipType.length, true];

                    const ship = new Ship(0, 0, size, isVertical, length);
                    this.placementShips.push(ship);
                }
            }

            this.placementShip = this.placementShips.pop();
            this.isLoading = false;
        });
    }

    draw() {
        this.drawHorizontalLines();
        this.drawVerticalLines();

        if (this.placementPhase) {
            this.placementDraw();
        } else {
            this.firingDraw();
        }
    }

    placementDraw() {
        for (const ship of this.ships) {
            ship.draw([100]);
        }

        this.placementShip.draw([255, 69, 0, 160]);
    }

    firingDraw() {
        for (const shot of this.shots) {
            shot.draw();
        }

        this.targeter.draw();
    };

    drawHorizontalLines() {
        push();
        stroke(255);
        for (let space = 0; space <=this.size; space+=this.gap) {
            line(0, 0, this.size, 0);
            translate(0, this.gap);
        }
        pop();
    }

    drawVerticalLines() {
        push();
        stroke(255);
        for (let space = 0; space <= this.size; space+=this.gap) {
            line(0, 0, 0, this.size);
            translate(this.gap, 0);
        }
        pop();
    }

    movePlacementShip(key) {
        this.placementShip.move(key);
    }

    moveTargeter(key) {
        this.targeter.move(key);
    }

    setPlacementShip() {
        this.ships.push(this.placementShip);

        if (this.placementShips && this.placementShips.length < 1) {
            this.placementPhase = false;
            this.placementShip = undefined;

            return;
        }

        this.placementShip = this.placementShips.pop();
    }

    fireShot() {
        const result = this.targeter.fire();

        this.shots.push(result);
    }

}
