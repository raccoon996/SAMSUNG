from collections import deque
import sys

input = sys.stdin.readline

# N, M, x, y, K = map(int, input().split()) 

# # 필드
# Box = [list(map(int, input().split())) for _ in range(N)]

# # 이동명령
# move_order = list(map(int, input().split()))

N, M, x, y, K = 4, 2, 0, 0, 8
Box = [[0, 2], [3, 4], [5, 6], [7, 8]]

move_order = [4, 4, 4, 1, 3, 3, 3, 2]

# 동서북남 (1,2,3,4)
move_dx = [0, 0, -1, 1]
move_dy = [1, -1, 0, 0]

# 주사워
dice = [0]*6
# 1 - 4 - 6 - 3 - 1 y축
dice_y = [3, 2, -3, -2]
# 1 - 2 - 6 - 5 - 1 x축
dice_x = [1, 4, -1, -4]
# 주사워 윗 면 위치
dice_top = 1
dice_sur_x = 3 # 윗면 오른쪽
dice_sur_y = 5 # 윗면 아래쪽

# global dice

# def dice_move(move): # 동서북남
#     if move == 1:
        
for i in range(len(move_order)):
    # 주사워 위치
    x += move_dx[move_order[i] - 1]
    y += move_dy[move_order[i] - 1]

    if move_order[i] == 1:
        Temp = dice_top
        dice_top = dice_sur_x
        dice_sur_x = (7 - Temp)
        if Box[x][y] == 0:
            Box[x][y] = dice[7-dice_top]
        else: # Box에 숫자가 적혀있음
            dice[7-dice_top] = Box[x][y]
            Box[x][y] = 0

    elif move_order[i] == 2:
        Temp = dice_top
        dice_top = (7 - dice_sur_x)
        dice_sur_x = (7 - Temp)        
        if Box[x][y] == 0:
            Box[x][y] = dice[7-dice_top]
        else: # Box에 숫자가 적혀있음
            dice[7-dice_top] = Box[x][y]
            Box[x][y] = 0

    elif move_order[i] == 3:
        Temp = dice_top
        dice_top = (7 - dice_sur_y)
        dice_sur_y = (7 - Temp)
        if Box[x][y] == 0:
            Box[x][y] = dice[7-dice_top]
        else: # Box에 숫자가 적혀있음
            dice[7-dice_top] = Box[x][y]
            Box[x][y] = 0
    
    elif move_order[i] == 4:
        Temp = dice_top
        dice_top = dice_sur_y
        dice_sur_y = (7 - Temp)
        if Box[x][y] == 0:
            Box[x][y] = dice[7-dice_top]
        else: # Box에 숫자가 적혀있음
            dice[7-dice_top] = Box[x][y]
            Box[x][y] = 0
    
    # 이동할때마다 윗면 출력
    print(dice[dice_top-1])

        

