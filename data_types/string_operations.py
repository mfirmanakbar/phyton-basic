my_str = "welcome to the tutorial"
my_str_2 = "this is my string"
print(my_str)
print(my_str_2, end="\n\n")

print("print all: ", my_str[:])
print("from index 2 until index 9 and skip index 10: ", my_str[2:10])
print("from index 0 until index 13 and skipping 1 element: ", my_str[0:14:1])
print("from index 0 until index 13 and skipping 2 elements: ", my_str[0:14:2])
print("my_str[::-1]: ", my_str[::-1])
print("my_str[-7:-1]: ", my_str[-7:-1], end="\n\n")

# other function
my_str = "welcome to the tutorial"
print("length: ", len(my_str))
print("count `t`: ", my_str.count("t"))
print("lower: ", my_str.lower())
print("upper: ", my_str.upper())
print("find `l`: ", my_str.find("l")) # return index of the element found
print("partition `to`: ", my_str.partition("to")) # breaks the string into tuple for the element passed
print("split space: ", my_str.split(" "))
print("replace `welcome` to `hi, welcome`: ", my_str.replace("welcome", "hi, welcome"), end="\n\n")
