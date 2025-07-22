import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data_normal = np.random.normal(loc=170, scale=10, size=1000)
sns.histplot(data_normal, kde=True, color='blue')
plt.title('Normal Distribution (Students Heights)')
plt.xlabel('Height (cm)')
plt.ylabel('Frequency')
plt.show()