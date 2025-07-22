import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")
avg_by_duration = health_data.groupby("Duration")["Calories_Burnage"].mean()
print(avg_by_duration);
