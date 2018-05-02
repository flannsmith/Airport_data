import argparse
import csv
import io
import geopy.distance
from operator import itemgetter
from collections import Counter
from utils import utils
from currency import Currency
from airport import Airport
from cost import Cost
 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file_path")
    parser.add_argument("--encoding", default="utf_8")
    options = parser.parse_args()
    _utObject = utils()
    testCsv, aircraftCode, aircraftRange = _utObject.input(options)
    # print("TESTCSV:::::::::",testCsv)
    # print(aircraftCode)
    # print(aircraftRange)
    outputList=[]
    _airdict = Airport()
    parsedAirportDict = _airdict.parseAirport('airport.csv')
    for tCi,tC in enumerate(testCsv):
        #Iterates over IATA code in testCsv storing their into a dictionary as tuples
        #Saving lat and long values for each IATA  
        distances = {}
        for row in tC:
            data = parsedAirportDict.get(row)
            distances[row] = data
        # print(distances)

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
        
        finalSource = airports_visited[-1]
        finalDestination = airports_visited[0]
        finalSourceDist = parsedAirportDict.get(finalSource)
        finalDestinationDist = parsedAirportDict.get(finalDestination)
    

        finalDistance = _airdict.distanceBetweenAirports(finalSourceDist[0],finalSourceDist[1],finalDestinationDist[0],finalDestinationDist[1])
        #print(finalDistance)
        #Append final dist to list of distances
        airports_visited.append(finalDestination)
        print("Itinerary:", airports_visited, '\n')

        min_dist.append(finalDistance)
        print("Itinerary Distances:", min_dist, '\n')
        print('________________________________________________', '\n')
        #Destination is the last index of airports_visited list
        _currencyobject = Currency()
        parsedCurrencyCost = _currencyobject.currencyParser('Currency_code_concat.csv')

        billingCountry = airports_visited[-1]

        _costObject = Cost()
        toEuroRate = _costObject.toEuroRate(billingCountry,'airport.csv','countrycurrency.csv','currencyrates.csv')
        print(toEuroRate)

        print("Cost of round trip: ", "€",(sum(min_dist)//toEuroRate))

        #Also calculate distance from last dest in list to home 
        #  

        print('________________________________________________')
        print("Checking if Itinerary is possible with provided aircraft")
        journeyPossible = _airdict.isItineraryPossible(aircraftRange[tCi],min_dist)
        if journeyPossible==False:
            print("Sorry, with the provided aircraft this journey cannot be made. Try again!")
            airports_visited.append("No Route")
            outputList.append(airports_visited)
        else:
            remainingFuel=aircraftRange[tCi]
            print("\t\t\tRemaining Fuel::: ",remainingFuel)
            totalCosttoRefuel = 0
            toEuroRate = _costObject.toEuroRate(
                airports_visited[0], 'airport.csv', 'countrycurrency.csv', 'currencyrates.csv')
            print("\t\t\t\t\tItinerary Scheduled:  ",airports_visited)
            print("\t\t\t\t\tItinerary Scheduled:  ", min_dist)
            totalCosttoRefuel += aircraftRange[tCi]*toEuroRate
            for i,val in enumerate(min_dist):
                toEuroRate = _costObject.toEuroRate(
                    airports_visited[i+1], 'airport.csv', 'countrycurrency.csv', 'currencyrates.csv')

                print("\t\t\tAT Airport: ", airports_visited[i+1])
                print("\t\t\tAT Airport: ", airports_visited[i+1],"the EURO Rate is: ",toEuroRate)
                if remainingFuel>=val:
                    print("\t\t\t\tProceeding")
                    remainingFuel-=val
                else:
                    print("\t\t\tRefueling")
                    costOfRefuel = (aircraftRange[tCi]-remainingFuel)*toEuroRate
                    totalCosttoRefuel+=costOfRefuel
                    remainingFuel=aircraftRange[tCi]-val
                    print("\t\t\t\t",costOfRefuel)
                print("\t\t\t\tRemaining", remainingFuel)
            airports_visited.append(totalCosttoRefuel)
            outputList.append(airports_visited)
            print("TOTAL COST FOR ITINERARY IS: ",totalCosttoRefuel)

    print("Generating output csv file")
    _utObject.tocsv(outputList)



if __name__ == "__main__":
    main()


