import operator
import csv
import io
import geopy
import itertools

class Airport:

    def __init__(self):
        self.__csv_data = []

    def parseAirport(self, csv_path):
        """ Sorts airport.csv into dict """
        csv_reader = csv.reader(io.open(csv_path, "r"), delimiter=",", quotechar='"')

        self.__airports_data = {}
        #sort by alphabetical order
        sort1 = sorted(csv_reader, key=operator.itemgetter(1))
        for row in sort1:
            #Declaring IATA as key in airports dict
            
            airport_id = row[4]
            self.__airports_data[airport_id] = float(row[6]), float(row[7])
        #print(self.__airports_data)
        return self.__airports_data

    def Aircraft(self, csv_path):
        aircraft_ranges = open(csv_path, "r")
        csv3 = csv.reader(aircraft_ranges,delimiter=",", quotechar='"')
        next(csv3)
        self.__aircraft = {}
        for row in csv3:
            aircraft_id = row[0]
            #convert imperial to metric
            if row[2] == 'imperial':
                self.__aircraft[aircraft_id] = float(row[4]) * 1.60934
            else:
                self.__aircraft[aircraft_id] = float(row[4])
        return self.__aircraft
                

    def distanceBetweenAirports(self, latitude1,longitude1,latitude2,longitude2):
            # """Calculates the distance from between 2 airports and returns a float"""
            # print("Latitude1: {}; Longitude1: {}, Latitude2: {}, Longitude:{} ".format(latitude1,longitude1,latitude2,longitude2))
            coords_1 = (latitude1, longitude1)
            coords_2 = (latitude2, longitude2)
            if latitude1 == latitude2 and longitude1 == longitude2:
                return 0
            else:
                return geopy.distance.vincenty(coords_1, coords_2).km

  
    def isItineraryPossible(self,airRange,itinerary):
        for i in itinerary:
            if airRange >= i:
                continue
            else:
                return False




    




