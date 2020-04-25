def add(x, y):
    print("the sum of x and y is ", (x + y))


def multiply(x, y):
    print("the product of x and y is ", (x * y))


add(5, 10)
multiply(7, 5)
add(7, 13)
multiply(5, 20)

list1 = [1, 0, 3]
print(abs(-7))  # return positive value
print(all(list1))  # return true if all elements are true
print(any(list1))  # return true if any element is true
print(len(list1))
print(min(list1))
print(max(list1))
print(sum(list1))
print(type(list1))

'''
the sum of x and y is  15
the product of x and y is  35
the sum of x and y is  20
the product of x and y is  100
7
False
True
3
0
3
4
<class 'list'>
'''
