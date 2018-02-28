
class Game {
    constructor(name, size, numSpaces, targeter) {
        this.name = name;
        this.placementPhase = true;

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
                const [size, isVertical, length, name, is_alive]= [this.gap, shipType.length, true, shipType.name, true];
                const ship = new Ship(midPoint, midPoint, size, isVertical, length, name, is_alive);
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
        $.post(`${apiUrl}/api/place/ship`, {'game': this.name, 'ship':JSON.stringify({
          'col': this.placementShip.col, 'row': this.placementShip.row,
          'length': this.placementShip.length, 'type': this.placementShip.name,
          'is_vertical': this.placementShip.isVertical})}).done(resp => {
              console.log(resp);
            });
        if (this.placementShips && this.placementShips.length < 1) {
            this.placementPhase = false;
            this.placementShip = undefined;

            return;
        }

        this.placementShip = this.placementShips.pop();
    }

    fireShot() {
        this.isShotAHit()
    }

    checkShot() {
        const [row, col] = this.targeter.position;

        this.isShotAHit(row, col);
    }

    isShotAHit(row, col) {
        console.log('checking shot on server ', this.name, `${apiUrl}/api/fire/shot`);
        const game = this.name;
        const shot = [col, row];

        $.post(`${apiUrl}/api/fire/shot`, {
            game, 'shot': JSON.stringify(shot)
        }).done(resp => {
            console.log(resp);

            const isHit = resp['is_hit'];
            const shot = this.targeter.getShot(isHit);

            this.addShot(shot);
        });
    }

    addShot(shot) {
        this.shots.push(shot);
    }
}
