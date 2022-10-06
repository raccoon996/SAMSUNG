from collections import deque
import sys
input = sys.stdin.readline

n, m= map(int, input().split)
Box = []

for i in range(n):
    Box.append(list(input()))
    for j in range(m):
        if Box[i][j] == 'R':
            rm, rn = i, j
        elif Box[i][j] == 'B':
            bm, bn = i, j

# BFS함수
def bfs(rm, rn, bm, bn):
    # 초기화
    q = deque() # 스택을 쌓는 곳
    q.append((rm, rn, bm, bn))
    visited = [] # 들른 곳을 확인
    visited.append((rm, rn, bm, bn))

    # 이동 상, 하, 좌, 우
    move_m = [-1, 1, 0, 0]
    move_n = [0, 0, -1, 1]

    count = 0
    # BFS 알고리즘 
    while q:
        # for _ in range(len(q)): # 다음 좌표로 이동 가능한 개수만큼 돌려보기
        rm, rn, bm, bn = q.popleft()
        #------------------------------------
        if count > 10:
            print('-1')
            return
        if Box[rm][rn] == 'O':
            print(count)
            return
        #------------------------------------
        # 4방향 이동
        for i in range(4):
            # 빨간 공
            temp_rm, temp_rn = rm, rn
            while True: # 멈추기 전까지 이동 얼마난 이동할지 모름
                temp_rm += move_m[i]
                temp_rn += move_n[i]
                if Box[temp_rm][temp_rn] == 'O':
                    # print(count)
                    break
                if Box[temp_rm][temp_rn] == '#':
                    temp_rm -= move_m[i]
                    temp_rn -= move_n[i]
                    break
                

            # 파란 공
            temp_bm, temp_bn = bm, bn
            while True:
                temp_bm += move_m[i]
                temp_bn += move_n[i]                
                if Box[temp_bm][temp_bn] == 'O':
                    break
                if Box[temp_rm][temp_rn] == '#':
                    temp_rm -= move_m[i]
                    temp_rn -= move_n[i]
                    break
            
            if Box[temp_bm][temp_bn] == 'O':
                continue
            
            # 공 2개가 같은 좌표에 있으면
            if temp_rm == temp_bm and temp_rn == temp_rn:
                if abs(temp_rm - rm) + abs(temp_rn - rn) > abs(temp_bm - bm) + abs(temp_bn - bn):
                    temp_rm -= move_m[i]
                    temp_rn -= move_n[i]
                else:
                    temp_rm -= move_m[i]
                    temp_rn -= move_n[i]
        if (temp_rm, temp_rn, temp_rm, temp_rn) not in visited:
            q.append(temp_rm, temp_rn, temp_rm, temp_rn)
            visited.append(temp_rm, temp_rn, temp_rm, temp_rn)

        # 이거 여기에 들어가면 안될것 같은데...
    count += 1

            
    

