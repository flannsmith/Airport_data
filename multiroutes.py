import geopy.distance
import csv
import operator
import argparse
import geopy.distance
from operator import itemgetter


#Taking input of destinations from user in the form of one long string
#To input a chain of destinations/run program type:
#multiroutes.py -l "DUB SYD GBK QTN"
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

#append values into list ==> then have group of values which comprise coords- latitude and longitude

print(distances)

list2 =[]

for key, value in distances.items():
    list2.append(value)

# print(list2)

# origin = list2[0]
# home = list2[-1]
# print(origin)
# print(home)


#Sort elements in middle of list by 'sorted' function => sorts based on latitude
sorted_dests = sorted(list2, key=itemgetter(slice(1,-1)))
print(sorted_dests)


#Next step is to calculate distance between each element in sorted_dests list and apply selection sort algorithm
def distanceBetweenAirports(coords_1, coords_2):
	"""Calculates the distance from between 2 airports and returns a float"""
	# coords_1 = (latitude1, longitude1)
	# coords_2 = (latitude2, longitude2)
	return geopy.distance.vincenty(coords_1, coords_2).km



# ---------------------------------------------
# print("Unsorted list distances")
# print(distanceBetweenAirports(origin, list2[1]))
# print(distanceBetweenAirports(list2[1],list2[2]))
# print(distanceBetweenAirports(list2[2], home))


# def selection_sort(items):
# # """Sorts a list of items into ascending order using the
# #        selection sort algorithm."""
#    # Find the location of the smallest element in list
#     for step in range(len(items)):
#         closest_location = step
#         for i in range(step, len(list2)):
#             if distanceBetweenAirports(list2[i],list2[1]) < distanceBetweenAirports(list2[1],list2[2]):
#                 closest_location = step
#                 temporary_item = items[step]
#         items[step] = items[closest_location]
#         items[closest_location] = temporary_item

# print(selection_sort(list2))
