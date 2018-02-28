
class Targeter {
    constructor(initRow, initCol, shotSize, gearSound) {
        this.position = [initCol, initRow];
        this.shotSize = shotSize;

        this.gearSound = gearSound;
    }

    draw() {
        push();
        noStroke();
        fill(255, 255, 0, 190);

        const strokeWeight = 15;
        const [col, row] = this.position.map(x => x * this.shotSize + strokeWeight);
        const targeterSize = this.shotSize - 2*strokeWeight;

        rect(col, 0, targeterSize, width);
        rect(0, row, height, targeterSize);

        pop();
    }

    move(key) {
        let [col, row] = this.position;

        if (this.isControlKey(key)) {
            this.gearSound.play();
        }

        switch(key) {
            case "W": {
                row-=1;
                break;
            }
            case "S": {
                row+=1;
                break;
            }
            case "D": {
                col+=1;
                break;
            }
            case "A": {
                col-=1;
                break;
            }
        }

        this.position = [col, row];
    }

    isControlKey(key) {
        return key == "W" ||
            key == "A" ||
            key == "S" ||
            key == "D";
    }

}
