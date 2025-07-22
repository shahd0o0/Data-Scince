import matplotlib.pyplot as plt
from numpy import mean

x = ["1st Quarter", "2nd Quarter", "3rd Quarter", "4th Quarter"]
y = [130, 135, 140, 160]

plt.plot(x, y, marker='o', color='blue')
mean_y = mean(y)
max_y = max(y)

plt.axhline(mean_y, color='r', linestyle=':')
plt.annotate('Peak Sales', xy=(3, 160), xytext=(2, 150),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.title("Quarterly Sales")
plt.xlabel("Quarter")
plt.ylabel("Sales ($ Thousands)")
plt.grid()
plt.show();