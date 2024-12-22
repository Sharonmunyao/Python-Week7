import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset from a local file
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv('/Users/mm/Desktop/PLP/iris.csv', names=columns)


# 1. Line Chart (example trend over time, simulating a trend in class mean sepal length)
# Since the dataset doesn't have a time column, we simulate a time-like sequence
df['index'] = df.index  # Using the index as a placeholder for time
plt.figure(figsize=(10, 6))
sns.lineplot(x='index', y='sepal_length', data=df, hue='class', marker='o')
plt.title('Trends in Sepal Length Over Time (Simulated)')
plt.xlabel('Index (Simulating Time)')
plt.ylabel('Sepal Length')
plt.legend(title='Species')
plt.grid(True)
plt.show()

# 2. Bar Chart (Comparison of average petal length per class)
plt.figure(figsize=(8, 6))
sns.barplot(x='class', y='petal_length', data=df, estimator='mean')
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

# 3. Histogram (Distribution of sepal length)
plt.figure(figsize=(8, 6))
sns.histplot(df['sepal_length'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter Plot (Sepal Length vs Petal Length)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal_length', y='petal_length', data=df, hue='class', palette='Set1')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()
