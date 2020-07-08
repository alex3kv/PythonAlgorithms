'''
Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).

Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
'''

def bfs(graph, start, finish):
    parent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]

    deq = deque([start])
    is_visited[start] = True

    while len(deq) > 0:

        curent = deq.pop()

        if curent == finish:
            return parent
            break

        for i, vertex in enumerate(graph[curent]):
            if vertex == 1 and not is_visited[1]:
                is_visited[i] = True
                parent[i] = curent
                deq.appendleft(i)

    else:
        return f"Из вершины {start} нельзя попасть в вершину {finish}"

    cost = 0
    way = deque([finish])
    i = finish

    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]

    cost += 1
    way.appendleft(start)

    return f"кратчайший путь {list(way)} длинной {cost} условных единиц"


