'''
Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).

Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
'''



def dfs(graph, start):
    lenght = len(graph)
    visited = [False] * lenght
    prev = [None] * lenght

    def _dfs(start):
        nonlocal graph, visited, prev

        visited[start] = True

        for i in graph[start]:
            if not visited[i]:
                prev[i] = start 
                _dfs(i)

    _dfs(start)

    return visited



# генерируем не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, в виде списка смежности
def build_graph(count):    
    return [[j for j in range(count) if j != i] for i in range(count)]

graph = build_graph(5)
print(graph)

result = dfs(graph, 1)
print(result)
