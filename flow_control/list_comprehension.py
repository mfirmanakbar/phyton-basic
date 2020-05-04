print("non-list comprehension")
mylist = []
for i in range(0, 5):
    mylist.append(i)
print(mylist)

print("list comprehension")
mylist.clear()
mylist = [i for i in range(0, 5)]
print(mylist, end="\n\n")

print("non-list comprehension")
mylist.clear()
for i in range(0, 10):
    if i % 2 == 0:
        mylist.append(i * 5)
print(mylist)

print("list comprehension")
mylist.clear()
mylist = [i * 5 for i in range(0, 10) if i % 2 == 0]
print(mylist, end="\n\n")