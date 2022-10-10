import sys
import copy
input = sys.stdin.readline


# N, M = 5, 5
# paper = [[1,2,3,4,5],[5,4,3,2,1],[2,3,4,5,6],[6,5,4,3,2],[1,2,1,2,1]]

# N, M = 4, 5
# paper = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]

N, M = 4, 10
paper = [[1,2,1,2,1,2,1,2,1,2],[1,2,1,2,1,2,1,2,1,2],[1,2,1,2,1,2,1,2,1,2],[1,2,1,2,1,2,1,2,1,2]]

# # 입력
# # 종이 크기
# N, M = list(map(int, input().split()))
# paper = []
# # 종이 안에 숫자
# paper = [list(map(int, input().split())) for _ in range(N)]
# # 지나갔으면 0으로 만들기


# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최대값에 대한 답 
ans = 0

# block 함수 DFS
def DFS_block(block_x, block_y, block_count, block_sum):
    global ans

    if block_count == 4:
        ans = max(ans, block_sum)
        return
    
    # 4방향 확인
    for i in range(4):
        # 한칸 이동
        DFS_block_x = block_x + dx[i]
        DFS_block_y = block_y + dy[i]
        if 0 <= DFS_block_x < N and 0 <= DFS_block_y < M and Temp_paper[DFS_block_x][DFS_block_y] != 0:
            Temp_num = Temp_paper[DFS_block_x][DFS_block_y]
            Temp_paper[DFS_block_x][DFS_block_y] = 0
            DFS_block(DFS_block_x, DFS_block_y, block_count+1, block_sum+Temp_num)
            Temp_paper[DFS_block_x][DFS_block_y] = Temp_num

# extra 함수
# 예외 2가지 처리(모서리, 꼭지점)
def extra(block_x, block_y):
    global ans
    extra_count = 0
    extra_block = []
    extra_sum = 0

    if (block_x == 0 and block_y == 0) or (block_x == N - 1 and block_y == 0) or (block_x == 0 and block_y == M - 1) or (block_x == N - 1 and block_y == M - 1):
        # 꼭지점 부분
        return
    elif block_x == 0 or block_y == 0 or block_x == N - 1 or block_y == M - 1:
        # 모서리 부분
        if block_x == 0:
            extra_block = [Temp_paper[block_x+1][block_y], Temp_paper[block_x][block_y-1], Temp_paper[block_x][block_y+1]]
        elif block_y == 0:
            extra_block = [Temp_paper[block_x-1][block_y], Temp_paper[block_x+1][block_y], Temp_paper[block_x][block_y+1]]
        elif block_x == N - 1:
            extra_block = [Temp_paper[block_x-1][block_y], Temp_paper[block_x][block_y-1], Temp_paper[block_x][block_y+1]]
        elif block_y == M - 1:
            extra_block = [Temp_paper[block_x-1][block_y], Temp_paper[block_x+1][block_y], Temp_paper[block_x][block_y-1]]
        extra_sum = Temp_paper[block_x][block_y] + sum(extra_block)
    else: 
        # 4방향 모두 있을 수 있는 경우
        extra_block = [Temp_paper[block_x-1][block_y], Temp_paper[block_x+1][block_y], Temp_paper[block_x][block_y-1], Temp_paper[block_x][block_y+1]]
        extra_sum = Temp_paper[block_x][block_y] + sum(extra_block) - min(extra_block)

    ans = max(ans, extra_sum)


# main
Temp_paper = []
count = 0
# main 함수
for i in range(N):
    for j in range(M):
        Temp_paper = copy.deepcopy(paper) # 들렸던 곳 리셋
        Temp_num = Temp_paper[i][j] # 처음 들렸던 곳
        Temp_paper[i][j] = 0 # 처음 들렸던 곳

        # 함수 돌리기DFS
        DFS_block(i, j, count+1, Temp_num)
        Temp_paper[i][j] = Temp_num # 원상복구
        extra(i, j)

print(ans)

