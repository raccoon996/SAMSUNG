from collections import deque

import sys
sys.stdin = open("input.txt", "r")

# 입력
N, L, R = list(map(int, input().split()))
area = [list(map(int, input().split())) for _ in range(N)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visit = [[False] * N for _ in range(N)]

def bfs(x,y):
    global visit
    dq = deque()
    dq.append([x, y])
    visit[x][y] = True

    union = [[x, y]]    
    count = area[x][y]

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if visit[nx][ny]:
                continue
            if L <= abs(area[x][y] - area[nx][ny]) <= R:
                dq.append([nx, ny])
                visit[nx][ny] = True

                count += area[nx][ny]
                union = union + [[nx, ny]]
    for x, y in union:
        area[x][y] = count // len(union)
    return len(union) # 2 이상이면 연합인것

def main(day):
    global visit
    result = day
    while True:
        flag = False
        visit = [[False] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if not visit[i][j]:
                    if bfs(i, j) > 1:
                        flag = True
        if not flag:
            break
        result += 1
    return result

result = main(day = 0)
print(result)