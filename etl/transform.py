from extract import get_amazon_data

df = get_amazon_data()

# Remove Duplicates
df = df.drop_duplicates()
df_backup = df

# Standarize column name
df.columns = df.columns.str.replace(' ','_')
df.columns = df.columns.str.replace('-','_')

df.columns = df.columns.str.lower()
df.columns = df.columns.str.rstrip('_')
df.columns = df.columns.str.replace(' ','_')

df['amount'] = df['amount'].apply(lambda x: abs(x))

