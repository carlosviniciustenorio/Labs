function sort(array)
{
    if(array.length <= 1)
        return array;

    const middle = Math.floor(array.length / 2);
    const left = array.slice(0, middle);
    const right = array.slice(middle);

    return merge(sort(left), sort(right));
}

function merge(left, right)
{
    let result = [];
    let i = 0, j = 0;

    while(i < left.length && j < right.length)
    {
        if(left[i] <= right[j])
        {
            result.push(left[i]);
            i++;
        }
        else
        {
            result.push(right[j]);
            j++
        }
    }

    while(i < left.length)
    {
        result.push(left[i]);
        i++;
    }

    while(j < right.length)
    {
        result.push(right[j]);
        j++;
    }

    return result;
}

const rootArray = [2,1,4,5,7,6,9,8];
console.log(rootArray);
let arraySorted = sort(rootArray);
console.log(arraySorted);