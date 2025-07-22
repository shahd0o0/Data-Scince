import matplotlib.pyplot as plt

market_share = [130, 70, 78]
labels = ['Apple', 'Samsung', 'Huawei']

plt.pie(market_share, labels=labels, autopct='%1.1f%%')
plt.title("Mobile Phone Market Share")
plt.show();