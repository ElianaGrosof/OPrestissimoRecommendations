#test_apyroi.py
#@author: Eliana Grosof, April 2019

#all of our problems solved by https://stackoverflow.com/questions/52688220/python-apyori-sorting-by-lift?fbclid=IwAR3CV0vVKyTxn4OcxFsdzNTfugCgMQf52VdYx_LkjUspWo57cf_FcfQJ7fE

import dfmethods

import sys
import csv
from apyori import apriori, load_transactions

import pandas as pd

#converts a csv file into an array
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

    df.sort_values(by ='Lift', ascending = False, inplace = True)

    return df

def replacecrns(liftdf):
    crndict = dfmethods.makedict("courses.csv")

    for crn in liftdf['Items']:
        crn = str(crn)
        print("crn is:",crn)
        if crn is not None:
            crnsplit = replacehelper(crn)

        if crn is not None and len(crnsplit) == 1:
            name = crndict[crnsplit[0]]
            ogcrn = crnsplit[0]
            print("crn and crndict:", ogcrn, name)
            liftdf['Items'] = liftdf['Items'].replace(set(ogcrn), set(name), regex=True, inplace=True)
            print(liftdf['Items'])

    # for i in range (0, len(liftdf['Items'])):
    #     val = liftdf['Items'].values[i]
    #
    #     print("val is: ", val)
    #
    #     values = replacehelper(val)
    #
    #     if values != 'Skip':
    #         print(values[0])
    #         newval = crndict[values[0]]
    #         for v in values[1:]:
    #             newval = newval + ", " + crndict[v]
    #         liftdf['Items'] = liftdf['Items'].replace(val, newval, regex=True, inplace=True)
    #         print("val is:", val, newval)

    print(liftdf)
    return liftdf

def replacehelper(val):
    values = str(val).split()
    bettervalues = []
    for value in values:
        value = strip_punctuation(value)
        if value != '':
            bettervalues.append(value)
    # print("values is: ", bettervalues)
    if bettervalues != []:
        return bettervalues
    else:
        return "Skip"

def strip_punctuation(s):
    punctuation = ["'", '{', '}', ',']
    return ''.join(c for c in s if c not in punctuation)

def tinytest():
    transactions = [['beer', 'nuts'], ['beer', 'cheese']]
    results = list(apriori(transactions, min_support=0.6))
    print(results)

def main():
    min_sup = float(sys.argv[1]) #0.004 or 0.003 is a good number #0.025 is managable on cartsof2014
    file = sys.argv[2]
    carts = dfmethods.makecarts(file) #"carts.csv"
    #carts = arrayify("store_data.csv")
    liftdf = generatelist(carts, min_sup)
    replacecrns(liftdf)

    #tinytest()

main()
