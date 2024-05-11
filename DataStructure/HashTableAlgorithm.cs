// using System;
// using System.Collections.Generic;

// class HashTable {
//     private const int SIZE = 10;
//     private List<int>[] table;

//     // Construtor
//     public HashTable() {
//         table = new List<int>[SIZE];
//         for (int i = 0; i < SIZE; i++) {
//             table[i] = new List<int>();
//         }
//     }

//     // Função de hash simples
//     private int HashFunction(int key) {
//         return key % SIZE;
//     }

//     // Inserção (O(1))
//     public void Insert(int key) {
//         int index = HashFunction(key);
//         table[index].Add(key);
//     }

//     // Busca (O(n) no pior caso, mas O(1) na média de tempo)
//     public bool Search(int key) {
//         int index = HashFunction(key);
//         foreach (int item in table[index]) {
//             if (item == key)
//                 return true;
//         }
//         return false;
//     }

//     // Exclusão (O(1) no pior caso, mas O(n) na média de tempo)
//     public void Delete(int key) {
//         int index = HashFunction(key);
//         table[index].Remove(key);
//     }
// }

// class Program {
//     static void Main(string[] args) {
//         HashTable hashTable = new HashTable();

//         // Inserção (O(1))
//         hashTable.Insert(10);
//         hashTable.Insert(20);
//         hashTable.Insert(30);

//         // Busca (O(1) na média de tempo)
//         Console.WriteLine("Busca por 20: " + hashTable.Search(20));

//         // Exclusão (O(1) na média de tempo)
//         hashTable.Delete(20);
//         Console.WriteLine("Busca por 20 após exclusão: " + hashTable.Search(20));
//     }
// }


// // Inserção: A função de dispersão é aplicada à chave para calcular o índice na tabela. A inserção em uma lista vinculada em um índice específico é uma operação de tempo constante, O(1).
// // Busca: Embora a complexidade de tempo na pior situação seja O(n) devido a colisões, na média, a busca é O(1) devido à dispersão uniforme dos elementos.
// // Exclusão: Assim como a busca, a exclusão é O(1) no pior caso, mas O(n) na média, devido à necessidade de procurar o elemento na lista vinculada.