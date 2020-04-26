# example fibonacci : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ..
# 34 = 21 + 13, etc

def fibonacci(n):
    if n < 1:
        return "error"
    elif n == 1 or n == 2:
        return n - 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


result = fibonacci(10)
print(result)

'''
34
'''