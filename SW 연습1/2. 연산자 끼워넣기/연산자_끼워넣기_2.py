import sys

sys.stdin = open("input.txt", "r")

def bfs(ans, cnt):
    global N, ans_max, ans_min
    # 마지막인지 확인
    if cnt == N:
        ans_max = max(ans_max, ans)
        ans_min = min(ans_min, ans)
        return

    # 남은 연산자 가지 수 만큼 넣기
    if Ope[0]: # +
        next_ans = ans + num[cnt]
        Ope[0] -= 1
        bfs(next_ans, cnt + 1)
        Ope[0] += 1
    if Ope[1]: # -
        next_ans = ans - num[cnt]
        Ope[1] -= 1
        bfs(next_ans, cnt + 1)
        Ope[1] += 1
    if Ope[2]: # *
        next_ans = ans * num[cnt]
        Ope[2] -= 1
        bfs(next_ans, cnt + 1)
        Ope[2] += 1
    if Ope[3]: # /
        next_ans = int(ans / num[cnt])
        Ope[3] -= 1
        bfs(next_ans, cnt + 1)
        Ope[3] += 1
        

N = int(input())
num = list(map(int, input().split()))
# + - * //
Ope = list(map(int, input().split()))

ans_max, ans_min = -9**N, 9**N
dic = {}
# dic = {0: '+', 1: '-', 2: '*', 3: '//'}

bfs(num[0], 1)
print(ans_max)
print(ans_min)