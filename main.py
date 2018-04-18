import argparse
import csv
import io
from operator import itemgetter
from collections import Counter
from utils import utils
from currency import Currency
from airport import Airport
import geopy.distance


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
        # print(distances)

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


    


    
        #data is storing distances 
           # _airdict.distanceBetweenAirports(data[0],data[1])
        

    # _currencyobject = Currency()
    # parsedCurrencyCost = _currencyobject.currencyParser('Currency_code_concat')


    #print(dist_object.distanceEdges(testCsv))

    # for i in v:
    #     print(i)

    # distance = airport.Airport()
    
        #calculate distance between routes 

    # print(testCsv)
    # _airdict = airport.Airport()
    # parsedAirportCsv = _airdict.parseAirport('airport.csv')
    # for item in parsedAirportCsv:
    #     print(parsedAirportCsv[item])
     
    # print(parsedAirportCsv)

    

if __name__=="__main__":
    main()












