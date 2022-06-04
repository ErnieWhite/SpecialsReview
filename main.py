import pandas as pd
import csv


def main():
    data_types = {
        Matrix ID,
        Matrix Tag Comment,
        Matrix Type,
        Diff. Matrix Info.,
                           Branch/Terr.,Home Branch,Bill To ID,Customer ID,Customer Name,Price Class,Outside Salesperson,Price Line,SellGroupAll,SellGroupMscAll,SellGroupMregAll,PROD_NBR,Product Description,Price Date Ovrd.,LIST,UMSP,CMP,STD-COST,REP-COST,AVG-COST,LASTCOST,Lnd Cost,Avg Lnd,Price Basis#,Price Formula,Qty Break Basis,Qty Break Formula,Qty Brk. Form Constant,Qty Break Points,Qty Break UOM,Qty Brk. Form Multplier,Split Qty,Cost Basis#,Cost Formula,Effective Date,Expire Date,Enable Rnding Rules
}
    cs_df = pd.read_csv('data/cs.csv', header=0, encoding='Windows-1252')
    print(cs_df.head())

if __name__ == "__main__":
    main()
