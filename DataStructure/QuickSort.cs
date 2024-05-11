using System;

class HeapSort {
    public static void Sort(int[] arr) {
        int n = arr.Length;

        // Constrói o heap
        for (int i = n / 2 - 1; i >= 0; i--)
            Heapify(arr, n, i);

        // Extrai elementos um por um do heap
        for (int i = n - 1; i > 0; i--) {
            // Move a raiz atual para o final do array
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            // Chama Heapify na subárvore reduzida
            Heapify(arr, i, 0);
        }
    }

    private static void Heapify(int[] arr, int n, int i) {
        int largest = i; // Inicializa o maior como raiz
        int left = 2 * i + 1; // Índice do filho esquerdo
        int right = 2 * i + 2; // Índice do filho direito

        // Se o filho esquerdo é maior que a raiz
        if (left < n && arr[left] > arr[largest])
            largest = left;

        // Se o filho direito é maior que o maior até agora
        if (right < n && arr[right] > arr[largest])
            largest = right;

        // Se o maior não é a raiz
        if (largest != i) {
            int temp = arr[i];
            arr[i] = arr[largest];
            arr[largest] = temp;

            // Recursivamente Heapify a subárvore afetada
            Heapify(arr, n, largest);
        }
    }

    // Função de utilidade para imprimir um array
    public static void PrintArray(int[] arr) {
        int n = arr.Length;
        for (int i = 0; i < n; ++i)
            Console.Write(arr[i] + " ");
        Console.WriteLine();
    }
}

class Program {
    static void Main(string[] args) {
        int[] arr = { 12, 11, 13, 5, 6, 7 };
        int n = arr.Length;

        Console.WriteLine("Array original:");
        HeapSort.PrintArray(arr);

        HeapSort.Sort(arr);

        Console.WriteLine("Array ordenado:");
        HeapSort.PrintArray(arr);
    }
}


// A função Sort implementa o algoritmo Heapsort.
// A função Heapify mantém a propriedade de heap para um determinado nó.
// A função PrintArray é uma função de utilidade para imprimir o array antes e depois da ordenação.