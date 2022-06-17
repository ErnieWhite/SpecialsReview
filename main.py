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
        key = ':'.join([special['Branch/Terr.'], special['Customer ID'], special['PROD_NBR']])
        if key not in specials_dict:
            specials_dict[key] = special
        if key in specials_dict and special['Matrix ID'] > specials_dict[key]['Matrix ID']:
            specials_dict[key] = special
    return specials_dict


def create_rate_card_dict(rate_cards):
    rate_card_dict = dict()
    while len(rate_cards) > 0:
        entry = rate_cards.pop(0)
        key = ':'.join([entry['Branch/Terr.'], entry['Customer Class'], entry['PROD_NBR']])
        if key not in rate_card_dict:
            rate_card_dict[key] = entry
        if key in rate_card_dict and entry['Matrix ID'] > rate_card_dict[key]['Matrix ID']:
            rate_card_dict[key] = entry
    return rate_card_dict


def main():
    cs = read_data('data/cs.csv')
    bs = read_data('data/bs.csv')
    rc = read_data('data/rc.csv')
    print(f'CS: {len(cs)}')
    print(f'BS: {len(bs)}')
    print(f'RC: {len(rc)}')
    cs_dict = create_specials_dict(cs)
    bs_dict = create_specials_dict(bs)
    rc_dict = create_rate_card_dict(rc)
    print(f'CS: {len(cs_dict)}')
    print(f'BS: {len(bs_dict)}')
    print(f'RC: {len(rc_dict)}')


if __name__ == "__main__":
    main()
