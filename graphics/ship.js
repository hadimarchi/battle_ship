
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

    move(key) {
        switch(key) {
            case "W": {
                this.aft-=1;
                break;
            }
            case "S": {
                this.aft+=1;
                break;
            }
            case "D": {
                this.fore+=1;
                break;
            }
            case "A": {
                this.fore-=1;
                break;
            }
            case "R": {
                this.isVertical = !this.isVertical;
                break;
            }
        }
    }
}
