'''
Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
'''

def dijkstra(graph, start):
    lenght = len(graph)
    is_visited = [False] * lenght
    cost = { i: [float("inf"),[]] for i in range(lenght)}
    parent = [-1] * lenght

    cost[start][0] = 0    
    min_cost = 0

    while min_cost < float("inf"):

        is_visited[start] = True
                
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i][0] > vertex + cost[start][0]:
                    cost[i][0] = vertex + cost[start][0]
                    cost[i][1] = cost[start][1] + [start]
                    parent[i] = start

        min_cost = float("inf")
        for i in range(lenght):
            if min_cost > cost[i][0] and not is_visited[i]:
                min_cost = cost[i][0]
                start = i

    return cost

#        0_ 1_ 2_ 3_ 4_ 5_ 6_ 7
graf = [[0, 0, 1, 1, 9, 0, 0, 0],
        [0, 0, 9, 4, 0, 0, 7, 0],
        [0, 9, 0, 0, 3, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 7, 0, 8, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 2, 0]]

result = dijkstra(graf, 0)

for key, value in result.items():
    print(f"К вершине {key} потребуется {value[0]} условных единиц, маршрут по вершинам {value[1]}")
