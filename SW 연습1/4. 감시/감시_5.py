import copy
import sys

N, M = 0, 0
CCTV_cnt = 0 # CCTV 개수
CCTV_xy = [] # CCTV 좌표
visited = [] # CCTV 사용중인 것
zero_cnt = 0 # 사각지대 개수
CCTV_mode = [
    [],
    [[0], [1], [2], [3]], # 1
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]],

]

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

sys.stdin = open("input.txt", "r")
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

# 시야 함수
def look(ccx, ccy, type, z_cnt, box_temp): # z_cnt개수 반환
    global N, M
    for dir in type:
        nx = ccx
        ny = ccy
        while True:
            nx += dx[dir]
            ny += dy[dir]
            # map 밖으로 나가는 경우
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
            # 감시카메라나 벽에 부닥치는 경우
            #-----------------------------------
            if box_temp[nx][ny] != 0:
                # 중복으로 감시되는 경우
                if box_temp[nx][ny] == '#' or 0 < box_temp[nx][ny] <= 5: # 1, 2, 3, 4, 5
                    continue
                break
            box_temp[nx][ny] = '#'
            z_cnt -= 1
            # 감시 카메라는 통과한다.........
    return z_cnt

def dfs(cnt, z_cnt, box_graph):
    global CCTV_cnt, zero_cnt
    if cnt == CCTV_cnt: # 종료 조건
        zero_cnt = min(zero_cnt, z_cnt)
        return
    
    cx, cy = CCTV_xy[cnt]
    CCTV_type = box_graph[cx][cy]
    box_temp = copy.deepcopy(box_graph)
    z_cnt_temp = z_cnt

    for i in CCTV_mode[CCTV_type]:
        z_cnt = look(cx, cy, i, z_cnt, box_temp)
        dfs(cnt+1, z_cnt, box_temp)
        z_cnt = z_cnt_temp
        box_temp = copy.deepcopy(box_graph)

dfs(0, zero_cnt, box)
print(zero_cnt)
