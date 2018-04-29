import csv

class Cost:

    def toEuroRate(self,country_dest,csvPath0,csvPath1,csvPath2):
        """Calculates cost of one-way trip in euros presuming use of country of destination's exchange rate"""
        #country_dest = billingCountry
        airports = open(csvPath0, "r")
        csv0 = csv.reader(airports, delimiter=",", quotechar='"')
        for row in csv0:
            airport_id = row[4]
            if airport_id == country_dest:
                #print(row)
                countryName = row[3]
                print("Your final destination is:", countryName, '\n')

        country = countryName
        country_currency = open(csvPath1, 'r')
        csv1 = csv.reader(country_currency, delimiter=',')
        #skips header in countrycurrency.csv
        next(csv1)
        for row in csv1:
            if row[0] == country:
                #print(row)
                #print(row['currency_alphabetic_code'])
                CurrCode = row[14]
        print("The destination's currency is:",CurrCode, '\n')

        curr_rate = open(csvPath2, 'r')
        csv2 = csv.reader(curr_rate, delimiter=',')
        for row1 in csv2:
            if row1[1] == CurrCode:
                #print(row1[2])
                CurrRate = row1[3]
        return float(CurrRate)
