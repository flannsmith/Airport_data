import unittest

from time import time

#Time testing

def compute_average(n):
    """Performs n appends to an empty list and return average time elapsed"""
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return(end - start)/n

def compute_average_list(n, data):
    """Performs n appends to an empty list and return average time elapsed"""
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return(end - start)/n

list1 = [1,2,3,4,5,6]
list1.pop(2)

print(list1)