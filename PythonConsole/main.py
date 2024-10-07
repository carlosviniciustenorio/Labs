numbers = [1,2,3,4,5,6,7,8,9]

# print(list(filter(lambda x: x % 2 == 0, numbers)))
# print([number for number in numbers if number % 2 == 0])

numbers.extend([10,11,12,13,14])
numbers.pop()
print(numbers)
numbers.remove(2)
print(numbers)
numbers.insert(1,2)
print(numbers)
numbers.pop(0)
print(numbers)
numbers.insert(0,1)
print(numbers)
numbers.clear()
print(numbers)