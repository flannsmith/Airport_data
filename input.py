import argparse
import csv
import io
from operator import itemgetter
from collections import Counter
from utils import utils


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file_path")
    parser.add_argument("--encoding", default="utf_8")
    options = parser.parse_args()
    _utObject = utils()
    testCsv = _utObject.input(options)
    print(testCsv)

if __name__=="__main__":
    main()

# #Accept input from command line in the form of csv



#         #if aircode is not in airports_dict[id]
#         #aircode remove from list
    
#         #check for aircraft code
#         #if aircraft code 
   
    
# print(csv_data)
# #print(D)




# #dups_dict = {row: count for row, count in csv_reader.most_common() if count > 1}
# #print(dups_dict)


#     # for example: columns 0, 2 and 4 comprise the key





#check for type of input
# print(type(row))

#how to find duplicate values in a list - error if duplicate values


#iterate through aircode and look for duplicate values 
#for row in csv_reader: 

#check for airports that are not in there

#check if aircraft is given




