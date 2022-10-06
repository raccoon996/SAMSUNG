from collections import deque
import sys
input = sys.stdin.readline

# # 보드의 크기
# N = int(input())
# # 초기 상태
# Box = []
# for i in range(N):
#     Box.append(list(input()))

Box = list(map(int, input().split()))
# Box = Box[:len(Box)-1] # list(input())을 사용했을 때 사용
dx = -1

def list_sum(num_list):
    Temp_column_list = num_list[:] + [0]
    Temp_num_old = 0
    Stack = []
    
    while Temp_column_list:
        # for _ in range(len(Temp_column_list)+1):
        Temp_num = int(Temp_column_list.pop(0))
        if Temp_num_old == 0: # 0인 경우
            Temp_num_old = Temp_num
        elif Temp_num_old == Temp_num: # 같으면 더하고 stack에 업데이트
            Stack.append(Temp_num_old + Temp_num)
            Temp_num_old, Temp_num = 0, 0
        elif Temp_num_old != Temp_num: # 같지 않으면 stack에 올리고 업데이트
            Stack.append(Temp_num_old)
            Temp_num_old = Temp_num
    Stack.extend([0]*(len(num_list)-len(Stack)))
    return Stack


# def list_sum_1(num_list, dx):
#     if dx == -1: # 상
#         Temp_column_list = num_list[:] + [0]
#         Temp_num_old = 0
#         Stack = []
        
#         while Temp_column_list:
#             # for _ in range(len(Temp_column_list)+1):
#             Temp_num = int(Temp_column_list.pop(0))
#             if Temp_num_old == 0: # 0인 경우
#                 Temp_num_old = Temp_num
#             elif Temp_num_old == Temp_num: # 같으면 더하고 stack에 업데이트
#                 Stack.append(Temp_num_old + Temp_num)
#                 Temp_num_old, Temp_num = 0, 0
#             else: # 같지 않으면 stack에 올리고 업데이트
#                 Stack.append(Temp_num_old)
#                 Temp_num_old = Temp_num
#         # Stack.append(Temp_num) # 마지막 숫자

#         for i in range(len(num_list)-len(Stack)): # 나머지 칸에 0 채우기 
#             Stack.append(0)
#         return Stack

#     elif dx == 1: # 하
#         Temp_column_list = deque()
#         Temp_column_list.append(num_list[:])
#         Temp_num_old = int(Temp_column_list.pop)
#         Stack = []
#         while Temp_column_list:
#             Temp_num = int(Temp_column_list.pop)
#             if Temp_num_old == Temp_num: # 같으면 더하고 stack에 업데이트
#                 Stack.append(Temp_num_old + Temp_num)
#                 Temp_num_old = int(Temp_column_list.pop)
#             else: # 같지 않으면  stack에 올리고 업데이트
#                 Stack.append(Temp_num_old)
#                 Temp_num_old = Temp_num
#         for i in range(len(num_list)-len(Stack)): # 나머지 칸에 0 채우기 
#             Stack.append(0)
#         Stack.reverse()
#         return Stack

print(list_sum(Box))
