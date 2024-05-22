const rootArray = [9,7,4,1,5,6,2,8];
console.log(rootArray);
let arraySorted = sort(rootArray);
console.log(arraySorted);

function sort(array){
    if(array.length <= 1)
        return array;

    let tmp = 0;
    
    for(i = 0; i < array.length - 1; i++){
        for(j = i + 1; j < array.length; j++){
            if(array[i] > array[j]){
                tmp = array[i];
                array[i] = array[j];
                array[j] = tmp;
            }
        }
    }

    return array;
}