from collections import deque
import copy

import sys
sys.stdin = open("input.txt", "r")

def game(dfs_graph):
    global N, H
    x = 1
    y = 1
    stand = 0
    success = False
    while True:
        
        if x == H + 1: # 다 내려옴
            if not stand == 0: # 실패
                break
            y += 1 # 다음 칸으로 이동
            x = 1
            if y == N + 1: # 게임이 끝남
                success = True
                break
        if dfs_graph[x][y] == 2 or dfs_graph[x][y-1] == 2: # 우, 좌에 선이 있음
            T = dfs_graph[x][y] - dfs_graph[x][y-1]
            stand += (T) // abs(T)
            y += (T) // abs(T)
            x +=1
        else: # 없으면 아래로 한칸 이동
            x +=1
    return success

N, M, H = list(map(int, input().split()))
line = []
for i in range(M):
    line_t = [list(map(int, input().split()))]
    line = line + line_t

graph = [[0 for _ in range(N-1)] for _ in range(H)]


# 상, 하, 왼쪽, 오른쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

mn = 0

for x, y in line:
    x -= 1
    y -= 1
    graph[x][y] = 2

# for i in range(H):
#     print(graph[i])

cnt = [0 for _ in range(N-1)]

for i in range(N-1):
    for j in range(H):
        if graph[j][i] == 2:
            cnt[i] += 1

for i in range(N-1):
    if cnt[i] % 2 != 0:
        mn += 1

graph = [[0 for _ in range(N+1)] for _ in range(H+1)]
for i in [0, N]:
    for j in range(H+1):
        graph[j][i] = 1
for x, y in line:
    graph[x][y] = 2
    for i in [2, 3]:
        ny = y + dy[i]
        graph[x][ny] = 1

if mn != 0:
    if mn > 3:
        mn = -1
        print(-1)
    else:
        if H % 2 == 1:
            print(-1)
        else:
            print(mn)
else:
    if game(graph): # 게임이 성공하면
        print(0)
    else:
        print(-1)