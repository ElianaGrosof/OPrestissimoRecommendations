#test_apyroi.py

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
    results = list(apriori(dataset, min_confidence=0.8))
    print(results)

def main():
    file = "store_data.csv"
    dataset = arrayify(file)
    generatesupport(dataset)
    copiedcode(file)

main()
