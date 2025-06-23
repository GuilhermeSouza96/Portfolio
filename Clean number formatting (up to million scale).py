import pandas as pd

# Clean the number formating up to Million
def limpa_valor(df, coluna):
        df[coluna] = (
            df[coluna]
            .astype(str)
            .str.replace(r'(?<=\d)\.(?=\d{3}(?:\.\d{3})*,)', '', regex=True)
            .str.replace(',', '.', regex=False)
        )
        df[coluna] = pd.to_numeric(df[coluna], errors='coerce')
        return df
