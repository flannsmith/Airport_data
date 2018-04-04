import geopy.distance
import csv
import operator
import argparse

#Taking input of destinations from user in the form of one long sting
#-l "DUB SYD GBK QTN"
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
            print(airport_id)
            distances.update({airport_id : airports[airport_id]})
            #distances.update({'Aircode': airports[airport_id]})
            #distances == airports[airport_id]
            print(distances)











# def routes(a_list):
#     print(a_list)

# routes(*dests)

  

