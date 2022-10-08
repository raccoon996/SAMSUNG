from collections import deque
import sys
input = sys.stdin.readline

N, M = 5, 5
paper = [[1,2,3,4,5],[5,4,3,2,1],[2,3,4,5,7],[6,5,4,3,2],[1,2,1,2,1]]

# # 입력
# # 종이 크기
# N, M = list(map(int, input().split()))
# paper = []
# # 종이 안에 숫자
# paper = [list(map(int, input().split())) for _ in range(N)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최대값에 대한 답
ans = 0

def max_index():
    # paper의 최대값 찾기
    paper_max = list(map(max, paper)) # 각 즐의 최대값
    print(max(paper_max))
    paper_index1 = paper_max.index(max(paper_max)) # 최대값의 x좌표
    paper_index2 = paper[paper_index1].index(max(paper_max)) # 최대값의 y좌표
    return paper_index1, paper_index2

# 블럭을 만드는 함수
def one_block(block_x, block_y, count): # block의 위치, count는 1-4 
    block_shape = []
    
    for i in range(4): # 블럭 4방향 확인
        Temp_block_x = block_x +  dx[i]
        Temp_block_y = block_y +  dy[i]
        block_shape = one_block(Temp_block_x, Temp_block_y, count+1)

    if count == 4:
        block_shape.append([block_x, block_y])
        return block_shape
        
# 블럭을 사용했는 지 확인
# def block_visited():