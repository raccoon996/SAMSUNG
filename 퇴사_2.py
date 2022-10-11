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

# def money_max(next_day, sum_money_pre):
#     global ans, N
        
#     for i in range(N - (next_day - 1)): # N - (next_day - 1) = 남은 day에 대한 경우(next_day 포함)
        
#         if next_day + work[(next_day-1) + i][0] <= N:
#             sum_money_now = sum_money_pre + work[(next_day-1) + i][1]
#             # 상담을 받은 경우
#             visited[(next_day-1) + i] = True
#             money_max(next_day + work[(next_day-1) + i][0], sum_money_now)
#             # 상담을 받지 않은 경우 for문으로 다음 날짜로 이동
#             visited[(next_day-1) + i] = False
#         else:
#             ans = max(ans, sum_money_pre)
#     return


def money_max(next_day, sum_money_pre):
    global ans, N
    if next_day == 10:
        next_day

    if next_day > N:
        ans = max(ans, sum_money_pre)
        return

    for i in range(N - (next_day - 1)): # N - (next_day - 1) = 남은 day에 대한 경우(next_day 포함)
        
        # 현재 날짜 + i번째 날짜와 상담기간의 합이 N 이하인지
        if (next_day - 1 + i) + work[next_day + i - 1][0] <= N:
            # 지금 상담이 가능하다고 판단해 이전 sum_money_pre와 지그 상담이 끝나면 받을 돈의 합
            sum_money_now = sum_money_pre + work[next_day + i - 1][1]
            # 상담을 받은 경우
            visited[next_day + i - 1] = True
            # 다음 날짜 넣기
            money_max(next_day + i + work[next_day + i - 1][0], sum_money_now)
            # 상담을 받지 않은 경우 for문으로 다음 날짜로 이동
            visited[next_day + i - 1] = False
        else: # 다음 날짜 + i번째 날짜와 상담기간의 합이 N 이하 아니면 다음 상담 보기
            ans = max(ans, sum_money_pre)
    return

money_max(1, 0) # 1일차 시작
print(ans)