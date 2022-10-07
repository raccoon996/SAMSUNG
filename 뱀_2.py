from collections import deque
import sys
input = sys.stdin.readline

# N = 6
# k = 3
# apple = [[3, 4], [2, 5], [5, 3]]
# L = 3
# snake_move = [['3', 'D'], ['15', 'L'], ['17', 'D']]

# N = 10
# k = 4
# apple = [[1, 2], [1, 3], [1, 4], [1, 5]]
# L = 4
# snake_move = [['8', 'D'], ['10', 'D'], ['11', 'D'], ['13', 'L']]

# N = 10
# k = 5
# apple = [[1, 5], [1, 3], [1, 2], [1, 6], [1, 7]]
# L = 4
# snake_move = [['8', 'D'], ['10', 'D'], ['11', 'D'], ['13', 'L']]

N = int(input())
K = int(input())
apple = []
apple = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
snake_move = []
snake_move = [list(map(str, input().split())) for _ in range(L)]


Box = [[0]*N for _ in range(N)] # 게임공간
# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 뱀 시작은 1, 1
snake_head_dx = 1
snake_head_dy = 1
# 시작 방향 오른쪽
move = 0

# 뱀 몸 stack
snake_body = deque()

# L 번만큼 변함(첫번째)
L_time = 0
Time = 0


while True: 
    # 게임이 끝나는 경우(2가지)
    if snake_head_dx > N or snake_head_dy > N or snake_head_dx < 1 or snake_head_dy < 1: # 벽을 넘어간 경우
        print(Time)
        break
    if ([snake_head_dx, snake_head_dy]) in snake_body: # 자신 몸에 부닥친 경우
        print(Time)
        break
    
    # 사과 먹으면 / 안먹은 경우
    if [snake_head_dx, snake_head_dy] in apple:
        apple.remove([snake_head_dx, snake_head_dy])
        snake_body.append([snake_head_dx - dx[move], snake_head_dy - dy[move]]) # 이전 머리 위치가 필요
    elif len(snake_body) != 0:
        snake_body.append([snake_head_dx - dx[move], snake_head_dy - dy[move]])
        snake_body.popleft()

    # 뱀이 방향 변화
    if L_time < L:        
        if Time == int(snake_move[L_time][0]):
            if snake_move[L_time][1] == 'D': # 오른쪽
                move = (move + 1) % 4
            elif snake_move[L_time][1] == 'L': # 왼쪽
                move = (move - 1) % 4
            if L_time >= L:
                snake_move[L_time][0] = '0'      
            L_time += 1

    # 방향 전환 안하면 직진
    Time += 1
    snake_head_dx += dx[move]
    snake_head_dy += dy[move]

