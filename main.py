import csv
import pprint


def get_basis_name(basis_number):
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


def read_data(f: str) -> list[dict]:
    with open(f, 'r', encoding='Windows-1252', newline='') as csv_file:
        lst = list(csv.DictReader(csv_file))

        return lst


"""
{
    branch number:
        {
            key: {
                'Branch/Terr.': string,
                'Diff. Matrix Info.': string,
                'Home Branch': string,
                'Job': string,
                'Bill To ID': string,
                'Customer ID': string,
                'Customer Name': string,
                'Rate Card': string,
                'Outside Salesperson': string,
                'Price Line': string,
                'PROD_NBR': string,
                'Product Description': string,
                'Effective Date': string,
                'Expire Date': string,
                'Price Data': {
                    'Matrix ID': string,
                    'SellGroupAll': string,
                    'SellGroupMscAll': string,
                    'SellGroupMregAll': string,
                    'Price Date Ovrd.': string,
                    'LIST': float,
                    'UMSP': float,
                    'CMP': float,
                    'STD-COST': float,
                    'REP-COST': float,
                    'AVG-COST': float,
                    'LASTCOST': float,
                    'Lnd Cost': float,
                    'Avg Lnd': float,
                    'Price Basis': string,
                    'Price Formula': string,
                    'Enable Rnding Rules': string,
                    },               
                'Cost Data': {
                    'Matrix ID': string,
                    'Cost Basis': string,
                    'Cost Formula': string,
                    },
            }
        }
}
                    
"""


def create_specials_dict(specials: list[dict]):
    specials_dict = dict()
    while len(specials) > 0:
        special = specials.pop(0)
        branch = special['Home Branch'] if special['Home Branch'] != '1000' else special['Branch/Terr.']
        if branch not in specials_dict:
            specials_dict[branch] = {}
        if not special['PROD_NBR'].isdecimal():
            special['PROD_NBR'] = special['PROD_NBR'][1:]
        key = ':'.join([special['Branch/Terr.'], special['Customer ID'], special['PROD_NBR']])
        if key not in specials_dict[branch]:
            specials_dict[branch][key] = {
                'Branch/Terr.': special['Branch/Terr.'] if special['Branch/Terr.'] != '' else 'ALL',
                'Diff. Matrix Info.': special['Diff. Matrix Info.'],
                'Home Branch': special['Home Branch'],
                'Job': 'Y' if special['Bill To ID'] == special['Customer ID'] else 'N',
                'Bill To ID': special['Bill To ID'] if special['Bill To ID'] != '' else special['Customer ID'],
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
                if ('Price Data' not in specials_dict[branch][key]) or (
                        special['Matrix ID'] > specials_dict[branch][key]['Price Data']['Matrix ID']):
                    specials_dict[branch][key]['Price Data'] = {
                        'Matrix ID': special['Matrix ID'],
                        'SellGroupAll': special['SellGroupAll'],
                        'SellGroupMscAll': special['SellGroupMscAll'],
                        'SellGroupMregAll': special['SellGroupMregAll'],
                        'Price Date Ovrd.': special['Price Date Ovrd.'],
                        'LIST': float(special['LIST']),
                        'UMSP': float(special['UMSP']),
                        'CMP': float(special['CMP']),
                        'STD-COST': float(special['STD-COST']),
                        'REP-COST': float(special['REP-COST']),
                        'AVG-COST': float(special['AVG-COST']),
                        'LASTCOST': float(special['LASTCOST']),
                        'Lnd Cost': float(special['Lnd Cost']),
                        'Avg Lnd': float(special['Avg Lnd']),
                        'Price Basis': get_basis_name(special['Price Basis#']),
                        'Price Formula': special['Price Formula'],
                        'Enable Rnding Rules': special['Enable Rnding Rules'],
                    }

            if special['Cost Basis#']:
                if ('Cost Data' not in specials_dict[branch][key]) or (
                        special['Matrix ID'] > specials_dict[branch][key]['Cost Data']['Matrix ID']):
                    specials_dict[branch][key]['Cost Data'] = {
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
    with open('cs_output.txt', 'wt') as out:
        pprint.pprint(cs_dict, stream=out)
    with open('bs_output.txt', 'wt') as out:
        pprint.pprint(bs_dict, stream=out)


if __name__ == "__main__":
    main()
