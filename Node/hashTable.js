// Hashing: Hashing é o processo de transformar uma entrada (chave) em uma saída fixa (índice) usando uma função hash. O objetivo é distribuir uniformemente as chaves em um espaço de índice fixo.

// Função Hash: Uma função hash mapeia uma chave para um índice em um array. Um exemplo simples de função hash poderia ser a soma dos valores dos caracteres da chave.

// Colisões: Colisões ocorrem quando duas chaves diferentes produzem o mesmo índice. Existem várias estratégias para lidar com colisões, como encadeamento (chaining) e endereçamento aberto (open addressing).

// Exemplo Prático
// Imagine uma tabela hash que armazena informações de estudantes. Cada estudante tem uma ID (chave) e um nome (valor).

// Tamanho da tabela: 10
// Função Hash: hash(key) = soma dos códigos ASCII dos caracteres da chave % tamanho da tabela
// Suponha que queremos inserir três estudantes:

// ID: "123", Nome: "Alice"
// ID: "456", Nome: "Bob"
// ID: "789", Nome: "Charlie"
// Passos
// Calcular o índice usando a função hash:

// Para "123": hash("123") = (49 + 50 + 51) % 10 = 150 % 10 = 0
// Para "456": hash("456") = (52 + 53 + 54) % 10 = 159 % 10 = 9
// Para "789": hash("789") = (55 + 56 + 57) % 10 = 168 % 10 = 8
// Inserir na tabela:

// "123" -> índice 0
// "456" -> índice 9
// "789" -> índice 8
// Lidar com colisões:

// Se outra chave gerasse o mesmo índice (por exemplo, "124" que também resulta em índice 0), usaríamos encadeamento para armazenar várias entradas no mesmo índice.


class HashTable {
    constructor(size = 10) {
        this.table = new Array(size);
    }

    // Função hash simples
    _hash(key) {
        let hash = 0;
        for (let i = 0; i < key.length; i++) {
            hash += key.charCodeAt(i);
        }
        return hash % this.table.length;
    }

    // Inserir um valor na tabela hash
    set(key, value) {
        const index = this._hash(key);
        if (!this.table[index]) {
            this.table[index] = [];
        }
        this.table[index].push([key, value]);
    }

    // Obter um valor da tabela hash
    get(key) {
        const index = this._hash(key);
        const bucket = this.table[index];
        if (bucket) {
            for (let i = 0; i < bucket.length; i++) {
                if (bucket[i][0] === key) {
                    return bucket[i][1];
                }
            }
        }
        return undefined;
    }

    // Remover um valor da tabela hash
    remove(key) {
        const index = this._hash(key);
        const bucket = this.table[index];
        if (bucket) {
            for (let i = 0; i < bucket.length; i++) {
                if (bucket[i][0] === key) {
                    bucket.splice(i, 1);
                    return true;
                }
            }
        }
        return false;
    }
}

// Exemplo de uso
const hashTable = new HashTable();

hashTable.set("123", "Alice");
hashTable.set("456", "Bob");
hashTable.set("789", "Charlie");

console.log(hashTable.get("123")); // Alice
console.log(hashTable.get("456")); // Bob
console.log(hashTable.get("789")); // Charlie

hashTable.remove("456");
console.log(hashTable.get("456")); // undefined
