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
    #print(type(crn_dict))
    #print(crn_dict)
    return crn_dict

# converts course lists to carts (lists of "semcrns", type=str)
def makecarts(file):
    df = pd.read_csv(file, dtype='str', error_bad_lines=False)
    cart_col = df["courses"]

    carts = []
    for c in cart_col:
        if type(c) != type(1.0) and c != " " and c != None:
            new_cart = c.split(" ")
            carts.append(new_cart)

    return carts
# converts course lists to carts (lists of "short_title"s, type=str)
def makecarts1(file1, file2):
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
    #courses_csv = 'courses.csv'
    #crn_dict = makedict(courses_csv)

    carts_csv = 'carts.csv'
    carts = makecarts(carts_csv)



#main()
