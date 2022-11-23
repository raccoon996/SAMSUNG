from collections import deque
import copy

import sys
sys.stdin = open("input.txt", "r")

N, M, H = list(map(int, input().split()))
line = []
for i in range(M):
    line_t = [list(map(int, input().split()))]
    line = line + line_t

graph = [[0 for _ in range(N+1)] for _ in range(H+1)]

for i in [0, N]:
    for j in range(H+1):
        graph[j][i] = 1

# 상, 하, 왼쪽, 오른쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

mn = 4

# 시도한 방법인지 
visit = []

for x, y in line:
    graph[x][y] = 2
    for i in [2, 3]:
        ny = y + dy[i]
        graph[x][ny] = 1

# for i in range(H+1):
#     print(graph[i])

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

def dfs(cnt, xy_num, dfs_graph):
    global N, H, mn
    if cnt > 3: # 3번 이상이면
    #     cnt = -1
        return  
    if game(dfs_graph): # 게임이 성공하면
        mn = min(mn, cnt)
        return

    for i in range(xy_num, (N-1)*H): # 선택된 곳 다음부터 확인
        x = i // (N-1) + 1
        y = i % (N-1) + 1
        t_graph = copy.deepcopy(dfs_graph)
        if dfs_graph[x][y] == 0:
            dfs_graph[x][y] = 2
            for i in [2, 3]:
                ny = y + dy[i]
                dfs_graph[x][ny] = 1
            dfs(cnt = cnt + 1, xy_num = i, dfs_graph = dfs_graph)
        dfs_graph = copy.deepcopy(t_graph)
    
dfs(cnt = 0, xy_num = 0, dfs_graph = graph)
if mn == 4:
    mn = -1
print(mn)