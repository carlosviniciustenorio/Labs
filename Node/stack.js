class Stack{
    constructor(size){
        this.data = new Array(size);
    }

    insert(value){
        if(value <= 0)
            return "Input a valid data";

        this.data.push(value);
    }

    search = () => this.data[this.data.length - 1];

    remove = () => this.data.pop();

    isEmpty = () => this.data.length === 0;
}

const stack = new Stack();
stack.insert(10);
stack.insert(7);
console.log(`Searching the latest value inputed: ${stack.search()}`);
stack.insert(8);
console.log(`Searching the latest value inputed: ${stack.search()}`);
stack.insert(9);
console.log(`Searching the latest value inputed: ${stack.search()}`);
stack.insert(4);
console.log(`Searching the latest value inputed: ${stack.search()}`);
stack.insert(3);
console.log(`Searching the latest value inputed: ${stack.search()}`);
stack.insert(14);
console.log(`Searching the latest value inputed: ${stack.search()}`);
stack.insert(12);
console.log(`Searching the latest value inputed: ${stack.search()}`);
stack.insert(15);
console.log(`Searching the latest value inputed: ${stack.search()}`);
stack.insert(13);
console.log(`Searching the latest value inputed: ${stack.search()}`);

stack.remove();
console.log(`Searching the latest value existing: ${stack.search()}`);