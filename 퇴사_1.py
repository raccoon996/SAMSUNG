import sys
input = sys.stdin.readline

# # 입력
# N = int(input()) # 날짜
# work = [list(map(int, input().split())) for _ in range(N)]
# # work[i][0] == Ti & work[i][1] == Pi

# N = 7
# work = [[3, 10],[5, 20],[1, 10],[1, 20],[2, 15],[4, 40],[2, 200]]

# N = 10
# work = [[1, 1],[1, 2],[1, 3],[1, 4],[1, 5],[1, 6],[1, 7],[1, 8],[1, 9],[1, 10]]

N = 10
work = [[5, 50],[4, 40],[3, 30],[2, 20],[1, 10],[1, 10],[2, 20],[3, 30],[4, 40],[5, 50]]

visited = [False]* N

# 최종 결과
ans = 0

def money_max(day, sum_money):
    global ans, N
    if day >= N:
        ans = max(ans, sum_money)
        return


    for i in range(N - day):
        counsel = 1
        # day += Ti
        # day += Pi
        for _ in range(2): # 상담하는 경우 & 상담하지 않는 경우
            if day + work[day + i][0] <= N: # 지금 날짜에 상담완료시간이 퇴사 이전인지
                # sum_money + work[day][1]
                # 더하는 것은 어떻게 할까? (일하는 경우, 안하는 경우)
                if counsel == 1: # 상담하는 경우
                    money_max(day + work[day + i][0], sum_money + work[day][1])
                    counsel = 0
                # 상담 받지 않으면 그냥 지나감
            # else: 
                # ans = max(ans, sum_money)

        # if day + work[day + i][0] <= N and day > 0: # 다음 날짜
        #     visited[day + work[day + i][0]] = True
        #     money_max(day + work[day + i][0], sum + work[day][1])
        #     visited[day + work[day + i][0]] = False

money_max(0, 0) # 1일차 시작
print(ans)