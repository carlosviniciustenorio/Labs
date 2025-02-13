data = [7, 5, 1, 3, 2, 8, 4, 6, 9]

#Best Case: O(n)
#Average: O(n^2)
#Worst Case: O(n^2)
def sort(data):
    n = len(data) - 1
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
        
        data[i], data[min_index] = data[min_index], data[i]
        
sort(data)
print(data)