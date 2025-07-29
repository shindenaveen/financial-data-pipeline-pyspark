import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cleaned_data.csv')
print(df.describe())
df['debt_to_income'].hist()
plt.title('Debt to Income Ratio Distribution')
plt.show()
