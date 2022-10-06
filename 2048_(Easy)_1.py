from collections import deque
import sys
input = sys.stdin.readline

# 게임판 초기 상태
# 0은 빈칸, 숫자는 2의 제곱
# 최대 5번 이동시켜 가장 큰 블록을 출력

# 보드의 크기
N = int(input())
# 초기 상태
Box = []
for i in range(N):
    Box.append(list(input()))

# 이동 (상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# Lsit 한 줄에 대한 합 
def list_sum(num_list):
    Temp_column_list = num_list[:] + [0]
    Temp_num_old = 0
    Stack = []
    
    while Temp_column_list:
        # for _ in range(len(Temp_column_list)+1):
        Temp_num = int(Temp_column_list.pop(0))
        if Temp_num_old == 0: # 0인 경우
            Temp_num_old = Temp_num
        elif Temp_num_old == Temp_num: # 같으면 더하고 stack에 업데이트
            Stack.append(Temp_num_old + Temp_num)
            Temp_num_old, Temp_num = 0, 0
        elif Temp_num_old != Temp_num: # 같지 않으면 stack에 올리고 업데이트
            Stack.append(Temp_num_old)
            Temp_num_old = Temp_num
    Stack.extend([0]*(len(num_list)-len(Stack)))
    return Stack

def rotation(list_rotation): # 90도 행렬 회전
    n = len(list_rotation) # 행 x축
    m = len(list_rotation[0]) # 열 y축
    new = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new[j][m-i-1] = list_rotation[i][j]
    return new


def move(d_move): # 상, 하, 좌, 우
    if d_move == 0:
        for i in range(N):
            Box[i] = list_sum(Box)
    elif d_move == 1:
        






