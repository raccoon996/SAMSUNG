import sys
import copy
input = sys.stdin.readline

# 입력
# 종이 크기
N, M = list(map(int, input().split()))
paper = []
# 종이 안에 숫자
paper = [list(map(int, input().split())) for _ in range(N)]
# 지나갔으면 0으로 만들기


# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최대값에 대한 답 
ans = 0

# block 함수 DFS
def DFS_block(block_x, block_y, block_count, block_sum):
    global ans

    DFS_block_x = 0
    DFS_block_y = 0

    if block_count == 4:
        ans = max(ans, block_sum)
        return
    
    # 4방향 확인
    for i in range(4):
        # 한칸 이동
        DFS_block_x = block_x + dx[i]
        DFS_block_y = block_x + dy[i]
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

    for i in range(4):
        # 한칸 이동
        block_x += dx[i]
        block_y += dy[i]

        # extra block
        extra_count += 1
        extra_block.append(Temp_paper[block_x][block_y])
        extra_sum += Temp_paper[block_x][block_y]
        if extra_count == 3:
            ans = max(ans, extra_sum)
        elif extra_count == 4:
            extra_sum = extra_sum - min(extra_block)
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

