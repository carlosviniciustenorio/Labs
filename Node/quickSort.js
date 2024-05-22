function quickSort(array)
{
    if(array.length <= 1)
        return array;

    const pointer = array[0];
    const left = array.filter(d => d < pointer);
    const equal = array.filter(d => d === pointer);
    const right = array.filter(d => d > pointer);

    return quickSort(left)+quickSort(equal)+quickSort(right);
}


const rootArray = [5,1,4,2,7,6,9,8];
console.log(rootArray);
let arraySorted = quickSort(rootArray);
console.log(arraySorted);