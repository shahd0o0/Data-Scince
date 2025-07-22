import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
# بيانات افتراضية
x = np.linspace(0, 10, 100)
y = np.sin(x)

# الرسم باستخدام Seaborn
sns.set_style("whitegrid")
plt.figure(figsize=(8, 4))
sns.lineplot(x=x, y=y, color='red', linewidth=2)
plt.title('Sine Wave using Seaborn')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()