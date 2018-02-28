
class Game {
    constructor(name, size, numSpaces, targeter) {
        this.name = name;
        this.placementPhase = false;

        this.size = size;
        this.numSpaces = numSpaces;
        this.gap = size / numSpaces;
        const length = 2;

        this.ships = [];
        this.shots = [];

        this.isLoading = true;

        this.targeter = targeter;

        this.fetchPlacementShips()
    }

    fetchPlacementShips() {
        $.getJSON(`${apiUrl}/api/ships/types`, ships => {
            this.placementShips = [];

            const midPoint = Math.floor(this.numSpaces / 2) - 1;
            for (const shipType of ships) {
                const [size, isVertical, length, name]= [this.gap, shipType.length, true, shipType.name];

                const ship = new Ship(midPoint, midPoint, size, isVertical, length, name);
                this.placementShips.push(ship);
            }

            this.placementShip = this.placementShips.pop();
            this.isLoading = false;
        });
    }

    draw() {
        this.drawHorizontalLines();
        this.drawVerticalLines();

        (this.placementPhase) ?
            this.placementDraw() :
            this.firingDraw();
    }

    placementDraw() {
        if (this.isLoading) {
            return;
        }

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
        const [row, col] = this.targeter.position;
        console.log('pos ', row, col);


        this.isShotAHit(row, col);

    }

    isShotAHit(row, col) {
        $.post(`${apiUrl}/api/fire/shot`, {
            game: this.name,
            shot: JSON.stringify([col, row])
        }).done(resp => {
            console.log(resp);

            const isHit = resp['is_hit'];
            const shot = this.getShot(isHit, row, col);

            this.addShot(shot);
        });
    }

    getShot(isHit, row, col) {
        const shot = (isHit) ?
            new Hit(row, col, this.gap) :
            new Miss(row, col, this.gap);

        return shot
    }

    addShot(newShot) {
        const [row, col] = newShot.position;

        const duplicatShots = this.shots
            .filter(s => s[0] !== col || s[1] !== row);

        if (duplicatShots.length > 0) {
            return;
        }

        this.shots.push(newShot);
    }
}
