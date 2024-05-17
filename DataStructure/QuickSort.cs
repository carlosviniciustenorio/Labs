// int[] arrayToQuickSort = { 4, 3, 1, 6, 7, 9, 5, 8, 11, 15, 14, 25, 0 };
//
// int[] QuickSort(int[] array)
// {
//     if (array.Length == 0 || array.Length == 1) return array;
//     
//     int pointer = array[0];
//     int[] head = array.Where(d => d < pointer).ToArray();
//     int[] equal = array.Where(d => d == pointer).ToArray();
//     int[] tail = array.Where(d => d > pointer).ToArray();
//
//     return QuickSort(head).Concat(equal).Concat(QuickSort(tail)).ToArray();
// }
//
// string arrayToQuickSortString = string.Join(" ,", arrayToQuickSort);
//
// var result = QuickSort(arrayToQuickSort);
// Console.WriteLine($"The quicksort result of list: {arrayToQuickSortString} is: {string.Join(" ,", result)}");