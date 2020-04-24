s = "10010"
c = int(s, 2)
e = float(s)
print("convert the string ", s, " to int base 2 : ", c, end='\n')
print("convert the string ", s, " to float : %f" % e, end='\n')

s = "4"
c = ord(s)
print("convert the character ", s, " to integer : %c" % c, end='\n')

s = 24
c = hex(s)
e = oct(s)
print("convert the integer ", s, " to hexadecimal string : ", c, end='\n')
print("convert the integer ", s, " to octal string : ", e, end='\n')

s = "firman"
c = tuple(s)
e = set(s)
f = list(s)
print("convert the string ", s, " to tuple : ", c, end='\n')
print("convert the string ", s, " to set : ", e, end='\n')
print("convert the string ", s, " to list : ", f, end='\n')

a = 1
b = 2
tup = (('a', 1), ('f', 2), ('g', 3))  # initializing tuple (key, value)
c = complex(a, b)
e = str(a)
f = dict(tup)
print("convert the integer ", a, b, " to complex : ", c, end='\n')
print("convert the integer ", a, " to string : ", e, end='\n')
print("convert the tup to dictionary : ", f, end='\n')

'''
# response
convert the string  10010  to int base 2 :  18
convert the string  10010  to float : 10010.000000
convert the character  4  to integer : 4
convert the integer  24  to hexadecimal string :  0x18
convert the integer  24  to octal string :  0o30
convert the string  firman  to tuple :  ('f', 'i', 'r', 'm', 'a', 'n')
convert the string  firman  to set :  {'n', 'f', 'i', 'a', 'm', 'r'}
convert the string  firman  to list :  ['f', 'i', 'r', 'm', 'a', 'n']
convert the integer  1 2  to complex :  (1+2j)
convert the integer  1  to string :  1
convert the tup to dictionary :  {'a': 1, 'f': 2, 'g': 3}
'''