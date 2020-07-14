#!/usr/bin/env python
"""
This program generates the support, confidence, and lift of a set of "carts" of related classes
using the apyroi implementation of the apriori algorithm.

@author: Eliana Grosof, April 2019, edited July 2020
"""
#Meta information
__author__ = "Eliana Grosof"
__credits__ = ["Olivia Vasquez", "Leah Yassky"]

import csv
from apyori import apriori, load_transactions

import pandas as pd

import time

#converts a csv file into an array
#not used in current implementation but potentially useful
def arrayify(file):
    """
    Converts a comma-separated file of carts into a list of lists.
    :param file: a .csv file containing rows of carts
    :return: a list containing lists of carts
    """
    results = []
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',') # change contents to floats
        for row in reader: # each row is a list
            results.append(row)
    return results

def run_apriori(dataset, min_sup, min_confidence):
    """
    This function runs the apyroi implementation of the
    apriori algorithm, and converts it to a Pandas DataFrame.

    :param dataset: list of lists of carts
    :param min_sup: minimum support
    :param min_confidence: minimum confidence
    :return: DataFrame containing information about support, confidence, and lift
    """

    results = list(apriori(dataset, min_support=min_sup, min_confidence=min_confidence)) #, min_confidence=0.8

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

    return df


def generatecourse(df):
    """ generates a random course from DataFrame of courses """
    return df['Antecedent'].sample(n=1)

def tinytest():
    """ Test for apriori algorithm from apyroi. """
    transactions = [['beer', 'nuts'], ['beer', 'cheese']]
    results = list(apriori(transactions, min_support=0.6))
    print(results)

def main():
    min_sup = 0.0006
    min_conf = 0.1
    carts = arrayify('../data/converted_carts.csv')#carts_list
    sorteddf = run_apriori(carts, min_sup, min_conf)
    pd.set_option('display.max_columns', None)
    print(sorteddf)
    #write to .csv file
    sorteddf.to_csv('../data/rules_conf=0.1.csv')

main()
