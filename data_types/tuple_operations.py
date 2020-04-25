# initialize tuples
my_tuple = ()
my_tuple_2 = tuple()
print("empty my_tuple:", my_tuple)
print("empty my_tuple_2:", my_tuple_2)
my_tuple = my_tuple + (1, 2, 3)
print("init my_tuple from plus: ", my_tuple, end="\n\n")

# initialize elements to the tuple
my_tuple = (1, 2, 3)
my_tuple_2 = tuple(("python", "for", "firman"))
print("data type: ", type(my_tuple))
print("my_tuple_2: ", my_tuple_2, end="\n\n")

# accessing element of tuple
my_tuple = (1, 2, 3)
my_tuple_2 = ("python", "for", "firman")
my_tuple_3 = (4, 5, 6, ["golang", "ruby"])
print("get index 0 -> my_tuple[0]", my_tuple[0])
print("get all -> my_tuple_2[:]", my_tuple_2[:])
print("get ruby -> my_tuple_3[3][1]", my_tuple_3[3][1], end="\n\n")

# changing element of tuple
my_tuple_3 = (4, 5, 6, ["golang", "ruby"])
my_tuple_3[3][1] = "java"
print("change ruby to java -> my_tuple_3: ", my_tuple_3)

'''
empty my_tuple: ()
empty my_tuple_2: ()
init my_tuple from plus:  (1, 2, 3)

data type:  <class 'tuple'>
my_tuple_2:  ('python', 'for', 'firman')

get index 0 -> my_tuple[0] 1
get all -> my_tuple_2[:] ('python', 'for', 'firman')
get ruby -> my_tuple_3[3][1] ruby

change ruby to java -> my_tuple_3:  (4, 5, 6, ['golang', 'java'])
'''