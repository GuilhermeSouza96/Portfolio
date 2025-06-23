# Invoice Data Reconciliation

This project performs reconciliation between Invoices and Credit Memos (Refunds), using filters such as product list and invoice status.

## ⚙️ How it works

- Filters invoices by `Status_Sii == "Autorizada"`
- Cross-checks with product list and refunds
- Flags invoices with associated refunds (Credit Memos)

## 📦 Requirements

- Python 3.x
- pandas
- numpy

## ▶️ Run

```bash
python "Invoice Data Reconciliation.py"
