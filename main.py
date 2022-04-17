import csv
import tkinter as tk
from tkinter import ttk


def get_csv_special_data(f: str):
    """Load the data in f into a dictionary"""

    d = dict()
    with open(f) as csv_file:
        rows = csv.DictReader(csv_file)
        for row in rows:
            key = ':'.join([row['Branch/Terr.'], row['Customer ID'], row['PROD_NBR']])
            d[key] = d.get(key, []) + [row]
    return d


def get_csv_rate_card_data(f: str):
    """Load the data in f into a dictionary"""

    d = dict()
    with open(f) as csv_file:
        rows = csv.DictReader(csv_file)
        for row in rows:
            key = ':'.join([row['Branch/Terr.'], row['Customer Class'], row['PROD_NBR']])
            d[key] = d.get(key, []) + [row]
    return d


bs = get_csv_special_data('bs.csv')
cs = get_csv_special_data('cs.csv')
rc = get_csv_rate_card_data('rc.csv')
print(f'BS Price: {len(bs)}')
print(f'CS Price: {len(cs)}')
print(f'RC Price: {len(rc)}')

for key in bs:
    if len(bs[key]) > 1:
        for entry in bs[key]:
            print(key, entry)
