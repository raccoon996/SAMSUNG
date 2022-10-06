from collections import deque
import copy
import sys
input = sys.stdin.readline

# 게임판 초기 상태
# 0은 빈칸, 숫자는 2의 제곱
# 최대 5번 이동시켜 가장 큰 블록을 출력

def move(d_move): # 상, 하 , 좌, 우 (이동)
    if d_move == 0: # 상
        for j in range(N): # y 축
            i_old = 0
            for i in range(1,N): # x 축
                if Box[i][j] != 0:
                    temp = Box[i][j]
                    Box[i][j] = 0
                    if Box[i_old][j] == 0:
                        Box[i_old][j] = temp
                    elif Box[i_old][j] == temp:
                        Box[i_old][j] *= 2
                        i_old += 1
                    elif Box[i_old][j] != temp:
                        i_old += 1
                        Box[i_old][j] = temp

    elif d_move == 1: # 하
        for j in range(N): # y 축
            i_old = N - 1
            for i in range(N-2,-1,-1): # x 축
                if Box[i][j] != 0:
                    temp = Box[i][j]
                    Box[i][j] = 0
                    if Box[i_old][j] == 0:
                        Box[i_old][j] = temp
                    elif Box[i_old][j] == temp:
                        Box[i_old][j] *= 2
                        i_old -= 1
                    elif Box[i_old][j] != temp:
                        i_old -= 1
                        Box[i_old][j] = temp

    elif d_move == 2: # 좌
        for i in range(N): # x 축
            j_old = N - 1
            for j in range(N-2,-1,-1): # y 축
                if Box[i][j] != 0:
                    temp = Box[i][j]
                    Box[i][j] = 0
                    if Box[i][j_old] == 0:
                        Box[i][j_old] = temp
                    elif Box[i][j_old] == temp:
                        Box[i][j_old] *= 2
                        j_old -= 1
                    elif Box[i][j_old] != temp:
                        j_old -= 1
                        Box[i][j_old] = temp

    elif d_move == 3: # 우
        for i in range(N): # x 축
            j_old = 0
            for j in range(1,N): # y 축
                if Box[i][j] != 0:
                    temp = Box[i][j]
                    Box[i][j] = 0
                    if Box[i][j_old] == 0:
                        Box[i][j_old] = temp
                    elif Box[i][j_old] == temp:
                        Box[i][j_old] *= 2
                        j_old += 1
                    elif Box[i][j_old] != temp:
                        j_old += 1
                        Box[i][j_old] = temp                    

def dfs_count(count):
    global ans, Box
    if count == 5: # 5 번까지만 확인 (5번이 최대)
        for i in range(N): # 보드판 크기만큼 x 축
            ans = max(ans, max(Box[i])) # 뭐지????
        return

    copyBox = copy.deepcopy(Box)
    for i in range(4): # 4 방향
        move(i) # 여기서 변하고 
        dfs_count(count + 1) # 재귀함수로 DFS 알고리즘 완성
        Box = copy.deepcopy(copyBox) # 다시 리셋


# 보드의 크기
N = int(input())
# 초기 상태
Box = []
# for i in range(N):
#     Box = list(map(int, input().split()))
Box = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs_count(0)
print(ans)