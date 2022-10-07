from collections import deque
import sys
input = sys.stdin.readline

# # N 개 시험장
# N = int(input())
# # 각 시험장당 응시자 수
# A = list(map(int, input().split()))
# B, C = map(int, input().split()) # 총감독관 가시인원, 부감독관 감시자 수

# N = 5
# A = [1000000, 1000000, 1000000, 1000000, 1000000]
# B, C = 5, 7

# N = 5
# A = [10, 9, 10, 9, 10]
# B, C = 7, 2

N = 1
A = [1]
B, C = 2, 1


# 최소 감독관 수
min_ans = 0

for i in range(N):
    
    if (A[i] - B) < 0:
        min_ans += 1
    else:
        min_ans += ((A[i] - B) / C ) + 1 # 부감독관 + 총감독관
        
    if min_ans != int(min_ans):
        min_ans = int(min_ans) + 1
print(int(min_ans))
