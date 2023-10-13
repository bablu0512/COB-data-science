import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from scipy import stats
df = pd.read_csv("dataset - netflix1.csv") # Load the dataset
numeric_columns = df.select_dtypes(include=['number'])
categorical_columns = df.select_dtypes(exclude=['number'])
numeric_imputer = SimpleImputer(strategy="mean")
df[numeric_columns.columns] = numeric_imputer.fit_transform(df[numeric_columns.columns])
categorical_imputer = SimpleImputer(strategy="most_frequent")
df[categorical_columns.columns] = categorical_imputer.fit_transform(df[categorical_columns.columns])
df.to_csv("cleaned_dataset.csv", index=False)
print("Cleaning and preprocessing completed.")
 
