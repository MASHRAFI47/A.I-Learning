# https://leetcode.com/problems/customers-who-never-order/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    arr = customers[~customers['id'].isin(orders['customerId'])]
    arr2 = arr[['name']].rename(columns={'name':'Customers'})
    return arr2