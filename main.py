import pandas as pd
import csv


def read_data(f):
    with open(f, 'r', encoding='Windows-1252', newline='') as csv_file:

        lines = csv.DictReader(csv_file)

        lst = [[], []]

        for line in lines:
            if line['Price Basis#']:
                lst[0].append(line)
            if line['Cost Basis#']:
                lst[1].append(line)

        return lst


def main():
    cs = read_data('data/cs.csv')
    bs = read_data('data/bs.csv')
    rc = read_data('data/rc.csv')
    print(f'Price: {len(cs[0])}\tCost: {len(cs[1])}')
    print(f'Price: {len(bs[0])}\tCost: {len(bs[1])}')
    print(f'Price: {len(rc[0])}\tCost: {len(rc[1])}')


if __name__ == "__main__":
    main()
