from collections import deque
from itertools import count
import sys
input = sys.stdin.readline


# 입력
# 종이 크기
N, M = list(map(int, input().split()))
paper = []
# 종이 안에 숫자
paper = [list(map(int, input().split())) for _ in range(N)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최대값에 대한 답 
ans = 0

# 블럭을 만드는 함수
def one_block(block_x, block_y, count, sum, visited_block): # block의 위치, count는 1-4 
    global ans
    visited = []
    if count == 3:
        ans = max(ans, sum) # 블럭 전체 합이 제일 큰것을 찾자        
        return
    
    for i in range(4): # 블럭 4방향 확인
        Temp_block_x = block_x +  dx[i]
        Temp_block_y = block_y +  dy[i]
        if Temp_block_x < 0 or Temp_block_x >= N or Temp_block_y < 0 or Temp_block_y >= M:
            continue
        elif [Temp_block_x, Temp_block_y] in visited_block:
            continue
        else:
            visited = visited_block + [[Temp_block_x,Temp_block_y]]
            one_block(Temp_block_x, Temp_block_y, count+1, sum + paper[Temp_block_x][Temp_block_y], visited)



for i in range(N): # x축
    for j in range(M): # y축
        block_count = 0
        block_sum = 0

        Temp_middle_finger = []

        out = 0
        for middle_finger in range(4):
            Temp_mf_x = i +  dx[middle_finger]
            Temp_mf_y = j +  dy[middle_finger]
            if Temp_mf_x < 0 or Temp_mf_x >= N or Temp_mf_y < 0 or Temp_mf_y >= M:
                if out == 2:
                    break
                out += 1
                continue
            else:
                Temp_middle_finger.append(paper[Temp_mf_x][Temp_mf_y])
        if out == 1:
            ans = max(ans, sum(Temp_middle_finger))
        else:
            ans = max(ans, sum(Temp_middle_finger)-min(Temp_middle_finger))
        block_sum = paper[i][j]
        visited = [[i, j]]
        one_block(i, j, block_count, block_sum, visited)

print(ans)
