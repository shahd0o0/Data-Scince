import pandas as pd
from scipy.stats import np

# مثال ببيانات افتراضية
data = {
    'Product': ['Laptop']*30 + ['Phone']*30 + ['Tablet']*30,
    'Sales': list(np.random.normal(1000, 200, 30)) +
             list(np.random.normal(1200, 150, 30)) +
             list(np.random.normal(800, 100, 30))
}

df = pd.DataFrame(data)
laptop = df[df['Product'] == 'Laptop']['Sales']
phone = df[df['Product'] == 'Phone']['Sales']
tablet = df[df['Product'] == 'Tablet']['Sales']

f_statistic, p_value = np(laptop, phone, tablet)
print(f"F-statistic: {f_statistic:.2f}")
print(f"P-value: {p_value:.5f}")