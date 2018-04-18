class Cost:

    def legOfJourney(self,inputs):
        """Calculates cost of one-way trip in euros presuming use of country of destination's exchange rate"""
        
        country_dest = inputs[1]
        for row in sort1:
            airport_id = row[4]
            if airport_id == country_dest:
                #print(row)
                countryName = row[3]
                #print(countryName)

        country = countryName
        country_currency = open('countrycurrency.csv', 'r')
        csv1 = csv.reader(country_currency, delimiter=',')
        #skips header in countrycurrency.csv
        next(csv1)

        with open('countrycurrency.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['name'] == country:
                    #print(row)
                    #print(row['currency_alphabetic_code'])
                    CurrCode = row['currency_alphabetic_code']

        curr_rate = open('currencyrates.csv', 'r')
        csv2 = csv.reader(curr_rate, delimiter=',')
        for row1 in csv2:
            if row1[1] == CurrCode:
                #print(row1[2])
                CurrRate = row1[2]
        return float(CurrRate)
