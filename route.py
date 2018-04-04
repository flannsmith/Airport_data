import geopy.distance
import csv
import operator
import argparse
multilegitinerary = input("Enter route you wish to visit (e.g. ORIGIN: DEST1: DEST2: DEST3: HOME:")


# parser.add_argument('multi_dest_trip', type=str, help="Enter route you wish to visit (e.g. ORIGIN: DEST1: DEST2: DEST3: HOME:")
# parser.add_argument('origin', type=str, help="3 letter airport aircode/id e.g. 'DUB'")
# parser.add_argument('dest1', type=str, help="3 letter airport aircode/id e.g. 'SYD'")
# args = parser.parse_args()

# s = args.multi_dest_trip

#creating a list and adding input of multilegitinerary to it
#next step = organising list in order of distance and sorting elements

List1 = []
#print(multilegitinerary)
words = multilegitinerary.split(" ")
List1.append(words)
print(List1)

#print(type(List1))

# def Route(*params):
#     """Takes list argument and handles each list item as a separate parameter"""
#     print(*params)

# print (Route(List1))

#print(List1)

#s = set(List1)
#print(s)
#iterate through dictionary to find the values in my list 

origin = List1[0]
home = List1[-1]
destinations = List1[1:-2]

airport_names = open('airport.csv', 'r')
csv0 = csv.reader(airport_names, delimiter=',')
#sort by column id (does this make it quicker?)
sort1 = sorted(csv0, key=operator.itemgetter(1))
airports = {}
distances = {}

for row in sort1:
    airport_id = row[4]
    airports[airport_id] = float(row[6]), float(row[7])
    for item in List1:
      if item == airports[airport_id]:
          print("Found they key")
            

# def Route(List1): 

# for key in airports:
#     for item in List1:
#         if item == airports[key]:
#         #if item is a key in airport dictionary
#         #make a new dictionary returning the corresponding row
#             print(airports[key])




