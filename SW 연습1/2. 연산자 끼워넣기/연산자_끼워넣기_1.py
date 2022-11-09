import copy
import sys

sys.stdin = open("input.txt", "r")

def bfs(ans, cnt):
    global N, ans_max, ans_min
    # 방문 여부 확인
    if cnt == (N-1):
        ans_max = max(ans_max, ans)
        ans_min = min(ans_min, ans)
        return
    # 남은 연산자 가지 수 만큼 넣기
    for i in range(N-1):
        # ans [] next
        if visited_ope[i] == False:
            next_dic = dic[i]
            if next_dic == '+':
                next_ans = ans + num[cnt+1]
            elif next_dic == '-':
                next_ans = ans - num[cnt+1]
            elif next_dic == '*':
                next_ans = ans * num[cnt+1]
            elif next_dic == '//':
                next_ans = int(ans / num[cnt+1])
            visited_ope[i] = True
            bfs(next_ans, cnt + 1)
            visited_ope[i] = False
    return
        

N = int(input())
num = list(map(int, input().split()))

# + - * //
Ope = list(map(int, input().split()))

# 연산자를 사용했는 지 확인
visited_ope = [False] * (N-1)

ans_max, ans_min = 0, 9**N
dic = {}
# dic = {0: '+', 1: '-', 2: '*', 3: '//'}

# dic[4] = '%'

for i in range(N - 1):
    if Ope[0] != 0:
        dic[i] = '+'
        Ope[0] -= 1
    elif Ope[1] != 0:
        dic[i] = '-'
        Ope[1] -= 1
    elif Ope[2] != 0:
        dic[i] = '*'
        Ope[2] -= 1
    elif Ope[3] != 0:
        dic[i] = '//'
        Ope[2] -= 1

cnt = 0
bfs(num[0], cnt)
print(ans_max)
print(ans_min)