// LinkedList linkedList = new();
// linkedList.Insert(10);
// linkedList.Insert(20);
// linkedList.Insert(30);
// linkedList.Insert(5);
//
// Console.WriteLine("Try search a value into LinkedList, press a number now.");
// Console.WriteLine("If your number is found, it will be printed, but otherwise -1 will be returned.");
// var valueToSearch = Console.ReadLine();
// Console.WriteLine($"Searching the node with value {valueToSearch}: value searched: {linkedList.Search(Convert.ToInt32(valueToSearch))}");
//
// Console.WriteLine("Try to delete a value into LinkedList, press a number now.");
// var valueToDelete = Console.ReadLine();
// Console.WriteLine($"Deleted: {linkedList.Delete(Convert.ToInt32(valueToDelete))}");
// Console.WriteLine($"Trying to search the deleted value: {valueToDelete}: value searched: {linkedList.Search(Convert.ToInt32(valueToDelete))}");
//
// Console.WriteLine("Try to update a value into LinkedList, press a number who you wanna update now.");
// var valueToUpdate = Console.ReadLine();
// Console.WriteLine("Press a number to be the new value of your node.");
// var newValue = Console.ReadLine();
//
// linkedList.Update(Convert.ToInt32(valueToUpdate), Convert.ToInt32(newValue));
// Console.WriteLine($"Updated");
// Console.WriteLine($"Trying to search the updated value: {valueToUpdate}: the actually value finded: {linkedList.Search(Convert.ToInt32(newValue))}");
//
// public class Node
// {
//     public int Value;
//     public Node next;
//
//     public Node(int value)
//     {
//         Value = value;
//         next = null;
//     }
// }
//
// public class LinkedList
// {
//     public Node head;
//
//     public LinkedList()
//     {
//         head = null;
//     }
//     
//     // Average: O(1) - Worst: O(1)
//     public void Insert(int value)
//     {
//         Node node = new(value);
//         node.next = head;
//         head = node;
//     }
//     
//     // Average: O(1) - Worst: O(n)
//     public int Search(int value)
//     {
//         Node current = head;
//         while (current != null)
//         {
//             if (current.Value == value)
//                 return current.Value;
//
//             current = current.next;
//         }
//
//         return -1;
//     }
//     
//     // Average: O(1) - Worst: O(n)
//     public bool Delete(int value)
//     {
//         Node current = head;
//         Node prev = null;
//
//         if (current.Value == value)
//         {
//             head = current.next;
//             return true;
//         }
//
//         while (current != null && current.Value != value)
//         {
//             prev = current;
//             current = current.next;
//         }
//
//         if (current is null)
//             return false;
//
//         prev.next = current.next;
//         return true;
//     }
//
//     // Average: O(1) - Worst: O(n)
//     public void Update(int value, int newValue)
//     {
//         Node current = head;
//         while (current != null)
//         {
//             if (current.Value == value)
//             {
//                 current.Value = newValue;
//                 return;
//             }
//
//             current = current.next;
//         }
//
//         throw new KeyNotFoundException("Valor informado não localizado");
//     }
// }