// O Bubble Sort é um algoritmo de ordenação simples que percorre repetidamente a lista,
// compara elementos adjacentes e os troca se estiverem na ordem errada. 
// Este processo é repetido até que a lista esteja ordenada.

const rootArray = [7,9,4,1,5,6,2,8];
console.log(rootArray);
let arraySorted = sort(rootArray);
console.log(arraySorted);

function sort(array){
    let lenghtArray = array.length - 1;
    for(let j = 0; j < lenghtArray; j ++){
        for (let i = 0; i < lenghtArray; i++) {
            if(array[i] > array[i + 1]){
                [array[i + 1], array[i]] = [[array[i], array[i + 1]]];
            }
        }
    }

    return array;
}