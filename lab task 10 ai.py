#Ai lab task 10:
import pandas as pd
import numpy as numpy
data = pd.read_csv('amazon.csv')
print('we have {} rows.'.format(data.shape[0])) 
print('we have {} columns.'.format(data.shape[1]))
print("null values per column:")
print(numpy.sum(pd.isnull(data))) 
if 'category' in data.columns:
  num = data['category'].mode()[0] 
  data['category'] = data['category'].fillna(num)    
if 'product_id' in data.columns: 
  data.drop('product_id' , axis=1, inplace=True) 
x = data.iloc[:, 0:-1] 
y = data.iloc[:, -1] 
print("Features (X) shape:",x.shape) 
print("Target (Y) shape:", y.shape) 
cat_columns = x.select_dtypes(['object']).columns 
x[cat_columns] = x[cat_columns].apply(lambda x: pd.factorize(x)[0]) 
print("\n--- Final Data Types ---")
print(x.dtypes)
