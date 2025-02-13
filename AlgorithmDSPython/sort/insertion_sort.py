data = [7, 5, 1, 3, 2, 8, 4, 6, 9]

#Best Case: O(n)
#Average: O(n^2)
#Worst Case: O(n^2)
#Space Complexity: O(1)
def sort(data):
    n = len(data)
    for i in range(1, n):
        key = data[i] 
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        
        data[j + 1] = key

sort(data)
print(data)
