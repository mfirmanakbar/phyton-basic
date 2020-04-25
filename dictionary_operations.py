# init Dictionary
my_dict = {1: 'phyton', 2: 'golang'}
my_dict_2 = dict({1: 'car', 2: 'ice'})
print("my_dict:", my_dict)
print("my_dict_2:", my_dict_2, end="\n\n")

# accessing element and changing
my_dict = {"First": "python", "second": "golang"}
print("get second", my_dict["second"])
print("get First", my_dict.get("First"))
print("original data: ", my_dict)
my_dict["second"] = "java"
print("change second: ", my_dict)
my_dict["third"] = "ruby"
print("adding third: ", my_dict, end="\n\n")

# removing
print("original data: ", my_dict)
a = my_dict.pop("third")
print("after pop third: ", my_dict)
b = my_dict.popitem()
print("after popitem: ", my_dict)
my_dict.clear()
print("clear: ", my_dict, end="\n\n")

# other functions
my_dict = {"First": "python", "second": "golang", "third": "java"}
print("my_dict.keys(): ", my_dict.keys())
print("my_dict.values(): ", my_dict.values())
print("my_dict.items(): ", my_dict.items())

'''
my_dict: {1: 'phyton', 2: 'golang'}
my_dict_2: {1: 'car', 2: 'ice'}

get second golang
get First python
original data:  {'First': 'python', 'second': 'golang'}
change second:  {'First': 'python', 'second': 'java'}
adding third:  {'First': 'python', 'second': 'java', 'third': 'ruby'}

original data:  {'First': 'python', 'second': 'java', 'third': 'ruby'}
after pop third:  {'First': 'python', 'second': 'java'}
after popitem:  {'First': 'python'}
clear:  {}

my_dict.keys():  dict_keys(['First', 'second', 'third'])
my_dict.values():  dict_values(['python', 'golang', 'java'])
my_dict.items():  dict_items([('First', 'python'), ('second', 'golang'), ('third', 'java')])
'''