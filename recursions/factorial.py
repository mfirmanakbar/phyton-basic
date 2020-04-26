# example factorial => 5! = 5 * 4 * 3 * 2 * 1 = 120

def factorial(n):
    if n == 0:
        return 1
    return (n * factorial(n - 1))


result = factorial(5)
print(result)

'''
120
'''
