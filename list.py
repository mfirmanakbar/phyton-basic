# empty list
my_list = []
print(my_list, end='\n')
my_list = list()
print(my_list, end='\n')

# adding element into the list
my_list = [1, 2, 3, 'firman', 'zaidin']
my_list_2 = list([4, 5, 6.89, 'papeda', 'ambon'])
print(my_list, end='\n')
print(my_list_2, end='\n')

# accessing elements of the list
my_list = [1, 2, 3, 'firman', 'zaidin', 'papeda', 'ambon']
print("all elements: ", my_list[:], end='\n')
print("4th element: ", my_list[4], end='\n')
print("element from index 1 to 3: ", my_list[1:3], end='\n')
print("elements in reverse order: ", my_list[::-1], end='\n')
print("elements from index 0 to 7 and jumping 2 elements: ", my_list[0:7:2], end='\n')
print("particular element of index 3 or firman: ", my_list[3][2], end='\n')

'''
# response
[]
[]
[1, 2, 3, 'firman', 'zaidin']
[4, 5, 6.89, 'papeda', 'ambon']
all elements:  [1, 2, 3, 'firman', 'zaidin', 'papeda', 'ambon']
4th element:  zaidin
element from index 1 to 3:  [2, 3]
elements in reverse order:  ['ambon', 'papeda', 'zaidin', 'firman', 3, 2, 1]
elements from index 0 to 7 and jumping 2 elements:  [1, 3, 'zaidin', 'ambon']
particular element of index 3 or firman:  r
'''