import pandas as pd

# Load dataset from a local file
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv('/Users/mm/Desktop/PLP/iris.csv', names=columns)

# Display the first few rows
print(df.head())
print(df.shape)
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Check data types
print(df.dtypes)

# Check unique values
print(df['class'].unique())

# Check for missing values
print(df.isnull())          
print(df.isnull().sum())

# Clean the data
df_cleaned = df.dropna()
print(df_cleaned)



