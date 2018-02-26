
class Targeter {
    constructor(initRow, initCol, shotSize, gearSound) {
        this.position = [initRow, initCol]
        this.shotSize = shotSize;

        this.gearSound = gearSound;
    }

    draw() {
        push();
        noStroke();
        fill(255, 255, 0, 200);

        const strokeWeight = 1;
        const [row, col] = this.position.map(x => x * this.shotSize + strokeWeight);
        const targeterSize = this.shotSize - strokeWeight;

        rect(row, col, targeterSize, targeterSize);

        pop();
    }

    fire() {
        const [row, col] = this.position;

        const shot = (this.isShotAHit(row, col)) ?
            new Hit(row, col, this.shotSize) :
            new Miss(row, col, this.shotSize);

        return shot
    }

    move(key) {
        let [row, col] = this.position;
        this.gearSound.play();
        switch(key) {
            case "W": {
                col-=1;
                break;
            }
            case "S": {
                col+=1;
                break;
            }
            case "D": {
                row+=1;
                break;
            }
            case "A": {
                row-=1;
                break;
            }
        }

        this.position = [row, col];
    }

    isShotAHit(row, col) {
        return random() > 0.5;
    }
}
