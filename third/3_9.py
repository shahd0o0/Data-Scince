import pandas as pd

data = {'Salary': [2000, 2500, 3000, 3500, 4000]}

df = pd.DataFrame(data)

# حساب التباين والانحراف المعياري
variance = df['Salary'].var()
std_dev = df['Salary'].std()

print(f"Variance: {variance:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")