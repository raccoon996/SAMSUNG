# from collections import deque
# import sys

# sys.stdin = open("input.txt", "r")
# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 청소기 알고리즘
def robot(bot_r, bot_c, dir):
    cnt = 1

    while True:
        # 1번 현재자리 청소
        box[bot_r][bot_c] = 2
        # 2번
        for k in range(dir-1, dir -1 -4 ,-1):
            k += 4
            k = k % 4
            temp_bot_r = bot_r + dx[k]
            temp_bot_c = bot_c + dy[k]
            # 왼쪽이 청소 되었는 지 확인
            if box[temp_bot_r][temp_bot_c] == 0:
                dir = k
                bot_r = temp_bot_r
                bot_c = temp_bot_c
                cnt += 1
                break
        
        # 4 방향 모두 청소 되어있음 or 벽이 있던
        else: # for문과 이어지는 else문
            temp_bot_r = bot_r - dx[dir]
            temp_bot_c = bot_c - dy[dir]
            if box[temp_bot_r][temp_bot_c] != 1:
                bot_r = temp_bot_r
                bot_c = temp_bot_c
            else:
                break
    print(cnt)   
            


N, M = list(map(int, input().split()))
r, c, dir = list(map(int, input().split()))
# 방향은 상 우 하 좌 [0 1 2 3]  
box = [list(map(int, input().split())) for _ in range(N)]


robot(r, c, dir)


