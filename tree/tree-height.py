# Количество вершин в дереве
n = int(input())

# Отношения в дереве, где i-ый элемент -- ребенок i-ой вершины
nodes = [[int(s), -1] for s in input().split()]


def depth(vertex):
    """Рекурсивная функция, которая находит глубину вершины vertex

    Если глубина ещё не вычислена, рекурсивно вычисляет глубину потомков
    и сохраняет результат в nodes[vertex][1]
    """
    if nodes[vertex][1] == -1:
        if nodes[vertex][0] == -1:
            nodes[vertex][1] = 1
        else:
            nodes[vertex][1] = 1 + depth(nodes[vertex][0])

    return nodes[vertex][1]


# Высота дерева -- максимальная глубина из глубин вершин
print(max(depth(i) for i in range(n)))
