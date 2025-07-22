import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")
import requests
from bs4 import BeautifulSoup
url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
print(soup.title.text);