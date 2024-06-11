function heapify(array, n, i){
    let largest = i;
    let left = 2 * i + 1;
    let right = 2 * i + 2;

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

    for(let i = Math.floor(n / 2); i >= 0; i--){
        heapify(array, n, i);
    }
}


let arr = [6,12,7,9,10,20,5,14];
console.log("Array inicial:");
console.log(arr);

heapSort(arr);

console.log("Array ordenado:");
console.log(arr);
