from collections import defaultdict

#Dijkstra is advanced feature to provide support to calculate best route from Airport 1 to 5,
#visitng airports 2,3,4

class dijsktraGraph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
   # self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance
    #self.distances[(to_node, from_node)] = distance


def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes:
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distances[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path

digits = [7808.524966508974, 6111.827154987743, 6179.15872958464, 17209.086206137745, 2072.1541637678374,
    1833.6097112074265, 9598.623177835954, 334.01373014041366, 11502.858754476589, 11359.707775994646]


g = dijsktraGraph()
g.add_node('a')
g.add_node('b')
g.add_node('c')
g.add_node('d')
g.add_node('e')

g.add_edge('a', 7808.524966508974,  6111.827154987743)
g.add_edge('b', 6179.15872958464, 10)
g.add_edge('c', 6, 15)


print(dijsktra(g, 'a'))


