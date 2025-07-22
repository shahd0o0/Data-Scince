import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")
sales_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Revenue': [1000, 1500, 1700, 1200]
})
print(sales_data["Revenue"].sum());