import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    'Name': ['Arya', 'Rahul', 'Sneha', 'Arjun', 'Priya', 'Ravi', 'Neha', 'Karan', 'Divya', 'Amit'],
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'Age': [22, 25, 23, 27, 24, 30, 21, 29, 26, 28]
}
df = pd.DataFrame(data)
sns.set(style='whitegrid')

# Bar chart - Gender distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Gender', palette='pastel')
plt.title('Gender Distribution in Sample Population')
plt.xlabel('Gender')
plt.ylabel('Number of People')
plt.show()

# Histogram - Age distribution
plt.figure(figsize=(6, 4))
sns.histplot(data=df, x='Age', bins=5, kde=True, color='skyblue')
plt.title('Age Distribution in Sample Population')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
