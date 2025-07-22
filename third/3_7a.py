import matplotlib.pyplot as plt
import numpy as np

# بيانات افتراضية
x = np.linspace(0, 10, 100)
y = np.sin(x)

# الرسم باستخدام Matplotlib
plt.figure(figsize=(8, 4))
plt.plot(x, y, color='blue', linestyle='-', linewidth=2)
plt.title('Sine Wave using Matplotlib')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()