from collections import defaultdict
from collections import deque
import collections

# adjacency list for the graph

import collections


def bfs(graph, root):
    seen, queue = set([root]), collections.deque([root])
    while queue:
        vertex = queue.popleft()
        visit(vertex)
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)


def visit(n):
    print(n)


if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2, 0], 2: []}
    bfs(graph, 0)


graph = {0: [1, 2], 1: [2, 0], 2: []}

#graph = {0: [16938.218002725473, 10247.251519672844, 14947.425152241693, 14614.05445050763], 1: [16937.727519352335, 20570.1316875763, 16549.80571847769, 16576.162310155876], 2: [16294.04194595942, 13387.717894338273, 11396.925043854491, 11063.554342120431], 3: [12304.90580075191, 15210.248885626777, 15937.30996897588, 11943.340591555452], 4: [11818.028043989907, 14723.371128864776, 15450.432212213876, 11430.106243115264]}






