import os
import pandas as pd
path = r'C:\Users\giova\.cache\kagglehub\datasets\olistbr\brazilian-ecommerce\versions\2'


df_items = pd.read_csv(f'{path}/olist_order_items_dataset.csv')
df_orders = pd.read_csv(f'{path}/olist_orders_dataset.csv')
df_customers = pd.read_csv(f'{path}/olist_customers_dataset.csv')
df_products = pd.read_csv(f'{path}/olist_products_dataset.csv')
df_orders['order_purchase_timestamp'] = pd.to_datetime(df_orders['order_purchase_timestamp'])
df_orders_customers  = pd.merge(df_orders, df_customers, on='customer_id')
df_items_products = pd.merge(df_items, df_products, on='product_id')

print('\nMês com mais pedidos.\n')
print(df_orders['order_purchase_timestamp'].dt.month.value_counts().sort_index(ascending=True))

print('\nEstado com mais pedidos.\n')
print(df_orders_customers['customer_state'].value_counts())

print('\nCategoria mais vendida.\n')
print(df_items_products['product_category_name'].value_counts())
