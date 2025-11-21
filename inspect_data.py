import pandas as pd

df = pd.read_csv("data/cleaned_data.csv")

print("\n🔹 First 5 rows:")
print(df.head())

print("\n🔹 Dataset info:")
print(df.info())

print("\n🔹 Summary statistics:")
print(df.describe())

print("\n🔹 Missing values per column:")
print(df.isna().sum())
