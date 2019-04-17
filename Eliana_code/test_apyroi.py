#test_apyroi.py
#@author: Eliana Grosof, April 2019

import csv
from apyori import apriori, load_transactions

def arrayify(file):
    results = []
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',') # change contents to floats
        for row in reader: # each row is a list
            results.append(row)
    return results

def generatesupport(dataset):
    output = list(apriori(dataset, min_support=0.6)) #, min_confidence=0.8
    print(output)

def tinytest():
    transactions = [['beer', 'nuts'], ['beer', 'cheese']]
    results = list(apriori(transactions, min_support=0.6))
    print(results)

def main():
    file = "store_data.csv"
    dataset = arrayify(file)
    #print(dataset)
    #generatesupport(dataset)
    tinytest()

main()
