import geopy.distance
import csv
import operator
multilegitinerary = input("Enter route you wish to visit (e.g. ORIGIN: DEST1: DEST2: DEST3: HOME:")

# parser.add_argument('multi_dest_trip', type=str, help="Enter route you wish to visit (e.g. ORIGIN: DEST1: DEST2: DEST3: HOME:")

# s = args.multi_dest_trip

#creating a list and adding input of multilegitinerary to it
#next step = organising list in order of distance and sorting elements

List1 = []
#print(multilegitinerary)
words = multilegitinerary.split(" ")
List1.append(words)
print(type(List1))



#print(List1)

#set is much more efficient than List behind the scenes as python can attempt to directly access the target number in the set, rather than iterate through every item in the list and compare every item to the target number.

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
print (airports[airport_id])
    # for item in List1:
    #     if item == airports[airport_id]:
    #         print(item)

# def Route(List1): 

# for key in airports:
#     for item in List1:
#         if item == airports[key]:
#         #if item is a key in airport dictionary
#         #make a new dictionary returning the corresponding row
#             print(airports[key])




