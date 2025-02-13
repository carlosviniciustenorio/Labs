data = [7, 5, 1, 3, 2, 8, 4, 6, 9]

#Best Case: O(n)
#Average: O(n^2)
#Worst Case: O(n^2)
#Space Complexity: O(1)
def sort(data):
    n = len(data) - 1
    for i in range(n):
        has_changed = False
        for j in range(n - i):
            if data[j] > data[j + 1]:
                data[j], data[j+1] = data[j+1], data[j]
                has_changed = True
        if not has_changed:
            break
    
sort(data)
print(data)