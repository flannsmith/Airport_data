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
    
    #making 
    #nodes are list of keys 
    graph_nodes = (list(dict_air.keys()))
    print(graph_nodes)

    airports_visited = []
    min_dist = []
    airIndices = []
    new_source = graph_nodes[0]
    # airIndices.append(0)
    for s in graph_nodes:
        # print("Dest",new_source)
        airports_visited.append(new_source)
        distances = dict_air.get(new_source)
        for i in airIndices:
            # print(s)
            distances[i] = 9999999
        # print(distances)
        index=-1
        for i,element in enumerate(distances):
            if element == 0: 
                index=i
                distances[i] = 9999999
        airIndices.append(index)
        mDist = min(distances)
        #print(mDist)
        airpIndex = distances.index(mDist)
        airIndices.append(airpIndex)
        #print("Index:",airpIndex)
        new_source = graph_nodes[airpIndex]
        min_dist.append(min(distances))
        #print(min_dist)
        
    #min_dist = min_dist[:-1]
    #print(airports_visited)
    newSrc = airports_visited[-1]
    home = airports_visited[0]
    airports_visited.append(home)
    #print(airports_visited)
    #print(min_dist)

    _currencyobject = Currency()
    parsedCurrencyCost = _currencyobject.currencyParser('Currency_code_concat')
    print(parsedCurrencyCost)





          

            


            # parsedAircraftDict = _airdict.Aircraft('aircraft.csv')
            # if aircraft_code in parsedAircraftDict:
            #     print(parsedAircraftDict.get(aircraft_code))




            #print(parsedAircraftDict)


            #check aircraft input and save it to return range from key
            #check key value pairs 

            #and print(min(element))

    

        # if element != 0 
        #     print(element)
   #find the minimum value in the list, append it to min_dist

   





    # for key in dict_air:
    #     print(dict_air.get(key))



if __name__ == "__main__":
    main()


    #print(graph_nodes)


    #List = airports visitied

    #check 0
    #is aircraft range below this
    #else cannot do trip
    #minimum value
    #index of value

    #List = Airports Visited
    #airports_visited = []
#     new_source = dict_air #key[0] return key of dict
#     Distances = Get[]