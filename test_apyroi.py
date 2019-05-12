#test_apyroi.py
#@author: Eliana Grosof, April 2019
#This program prints a sorted table of relationships that is determined by running the apriori algorithm. 

#all of our problems solved by https://stackoverflow.com/questions/52688220/python-apyori-sorting-by-lift?fbclid=IwAR3CV0vVKyTxn4OcxFsdzNTfugCgMQf52VdYx_LkjUspWo57cf_FcfQJ7fE

import dfmethods

import sys
import csv
from apyori import apriori, load_transactions

import pandas as pd

#converts a csv file into an array
#not used in current implementation but potentially useful
def arrayify(file):
    results = []
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',') # change contents to floats
        for row in reader: # each row is a list
            results.append(row)
    return results

def generatelist(dataset, min_sup):

    results = list(apriori(dataset, min_support=min_sup)) #, min_confidence=0.8

    df = pd.DataFrame(columns=('Items','Antecedent','Consequent','Support','Confidence','Lift'))

    Support =[]
    Confidence = []
    Lift = []
    Items = []
    Antecedent = []
    Consequent=[]

    for RelationRecord in results:
        for ordered_stat in RelationRecord.ordered_statistics:
            Support.append(RelationRecord.support)
            Items.append(RelationRecord.items)
            Antecedent.append(ordered_stat.items_base)
            Consequent.append(ordered_stat.items_add)
            Confidence.append(ordered_stat.confidence)
            Lift.append(ordered_stat.lift)

    df['Items'] = list(map(set, Items))
    df['Antecedent'] = list(map(set, Antecedent))
    df['Consequent'] = list(map(set, Consequent))
    df['Support'] = Support
    df['Confidence'] = Confidence
    df['Lift']= Lift

    df = df[df.Lift != 1.0]
    df.sort_values(by =['Support','Lift'], ascending = [True, False], inplace = True)

    #df.head(10) will print out 10 Relation Records
    print(df.head())
    #only if you want to print out the results in a CSV: 
    #df.head().to_csv('./outputs/s2013.csv', sep='\t', encoding='utf-8')
    return df

#generates a random course from the list of courses
def generatecourse(df):
    return df['Antecedent'].sample(n=1)

#doesn't work yet
def findmostrelated(df, course):
    return df.loc[df['Antecedent'] == course]

def tinytest():
    transactions = [['beer', 'nuts'], ['beer', 'cheese']]
    results = list(apriori(transactions, min_support=0.6))
    print(results)

def main():
    min_sup = float(sys.argv[1]) #0.004 or 0.003 is a good number #0.025 is managable on cartsof2014
    file1 = sys.argv[2]
    file2 = sys.argv[3]
    carts = dfmethods.cartsnames(file1, file2) #"carts.csv"
    sorteddf = generatelist(carts, min_sup)

main()
