import copy
import sys

sys.stdin = open("input.txt", "r")

N, M = list(map(int, input().split()))
box = [0]*N
CCTV_cnt = 0
CCTV_xy = []
visited = []
mx = 0
zero_cnt = 0

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    box[i] = list(map(int, input().split()))
    for j in range(len(box[i])):
        if 0 < box[i][j] < 6:
            CCTV_cnt += 1
            CCTV_xy = CCTV_xy + [[i, j]] # 리스트 합치기
        if box[i][j] == 0:
            zero_cnt += 1


def vis(cnt, CCTV_x, CCTV_y):
    global visited
    # 다음 것으로
    if [CCTV_x, CCTV_y] not in visited:
        visited = visited + [[CCTV_x, CCTV_y]]
        dfs(cnt + 1)
        visited.remove([CCTV_x, CCTV_y])


def dfs(cnt):
    global N, CCTV_cnt, box, mx
    shap_cnt = 0
    if cnt == CCTV_cnt:
        for i in range(N):
            shap_cnt += box[i].count('#')
        mx = max(mx, shap_cnt)
        return
     
    CCTV_x, CCTV_y = CCTV_xy[cnt]
    temp_box = copy.deepcopy(box)
    # CCTV 종류
    box[CCTV_x][CCTV_y]
    if box[CCTV_x][CCTV_y] == 1:
        for i in range(4): # 상, 우, 하, 좌 # CCTV 돌려보기
            n_x, n_y = CCTV_x, CCTV_y
            while True:
                n_x += dx[i]
                n_y += dy[i]
                if 0 <= n_x < N and 0 <= n_y < M: # box 안
                    if box[n_x][n_y] == '#' or box[n_x][n_y] == 0:
                        box[n_x][n_y] = '#'
                    else:
                        break
                else:
                    break
            vis(cnt, CCTV_x, CCTV_y)
            box = copy.deepcopy(temp_box)

    elif box[CCTV_x][CCTV_y] == 2:
        for i in range(2): # CCTV 돌려보기
            n_x1, n_y1 = CCTV_x, CCTV_y
            n_x2, n_y2 = CCTV_x, CCTV_y
            while True:
                n_x1 += dx[i]
                n_y1 += dy[i]
                if 0 <= n_x1 < N and 0 <= n_y1 < M: # box 안
                    if box[n_x1][n_y1] == '#' or box[n_x1][n_y1] == 0:
                        box[n_x1][n_y1] = '#'
                    else:
                        break
                else:
                    break
            
            while True:
                n_x2 -= dx[i]
                n_y2 -= dy[i]
                if 0 <= n_x2 < N and 0 <= n_y2 < M: # box 안
                    if box[n_x2][n_y2] == '#' or box[n_x2][n_y2] == 0:
                        box[n_x2][n_y2] = '#'
                    else:
                        break
                else:
                    break
            vis(cnt, CCTV_x, CCTV_y)
            box = copy.deepcopy(temp_box)
            
    elif box[CCTV_x][CCTV_y] == 3:
        for i in range(4): # CCTV 돌려보기
            n_x1, n_y1 = CCTV_x, CCTV_y
            n_x2, n_y2 = CCTV_x, CCTV_y
            while True:
                n_x1 += dx[i]
                n_y1 += dy[i]
                if 0 <= n_x1 < N and 0 <= n_y1 < M: # box 안
                    if box[n_x1][n_y1] == '#' or box[n_x1][n_y1] == 0:
                        box[n_x1][n_y1] = '#'
                    else:
                        break
                else:
                    break
            while True:
                n_x2 += dx[(i+1)%4]
                n_y2 += dy[(i+1)%4]
                if 0 <= n_x2 < N and 0 <= n_y2 < M: # box 안
                    if box[n_x2][n_y2] == '#' or box[n_x2][n_y2] == 0:
                        box[n_x2][n_y2] = '#'
                    else:
                        break
                else:
                    break
            vis(cnt, CCTV_x, CCTV_y)
            box = copy.deepcopy(temp_box)

    elif box[CCTV_x][CCTV_y] == 4:
        for i in range(4): # 상, 우, 하, 좌 # CCTV 돌려보기
            n_x1, n_y1 = CCTV_x, CCTV_y
            n_x2, n_y2 = CCTV_x, CCTV_y
            n_x3, n_y3 = CCTV_x, CCTV_y
            while True:
                n_x1 += dx[i]
                n_y1 += dy[i]
                if 0 <= n_x1 < N and 0 <= n_y1 < M: # box 안
                    if box[n_x1][n_y1] == '#' or box[n_x1][n_y1] == 0:
                        box[n_x1][n_y1] = '#'
                    else:
                        break
                else:
                    break
            while True:
                n_x2 += dx[(i+1)%4]
                n_y2 += dy[(i+1)%4]
                if 0 <= n_x2 < N and 0 <= n_y2 < M: # box 안
                    if box[n_x2][n_y2] == '#' or box[n_x2][n_y2] == 0:
                        box[n_x2][n_y2] = '#'
                    else:
                        break
                else:
                    break
            while True:
                n_x3 += dx[(i+2)%4]
                n_y3 += dy[(i+2)%4]
                if 0 <= n_x3 < N and 0 <= n_y3 < M: # box 안
                    if box[n_x3][n_y3] == '#' or box[n_x3][n_y3] == 0:
                        box[n_x3][n_y3] = '#'
                    else:
                        break
                else:
                    break
            vis(cnt, CCTV_x, CCTV_y)
            box = copy.deepcopy(temp_box)

    elif box[CCTV_x][CCTV_y] == 5:  
        i = 0
        n_x1, n_y1 = CCTV_x, CCTV_y
        n_x2, n_y2 = CCTV_x, CCTV_y
        n_x3, n_y3 = CCTV_x, CCTV_y
        n_x4, n_y4 = CCTV_x, CCTV_y
        while True:
            n_x1 += dx[i]
            n_y1 += dy[i]
            if 0 <= n_x1 < N and 0 <= n_y1 < M: # box 안
                if box[n_x1][n_y1] == '#' or box[n_x1][n_y1] == 0:
                        box[n_x1][n_y1] = '#'
                else:
                    break
            else:
                break
        while True:
            n_x2 += dx[(i+1)%4]
            n_y2 += dy[(i+1)%4]
            if 0 <= n_x2 < N and 0 <= n_y2 < M: # box 안
                if box[n_x2][n_y2] == '#' or box[n_x2][n_y2] == 0:
                        box[n_x2][n_y2] = '#'
                else:
                    break
            else:
                break
        while True:
            n_x3 += dx[(i+2)%4]
            n_y3 += dy[(i+2)%4]
            if 0 <= n_x3 < N and 0 <= n_y3 < M: # box 안
                if box[n_x3][n_y3] == '#' or box[n_x3][n_y3] == 0:
                        box[n_x3][n_y3] = '#'
                else:
                    break
            else:
                break
        while True:
            n_x4 += dx[(i+3)%4]
            n_y4 += dy[(i+3)%4]
            if 0 <= n_x4 < N and 0 <= n_y4 < M: # box 안
                if box[n_x4][n_y4] == '#' or box[n_x4][n_y4] == 0:
                        box[n_x4][n_y4] = '#'
                else:
                    break
            else:
                break
        vis(cnt, CCTV_x, CCTV_y)
        box = copy.deepcopy(temp_box)

dfs(0)
print(zero_cnt - mx)