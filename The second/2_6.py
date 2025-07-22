import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")
health_data.fillna(health_data.mean(numeric_only=True), inplace=True)
print(health_data);
