# recursive
# array = [6, 19, 4, 55, 24, 30, 58, 45, 35, 17, 2, 9]
# n = 11 (n is last index of array if the length of array is 12 then last index is 11)
# highest = -1 (by default is min integer value is -1)

def find_biggest_number(arr, n, highest):
    if n is -1:
        return highest
    else:
        if arr[n] > highest:
            highest = arr[n]
        return find_biggest_number(arr, (n - 1), highest)


# iterative
def find_biggest_number_iterative(arr):
    biggestNumber = arr[0]
    for i in arr:
        if i > biggestNumber:
            biggestNumber = i
    return biggestNumber


array = [6, 19, 4, 55, 24, 30, 58, 45, 35, 17, 2, 9]

result = find_biggest_number_iterative(array)
print("iterative: ", result)

result = find_biggest_number(array, (len(array) - 1), -1)
print("recursive: ", result)

# there are 2 types of algorithm, there are iterative and recursive
