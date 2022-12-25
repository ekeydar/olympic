import csv
import os
import pathlib

import pandas as pd

PATH = pathlib.Path('data/athlete_events.csv')

SPORT = 'Athletics'

EVENT= "Athletics Men's 10,000 metres"

def get_10000():
    df = pd.read_csv(PATH)
    df1 = df[df['Sport'] == SPORT]
    df2 = df[df['Event'] == EVENT]
    return df2

def main():
    df = get_10000()
    os.makedirs('out', exist_ok=True)
    df.to_excel("out/olympic_10000.xlsx")
    

if __name__ == '__main__':
    main()
