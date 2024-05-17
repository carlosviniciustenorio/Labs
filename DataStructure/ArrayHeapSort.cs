// public class Heap
// {
//     private int[] heapArray;
//     private int size;
//
//     public Heap(int capacity)
//     {
//         heapArray = new int[capacity];
//         size = 0;
//     }
//
//     public void Insert(int value)
//     {
//         if (size == heapArray.Length)
//         {
//             throw new InvalidOperationException("Heap is full");
//         }
//
//         heapArray[size] = value;
//         size++;
//         HeapifyUp(size - 1);
//     }
//
//     public int RemoveMax()
//     {
//         if (size == 0)
//         {
//             throw new InvalidOperationException("Heap is empty");
//         }
//
//         int root = heapArray[0];
//         heapArray[0] = heapArray[size - 1];
//         size--;
//         HeapifyDown(0);
//
//         return root;
//     }
//
//     private void HeapifyUp(int index)
//     {
//         int parent = (index - 1) / 2;
//         while (index > 0 && heapArray[index] > heapArray[parent])
//         {
//             Swap(index, parent);
//             index = parent;
//             parent = (index - 1) / 2;
//         }
//     }
//
//     private void HeapifyDown(int index)
//     {
//         int largest = index;
//         int leftChild = 2 * index + 1;
//         int rightChild = 2 * index + 2;
//
//         if (leftChild < size && heapArray[leftChild] > heapArray[largest])
//         {
//             largest = leftChild;
//         }
//
//         if (rightChild < size && heapArray[rightChild] > heapArray[largest])
//         {
//             largest = rightChild;
//         }
//
//         if (largest != index)
//         {
//             Swap(index, largest);
//             HeapifyDown(largest);
//         }
//     }
//
//     private void Swap(int index1, int index2)
//     {
//         int temp = heapArray[index1];
//         heapArray[index1] = heapArray[index2];
//         heapArray[index2] = temp;
//     }
//
//     public static void HeapSort(int[] array)
//     {
//         int n = array.Length;
//         Heap heap = new Heap(n);
//
//         // Build the heap
//         for (int i = 0; i < n; i++)
//         {
//             heap.Insert(array[i]);
//         }
//
//         // Extract elements from the heap
//         for (int i = n - 1; i >= 0; i--)
//         {
//             array[i] = heap.RemoveMax();
//         }
//     }
//
//     public static void Main()
//     {
//         int[] array = { 12, 11, 13, 5, 6, 7 };
//         Console.WriteLine($"Original array: {string.Join(" ,", array)}");
//         
//         HeapSort(array);
//
//         Console.WriteLine($"Sorted array: {string.Join(" ,", array)}");
//     }
// }
