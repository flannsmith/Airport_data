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


    # def distanceBetweenAirports(self, latitude1, longitude1, latitude2, longitude2):
	#     """Calculates the distance from between 2 airports and returns a float"""
	#     coords_1 = (latitude1, longitude1)
	#     coords_2 = (latitude2, longitude2)

	#     return geopy.distance.vincenty(coords_1, coords_2).km


    def Aircraft(self, csv_path):
        """Parses Aircraft file, creating dict with aircraft code and range"""
        aircraft_ranges = open(csv_path, "r")
        csv3 = csv.reader(aircraft_ranges,delimiter=",", quotechar='"')
        self.__aircraft = {}
        for row in csv3:
            aircraft_id = row[0]
            self.__aircraft[aircraft_id] = row[4]
        return self.__aircraft

    def distanceBetweenAirports(self, latitude1,longitude1,latitude2,longitude2):
            # """Calculates the distance from between 2 airports and returns a float"""
            # print("Latitude1: {}; Longitude1: {}, Latitude2: {}, Longitude:{} ".format(latitude1,longitude1,latitude2,longitude2))
            # coords_1 = (latitude1, longitude1)
            # coords_2 = (latitude2, longitude2)
            if latitude1 == latitude2 and longitude1 == longitude2:
                return 0
            else:
                return geopy.distance.vincenty(latitude1, longitude1, latitude2, longitude2).km

    #minimum edge value
    # 
    def distanceEdges(self, testdests):
        self.__distance_list = []
        for p0, p1 in itertools.combinations(testdests, 2):
            distance_btw_airports = geopy.distance.vincenty(p0, p1).km
            # distance_btw_airports = distanceBetweenAirports(p0, p1)
            print("Distance between:", p0, p1, "is", distance_btw_airports)
            self.__distance_list.append(distance_btw_airports)


    def minSpanningDistance(self, list2):
        """ Calculates distances between all airports in list """
        self.__distance_list = []
        print("No. of aircodes entered:", len(list2))
        if len(list2) <= 1:
            print("Enter a min of 2 aircodes needed to calculate distance")
        #elif len(list2) = 2: plug into original formula
        else:
            #min_distance = Airport.distanceBetweenAirports(list2[1], list2[2])
            for p0, p1 in itertools.combinations(list2, 2):
                distance_btw_airports = distanceBetweenAirports(p0, p1)
                print("Distance between:", p0, p1, "is", distance_btw_airports)
                self.__distance_list.append(distance_btw_airports)

        return self.__distance_list





    




