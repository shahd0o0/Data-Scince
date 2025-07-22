import matplotlib.pyplot as plt
x = ["1st Quarter", "2nd Quarter", "3rd Quarter", "4th Quarter"]
y = [130, 135, 140, 160]
plt.plot(x, y, marker='o', color='green', linestyle='--')
plt.title("Quarterly Sales")
plt.xlabel("Quarter")
plt.ylabel("Sales ($ Thousands)")
plt.grid()
plt.show()
