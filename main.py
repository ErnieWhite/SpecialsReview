import pandas as pd
import csv

def split_price_cost(specials):
   """Splits specials into to list"""
    lst = [[], []]
    while len(specials) > 0:
        special = specials.pop(0)
        if special['Price Basis#']:
            lst[0].append(special)
        if special['Cost Basis#']:
            lst[0].append(special)


def read_data(f):
    with open(f, 'r', encoding='Windows-1252', newline='') as csv_file:

        lst = list(csv.DictReader(csv_file))

        return lst


def create_specials_dict(specials):
    specials_dict = dict()
    while len(specials) > 0:
        special = specials.pop(0)
        key = ':'.join([special['Branch/Terr.'], special['Customer ID'], ['PROD_NBR']])
        if key in specials_dict:



def main():
    cs = read_data('data/cs.csv')
    bs = read_data('data/bs.csv')
    rc = read_data('data/rc.csv')
    print(f'Price: {len(cs[0])}\tCost: {len(cs[1])}')
    print(f'Price: {len(bs[0])}\tCost: {len(bs[1])}')
    print(f'Price: {len(rc[0])}\tCost: {len(rc[1])}')


if __name__ == "__main__":
    main()
