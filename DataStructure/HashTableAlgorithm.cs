using System;
using System.Collections.Generic;

class HashTable<TKey, TValue> {
    private const int SIZE = 10;
    private LinkedList<KeyValuePair<TKey, TValue>>[] table;

    // Construtor
    public HashTable() {
        table = new LinkedList<KeyValuePair<TKey, TValue>>[SIZE];
        for (int i = 0; i < SIZE; i++) {
            table[i] = new LinkedList<KeyValuePair<TKey, TValue>>();
        }
    }

    // Função de hash simples
    private int HashFunction(TKey key) {
        int hashCode = key.GetHashCode();
        return Math.Abs(hashCode) % SIZE;
    }

    // Inserção (O(1))
    public void Insert(TKey key, TValue value) {
        int index = HashFunction(key);
        foreach (var pair in table[index]) {
            if (pair.Key.Equals(key)) {
                throw new ArgumentException("Chave já existe na hashtable.");
            }
        }
        table[index].AddLast(new KeyValuePair<TKey, TValue>(key, value));
    }

    // Busca (O(1) na média de tempo)
    public TValue Search(TKey key) {
        int index = HashFunction(key);
        foreach (var pair in table[index]) {
            if (pair.Key.Equals(key)) {
                return pair.Value;
            }
        }
        throw new KeyNotFoundException("Chave não encontrada na hashtable.");
    }

    // Exclusão (O(1) na média de tempo)
    public void Delete(TKey key) {
        int index = HashFunction(key);
        bool removed = false;
        foreach (var pair in table[index]) {
            if (pair.Key.Equals(key)) {
                table[index].Remove(pair);
                removed = true;
                break;
            }
        }
        if (!removed) {
            throw new KeyNotFoundException("Chave não encontrada na hashtable.");
        }
    }
}

class Program {
    static void Main(string[] args) {
        HashTable<string, int> hashTable = new HashTable<string, int>();

        // Inserção (O(1))
        hashTable.Insert("A", 1);
        hashTable.Insert("B", 2);
        hashTable.Insert("C", 3);

        // Busca (O(1) na média de tempo)
        Console.WriteLine("Busca por 'B': " + hashTable.Search("B"));

        // Exclusão (O(1) na média de tempo)
        hashTable.Delete("B");
        Console.WriteLine("Busca por 'B' após exclusão: ");
        try {
            Console.WriteLine(hashTable.Search("B"));
        } catch (KeyNotFoundException) {
            Console.WriteLine("Chave não encontrada na hashtable.");
        }
    }
}
