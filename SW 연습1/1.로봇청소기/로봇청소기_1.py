from collections import deque
import sys

sys.stdin = open("input.txt", "r")
# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 청소기 알고리즘
def robot(bot_r, bot_c, dir):
    end = False
    while True: # 1번
        if end == True:
            print(count)
            break
        # 지금 있는 곳을 들른 곳으로 만든다.
        visited[bot_r][bot_c] = True
        count = 1

        while True: # 2번
            left = (dir - 1 + 4) % 4
            temp_bot_r = bot_r + dx[left]
            temp_bot_c = bot_c + dy[left]
            if visited[temp_bot_r][temp_bot_c] == False: # 2-1번
                count += 1
                dir = (dir - 1 + 4) % 4
                bot_r = temp_bot_r
                bot_c = temp_bot_c
                break
            elif box[temp_bot_r][temp_bot_c] == 1: # 2-2번
                dir = (dir - 1 + 4) % 4
                continue # 2번 반복
            elif visited[bot_r-1][bot_c] == True and visited[bot_r+1][bot_c] == True and visited[bot_r][bot_c-1] == True and visited[bot_r][bot_c+1] == True: # 2-3번
                back = (dir + 2) % 4 # 뒤 가기
                bot_r = bot_r + dx[back]
                bot_c = bot_c + dy[back]
                continue # 2번 반복
            elif visited[bot_r-1][bot_c] == True and visited[bot_r+1][bot_c] == True and visited[bot_r][bot_c-1] == True and box[bot_r][bot_c+1] == 1: # 2-4번
                end = True
                break


N, M = list(map(int, input().split()))
r, c, dir = list(map(int, input().split()))
# 방향은 상 우 하 좌 [0 1 2 3]  

visited = [[False for j in range(M)] for i in range(N)]

box = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            visited[i][j] = True

robot(r, c, dir)


