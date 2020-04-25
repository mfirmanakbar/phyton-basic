second = 10
while second >= 0:
    print(second, end="->")
    second -= 1
print('blastoff!', end="\n\n")

counter = 0
while counter < 3:
    print("hello?")
    counter += 1
else:
    print("why you are not replying bro?")

# nested loop
count = 1
for i in range(10):
    print(str(i) * i)
    for j in range(0, i):
        count += 1

'''
10->9->8->7->6->5->4->3->2->1->0->blastoff!

hello?
hello?
hello?
why you are not replying bro?

1
22
333
4444
55555
666666
7777777
88888888
999999999
'''