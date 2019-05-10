# dfmethods.py
# contains methods for transforming dataframes as relevant to this project
# @author Eliana Grosof May 2019

import pandas as pd

# creates a dictionary that maps the 'semcrn' to the 'short_title' of classes
def makedict(file):
    df = pd.read_csv(file, dtype='str', error_bad_lines=False)
    semcrn = df["semcrn"]
    short_title = df["short_title"]
    crn_dict = dict(zip(df.semcrn, df.short_title))
    return crn_dict

# converts course lists to carts (lists of "semcrns", type=str)
def cartscrns(file):
    df = pd.read_csv(file, dtype='str', error_bad_lines=False)
    cart_col = df["courses"]

    carts = []
    for c in cart_col:
        if type(c) != type(1.0) and c != " " and c != None:
            new_cart = c.split(" ")
            carts.append(new_cart)

    return carts
# converts course lists to carts (lists of "short_title"s, type=str)
def cartsnames(file1, file2):
    dictdf = makedict(file2)
    df = pd.read_csv(file1, dtype='str', error_bad_lines=False)
    cart_col = df["courses"]

    carts = []
    for c in cart_col:
        if type(c) != type(1.0) and c != " " and c != None:
            new_cart = c.split(" ")
            names = []
            for cart in new_cart:
                if cart in dictdf:
                    new_named = dictdf[str(cart)]
                    names.append(new_named)
            carts.append(names)

    return carts

def main():
    carts_csv = 'carts.csv'
    carts = cartsnames(carts_csv)



#main()
