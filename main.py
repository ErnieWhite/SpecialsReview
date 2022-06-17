import csv

def get_basis_name(basis_number: str):
    match_ups = {
            '1': 'LIST',
            '2': 'INTERNAL',
            '3': 'UMSP',
            '4': 'CMP',
            '5': 'STD-COST',
            '6': 'REP-COST',
            '8': 'AVG-COST',
            '9': 'LASTCOST',
            '10': 'CMP',
            '21': 'Lnd Cost',
            '22': 'Avg Lnd',
            '25': 'Ord COGS',
            '28': 'Ord Comm',
            '29': 'Strgc List',
            '30': 'Strgc Cost',
            '31': 'AVG-COST',
            }
    return match_ups.get(basis_number, basis_number)



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
            specials_dict[key] = {
                    'Branch/Terr.': special['Branch/Terr.'] if special['Branch/Terr.'] != '' else 'ALL',
                    'Diff. Matrix Info.': special['Diff. Matrix Info.'],
                    'Home Branch': special['Home Branch'],
                    'Job': 'Y' if special['Bill To ID'] == special['Customer ID'] else 'N',
                    'Bill To ID': special['Bill To ID'],
                    'Customer ID': special['Customer ID'],
                    'Customer Name': special['Customer Name'],
                    'Rate Card': special['Price Class'],
                    'Outside Salesperson': special['Outside Salesperson'],
                    'Price Line': special['Price Line'],
                    'PROD_NBR': special['PROD_NBR'],
                    'Product Description': special['Product Description'],
                    'Effective Date': special['Effective Date'],
                    'Expire Date': special['Expire Date'],
                   }
            if special['Price Basis#']:
                if ('Price Data' not in specials_dict[key]) or (special['Matrix ID'] > specials_dict[key]['Price Data']['Matrix ID']):
                    specials_dict[key]['Price Data'] = { 
                            'Matrix ID': special['Matrix ID'],
                            'SellGroupAll': special['SellGroupAll'],
                            'SellGroupMscAll': special['SellGroupMscAll'],
                            'SellGroupMregAll': special['SellGroupMregAll'],
                            'Price Date Ovrd.': special['Price Date Ovrd.'],
                            'LIST': special['LIST'],
                            'UMSP': special['UMSP'],
                            'CMP': special['CMP'],
                            'STD-COST': special['STD-COST'],
                            'REP-COST': special['REP-COST'],
                            'AVG-COST': special['AVG-COST'],
                            'LASTCOST': special['LASTCOST'],
                            'Lnd Cost': special['Lnd Cost'],
                            'Avg Lnd': special['Avg Lnd'],
                            'Price Basis': get_basis_name(special['Price Basis#']),
                            'Price Formula': special['Price Formula'],
                            'Enable Rnding Rules': special['Enable Rnding Rules'],
                        }
            if special['Cost Basis#']:
                if ('Cost Data' not in specials_dict[key]) or (special['Matrix ID'] > specials_dict[key]['Cost Data']['Matrix ID']):
                    specials_dict[key]['Cost Data'] = {
                        'Matrix ID': special['Matrix ID'],
                        'Cost Basis': get_basis_name(special['Cost Basis#']),
                        'Cost Formula': special['Cost Formula'],
                        }
    return specials_dict
 

def main():
    cs = read_data('data/cs.csv')
    bs = read_data('data/bs.csv')
    rc = read_data('data/rc.csv')
    print(f'CS {len(cs)}')
    print(f'BS {len(bs)}')
    print(f'RC {len(rc)}')

    cs_dict = create_specials_dict(cs)
    bs_dict = create_specials_dict(bs)

    print(f'CS Price {len(cs_dict)}')
    print(f'BS Price {len(bs_dict)}')


if __name__ == "__main__":
    main()
