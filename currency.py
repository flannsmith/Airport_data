import csv
import io

#inefficient to iterate through 2 dicts
#how to join 2 currency files based on same values? 

class Currency:
    
    def __init__(self):
        self.__currencyDict = {}
       
    def currencyParser(self, csv_path):
        #making list from concatenated currency csvs
        csv_reader = csv.reader(io.open(csv_path, "r"))
        #skips header in csv (country_currency) file
        next(csv_reader)
        #store values into dict
        for row in csv_reader:
            dictkey = row[11]
            #to euro rate = row[-1]
            self.__currencyDict[dictkey] = row[-1]
        return self.__currencyDict

    #calculate price by dividing distance from toEuroRate

 

           
        
    
        
