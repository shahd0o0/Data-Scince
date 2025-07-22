import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")
pd.set_option('display.max_rows', None)
print(health_data);