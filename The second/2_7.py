import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")
unique_data = health_data.drop_duplicates()
print(unique_data);