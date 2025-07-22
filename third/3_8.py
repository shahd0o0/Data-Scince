import pandas as pd

data = {'EmployeeName': ['حمد', 'سارة', 'البيلي', 'خالد', 'محمد'],
        'Salary': [2000, 2500, 3000, 10000, 2000]}

df = pd.DataFrame(data)

# حساب المقاييس الإحصائية
mean_salary = df['Salary'].mean()
median_salary = df['Salary'].median()
mode_salary = df['Salary'].mode()

print(f"Mean Salary: {mean_salary:.2f}")
print(f"Median Salary: {median_salary:.2f}")
print(f"Mode Salary: {mode_salary.values[0]}")