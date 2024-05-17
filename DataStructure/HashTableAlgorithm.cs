// HashTable<object,object> hashTable = new();
// hashTable.Insert("A", 1);
// hashTable.Insert(2, "B");
// hashTable.Insert("1", "C");
// hashTable.Insert(new { value = "car"}, "Camaro");
//
// Console.WriteLine($"Result: {hashTable.Search(Convert.ToInt32(2))}");
// Console.WriteLine($"Result: {hashTable.Search("A")}");
// Console.WriteLine($"Result: {hashTable.Search("1")}");
// Console.WriteLine($"Result: {hashTable.Search(new { value = "car"})}");
//
// Console.WriteLine($"Deleting: {new { value = "car"}}");
// hashTable.Delete(new { value = "car"});
//
// Console.WriteLine($"Result search new {{ value = \"car\"}}: {hashTable.Search(new { value = "car"})}");
//
// // Console.WriteLine("Set a value to search on hashtable");
// // var valueToSearch = Console.ReadLine();
// // Console.WriteLine($"Result: {hashTable.Search(Convert.ToInt32(valueToSearch))}");
//
// class HashTable<TKey, TValue>
// {
//     private const int capacity = 16;
//     private LinkedList<KeyValuePair<TKey, TValue>>[] table;
//     
//     public HashTable()
//     {
//         table = new LinkedList<KeyValuePair<TKey, TValue>>[capacity];
//         for (int i = 0; i < capacity; i++)
//         {
//             table[i] = new LinkedList<KeyValuePair<TKey, TValue>>();
//         }
//     }
//     
//     // Average: O(1) or constant time - Worst: O(n) or linear time
//     public void Insert(TKey key, TValue value)
//     {
//         var index = GetIndex(key);
//         foreach (var pair in table[index])
//         {
//             if (pair.Key.Equals(key))
//                 throw new ArgumentException("A chave já existe na tabela");
//         }
//         
//         table[index].AddLast(new KeyValuePair<TKey, TValue>(key, value));
//     }
//     
//     // Average: O(1) or constant time - Worst: O(n) or linear time
//     public KeyValuePair<TKey, TValue> Search(TKey key)
//     {
//         var index = GetIndex(key);
//         KeyValuePair<TKey, TValue> result = new();
//         
//         foreach (var pair in table[index])
//         {
//             if (pair.Key.Equals(key))
//                 result = pair;
//         }
//
//         if (result.Key is null)
//             throw new KeyNotFoundException("Chave informada não localizada");
//
//         return result;
//     }
//     
//     // Average: O(1) or constant time - Worst: O(n) or linear time
//     public void Delete(TKey key)
//     {
//         var index = GetIndex(key);
//         foreach (var item in table[index])
//         {
//             if (item.Key.Equals(key))
//                 table[index].Remove(item);
//             return;
//         }
//
//         throw new KeyNotFoundException("Chave informada não localizada");
//     }
//
//     public int GetIndex(TKey key)
//     {
//         var hash = key.GetHashCode();
//         return Math.Abs(hash) % capacity;
//     }
// }