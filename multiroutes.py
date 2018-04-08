import geopy.distance
import csv
import operator
import argparse
import geopy.distance
from operator import itemgetter
import math
import itertools

#Taking input of destinations from user in the form of one long string
#To input a chain of destinations/run program type:
#multiroutes.py -l "DUB LDN SYD AZ3 KDH"
#Gets converted into a list
#need to iterate through list and for each item create a new dictionary with corresponding latitude and longitide

parser = argparse.ArgumentParser(description="Enter the chain of airports/destinations you wish to visit as a string e.g. 'DUB LDN': ")
parser.add_argument('-l', '--list', help='-l "DUB SYD LDN HEA GLW"', type=str)
args = parser.parse_args()
my_list = [str(item) for item in args.list.split(' ')]

print(my_list)

airport_names = open('airport.csv', 'r')
csv0 = csv.reader(airport_names, delimiter=',')
#sort by column id (does this make it quicker?)
sort1 = sorted(csv0, key=operator.itemgetter(1))
airports = {}
distances = {}
for row in sort1:
    airport_id = row[4]
    airports[airport_id] = float(row[6]), float(row[7])
    for i in range(len(my_list)):
        if my_list[i] == airport_id:
            #print(airport_id)
            distances.update({airport_id : airports[airport_id]})
            #distances.update({'Aircode': airports[airport_id]})
            #distances == airports[airport_id]
            #print(distances)

#print(distances)

#append values into list ==> then have group of values which comprise coords- latitude and longitude

list2 =[]
for key, value in distances.items():
    list2.append(value)

#Sort elements in middle of list by 'sorted' function => sorts based on increasing latitude

list2[1:-1]= sorted(list2[1:-1])
print(list2)

#if distance between element[0] and element[1] > element[0] and element[2]
#swap values

#Next step is to calculate distance between each element in sorted_dests list and apply selection sort algorithm
def distanceBetweenAirports(coords_1, coords_2):
	"""Calculates the distance from between 2 airports and returns a float"""
	# coords_1 = (latitude1, longitude1)
	# coords_2 = (latitude2, longitude2)
	return geopy.distance.vincenty(coords_1, coords_2).km


def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

# min_distance = distance(list2[0], list2[1])
# for p0, p1 in itertools.combinations(list2, 2):
#     min_distance = min(min_distance, distance(p0, p1))
#     print(min_distance)

min_distance = distanceBetweenAirports(list2[0], list2[1])
for p0, p1 in itertools.combinations(list2, 2):
    distance_btw_airports = distanceBetweenAirports(p0, p1)
    #min_distance = min(min_distance, distanceBetweenAirports(p0, p1))
    #print("Distance between:", p0, p1, "is", distance_btw_airports)
    # if distance_btw_airports(p0, p1) > distance_btw_airports(p0, p1):
    #     p0,p1 = p0,p1
    #print("Distance between:",p0, p1, "is", min_distance)

min_distance = distanceBetweenAirports(list2[1], list2[2])
for p0,p1 in itertools.combinations(list2, 2):
    distance_btw_airports = distanceBetweenAirports(p0, p1)
    print("Distance between:", p0, p1, "is", distance_btw_airports)



def bestRoutes(list):
    """Calculates best routes from list of input"""
    #From user input as string of aircodes, aircodes are parsed into a list
    #next the middle elements of list are sorted 
    #iterates through sorted list calculating distance between each element
    #sums distance between each element
    #multiplies distance by cost to get total journey cost
    #iterate through sorted list to find corresponding lat and long in distances dict:
    #when found return the aircodes in order of least distance







def insertion_sort(list):
    for index in range(1,len(list)):
        value = list[index]
        i = index -1
        for p0, p1 in itertools.combinations(list, 2):
            if distanceBetweenAirports(p0, p1) < distanceBetweenAirports(p0, p1):
                list[i+1] = list[i]
                list[i] = value

print(insertion_sort(list2))

        # while i>=0:
        #     if value < list[i]:
        #         list[i+1] = list[i]
        #         list[i] = value




# min_distance = distanceBetweenAirports(sorted_dests[0], sorted_dests[1])
# #iterates over sorted_dests list 
# for p0, p1 in itertools.combinations(sorted_dests,2):
#     min_distance = min(min_distance, distanceBetweenAirports(p0, p1))
# print(min_distance)
#     print(distanceBetweenAirports(sorted_dests[0], sorted_dests[1]))
    
#print(dist_btwn)
# print(list2)
# origin = list2[0]
# home = list2[-1]
# print(origin)
# print(home)







# for element in sorted_dests:
#     print(distanceBetweenAirports(element[0], element[1]))

# print(distanceBetweenAirports())

    #for i in sorted_dests:
        # if distanceBetweenAirports(sorted_dests[0], sorted_dests[2]) > distanceBetweenAirports(sorted_dests[], sorted_dests[i+2]):
            # sorted_dests[i] == sorted_dests[i+1]

#     sorted_dests[1] == sorted_dests[2]
# print("Distance")
#print(sorted_dests)


# def selection_sort(items):
# # """Sorts a list of items into ascending order using the
# #        selection sort algorithm."""
#    # Find the location of the smallest element in list
#     for step in range(len(items)):
#         closest_location = step
#         for i in range(step, len(items)):
#             if distanceBetweenAirports(list2[i],list2[1]) > distanceBetweenAirports(list2[1],list2[2]):
#                 list2[1] = list2[2]
#                 closest_location = step
#                 temporary_item = items[step]
#         items[step] = items[closest_location]
#         items[closest_location] = temporary_item

# print(selection_sort(sorted_dests))

