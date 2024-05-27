class Queue {
    constructor() {
        this.data = [];
        this.maxSize = 10; // Exemplo de limite máximo de tamanho da fila
    }

    insert(value) {
        if (value <= 0) {
            console.error("Invalid input: Please input a valid positive number.");
            return;
        }

        if (this.data.length < this.maxSize) {
            this.data.push(value);
        } else {
            console.error("Queue overflow: The queue is full.");
        }
    }

    search() {
        return this.data.length > 0 ? this.data[0] : null;
    }

    remove() {
        if (!this.isEmpty()) {
            return this.data.shift();
        } else {
            console.error("Queue underflow: The queue is empty.");
            return null;
        }
    }

    isEmpty() {
        return this.data.length === 0;
    }
}

// Exemplo de uso:
const queue = new Queue();
queue.insert(10);
queue.insert(7);
console.log(`Searching the latest value inputed: ${queue.search()}`);
queue.insert(8);
console.log(`Searching the latest value inputed: ${queue.search()}`);
queue.insert(9);
console.log(`Searching the latest value inputed: ${queue.search()}`);
queue.insert(4);
console.log(`Searching the latest value inputed: ${queue.search()}`);
queue.insert(3);
console.log(`Searching the latest value inputed: ${queue.search()}`);
queue.insert(14);
console.log(`Searching the latest value inputed: ${queue.search()}`);
queue.insert(12);
console.log(`Searching the latest value inputed: ${queue.search()}`);
queue.insert(15);
console.log(`Searching the latest value inputed: ${queue.search()}`);
queue.insert(13);
console.log(`Searching the latest value inputed: ${queue.search()}`);

queue.remove();
console.log(`Searching the latest value existing: ${queue.search()}`);