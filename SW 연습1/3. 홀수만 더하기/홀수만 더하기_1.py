import copy
import sys

sys.stdin = open("input.txt", "r")

def findnum(list):
    temp_list = copy.deepcopy(list)
    for i in range(len(temp_list)):
        if temp_list[i]%2 != 1:
            temp_list[i] = 0
    return sum(temp_list)

T = int(input())
test = [0]*T
for i in range(T):
    test[i] = list(map(int, input().split()))

for i in range(T):
    print(f'#{i+1} {findnum(test[i])}')


