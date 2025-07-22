import matplotlib.pyplot as plt
from numpy import mean

x = ["1st Quarter", "2nd Quarter", "3rd Quarter", "4th Quarter"]
y = [130, 135, 140, 160]

plt.plot(x, y, marker='o', color='blue')
mean_y = mean(y)
plt.axhline(mean_y, color='r', linestyle=':')
plt.title("Quarterly Sales")
plt.xlabel("Quarter")
plt.ylabel("Sales ($ Thousands)")
plt.grid()
plt.savefig('quarterly_sales.png', dpi=300, bbox_inches='tight')