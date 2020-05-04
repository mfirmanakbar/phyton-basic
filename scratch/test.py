# calculate score by naming
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#
# sm = student_marks.get(query_name)
# ln = len(sm)
# sum_sm = sum(sm)
# answer = (sum_sm / ln)
# answer = '{0:.2f}'.format(answer)
# print(answer)

## second lowest score
# import copy
# n = 5
# # name = ['Harry', 'Berry', 'Tina', 'Akriti', 'Harsh']
# # score = [37.21, 37.21, 37.2, 41, 39]
# name = ['Harsh', 'Beria', 'Varun', 'Kakunami', 'Vikas']
# score = [20, 20, 19, 19, 21]
# score2 = copy.copy(score)
# score2 = set(score2)
# score2.remove(min(score2))
# min_score = min(score2)
# print(min_score)
# res_dct = {name[index]: score[index] for index, x in enumerate(name)}
# for key in sorted(res_dct.keys()):
#     ## print(key, " :: ", res_dct[key])
#     if res_dct[key] == min_score:
#         print(key)

## cubic
# x, y, z, n = 1, 1, 1, 2
# print([[a, b, c] for a in range(0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1) if a + b + c != n])

## runner-up / juara ke-2
# arr = [2, 3, 6, 6, 5]
# arr = set(arr)
# arr.remove(max(arr))
# print(arr.remove(max(arr)))
