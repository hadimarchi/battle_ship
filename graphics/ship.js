
class Ship {
    constructor(col, row, size, length, isVertical, name, is_alive) {
        this.padding = 7;
        this.size = size;
        this.col = col;;
        this.row = row;
        this.length = length;
        this.isVertical = isVertical;
        this.name = name
        this.is_alive = is_alive
    }

    draw(rgbArray) {
        push();
        fill(...rgbArray);
        const [col, row] = [this.col, this.row].map(v => v * this.size + this.padding);
        let [width, height] = [this.size, this.size];

        (this.isVertical) ?
            height *= this.length :
            width *= this.length;

        const innerPadding = 2*this.padding;

        rect(
            col,
            row,
            width - innerPadding,
            height - innerPadding
        );

        pop();
    }

    move(key) {
        if (isControlKey(key)) {
            splashSound.play();
        }

        switch(key) {
            case "W": {
                this.row-=1;
                break;
            }
            case "S": {
                this.row+=1;
                break;
            }
            case "D": {
                this.col+=1;
                break;
            }
            case "A": {
                this.col-=1;
                break;
            }
            case "R": {
                this.isVertical = !this.isVertical;
                break;
            }
        }
    }
}
