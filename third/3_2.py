import matplotlib.pyplot as plt
products = ['Laptop', 'Phone', 'Tablet']
sales = [120, 200, 80]
plt.bar(products, sales, color=['blue', 'green', 'red'])
plt.title("Product Sales")
plt.ylabel("Quantity Sold")
plt.show()
