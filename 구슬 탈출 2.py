from collections import deque
import sys
input = sys.stdin.readline # 빠른 입출력 위한 코드

# . 빈칸, # 벽, O 구멍, R 빨간 공, B 파란 공
# N 세로, M 가로
N, M= map(int, input().split())

# Box = [['#']*M]*N # 초기화
Box = [] # 초기화

for i in range(N): # N 세로
    Box.append(list(input()))
    for j in range(M): # M 가로
        if Box[i][j] == 'R': # 빨간구슬 위치
            Rn, Rm = i, j
        elif Box[i][j] == 'B': # 파란구슬 위치
            Bn, Bm = i, j

# 상, 하, 좌, 우 이동
move_N = [-1, 1, 0, 0]
move_M = [0, 0, -1, 1]

def BFS(Rn, Rm, Bn, Bm):
    q = deque() # 큐 제작
    q.append((Rn, Rm, Bn, Bm)) # 초기 큐

    visited = [] # 방문여부를 판단하기 위한 리스트
    visited.append((Rn, Rm, Bn, Bm))

    count = 0

    while q:
        for _ in range(len(q)):
            Rn, Rm, Bn, Bm = q.popleft() # 큐에 먼저 들어온것부터 사용

            # 끝나는 경우
            if count > 10: # 10번이상이 필요해서 - 완전 실패
                print('-1')
                return
            if Box[Rn][Rm] == 'O': # 현재 빨간공 위치가 구멍(O)이면 끝
                print(count)
                return

            # 탐색
            for i in range(4): # 4방향 탐색
                #--------------------------------------------------------------------
                # 빨간 공
                temp_Rn, temp_Rm = Rn, Rm
                # 이동하고, 빨간 공이 멈추는 경우 2가지 (벽, 구멍)
                while True:
                    temp_Rn += move_N[i]
                    temp_Rm += move_M[i]
                    if Box[temp_Rn][temp_Rm] == '#': # 바로 직전으로 이동
                        temp_Rn -= move_N[i]
                        temp_Rm -= move_M[i]
                        break
                    if Box[temp_Rn][temp_Rm] == 'O': # 바로 count를 출력을 안하는 이유는 파란공도 들어가는 경우 생각
                        break
                
                #--------------------------------------------------------------------                
                # 파란 공
                temp_Bn, temp_Bm = Bn, Bm
                # 이동하고, 빨간 공이 멈추는 경우 2가지 (벽, 구멍)
                while True:
                    temp_Bn += move_N[i]
                    temp_Bm += move_M[i]
                    if Box[temp_Bn][temp_Bm] == '#': # 바로 직전으로 이동
                        temp_Bn -= move_N[i]
                        temp_Bm -= move_M[i]
                        break
                    if Box[temp_Bn][temp_Bm] == 'O':
                        break

                #--------------------------------------------------------------------
                # 파란공이 구멍에 들어간 경우는 무시(count 안함) - 실패
                if Box[temp_Bn][temp_Bm] == 'O': # 계속 진행
                    continue
                
                #--------------------------------------------------------------------
                # 두개 공 위치가 같은 경우
                if temp_Rn == temp_Bn and temp_Rm == temp_Bm:
                    if abs(temp_Rn - Rn) + abs(temp_Rm - Rm) > abs(temp_Bn - Bn) + abs(temp_Bm - Bm): # 더 많이 이동한 공을 한칸 전으로
                        temp_Rn -= move_N[i]
                        temp_Rm -= move_M[i]
                    else:
                        temp_Bn -= move_N[i]
                        temp_Bm -= move_M[i] 
                
                #--------------------------------------------------------------------
                # 방문 여부를 판단 (방문한 적이 없으면)
                if (temp_Rn, temp_Rm, temp_Bn, temp_Bm) not in visited:
                    q.append((temp_Rn, temp_Rm, temp_Bn, temp_Bm))
                    visited.append((temp_Rn, temp_Rm, temp_Bn, temp_Bm))
        # 한번 이동했으니
        count += 1

    # 다 이동 했지만 도달하지 못하는 경우 - 완전 실패
    print('-1')

BFS(Rn, Rm, Bn, Bm)



