const rootArray = [7,9,4,1,5,6,2,8];
console.log(rootArray);
let arraySorted = sort(rootArray);
console.log(arraySorted);

function sort(array){
    let lenghtArray = array.length - 1;
    let valueOfLatest = 0;
    for(let j = 0; j < lenghtArray; j ++){
        for (let i = 0; i < lenghtArray; i++) {
            if(array[i] < array[i + 1]){
                continue;
            }else{
                valueOfLatest = array[i];
                array[i] = array[i + 1];
                array[i + 1] = valueOfLatest;
            }
        }
    }

    return array;
}