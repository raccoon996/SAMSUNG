from collections import deque
import sys
input = sys.stdin.readline

n, m= map(int, input().split)
Box = []

for i in range(n):
    Box.append(list(input()))
    for j in range(m):
        if Box[i][j] == 'R':
            rm, rn = i, j
        elif Box[i][j] == 'B':
            bm, bn = i, j


# BFS함수
def bfs(rm, rn, bm, bn):
    # 초기화
    q = deque()
    q.append((rm, rn, bm, bn))
    visited = []
    visited.append((rm, rn, bm, bn))

    # 이동 상, 하, 좌, 우
    move_m = [-1, 1, 0, 0]
    move_n = [-1, 1, 0, 0]

    # BFS 알고리즘 
    for _ in range(q):
        
        # 빨간 공
        temp_rm, temp_rn = rm, rn
        for i in range(4):
            


