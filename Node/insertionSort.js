//O Insertion Sort (ou ordenação por inserção) é um algoritmo simples e intuitivo de ordenação que funciona da maneira como muitas pessoas organizam cartas de baralho em suas mãos. A ideia principal é construir uma lista ordenada uma peça de cada vez, inserindo cada novo elemento na posição correta em relação aos elementos já ordenados.

// Função de ordenação por inserção
function insertionSort(array){
    for (let i = 1; i < array.length; i++) {
        let key = array[i];
        let j = i - 1;

        while(j >= 0 && array[j] > key){
            array[i] = array[j];
            j = j - 1;
        }

        array[j + 1] = key;
    }

    return array;
}

// Exemplo de uso
const rootArray = [9, 7, 4, 1, 5, 6, 2, 8];
console.log("Array original:", rootArray);
let arraySorted = insertionSort(rootArray);
console.log("Array ordenado:", arraySorted);
