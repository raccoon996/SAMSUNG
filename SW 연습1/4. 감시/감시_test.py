import 감시_다른사람
import 감시_3

def graph(graph_num):
    global N, M
    if graph_num == N * M:
        f = open("input.txt", 'w')
        f.write(f'{N} {M}\n')
        for i in range(N):
            data = ' '.join(str(s) for s in graph_test[i])
            f.write(f'{data}\n')
        f.close()
        # 여기다가 함수 넣기
        a = 감시_다른사람.main()
        b = 감시_3.main()
        if a != b:
            print('stop')
            print(f'a={a} != b={b}')
        else:
            print(f'a={a} == b={b}')
        return
    graph_x = graph_num // M
    graph_y = graph_num % M
    for num in range(6):
        graph_test[graph_x][graph_y] = num
        graph(graph_num+1)

while True:
    for N in range(1, 9): # 1 2 3 4 5 6 7 8
        for M in range(1, 9): # 1 2 3 4 5 6 7 8
            graph_test = [[0 for _ in range(M)] for _ in range(N)]
            # 모든 경우의 수
            graph(0)