// void Sort(int[] array, int left, int right)
// {
//     if (left < right)
//     {
//         int middle = (left + right) / 2;
//         
//         Sort(array, left, middle);
//         Sort(array, middle + 1, right);
//         Merge(array, left, middle, right);
//     }
// }
//
// void Merge(int[] array, int left, int middle, int right)
// {
//     var n1 = middle - left + 1;
//     var n2 = right - middle;
//
//     int[] leftArray = new int[n1];
//     int[] rightArray = new int[n2];
//     
//     Array.Copy(array, left, leftArray, 0, n1);
//     Array.Copy(array, middle + 1, rightArray, 0, n2);
//
//     int i = 0, j = 0;
//     int k = left;
//
//     while (i < n1 && j < n2)
//     {
//         if (leftArray[i] <= rightArray[j])
//         {
//             array[k] = leftArray[i];
//             i++;
//         }
//         else
//         {
//             array[k] = rightArray[j];
//             j++;
//         }
//         k++;
//     }
//
//     while (i < n1)
//     {
//         array[k] = leftArray[i];
//         i++;
//         k++;
//     }
//
//     while (j < n2)
//     {
//         array[k] = rightArray[j];
//         j++;
//         k++;
//     }
// }
//
// int[] array = {12,6,5,13,9,15,17,22};
// Console.WriteLine($"Given array: {string.Join(" ,", array)}");
// Sort(array, 0, array.Length - 1);
// Console.WriteLine($"\nSorted array: {string.Join(", ", array)}");