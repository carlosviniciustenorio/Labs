// using System;
//
// class MinHeap {
//     private int[] heap;
//     private int size;
//     private int capacity;
//
//     public MinHeap(int capacity) {
//         this.capacity = capacity;
//         heap = new int[capacity];
//         size = 0;
//     }
//
//     // Retorna o índice do pai de um nó
//     private int Parent(int index) {
//         return (index - 1) / 2;
//     }
//
//     // Retorna o índice do filho esquerdo de um nó
//     private int LeftChild(int index) {
//         return 2 * index + 1;
//     }
//
//     // Retorna o índice do filho direito de um nó
//     private int RightChild(int index) {
//         return 2 * index + 2;
//     }
//
//     // Troca os valores de dois nós no heap
//     private void Swap(int index1, int index2) {
//         int temp = heap[index1];
//         heap[index1] = heap[index2];
//         heap[index2] = temp;
//     }
//
//     // Insere um novo elemento no heap (O(logn))
//     public void Insert(int value) {
//         if (size == capacity) {
//             Console.WriteLine("Heap cheio, impossível inserir!");
//             return;
//         }
//
//         size++;
//         int currentIndex = size - 1;
//         heap[currentIndex] = value;
//
//         // Mantém a propriedade do heap
//         while (currentIndex != 0 && heap[Parent(currentIndex)] > heap[currentIndex]) {
//             Swap(currentIndex, Parent(currentIndex));
//             currentIndex = Parent(currentIndex);
//         }
//     }
//
//     // Remove e retorna o mínimo elemento do heap (O(logn))
//     public int DeleteMin() {
//         if (size == 0) {
//             Console.WriteLine("Heap vazio, impossível excluir!");
//             return -1;
//         }
//
//         if (size == 1) {
//             size--;
//             return heap[0];
//         }
//
//         int root = heap[0];
//         heap[0] = heap[size - 1];
//         size--;
//         MinHeapify(0);
//         return root;
//     }
//
//     // Mantém a propriedade de heap mínimo a partir de um índice específico
//     private void MinHeapify(int index) {
//         int smallest = index;
//         int left = LeftChild(index);
//         int right = RightChild(index);
//
//         if (left < size && heap[left] < heap[smallest])
//             smallest = left;
//
//         if (right < size && heap[right] < heap[smallest])
//             smallest = right;
//
//         if (smallest != index) {
//             Swap(index, smallest);
//             MinHeapify(smallest);
//         }
//     }
//
//     // Retorna o mínimo elemento do heap sem removê-lo (O(1))
//     public int FindMin() {
//         if (size == 0) {
//             Console.WriteLine("Heap vazio!");
//             return -1;
//         }
//
//         return heap[0];
//     }
// }
//
// class Program {
//     static void Main(string[] args) {
//         MinHeap minHeap = new MinHeap(10);
//
//         // Inserção (O(logn))
//         minHeap.Insert(10);
//         minHeap.Insert(20);
//         minHeap.Insert(15);
//
//         // Encontrar o mínimo (O(1))
//         Console.WriteLine("Mínimo elemento: " + minHeap.FindMin());
//
//         // Exclusão do mínimo (O(logn))
//         Console.WriteLine("Excluir mínimo: " + minHeap.DeleteMin());
//         Console.WriteLine("Novo mínimo elemento: " + minHeap.FindMin());
//     }
// }
//
// // Inserção: Insere um novo elemento no heap e, em seguida, mantém a propriedade do heap chamando uma função auxiliar para corrigir possíveis violações (heapify). A complexidade de tempo é O(logn) porque o heap tem altura logarítmica.
// // Exclusão do mínimo: Remove e retorna o menor elemento do heap e, em seguida, reorganiza o heap para manter a propriedade do heap mínimo. A complexidade de tempo é O(logn) porque o heap tem altura logarítmica.
// // Encontrar o mínimo: Retorna o mínimo elemento do heap sem removê-lo. Como o mínimo está sempre na raiz do heap, a operação é O(1), ou seja, constante.