import copy

def move(dir): # n e s w
    if dir == 0:
        for j in range(n): # y 축 0 ~ n
            idx = 0
            for i in range(1, n): # x 축 1 ~ n (0은 따로 움직이지 않아서)
                if graph[i][j] != 0: # if not 0 비어있는 공간이 아니면
                    temp = graph[i][j]
                    graph[i][j] = 0 # 이동할것이니 빈것으로
                    if graph[idx][j] == temp:
                        graph[idx][j] *= 2 # 2의 승이라
                        idx += 1 # 다음칸
                    elif graph[idx][j] == 0:
                        graph[idx][j] = temp  
                    elif graph[idx][j] != temp:
                        idx += 1
                        graph[idx][j] = temp
                        

    elif dir == 1:
        for i in range(n):
            idx = n-1
            for j in range(n-2, -1, -1):
                if graph[i][j] != 0: # if not 0
                    temp = graph[i][j]
                    graph[i][j] = 0
                    if graph[i][idx] == temp:
                        graph[i][idx] *= 2
                        idx -= 1
                    elif graph[i][idx] == 0:
                        graph[i][idx] = temp
                    elif graph[i][idx] != temp:
                        idx -= 1
                        graph[i][idx] = temp
                        
    
    elif dir == 2: # s
        for j in range(n):
            idx = n-1
            for i in range(n-2, -1, -1):
                if graph[i][j] != 0:
                    temp = graph[i][j]
                    graph[i][j] = 0
                    if graph[idx][j] == temp:
                        graph[idx][j] *= 2
                        idx -= 1
                    elif graph[idx][j] == 0:
                        graph[idx][j] = temp
                    elif graph[idx][j] != temp:
                        idx -= 1
                        graph[idx][j] = temp
                        

    elif dir == 3: # w
        for i in range(n):
            idx = 0
            for j in range(1, n):
                if graph[i][j] != 0:
                    temp = graph[i][j]
                    graph[i][j] = 0
                    if graph[i][idx] == temp:
                        graph[i][idx] *= 2
                        idx += 1
                    elif graph[i][idx] == 0:
                        graph[i][idx] = temp
                    elif graph[i][idx] != temp:
                        idx += 1
                        graph[i][idx] = temp
                        

def dfs(count):
    global ans, graph
    if count == 5: # 5인 경우
        for i in range(n):
            ans = max(ans, max(graph[i]))
        return

    copyGraph = copy.deepcopy(graph)
    for i in range(4):
        move(i)
        dfs(count + 1)
        graph = copy.deepcopy(copyGraph)
        

n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
ans = 0
dfs(0)
print(ans)