# import copy
# import sys

# sys.stdin = open("input.txt", "r")

# def findnum(list):
#     temp_list = copy.deepcopy(list)
#     for i in range(len(temp_list)):
#         if temp_list[i]%2 != 1:
#             temp_list[i] = 0
#     return sum(temp_list)

T = int(input())
test = [0]*T
ans = [0]*T
for i in range(T):
    test[i] = list(map(int, input().split()))

for i in range(T):
    for j in range(len(test[i])):
        if test[i][j]%2 != 1:
            test[i][j] = 0
    ans[i] = sum(test[i])
    print(f'#{i+1} {ans[i]}')


