import matplotlib.pyplot as plt
plt.figure(figsize=(12, 4))

# الرسم الخطي
plt.subplot(1, 3, 1)
x = ["1st Quarter", "2nd Quarter", "3rd Quarter", "4th Quarter"]
y = [130, 135, 140, 160]
plt.plot(x, y, marker='o', color='green', linestyle='--')
plt.title("Quarterly Sales")
plt.xlabel("Quarter")
plt.ylabel("Sales ($ Thousands)")
plt.grid()

# الرسم بالأعمدة
plt.subplot(1, 3, 2)
products = ['Laptop', 'Phone', 'Tablet']
sales = [120, 200, 80]
plt.bar(products, sales, color=['blue', 'green', 'red'])
plt.title("Product Sales")
plt.ylabel("Quantity Sold")

# الرسم الدائري
plt.subplot(1, 3, 3)
market_share = [130, 70, 78]
labels = ['Apple', 'Samsung', 'Huawei']
plt.pie(market_share, labels=labels, autopct='%1.1f%%')
plt.title("Mobile Phone Market Share")

plt.tight_layout()
plt.show()