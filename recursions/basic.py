def foo(n):
    if n < 1:
        return n
    else:
        foo(n - 1)
    print("hello ", n)


foo(3)

'''
The Output:
hello  1
hello  2
hello  3
'''