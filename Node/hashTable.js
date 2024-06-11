class HashTable{
    
    constructor(length){
        this.data = new Array(length);
    }

    generateHash(key){
        let hash = 0;
        for(let c = 0; c < key.length; c++){
            hash += key.charCodeAt(c);
        }
        return hash % this.data.length;
    }

    set(key, value){
        const index = this.generateHash(key);
        if(this.data[index]){
            for(let i = 0; i < this.data[index].length; i++){
                if(this.data[index][i][0] == key)
                    return `The key ${key} already exist!`;
            }
        }

        this.data[index] = [key,value];
        return `Key ${key} was inserted`;
    }

    search(key){
        const index = this.generateHash(key);
        const bucket = this.data[index];
        if(this.data[index]){
            for(let i = 0; i < bucket.length; i++){
                if(bucket[i][0] == key){
                    return bucket;
                }
            }
        }

        return "The data not exist!";
    }

    remove(key){
        const index = this.generateHash(key);
        const bucket = this.data[index];

        if(bucket){
            for(let i = 0; i < bucket.length; i++){
                if(bucket[i][0] == key){
                    bucket.splice(0,1);
                }
            }
        }

        return "The data not exist!";
    }
}

const hashTable = new HashTable(10);
console.log(hashTable.set("5", "b"));
console.log(hashTable.set("6", "c"));
console.log(hashTable.search("5"));
hashTable.remove("5");
console.log(hashTable.search("5"));
console.log(hashTable.search("6"));