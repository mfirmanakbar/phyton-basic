# loop
basket_of_fruits = ["apple", "orange", "banana", "watermelon"]
for fruit in basket_of_fruits:
    print(fruit)

numbers = [1, 2, 3, 4, 5]
sum_of_element = 0
for i in numbers:
    sum_of_element += i
    print(i)
print(sum_of_element)

for i in range(5):
    print(i)
print("\n")

for i in range(5, 10):
    print(i)
print("\n")

for i in range(5, 10, 2):
    print(i)
print("\n")

basket_of_fruits = ["apple", "orange", "banana", "watermelon"]
for fruit in basket_of_fruits:
    print(fruit)
else:
    print("no more fruits leftto eat")

'''
apple
orange
banana
watermelon
1
2
3
4
5
15
0
1
2
3
4


5
6
7
8
9


5
7
9


apple
orange
banana
watermelon
no more fruits leftto eat
'''