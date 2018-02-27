
class Targeter {
    constructor(initRow, initCol, shotSize, gearSound) {
        this.position = [initRow, initCol]
        this.shotSize = shotSize;

        this.gearSound = gearSound;
    }

    draw() {
        push();
        noStroke();
        fill(255, 255, 0, 190);

        const strokeWeight = 15;
        const [row, col] = this.position.map(x => x * this.shotSize + strokeWeight);
        const targeterSize = this.shotSize - 2*strokeWeight;

        rect(row, 0, targeterSize, HEIGHT );
        rect(0, col, width, targeterSize);

        pop();
    }

    getShot(isHit) {
        const shot = (isHit) ?
            new Hit(row, col, this.shotSize) :
            new Miss(row, col, this.shotSize);

        return shot
    }

    move(key) {
        let [row, col] = this.position;

        if (this.isControlKey(key)) {
            this.gearSound.play();
        }

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

    isControlKey(key) {
        return key == "W" ||
            key == "A" ||
            key == "S" ||
            key == "D";
    }

}
