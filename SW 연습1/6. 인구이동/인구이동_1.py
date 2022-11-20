from collections import deque

import sys
sys.stdin = open("input.txt", "r")

# 입력
N, L, R = list(map(int, input().split()))
area = [list(map(int, input().split())) for _ in range(N)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 연합이 있는 지 없는 지
Union = [i for i in range(N*N)] # 국가들
Union_Num = 1
Union_N = [0] # 연합 국가수 # 다음 연합의 list를 어떻게 늘린건지???????????
Union_N_pop = [0] # 연합 인구수 # 다음 연합의 list를 어떻게 늘린건지???????????

def BFS():
    global Union_Num
    Union_temp = deque()
    Union_temp.append([0, 0])
    while True:
        # 연합 추가 조건
        if len(Union_temp) == 0: # 더 이상 연합할 국가가 없음
            Union_N = Union_N + [0]
            Union_Num += 1
            if Union == []: # 비어있으면 # 종료조건
                # 계산
                for i in range(len(Union_N)):
                    popular = Union_N_pop[i] // Union_N[i]
                    # 연합국에 넣어야 하는데...
                break

        for _ in range(len(Union_temp)):
            x, y = Union_temp.popleft()
            for i in range(4): # 4개 방향과 비교
                nx, ny = x, y
                nx += dx[i]
                ny += dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N : # area 밖으로 나가는 경우
                    continue
                standard = area[x][y]
                # 인구 수 차이 조건에 만족
                if standard - R <= area[nx][ny] <= standard - L or standard + L <= area[nx][ny] <= standard + R:
                    temp = (nx * N) + ny
                    if temp in Union: # Union이 아직 연합에 등록이 되지 않았으면
                        Union_temp.append([x, y])
                        Union.remove(temp) # 연합에 등록되어서 연합 안된 리스트에서 제거
                        Union_N[Union_Num - 1] += 1 # 연합 국가수 추가
                        Union_N_pop[Union_Num - 1] += area[x][y] # 연합 인구 추가
    
    

        
                        

            
