import os
import pandas as pd
import numpy as np

user = os.getlogin()  # ou: os.getenv("USERNAME")

if user == 'mpa':
    path = f'C:/Users/mpa/OneDrive/Área de Trabalho'
else:
    path = f'C:/Users/{user}/Desktop'


arq = path + '/Refund.csv'
refund_db = pd.read_csv(arq, sep = ";")

arq = path + '/Invoice.csv'
invoice_db = pd.read_csv(arq, sep = ";")

arq = path + '/Product.csv'
product_db = pd.read_csv(arq, sep = ';')

refund_db = refund_db.drop_duplicates(subset="Credit Memo: Credit Memo Number")
invoice_db = invoice_db.dropna(subset=["Rate Plan Charge: WBE"])
invoice_db = invoice_db.drop_duplicates(subset="Invoice: Invoice Number")

invoice_db = invoice_db[invoice_db['Invoice: Status_Sii'] == "Autorizada"]

invoice_db_FP = invoice_db[invoice_db['Rate Plan Charge: Invoice Description'].isin(product_db['Produto']) |
                                    invoice_db['Account: XC_Segment'].isin(['B2B', 'B2G'])]

refund_db = refund_db.merge(invoice_db_FP[['Invoice: Invoice Number', 'Rate Plan Charge: Invoice Description']],
                                    on = 'Invoice: Invoice Number',
                                    how = 'left')


refund_db_FP = refund_db[refund_db['Rate Plan Charge: Invoice Description'].isin(product_db['Produto'])]

invoice_db_FP = invoice_db_FP.merge(refund_db_FP[['Invoice: Invoice Number', 'Credit Memo: Credit Memo Number', 'Credit Memo: Total Amount']],
                              on = 'Invoice: Invoice Number',
                              how = 'left')


invoice_db_FP['Credit Memo: Credit Memo Number'] = invoice_db_FP['Credit Memo: Credit Memo Number'].astype(str)
invoice_db_FP['Refund?'] = invoice_db_FP['Credit Memo: Credit Memo Number'].apply(lambda x: bool(x.strip()) and x != 'nan')

invoice_db_FP = invoice_db_FP[invoice_db_FP['Refund?'] == False]

invoice_db_FP.to_csv(path + "/Clean DB.csv", index = False)