import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")
cleaned_data = health_data.dropna()
print(cleaned_data);