import csv
import operator
#Fuel capacity for a given rout
#Aircraft class that has aircraft ranges data
#iterate through aircraft.csv to find aircraft ranges

aircraft_ranges = open('aircraft.csv', 'r')
        csv3 = csv.reader(aircraft_ranges, delimiter=',')
        #sort by column id (does this make it quicker?)
        #sort3 = sorted(csv3, key=operator.itemgetter(1))
for row in sort3:
            aircraft_id = row[0]
            aircraft[aircraft_id] = row[4]
        print(aircraft)




# g = Aircraft()
# g = get("C212")
# print(g)
