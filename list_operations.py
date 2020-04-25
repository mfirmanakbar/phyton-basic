# empty list
my_list = []
print(my_list)
my_list = list()
print(my_list, end='\n\n')

# adding element into the list
my_list = [1, 2, 3, 'firman', 'zaidin']
my_list_2 = list([4, 5, 6.89, 'papeda', 'ambon'])
print(my_list)
print(my_list_2, end='\n\n')

# accessing elements of the list
my_list = [1, 2, 3, 'firman', 'zaidin', 'papeda', 'ambon']
print("all elements: ", my_list[:])
print("4th element: ", my_list[4])
print("element from index 1 to 3: ", my_list[1:3])
print("elements in reverse order: ", my_list[::-1])
print("elements from index 0 to 7 and jumping 2 elements: ", my_list[0:7:2])
print("particular element of index 3 or firman: ", my_list[3][2], end='\n\n')

# adding data into the list
my_list = [1, 2, 3, 'firman', 'zaidin']
my_list_2 = list([4, 5, 3.142, 'papeda', 'ambon'])
print("length of my_list", len(my_list))
print("length of my_list_2", len(my_list_2))
my_list.append([552, 21])
print("add passed parameters as single element: ", my_list)
my_list_2.extend([552, 21])
print("extending list by adding all elements 1 by 1: ", my_list_2)
my_list.insert(1, "insert example")
print("insert passed parameter in index 1: ", my_list)
print("concatenation: ", my_list + ["concat example"])
print("multiply: ", my_list * 2)
print("my list back: ", my_list, end='\n\n')

# delete element from the list
my_list = [1, 2, 3, 'firman', 'zaidin']
print("my_list: ", my_list)
my_list.extend(["adin", "bima"])
print("my_list extend adin: ", my_list)
del my_list[4]
print("delete index 4 of list: ", my_list)
my_list.remove("firman")
print("remove element `firman`: ", my_list, end='\n\n')

# find and sorting
my_list = [1, 2, 3, 'firman', 'zaidin', 'firman']
my_list_2 = [6, 3, 5, 2, 9]
print("find the index of: ", my_list.index("firman"))
print("counting repeated: ", my_list.count("firman"))
print("origin my_list_2: ", my_list_2)
# print("sorted my_list_2: ", sorted(my_list_2))
my_list_2.sort()
print("sorted my_list_2: ", my_list_2)
my_list_2.sort(reverse=True)
print("reverse=True my_list_2: ", my_list_2)
my_list_2.reverse()
print("reverse() my_list_2: ", my_list_2)
my_list_3 = my_list_2.copy()
print("copy my_list_2 into my_list_3: ", my_list_3)

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

length of my_list 5
length of my_list_2 5
add passed parameters as single element:  [1, 2, 3, 'firman', 'zaidin', [552, 21]]
extending list by adding all elements 1 by 1:  [4, 5, 3.142, 'papeda', 'ambon', 552, 21]
insert passed parameter in index 1:  [1, 'insert example', 2, 3, 'firman', 'zaidin', [552, 21]]
concatenation:  [1, 'insert example', 2, 3, 'firman', 'zaidin', [552, 21], 'concat example']
multiply:  [1, 'insert example', 2, 3, 'firman', 'zaidin', [552, 21], 1, 'insert example', 2, 3, 'firman', 'zaidin', [552, 21]]
my list back:  [1, 'insert example', 2, 3, 'firman', 'zaidin', [552, 21]]

my_list:  [1, 2, 3, 'firman', 'zaidin']
my_list extend adin:  [1, 2, 3, 'firman', 'zaidin', 'adin', 'bima']
delete index 4 of list:  [1, 2, 3, 'firman', 'adin', 'bima']
remove element `firman`:  [1, 2, 3, 'adin', 'bima']

find the index of:  3
counting repeated:  2
origin my_list_2:  [6, 3, 5, 2, 9]
sorted my_list_2:  [2, 3, 5, 6, 9]
reverse=True my_list_2:  [9, 6, 5, 3, 2]
reverse() my_list_2:  [2, 3, 5, 6, 9]
copy my_list_2 into my_list_3:  [2, 3, 5, 6, 9]

'''
