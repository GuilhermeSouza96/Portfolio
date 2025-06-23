# Invoice Data Reconciliation

This project performs reconciliation between Invoices and Credit Memos (Refunds), using filters such as product list and invoice status.

## 📁 Folder Structure

- `data/`: Input files (`Invoice.csv`, `Refund.csv`, `Products.csv`)
- `output/`: Processed results (`Clean DB.csv`)
- `Invoice Data Reconciliation.py`: Main script

## ⚙️ How it works

- Filters invoices by `Status_Sii == "Autorizada"`
- Cross-checks with product list and refunds
- Flags invoices with associated refunds (Credit Memos)

## 📦 Requirements

- Python 3.x
- pandas
- numpy

1. Install the required libraries:

```bash
pip install pandas numpy
```

## ▶️ Run

```bash
python "Invoice Data Reconciliation.py"
