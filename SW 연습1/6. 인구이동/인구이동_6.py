# 실패 77% 시관초과
from collections import deque

import sys
sys.stdin = open("input.txt", "r")

# 입력
N, L, R = list(map(int, input().split()))
area = [list(map(int, input().split())) for _ in range(N)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
Union_N = [] # 각 연합 국가수
Union_N_pop = [] # 각 연합 인구수
Union_List = [False for i in range(N*N)] # 국가들 - N 번째 연합 넣기
Union_Day_List = [i for i in range(N*N)] # 국가들 - 하루에 연합에 넣은 것 빼기
visit = [[False] * N for _ in range(N)]

def BFS(Union_Num, area_N):
    global N, Union_N, Union_N_pop, Union_List, Union_Day_List
    Union_temp = deque() # 각 연합 인구수 비교를 위해
    x = area_N // N
    y = area_N % N
    Union_temp.append([x, y]) # 초기 비교 시작
    Union_N[Union_Num] += 1 # 연합 국가수 추가
    Union_N_pop[Union_Num] += area[x][y] # 연합 인구 추가
    Union_List[area_N] = Union_Num # N번째 연합 등록
    Union_Day_List.remove(area_N) # 연합에 등록되어서 연합 안된 리스트에서 제거
    visit[x][y] = True
    while Union_temp:
        x, y = Union_temp.popleft() # 기준이 되는 국가
        for i in range(4): # 4개 방향과 비교
            nx, ny = x, y
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N : # area 밖으로 나가는 경우
                continue
            if visit[nx][ny]:
                continue

            # 인구 수 차이 조건에 만족
            if area[x][y] - R <= area[nx][ny] <= area[x][y] - L or area[x][y] + L <= area[nx][ny] <= area[x][y] + R:
                temp_area_N = (nx * N) + ny
                if temp_area_N in Union_Day_List: # Union이 아직 연합에 등록이 되지 않았으면
                    Union_temp.append([nx, ny])
                    visit[nx][ny] = True
                    Union_N[Union_Num] += 1 # 연합 국가수 추가
                    Union_N_pop[Union_Num] += area[nx][ny] # 연합 인구 추가
                    Union_List[temp_area_N] = Union_Num # N번째 연합 등록
                    Union_Day_List.remove(temp_area_N) # 연합에 등록되어서 연합 안된 리스트에서 제거

def main(Union_Num, area_N, day):
    global N, Union_N, Union_N_pop, Union_List, Union_Day_List, visit
    while True:
        if Union_Day_List: # 아직 연합 안됨 리스트에 남았으면
            area_N = Union_Day_List[0]
            Union_N_pop = Union_N_pop + [0]
            Union_N = Union_N + [0]
            Union_Num += 1
            BFS(Union_Num, area_N)
        else: # 이제 인구이동
            if len(Union_N) == N*N: # 이제 더 이상 인구이동이 없으면 종료
                print(day) # 인구 이동이 발생한 일수
                return # 종료
            for i in range(len(Union_N)):
                pop = Union_N_pop[i] // Union_N[i] # 인구 계산
                for j in range(N*N): # 인구 넣기
                    if Union_List[j] == i: # N번째 연합
                        x = j // N
                        y = j % N
                        area[x][y] = pop
            # 다음날 비교
            # 초기화
            Union_Num = 0 # 연합 number
            Union_N = [0] # 각 연합 국가수
            Union_N_pop = [0] # 각 연합 인구수
            Union_List = [False for i in range(N*N)] # 국가들 - N 번째 연합 넣기
            Union_Day_List = [i for i in range(N*N)] # 국가들 - 하루에 연합에 넣은 것 빼기
            visit = [[False] * N for _ in range(N)]
            day += 1
            BFS(Union_Num, 0) # 다음날
        
main(-1, 0, 0)
        