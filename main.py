import argparse
import csv
import io
from operator import itemgetter
from collections import Counter
from utils import utils
from currency import Currency
from airport import Airport
from dijkstra_github import Graph
import geopy.distance
from bfs2 import bfs



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file_path")
    parser.add_argument("--encoding", default="utf_8")
    options = parser.parse_args()
    _utObject = utils()
    testCsv = _utObject.input(options)
    _airdict = Airport()
    parsedAirportDict = _airdict.parseAirport('airport.csv')
    
    for row in testCsv:
        distances = {}
        for i in row:
            data = parsedAirportDict.get(i)
            distances[i] = data
        #print(distances)


    #list of distances
    finDist = []
    for airs in distances:
        src = airs
        indivDist = []
        for airs2 in distances:
            dest = airs2
            indivDist.append(_airdict.distanceBetweenAirports(
                distances[src][0], distances[src][1], distances[dest][0], distances[dest][1]))
        finDist.append(indivDist)
    print(finDist)


    #To make dictionary of distances
    dict_air = {}
    for airs in distances:
        src = airs
        indivDist = []
        for airs2 in distances:
            dest = airs2
            indivDist.append(_airdict.distanceBetweenAirports(distances[src][0], distances[src][1], distances[dest][0], distances[dest][1]))
        dict_air[src] = indivDist
    print(dict_air)
    
    #nodes are list of keys 

    graph_nodes = (list(dict_air.keys()))
    #print(graph_nodes)

    g = Graph()
    #adding keys of dict to become the nodes in my graph
    for node in graph_nodes:
        g.add_node(node)
    g.add_edge('A', 'B', 10)
    g.add_edge('A', 'C', 20)
    g.add_edge('B', 'D', 15)
    g.add_edge('C', 'D', 30)
    g.add_edge('B', 'E', 50)
    g.add_edge('D', 'E', 30)
    g.add_edge('E', 'F', 5)
    
    #print(shortest_path(graph, 'A', 'D'))

    # _bfsobject = bfs()
    # bfs(finDist,finDist[0])




    # g.add_edge(node[0], node[-1], 15937.30996897588)
    # g.add_edge(node[0], node[-2], 11943.340591555452)

    # print(g, node[0], node[-1])


    # for i in dict_air:
    #     x = (dict_air[i])
    #     for k in x:
    #         print(k)
            #graph.add_edge(k)

    




  
if __name__ == "__main__":
        main()



    #Instead of having list of lists: have a dictionary where looks like:
    # DUB: [123,123,124]
    #SYD: [144, 444, 223]
    #AUD: [123,233,222]
    




    # _currencyobject = Currency()
    # parsedCurrencyCost = _currencyobject.currencyParser('Currency_code_concat')


    # distance = airport.Airport()
    
        #calculate distance between routes 

    # print(testCsv)
    # _airdict = airport.Airport()
    # parsedAirportCsv = _airdict.parseAirport('airport.csv')
    # for item in parsedAirportCsv:
    #     print(parsedAirportCsv[item])
     
    # print(parsedAirportCsv)

    

    











