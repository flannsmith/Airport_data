import csv
import io
import operator
import itertools
#inefficient to iterate through 2 dicts
#merged 2 currency files based on currency code 

class Currency:
    
    def __init__(self):
        self.__currencyDict = {}
    
    def currencyParser(self, csv_path):
        """Reads concat currency csv into list"""
        csv_reader = csv.reader(io.open(csv_path, "r"))
        #skips header in csv (country_currency) file
        next(csv_reader)
        #sort by alphabetical order
        sort_a = sorted(csv_reader, key=operator.itemgetter(1))
        
        #store values into dict
        for row in sort_a:
            currency_code = row[11]
            self.__currencyDict[currency_code] = (row[-1])
        return self.__currencyDict

           

    #calculate price by dividing distance from toEuroRate
    #presuming country of final destination will pay for total trip
    #Paying country will be last person in list 
    # def oneLegCost(self, IATA, toEuroRate, distance):
   



 

           
        
    
        
