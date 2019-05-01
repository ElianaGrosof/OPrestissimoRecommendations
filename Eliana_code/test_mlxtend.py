#test_mlxtend.py
#copied and pasted code from the tutorial
import dfmethods

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
    print("te_ary is: ", te_ary)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    return df

def output(df):
    print(apriori(df, min_support=0.6))

    frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)
    frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
    print(frequent_itemsets)

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
    carts = dfmethods.makecarts("carts.csv")
    dups = list_duplicates(carts)

    df = makedf(carts)
    output(df)

main()
