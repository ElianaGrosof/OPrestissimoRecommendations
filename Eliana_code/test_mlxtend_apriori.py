#test_mlxtend_apyroi.py
#note: if doesn't work, pip install mlxtend==0.15.0.0

import csv
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

def arrayify(file):
    results = []
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',') # change contents to floats
        for row in reader: # each row is a list
            results.append(row)
    return results

def makedataframe(dataset):
    transactencoder = TransactionEncoder()
    transactencoder_array = transactencoder.fit(dataset).transform(dataset)
    dataframe = pd.DataFrame(transactencoder_array, columns=transactencoder.columns_)
    return dataframe

def generatesupport(dataframe):
    apriori(dataframe, min_support=0.6)
    output = apriori(dataframe, min_support=0.6, use_colnames=True)
    print(output)

def main():
    file = "store_data.csv"
    dataset = arrayify(file)
    dataframe = makedataframe(dataset)
    #print(dataframe)
    generatesupport(dataframe)

main()
