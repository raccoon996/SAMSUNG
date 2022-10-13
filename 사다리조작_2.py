import sys
input = sys.stdin.readline

line = []
# 입력
# N, H, M = list(map(int, input().split()))
# line = [list(map(int, input().split())) for _ in range(H)]

# N, H, M = 5, 5, 6
# line = [[1,1],[3,2],[2,3],[5,1],[5,4]]

# N, H, M = 2, 1, 3
# line = [[1,1]]

N, H, M = 1, 2, 3
line = [[1,1]]

# N, H, M = 6, 5, 6
# line = [[1,1],[3,2],[1,3],[2,5],[5,5]]

# N, H, M = 5, 12, 6
# line = [[1,1],[1,3],[2,2],[2,4],[3,1],[3,3],[4,2],[4,4],[5,1],[5,3],[6,2],[6,4]]
 
# N, H, M = 5, 6, 6
# line = [[1,1],[3,1],[5,2],[4,3],[2,3],[1,4]]

Box = [[False]*(N-1) for _ in range(H)]

# Box에 line 있는 곳 표시
for i in range(len(line)):
    Box[line[i][0]-1][line[i][1]-1] = True

ans = (N-1) * H

# line 추가
def line_plus_dfs(start, count):
    global ans,N,H
    # 한번 돌려보기 게임
    result = game_start()
    if result == True:
        ans = min(ans, count)
        return # 최소를 찾는 거라 다음거 찾을 필요 없음
    if count == 3: # 3 이상은 보지 않는다.
        return

    # 남은 칸만 확인 중복 검사 방지
    for i in range(start, (N-1)*H):
        # 0부터 시작
        if i == 4:
            i
        x = i // (N-1)
        y = i % (N-1)
        if y == 0 and y == (N-2):
            if Box[x][y] == True:
                continue
        elif y == 0:
            if Box[x][y] == True or Box[x][y+1] == True:
                continue
        elif y == (N-2):
            if Box[x][y] == True or Box[x][y-1] == True:
                continue
        elif Box[x][y] == True or Box[x][y-1] == True or Box[x][y+1] == True:
            continue
        
        Box[x][y] = True
        line_plus_dfs(start + i, count+1)
        Box[x][y] = False
            
def game_start():
    for i in range(N):
        side = 0 # 오른쪽/ 왼쪽
        down = 0 # 아래로 내려가기 위해
        while True:
            if down == H:
                if side == 0:
                    break
                else: # 실패(i 가 i하고 이어지지 못함)
                    return False
            if i+side == 0:
                if Box[down][i+side] == True: #오른쪽에 선 있음
                    side += 1
            elif i+side == (N-1):
                if Box[down][i+side-1] == True: #왼쪽에 선 있음
                    side -= 1
            else:
                if Box[down][i+side] == True: #오른쪽에 선 있음
                    side += 1
                elif Box[down][i+side-1] == True: #왼쪽에 선 있음
                    side -= 1
            down += 1
    return True

line_plus_dfs(0, 0)
if ans > 3:
    print(-1)
else:
    print(ans)

