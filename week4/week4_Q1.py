import pandas as pd

idx = ["HDD", "SSD", "USB", "CLOUD"]
data = [19, 11, 5, 97]

series = pd.Series(data, index=idx)
series = series.iloc[lambda x: ((x.values > 10) & (x.values < 20))]

print(series)