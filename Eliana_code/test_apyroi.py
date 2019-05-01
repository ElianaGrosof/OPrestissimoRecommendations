#test_apyroi.py
#@author: Eliana Grosof, April 2019

import dfmethods

import sys
import csv
from apyori import apriori, load_transactions

#converts a csv file into an array
def arrayify(file):
    results = []
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',') # change contents to floats
        for row in reader: # each row is a list
            results.append(row)
    return results

def generatesupport(dataset, min_sup):
    output = list(apriori(dataset, min_support=min_sup)) #, min_confidence=0.8
    print(output)

def tinytest():
    transactions = [['beer', 'nuts'], ['beer', 'cheese']]
    results = list(apriori(transactions, min_support=0.6))
    print(results)

def main():
    min_sup = float(sys.argv[1]) #0.004 or 0.003 is a good number
    file = sys.argv[2]
    carts = dfmethods.makecarts(file) #"carts.csv"
    #carts = arrayify("store_data.csv")
    generatesupport(carts, min_sup)
    #tinytest()

main()
