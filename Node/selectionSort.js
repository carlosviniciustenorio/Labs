const rootArray = [1,9,4,7,5,6,2,8];
console.log(rootArray);
let arraySorted = sort(rootArray);
console.log(arraySorted);

function sort(array){
    const lengthArray = array.length;
    let tempValue = 0;

    for(let i = 0; i < lengthArray - 1; i++){
        let min_index = i;

        for(let j = i + 1; j < lengthArray; j++){
            if(array[j] < array[min_index])
                min_index = j;
        }

        if(array[i] > array[min_index]){
            tempValue = array[i];
            array[i] = array[min_index];
            array[min_index] = tempValue;
        }
    }
    return array;
}