import pandas as pd

# Load dataset from a local file
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv('/Users/mm/Desktop/PLP/iris.csv', names=columns)

# Get summary statistics
print(df.describe())

# Group by the 'class' column and compute the mean of numerical columns
grouped_means = df.groupby('class').mean()

print(grouped_means)

# Patterns or interesting findings from your analysis

# Iris-setosa tends to have the smallest sepal length and the largest sepal width.
# Iris-versicolor has an intermediate sepal length and width.
# Iris-virginica has a relatively long sepal length but a smaller sepal width.