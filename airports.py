import sys
import argparse
import operator
from math import sin, cos, acos, pi, radians
import csv
import geopy.distance


# #aircode2 is the destination

parser = argparse.ArgumentParser(description="Calculate distance between airports")
parser.add_argument('aircode1', type=str, help="3 letter airport aircode/id e.g. 'DUB'")
parser.add_argument('aircode2', type=str, help="3 letter airport aircode/id e.g. 'SYD'")
args = parser.parse_args()

airport_names = open('airport.csv', 'r')
csv0 = csv.reader(airport_names, delimiter=',')
#sort by column id (does this make it quicker?)
sort1 = sorted(csv0, key=operator.itemgetter(1))
airports = {}
for row in sort1:
    airport_id = row[4]
    airports[airport_id] = row[1], row[2], float(row[6]), float(row[7])

	
def distanceBetweenAirports(latitude1, longitude1, latitude2, longitude2):
	"""Calculates the distance from between 2 airports and returns a float"""
	coords_1 = (latitude1,longitude1)
	coords_2 = (latitude2, longitude2)

	return geopy.distance.vincenty(coords_1, coords_2).km

	# lat1 = radians(latitude1)
	# lon2 = radians(longitude1)
	# lat2 = radians(latitude2)
	# lon2 = radians(longitude2)
	# dlon = lon2 - lon1
	# dlat = lat2 - lat1

	# a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	# c = 2 * atan2(sqrt(a), sqrt(1 - a))
	# distance = R * c

	
#    radius_earth = 6371
#    theta1 = longitude1 * (2 * pi) / 360
#    theta2 = longitude2 * (2 * pi) / 360
#    phi1 = (90 - latitude1) * (2 * pi) /360
#    phi2 = (90 - latitude2) * (2 * pi) /360
#    distance = acos(sin(phi1)) * sin(phi2) * cos(theta1-theta2) + cos(phi1) * cos(phi2) * radius_earth
#distance = acos(sin(latitude1)) * sin(latitude2) + cos(latitude1)*cos(latitude2)*cos(longitude2-longitude1) * 6371

	

   
# Correct distance formula 
# Dist(point1, point2) =ACOS( SIN(lat1)*SIN(lat2) + COS(lat1)*COS(lat2)*COS(lon2-lon1) ) * 6371


def legOfJourney():
	"""Calculates cost of one-way trip in euros presuming use of country of destination's exchange rate"""
	country_dest = args.aircode2

	#sort by column id (does this make it quicker?)
	for row in sort1:
		airport_id = row[4]
		if airport_id == country_dest:
			#print(row)
			countryName = row[3]
			#print(countryName)

	country = countryName
	country_currency = open('countrycurrency.csv', 'r')
	csv1 = csv.reader(country_currency, delimiter=',')
	#skips header in countrycurrency.csv
	next(csv1)

	with open('countrycurrency.csv') as file:
		reader = csv.DictReader(file)
		for row in reader:
			if row['name'] == country:
				#print(row)
				#print(row['currency_alphabetic_code'])
				CurrCode = row['currency_alphabetic_code']
	curr_rate = open('currencyrates.csv', 'r')
	csv2 = csv.reader(curr_rate, delimiter=',')
	for row1 in csv2:
		if row1[1] == CurrCode:
			#print(row1[2])
			CurrRate = row1[2]
	return float(CurrRate)

def main():
	#get user to enter 1 airport_id e.g. 'DUB'
	#get user to enter 2nd airport_id e.g. 'SYD'
	airport1 = airports.get(args.aircode1)
	airport2 = airports.get(args.aircode2)
	lat1 = airport1[2]
	long1 = airport1[3]
	lat2 = airport2[2]
	long2 = airport2[3]
	print("Distance between airports: ", distanceBetweenAirports(lat1, long1, lat2, long2))
	distance = distanceBetweenAirports(lat1, long1, lat2, long2)
	cost = legOfJourney()
	print("Cost of single itinerary leg in €: ", cost * abs(distance))

if __name__ == "__main__":
    main()


#multilegitinerary = input("Enter route you wish to visit (e.g. ORIGIN: DEST1: DEST2: DEST3: HOME:")

# parser.add_argument('multi_dest_trip', type=str, help="Enter route you wish to visit (e.g. ORIGIN: DEST1: DEST2: DEST3: HOME:")

# s = args.multi_dest_trip

# print(s)



# List1 = []
# for string in multilegitinerary:
# 	List1.insert(string)

# def selection_sort(items):
# # """Sorts a list of items into ascending order using the
# #        selection sort algorithm."""
#    # Find the location of the smallest element in list
# 	for step in range(len(items)):
# 		origin = multilegitinerary[0]
# 		home = multilegitinerary[-1:]
# 		closest_location = step
# 		for i in range(step, len(List1)):
# 			if List1[i] < List1[i+1]:
# 				closest_location = step
# 				temporary_item = items[step]
# 		items[step] = items[closest_location]
# 		items[closest_location] = temporary_item
	




#def Route(airport_list):

#how to take input from command line and save it as a list?
# for Aircode in List:  

#[Origin, Dest1, Dest2, Dest3, Dest4, Home]
#Calculate distance between each destination
#For element in list, order list based on destinations with shorter distance 
#Sorting algorithm 
#loop through list and calculate distance between origin and Destinations:
#which 
#if distance between element [1] < element [0] swap them 
#if distance home less than element @ end swap them   



#make class called route (takes input of various destinations) (input of 5 airports)
#takes a series of destinations
#decide whether to make an ordered or unordered list
#set for inputs or sequence of best routes
