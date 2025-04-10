import pandas as pd
import numpy as  np
import openpyxl 
path = "data.xlsx"
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

data = pd.read_csv(url, header=None)

res = data.to_excel(path, index=False)
df = pd.DataFrame(data)
print(data.describe())
print(data.tail(10))
df1 = df.replace("?", np.nan)
print(df1)