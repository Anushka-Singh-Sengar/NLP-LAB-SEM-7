import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# Load the employee performance dataset
data_path = Path(r"D:\sem7\NLP LAB\Employe_Performance_dataset.csv")
df = pd.read_csv(data_path)

print("Dataset loaded successfully")
print("Shape:", df.shape)
print("Columns:", list(df.columns))
print(df.head())

# Calculate average salary department-wise
print("\n" + "="*50)
print("Average Salary by Department")
print("="*50)
avg_salary_by_dept = df.groupby('Department')['Salary'].mean()
print(avg_salary_by_dept)

# Create a bar graph
plt.figure(figsize=(10, 6))
avg_salary_by_dept.plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.title('Average Salary by Department', fontsize=14, fontweight='bold')
plt.xlabel('Department', fontsize=12)
plt.ylabel('Average Salary', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
