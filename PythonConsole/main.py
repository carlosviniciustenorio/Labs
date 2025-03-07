import json

numbers = [1,2,3,4,5,6,7,8,9]

value = '''
[
    {
        "id": "1",
        "name": "first",
        "next": "2"
    },
    {
        "id": 2,
        "name": "first",
        "next": "3"
    }
]
'''

data = json.loads(value)
print(data)
data.insert(2, {"id": 3, "name": "third", "next": 4})
print(data)

print([item['id'] for item in data])

for item in data:
    item['name'] = item['name'].upper()
    item['id'] = int(item['id']) + 1
    
data.pop()

print(data)

data.clear()
print(data)


# print(list(filter(lambda x: x % 2 == 0, numbers)))
# print([number for number in numbers if number % 2 == 0])

# numbers.extend([10,11,12,13,14])
# numbers.pop()
# print(numbers)
# numbers.remove(2)
# print(numbers)
# numbers.insert(1,2)
# print(numbers)
# numbers.pop(0)
# print(numbers)
# numbers.insert(0,1)
# print(numbers)
# numbers.clear()
# print(numbers)