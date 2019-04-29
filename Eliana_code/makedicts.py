#makedicts.py
#This program creates a dictionary that maps the semcrn to the "short_title" of classes
#https://pythonhow.com/accessing-dataframe-columns-rows-and-cells/

import pandas as pd

def grabcols(file):
    df = pd.read_csv(file, engine='python')
    #semcrn = df["semcrn"]
    #print(semcrn)


def main():
    file = "courses.csv"
    grabcols(file)


main()
