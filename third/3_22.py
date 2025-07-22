import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = x**2 + np.random.normal(0, 5, 100)

df_nonlinear = pd.DataFrame({'x': x, 'y': y})
corr_nonlinear = df_nonlinear['x'].corr(df_nonlinear['y'])
print(f"Correlation coefficient for nonlinear relationship: {corr_nonlinear:.2f}")

sns.scatterplot(x='x', y='y', data=df_nonlinear)
plt.title('Nonlinear Relationship (Correlation ≈ 0)')
plt.show()