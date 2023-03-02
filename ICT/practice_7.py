# 1.The shopping list simplified 

products = ['Apple', 'Banana']

print('Here is the list:', products)

newProduct = input('What do you want to add: ')

products.append(newProduct)

print('Here is the list:', products)

# 2.Print the even numbers 

numbers = []
for i in range(1, 21):
    numbers.append(i)

for i in numbers:
    if i % 2 == 0:
        print(i, end=' ')

# 3.The sum

numbers = [54, 6, 23, 1, 5, 98]
total = 0
for i in numbers:
    total += i

print(total)

# 4.Sorting 

numbers = [54, 6, 23, 1, 5, 98]
numbers.sort()
for i in numbers:
    print(i, end=' ')

# 5.The shopping list 

shoppingList = []

while True:
    operation = int(input('Do you want to add something (enter 1) or remove something (enter 2) or exit (enter 0):\n'))
    if operation == 1:
        product = input('What do you want to add: ')
        shoppingList.append(product)
    elif operation == 2:
        product = input('What do you want to remove: ')
        shoppingList.remove(product)
    else:
        break
    print('Here is the shopping list:')
    for i in shoppingList:
        print('-', i)

print('Here is the final shopping list:')
for i in shoppingList:
    print('-', i)
print('Goodbye !')


