class Shot {
    constructor(row, col, size) {
        this.position = [row, col]
        this.size = size;
    }
}

class Hit extends Shot {
    draw() {
        push();
        noStroke();
        fill(0, 255, 0);

        const strokeWeight = 1;
        const [row, col] = this.position.map(x => x * this.size + strokeWeight);
        const targeterSize = this.size - strokeWeight;

        rect(row, col, targeterSize, targeterSize);

        pop();
    }

    playSound() {
        expolsionSound.play();
    }
}

class Miss extends Shot {
    draw() {
        push();
        noStroke();
        fill(255, 0, 0);

        const strokeWeight = 1;
        const [row, col] = this.position.map(x => x * this.size + strokeWeight);
        const targeterSize = this.size - strokeWeight;

        rect(row, col, targeterSize, targeterSize);

        pop();
    }

    playSound() {
        splashSound.play();
    }
}


