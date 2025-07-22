import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")
import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts")
if response.status_code == 200:
    json_data = response.json()
    print(json_data[0]);