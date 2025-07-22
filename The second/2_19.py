import pandas as pd
import matplotlib.pyplot as plt
health_data = pd.read_csv("data.csv", header=0, sep=",")
health_data.plot(x="Duration", y="Calories_Burnage", kind="line")
plt.title("Calories Burned vs Duration")
plt.xlabel("Duration")
plt.ylabel("Calories Burned")
plt.show();