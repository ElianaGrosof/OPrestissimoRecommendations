#test_mlxtend.py
#copied and pasted code from the tutorial
import dfmethods
import random

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]

def makedf(dataset):
    te = TransactionEncoder()
    te_ary = te.fit(dataset).transform(dataset)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    return df

def output(df):
    print(apriori(df, min_support=0.003)) #0.002 gets us lots; 0.003 gets us 34; 0.004 gets us 11; 0.005 gets us 3

    frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)
    frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
    print(frequent_itemsets)

def generatefakecart():
    carts = []
    cs_class = [1, 2, 3, 4]
    for i in range(10):
        new_cart = []
        cs_classes_in_cart = random.randint(1, 4)
        for j in range(cs_classes_in_cart):
            random_cs_class = cs_class[random.randint(0, 3)]
            new_cart.append(random_cs_class)

        classes_left = 4-cs_classes_in_cart

        while classes_left > 0:
            non_cs_class = random.randint(100, 900)
            new_cart.append(non_cs_class)
            classes_left -= 1
        carts.append(new_cart)
    return carts

def list_duplicates(a):
    seen = {}
    dupes = []

    for l in a:
        for x in l:
            if x not in seen:
                seen[x] = 1
            else:
                if seen[x] == 1:
                    dupes.append(x)
                seen[x] += 1
    return seen

def printduplicates(dupdict):
    for key in dupdict:
        if dupdict[key] != 1:
            print(key, dupdict[key])

def main():
    carts = dfmethods.makecarts("carts.csv") #generatefakecart()
    dups = list_duplicates(carts)

    df = makedf(carts)
    output(df)

main()
