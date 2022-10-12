import copy
import sys
input = sys.stdin.readline

# 입력
N, M = list(map(int, input().split()))
lap = [list(map(int, input().split())) for _ in range(N)]

# N, M = 7, 7
# lap = [[2,0,0,0,1,1,0],[0,0,1,0,1,2,0],[0,1,1,0,1,0,0],[0,1,0,0,0,0,0],[0,0,0,0,0,1,1],[0,1,0,0,0,0,0],[0,1,0,0,0,0,0]]

two = []
for i in range(N):
    for j in range(M):
        if lap[i][j] == 2:
            two.append((i,j))


# 상,하,좌,우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

Temp = []
ans = 0

# 바이러스 함수
def covid():
    for two_num in range(len(two)):
        two_x, two_y = two[two_num]
        move(two_x, two_y)
    return

def move(x, y):
    for i in range(4): # 4방향으로 쭉 직진
        temp_x = x + dx[i]
        temp_y = y + dy[i]
        if 0 <= temp_x < N and 0 <= temp_y < M:
            if lap[temp_x][temp_y] == 0:
                lap[temp_x][temp_y] = 2
                move(temp_x,temp_y)
    return

def wall(start, count_wall):
    global N, M, ans, lap
    if count_wall == 3:
        copy_lap = copy.deepcopy(lap)
        covid()
        sum_zero = 0
        for sum_N in range(N):
            sum_zero += lap[sum_N].count(0)
        ans = max(ans, sum_zero)
        lap = copy.deepcopy(copy_lap)
        return
##################중요##########################
    for lap_i in range(start, N*M): # N*M 개의 칸을 좌표가 아닌 숫자로
        i = lap_i // M
        j = lap_i % M
        # 이전에 했던 경우를 다시 사용하지 않게 만들기
        if lap[i][j] == 0:
            lap[i][j] = 1
            wall(lap_i+1, count_wall+1)
            lap[i][j] = 0
#################중요##########################
wall(0, 0)
print(ans)
