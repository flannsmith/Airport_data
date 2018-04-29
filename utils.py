import argparse
import csv
import io
import operator
from operator import itemgetter
from collections import Counter
from airport import Airport

#make structures for retrieving data
#airports = Airport.getAirportData("./data/airports.csv")
#currency_rate = Currency.getCurrency("./data/currencyrates_updated.csv")
#country_currency = Currency.getCountryCurrency("./country_currency_updated.csv")
#aircraft = Airport.getAircraft("./data/aircraft.csv")

class utils:

    #init always present in class
    def __init__(self):
        self.__csv_data=[]

    #Utils class is checking csv input for 3 requirements:
    #duplicate values
    #more than 1 airport was inputted
    #checks for incorrect IATA code

    def input(self,csv_path):
        """Takes csv input from command-line and checks for errors"""
        csv_reader = csv.reader(io.open(
            csv_path.csv_file_path, "r", encoding=csv_path.encoding), delimiter=",", quotechar='"')
        self.__csv_data = []
        for row in csv_reader:
            #finding duplicate values
            D = [k for k, v in Counter(row).items() if v > 1]
            if len(D) != 0:
                print("There are duplicate values")
                #dont append row to csv_data
            _airdict = Airport()
            parsedAirportDict = _airdict.parseAirport('airport.csv')
            
            parsedAircraft = _airdict.Aircraft('aircraft.csv')
            #For length of input exluding last element(aircraft code)
            item = row[:-1]
            print(item)
    
            #remove last item from stack
            aircraft_code = row.pop()
            
            #Checking for incorrect IATA codes
            for item in csv_reader:
                if item != parsedAirportDict:
                    print("Incorrect IATA entered",'\n')
                if len(item) <= 1:
                    print("Need to enter a minimum of 2 aircodes", '\n')
            #create aircraft object
            for aircraft_code in csv_reader:
                if aircraft_code != parsedAircraft:
                    print("No aircode included")
                #else: 
                #     
                #else: somehow save value of aircraft for later use? 
            else:
                self.__csv_data.append(row)
        return self.__csv_data



    

            




    
