import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from scipy import stats

# Load the dataset
df = pd.read_csv("dataset - netflix1.csv")

# Separate numeric and non-numeric columns
numeric_columns = df.select_dtypes(include=['number'])
categorical_columns = df.select_dtypes(exclude=['number'])

# Handling Missing Values for numeric columns
numeric_imputer = SimpleImputer(strategy="mean")
df[numeric_columns.columns] = numeric_imputer.fit_transform(df[numeric_columns.columns])

# Handling Missing Values for categorical columns
categorical_imputer = SimpleImputer(strategy="most_frequent")
df[categorical_columns.columns] = categorical_imputer.fit_transform(df[categorical_columns.columns])

# Outlier Detection and Removal (assuming this is where the division issue occurs)
# You can skip outliers removal temporarily or apply it specifically to numeric columns.
# filtered_entries = (abs_z_scores < 3).all(axis=1)
# df = df[filtered_entries]

# Data Type Conversion, Data Transformation, Scaling, and Normalization
# Perform necessary data type conversions, transformations, scaling, and normalization here.
# Make sure that these operations are only applied to numeric columns.

# Save the cleaned dataset to a new CSV file
df.to_csv("cleaned_dataset.csv", index=False)
print("Cleaning and preprocessing completed.")
 