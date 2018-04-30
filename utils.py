import argparse
import csv
import io
import operator
from operator import itemgetter
from collections import Counter
from airport import Airport
import os
import errno
#make structures for retrieving data
#airports = Airport.getAirportData("./data/airports.csv")
#currency_rate = Currency.getCurrency("./data/currencyrates_updated.csv")
#country_currency = Currency.getCountryCurrency("./country_currency_updated.csv")
#aircraft = Airport.getAircraft("./data/aircraft.csv")

class utils:

    def __init__(self):
        self.__csv_data=[]

    #Utils class is checking csv input for 3 requirements:
    #duplicate values
    #more than 1 airport was inputted
    #checks for incorrect IATA code
    #checks for aircraft model

     #For length of input exluding last element(aircraft code)
        #print(parsedAircraft)

        #check for the presence of aircode in row
        #if aircode is in row, pop it off the stack LIFO style
        #return range

    def input(self,csv_path):
        """Takes csv input from command-line and checks for errors"""
        # test_routes_csv = csv.reader(io.open(
        #     csv_path.csv_file_path, "r", encoding=csv_path.encoding), delimiter=",", quotechar='"')

        inputFile = open(csv_path.csv_file_path, 'r', encoding='utf-8')
        fileReader = csv.reader(inputFile,delimiter=',')
        finalCsv = []
        aircrafts=[]
        aircraftRange=[]
        for row in fileReader:
            self.__csv_data = []
            # print("ROW:::", row)
            #finding duplicate values
            D = [k for k, v in Counter(row).items() if v > 1]
            if len(D) != 0:
                print("There are duplicate values")
                #dont append row to csv_data

            _airdict = Airport()
            parsedAirportDict = _airdict.parseAirport('airport.csv')
            parsedAircraft = _airdict.Aircraft('aircraft.csv')
            # print(parsedAircraft)
            #Checking for incorrect IATA codes
            dests = row[:-1]
            # print(dests)
            if len(dests) <= 1:
                print("Need to enter a minimum of 2 aircodes", '\n')
            else:
                for i in dests:
                    if i in list(parsedAirportDict.keys()):
                        self.__csv_data.append(i)
                    else:
                        print("Incorrect IATA entered", '\n')

            #Presuming Aircraft code will always be last item in csv file
            aircraft_code = row[-1]
            #print(aircraft_code)

            if aircraft_code in list(parsedAircraft.keys()):
                print("Aircraft range for", aircraft_code,
                    "is:", parsedAircraft.get(aircraft_code))
                #self.__csv_data.append(parsedAircraft.get(aircraft_code))
            else:
                print("Warning, please specify aircraft model")
            aircrafts.append(aircraft_code)
            aircraftRange.append(parsedAircraft.get(aircraft_code))
            finalCsv.append(self.__csv_data)
        return finalCsv, aircrafts, aircraftRange
    
    def tocsv(self,output):
        try:
            os.makedirs(os.path.join(os.getcwd(), "outputs"))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
        toFile = os.path.join(os.getcwd(), "outputs", "output.csv")
        try:
            with open(toFile, "w", newline='') as f:
                writer = csv.writer(f)
                try:
                    writer.writerows(output)
                    print("Output File Generated")
                except StopAsyncIteration as identifier:
                    print("Iteration stopped: ",identifier)
        except PermissionError as err:
            print("File seems to opened by some other application. Close the file and try again!")



    

            




    
