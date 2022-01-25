import pandas as pd


def trimKey(key):
    for element in range(0, len(key)):
        if key[element] >= '1' and key[element] <= '9':
            return key[element:]


df = pd.read_csv('./fact_table.csv')

df["payment_key"] = df["payment_key"].apply(trimKey)
df["coustomer_key"] = df["coustomer_key"].apply(trimKey)
df["time_key"] = df["time_key"].apply(trimKey)
df["item_key"] = df["item_key"].apply(trimKey)
df["store_key"] = df["store_key"].apply(trimKey)

df.to_csv('fact_table.csv', index=False)
