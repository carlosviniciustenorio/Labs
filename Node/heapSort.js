function heapify(array, n, i){
    let left = i * 2 + 1;
    let right = i * 2 + 2;
    let largest = i;

    if(left < n && array[left] > array[largest])
        largest = left;

    if(right < n && array[right] > array[largest])
        largest = right;

    if(largest != i){
        [array[i], array[largest]] = [array[largest], array[i]];
        heapify(array, n, largest); 
    }
}

function heapSort(array){
    let n = array.length;
    for(let i = Math.floor((n/2) - 1); i >= 0; i--){
        heapify(array, n, i);
    }

    for(let i = n - 1; i > 0; i--){
        [array[0], array[i]] = [array[i], array[0]];

        heapify(array, i, 0);
    }
}


let arr = [6,12,7,9,10,20,5,14];
console.log("Array inicial:");
console.log(arr);

heapSort(arr);

console.log("Array ordenado:");
console.log(arr);