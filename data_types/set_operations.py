# init, adding
my_set = {1, 2, 3, 4, 4, 5, 5, 5}
print("my_set: ", my_set)
my_set.add(6)
print("adding 6: ", my_set, end="\n\n")

# other methods in sets
my_set = {1, 2, 3, 4}
my_set_2 = {3, 4, 5, 6}
print("my_set: ", my_set)
print("my_set_2: ", my_set_2)
print("union: ", my_set.union(my_set_2), " <==> ", my_set | my_set_2)
print("intersection: ", my_set.intersection(my_set_2), " <==> ", my_set & my_set_2)  # intersection/persimpangan/yg sama
print("difference from set: ", my_set.difference(my_set_2), " <==> ", my_set - my_set_2)
print("difference from set_2: ", my_set_2.difference(my_set), " <==> ", my_set_2 - my_set)
print("difference all value: ", my_set_2.symmetric_difference(my_set), " <==> ", my_set_2 ^ my_set, end="\n\n")

# operators with set
superset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print("superset: ", superset)
print("s1: ", s1)
print("s2: ", s2)
print("if symmetric --> (s1 == s2): ", s1 == s2)
print("if not symmetric --> (s1 != s2): ", s1 != s2)
print("if s1 a subset of superset --> (s1 <= superset): ", s1 <= superset)  # subset/bagian
print("if s1 a proper subset of superset  --> (s1 < superset): ", s1 < superset)  # proper subset/bagian yang tepat
print("if s2 a subset of s1  --> (s1 >= s2): ", s1 >= s2)
print("if s2 a proper subset of s1  --> (s1 > s2): ", s1 > s2, end="\n\n")

''''
my_set:  {1, 2, 3, 4, 5}
adding 6:  {1, 2, 3, 4, 5, 6}

my_set:  {1, 2, 3, 4}
my_set_2:  {3, 4, 5, 6}
union:  {1, 2, 3, 4, 5, 6}  <==>  {1, 2, 3, 4, 5, 6}
intersection:  {3, 4}  <==>  {3, 4}
difference from set:  {1, 2}  <==>  {1, 2}
difference from set_2:  {5, 6}  <==>  {5, 6}
difference all value:  {1, 2, 5, 6}  <==>  {1, 2, 5, 6}

superset:  {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s1:  {1, 2, 3, 4}
s2:  {3, 4, 5, 6}
if symmetric --> (s1 == s2):  False
if not symmetric --> (s1 != s2):  True
if s1 a subset of superset --> (s1 <= superset):  True
if s1 a proper subset of superset  --> (s1 < superset):  True
if s2 a subset of s1  --> (s1 >= s2):  False
if s2 a proper subset of s1  --> (s1 > s2):  False
'''