import collections
import math
 
 
class Graph:
    ''' graph class inspired by https://gist.github.com/econchick/4666413
        adapted from http://alexhwoods.com/dijkstra/ to make unweighted
    '''

    def __init__(self):
        self.vertices = set()

        # makes the default value for all vertices an empty list
        self.edges = collections.defaultdict(list)
        self.weights = {}
 
    def add_vertex(self, value):
        self.vertices.add(value)
 
    def add_edge(self, from_vertex, to_vertex, distance):
        if from_vertex == to_vertex: pass  # no cycles allowed
        self.edges[from_vertex].append(to_vertex)
        self.edges[to_vertex].append(from_vertex) # undirected graph
        self.weights[(from_vertex, to_vertex)] = distance
        self.weights[(to_vertex, from_vertex)] = distance # undirected graph
 
    def __str__(self):
        string = "Vertices: " + str(self.vertices) + "\n"
        string += "Edges: " + str(self.edges) + "\n"
        string += "Weights: " + str(self.weights)
        return string
 

def dijkstra(graph, start):
    # initializations
    S = set()

    # delta represents the length shortest distance paths from start -> v, for v in delta.
    # We initialize it so that every vertex has a path of infinity (this line will break if you run python 2)
    delta = dict.fromkeys(list(graph.vertices), math.inf)
    previous = dict.fromkeys(list(graph.vertices), None)

    # then we set the path length of the start vertex to 0
    delta[start] = 0

    # while there exists a vertex v not in S
    while S != graph.vertices:
        # let v be the closest vertex that has not been visited...it will begin at 'start'
        v = min((set(delta.keys()) - S), key=delta.get)

        # for each neighbor of v not in S
        for neighbor in set(graph.edges[v]) - S:
            new_path = delta[v] + graph.weights[v,neighbor]

            # is the new path from neighbor through
            if new_path < delta[neighbor]:
                # since it's optimal, update the shortest path for neighbor
                delta[neighbor] = new_path

                # set the previous vertex of neighbor to v
                previous[neighbor] = v
        S.add(v)

    return (delta, previous)
 
 
 
def shortest_path(graph, start, end):
    '''Uses dijkstra function in order to output the shortest path from start to end
    '''
    delta, previous = dijkstra(graph, start)

    path = []
    vertex = end

    while vertex is not None:
        path.append(vertex)
        vertex = previous[vertex]

    path.reverse()
    return path
  
  
if __name__ == "__main__":

    g = Graph()
    vertices = ['a', 'b', 'c', 'd', 'e',]
    weights = [7808.524966508974, 6111.827154987743, 6179.15872958464, 17209.086206137745, 2072.1541637678374,
                1833.6097112074265, 9598.623177835954, 334.01373014041366, 11502.858754476589, 11359.707775994646]

    for v in vertices:
        g.add_vertex(v)
        for w in weights:
            g.add_edge(v,w)

   
    g.add_vertex(w)
    g.add_edge(vv)
    

    # 	vertex a adjacency list
    g.add_edge('a', 'b', 4)
    g.add_edge('a', 'c', 6)
    g.add_edge('a', 'd', 7)
    g.add_edge('a', 'e', 5)
    g.add_edge('a', 'j', 1)
    # 	vertex b adjacency list
    g.add_edge('b', 'e', 9)
    g.add_edge('b', 'f', 8)

    g.add_edge('c', 'd', 2)

    g.add_edge('d', 'j', 3)

    g.add_edge('e', 'f', 4)
    g.add_edge('e', 'h', 3)


    print("graph: ", g)
    print(dijkstra(g, 'c'))
    print(shortest_path(g, 'c', 'g'))


