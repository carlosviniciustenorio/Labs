data = [7, 2, 1, 3, 5, 8, 4, 6, 9]

#Best Case: O(n log n)
#Average: O(n log n)
#Worst Case: O(n^2)
def sort(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        
        return sort(left) + middle + sort(right)
      
print(f'Unsorted data: {data}')        
sorted_data = sort(data)
print(f'Sorted data: {sorted_data}')