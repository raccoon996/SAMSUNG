import copy
import sys

sys.stdin = open("input.txt", "r")


CCTV_cnt = 0 # CCTV 개수
CCTV_xy = [] # CCTV 좌표
visited = [] # CCTV 사용중인 것
zero_cnt = 0 # 사각지대 개수

# 입력
N, M = list(map(int, input().split()))

box = [0 for _ in range(N)]

for i in range(N):
    box[i] = list(map(int, input().split()))
    for j in range(len(box[i])):
        if 0 < box[i][j] < 6:
            CCTV_cnt += 1
            CCTV_xy = CCTV_xy + [[i, j]] # 리스트 합치기
        if box[i][j] == 0:
            zero_cnt += 1

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 시야 함수
def look(ccx, ccy, dir, z_cnt): # z_cnt개수 반환
    global N, M
    nx = ccx
    ny = ccy
    while True:
        nx += dx[dir]
        ny += dy[dir]
        # map 밖으로 나가는 경우
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            break
        # 감시카메라나 벽에 부닥치는 경우
        if box[nx][ny] != 0:
            # 중복으로 감시되는 경우
            if box[nx][ny] == '#':
                continue
            break
        box[nx][ny] = '#'
        z_cnt -= 1
    return z_cnt

def dfs(cnt, z_cnt):
    global CCTV_cnt, zero_cnt, box
    if cnt == CCTV_cnt:
        zero_cnt = min(zero_cnt, z_cnt)
        return
    box_temp = copy.deepcopy(box)
    z_cnt_temp = z_cnt
    # CCTV 개수만큼
    for i in range(cnt, CCTV_cnt): # start, stop
        cx, cy = CCTV_xy[i]
        CCTV_type = box[cx][cy]
        if CCTV_type == 1:
            for dir in range(4): # 상, 우, 하, 좌
                z_cnt = look(cx, cy, dir, z_cnt)
                # 다음 CCTV
                dfs(cnt+1, z_cnt)
                # 복구
                box = copy.deepcopy(box_temp)
                z_cnt = z_cnt_temp
        elif CCTV_type == 2:
            for dir in range(2): # 상, 우
                z_cnt = look(cx, cy, dir, z_cnt)
                z_cnt = look(cx, cy, dir+2, z_cnt)
                # 다음 CCTV
                dfs(cnt+1, z_cnt)
                # 복구
                box = copy.deepcopy(box_temp)
                z_cnt = z_cnt_temp
        elif CCTV_type == 3:
            for dir in range(4): # 상, 우, 하, 좌
                z_cnt = look(cx, cy, dir, z_cnt)
                z_cnt = look(cx, cy, (dir+1)%4, z_cnt)
                # 다음 CCTV
                dfs(cnt+1, z_cnt)
                # 복구
                box = copy.deepcopy(box_temp)
                z_cnt = z_cnt_temp
        elif CCTV_type == 4:
            for dir in range(4): # 상, 우, 하, 좌
                z_cnt = look(cx, cy, dir, z_cnt)
                z_cnt = look(cx, cy, (dir+1)%4, z_cnt)
                z_cnt = look(cx, cy, (dir+2)%4, z_cnt)
                # 다음 CCTV
                dfs(cnt+1, z_cnt)
                # 복구
                box = copy.deepcopy(box_temp)
                z_cnt = z_cnt_temp
        elif CCTV_type == 5:
            # 상
            dir = 0
            z_cnt = look(cx, cy, dir, z_cnt)
            z_cnt = look(cx, cy, dir+1, z_cnt)
            z_cnt = look(cx, cy, dir+2, z_cnt)
            z_cnt = look(cx, cy, dir+3, z_cnt)
            # 다음 CCTV
            dfs(cnt+1, z_cnt)
            # 복구
            box = copy.deepcopy(box_temp)
            z_cnt = z_cnt_temp

dfs(0, zero_cnt)
print(zero_cnt)