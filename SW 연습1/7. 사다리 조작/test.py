N, H = 5, 6

graph = [[i*j for i in range(N+1)] for j in range(H+1)]

for i in [0, N]:
    for j in range(H+1):
        graph[j][i] = 1

for i in range(H+1):
    print(graph[i])
num = 0
for i in range(num, (N-1)*H):
    x = i // (N-1) + 1
    y = i % (N-1) + 1
    print(f'{x} {y} = {graph[x][y]}')