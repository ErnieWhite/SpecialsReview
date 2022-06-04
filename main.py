import pandas as pd
import csv


def read_specials_file(f) -> list:
    with open(f, 'r', newline='') as csv_file:
        dct = list(csv.DictReader(csv_file))
        return dct

def create_specials_dictionary(f) -> dict:
    d = dict()
    for entry in f:
       if ':'.join([entry['Customer ID'], entry['PROD_NBR']]) in d.keys():
          if entry['Price Basis#'] != '':
              pass
          if entry['Cost Basis#'] != '':
              pass

def main():
    cs_all_entries = read_specials_file("./data/cs.csv")
    bs_all_entries = read_specials_file("./data/bs.csv")
    rc_all_entries = read_specials_file("./data/rc.csv")
    print(cs_all_entries[0].keys())
    print(bs_all_entries[0].keys())
    print(rc_all_entries[0].keys())


if __name__ == "__main__":
    main()
