function heapify(arr, n, i) {
    let largest = i; // Inicializa o maior como raiz
    let left = 2 * i + 1; // Filho à esquerda
    let right = 2 * i + 2; // Filho à direita

    // Se o filho à esquerda é maior que a raiz
    if (left < n && arr[left] > arr[largest]) {
        largest = left;
    }

    // Se o filho à direita é maior que o maior até agora
    if (right < n && arr[right] > arr[largest]) {
        largest = right;
    }

    // Se o maior não é a raiz
    if (largest != i) {
        [arr[i], arr[largest]] = [arr[largest], arr[i]]; // Troca

        // Recursivamente heapifica a subárvore afetada
        heapify(arr, n, largest);
    }
}

function heapSort(arr){
    let n = arr.length;

    // Constrói o max heap (reorganiza o array)
    for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }

    // Extrai um por um os elementos do heap
    for (let i = n - 1; i > 0; i--) {
        // Move a raiz atual para o fim
        [arr[0], arr[i]] = [arr[i], arr[0]];

        // Chama heapify na heap reduzida
        heapify(arr, i, 0);
    }
}

let arr = [6,12,7,9,10,20,5,14];
console.log("Array inicial:");
console.log(arr);

heapSort(arr);

console.log("Array ordenado:");
console.log(arr);
