import argparse
import csv
import io
import geopy.distance
from operator import itemgetter
from collections import Counter
from utils import utils
from currency import Currency
from airport import Airport
from dijkstra_github import Graph
from bfs2 import bfs
from bruteForce import MinDist
from cost import Cost

#queue to deque the 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file_path")
    parser.add_argument("--encoding", default="utf_8")
    options = parser.parse_args()
    _utObject = utils()
    testCsv = _utObject.input(options)
    _airdict = Airport()
    parsedAirportDict = _airdict.parseAirport('airport.csv')
    
    #Iterates over IATA code in testCsv storing their into a dictionary as tuples
    #Saving lat and long values for each IATA  
    for row in testCsv:
        distances = {}
        for i in row:
            data = parsedAirportDict.get(i)
            distances[i] = data
        #print(distances)

    #Calculating all possible distances between routes and storing them in a dict
    dict_air = {}
    for airs in distances:
        src = airs
        indivDist = []
        for airs2 in distances:
            dest = airs2
            indivDist.append(_airdict.distanceBetweenAirports(distances[src][0], distances[src][1], distances[dest][0], distances[dest][1]))
        dict_air[src] = indivDist
    #print(dict_air)
    
    #transform nodes(keys) of dict into a sequence
    graph_nodes = (list(dict_air.keys()))
  
    # _min_distance_obj = MinDist()
    # shortest_path = _min_distance_obj.bruteForce(graph_nodes,dict_air)

    airports_visited = []
    min_dist = []
    airIndices = []
    new_source = graph_nodes[0]
    # airIndices.append(0)
    for s in graph_nodes:
        # print("Destination:", new_source)
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
    
    #Popping last element off stack to get 4 shortest distances
    min_dist.pop()
    #print(min_dist)
    print('________________________________________________', '\n')
    print("Itinerary:",airports_visited, '\n')

    #Destination is the last index of airports_visited list
    _currencyobject = Currency()
    parsedCurrencyCost = _currencyobject.currencyParser('Currency_code_concat.csv')

    billingCountry = airports_visited[-1]

    _costObject = Cost()
    toEuroRate = _costObject.toEuroRate(billingCountry,'airport.csv','countrycurrency.csv','currencyrates.csv')
    #print(toEuroRate)

    print("Cost of round trip: ", "€",(sum(min_dist)//toEuroRate))

    print('________________________________________________')


    #For the cost do I have to calculate the cost from last destination to home as well?? 


    

    
 


    #why is my values saved in a tuple??? 
   # for key in parsedCurrencyCost.items():
        #print(key[0])
        #if billingCountry == key[0]:
           
        # print(key[0])
        # data = parsedCurrencyCost.get(billingCountry)
        #print(data)
        
        
        #if key == billingCountry:
  


        # 
        #     print(value)
    
    # for key,value in parsedCurrencyCost.items():
    #     #print(key,value)
    #     #print(parsedCurrencyCost[key])
    #     print(parsedCurrencyCost[value])
    #     if airports_visited[-1] == parsedCurrencyCost[key]:
    #         print(parsedCurrencyCost[value])
    #         #print(key[1])

  

    #if sum shortest_path is greater than aircraft range, aircraft range minus sum and print out
    #please refuel in ......... kms
   
   
    #print(parsedCurrencyCost)

  



 


    
    # #sequences implement
        
    # #min_dist = min_dist[:-1]
    # #print(airports_visited)
    # newSrc = airports_visited[-1]
    # home = airports_visited[0]
    # airports_visited.append(home)
    # #print(airports_visited)
    # min_dist.pop()
    # print(min_dist)

    #for iata in currencydict:
    #if code is there return to euro cost and save to list

    
    


#print(key, 'is the key for the value', value)

    






          

            


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
