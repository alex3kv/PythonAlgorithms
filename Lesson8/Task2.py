'''
Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
'''

def dijkstra(graph, start):
    lenght = len(graph)
    is_visited = [False] * lenght
    cost = [float("inf")] * lenght
    parent = [-1] * lenght

    cost[start] = 0
    min_cost = 0

    while min_cost < float("inf"):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float("inf")
        for i in range(lenght):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    return cost

#        0 1 2 3 4 5 6 7
graf = [[0, 0, 1, 1, 9, 0, 0, 0],
        [0, 0, 9, 4, 0, 0, 7, 0],
        [0, 9, 0, 0, 3, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 7, 0, 8, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 2, 0]]

result = dijkstra(graf, 0)

print(result)
