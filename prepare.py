import pandas as pd

# --------------------------
# Correct mapping dictionaries
# --------------------------
gender = {
    1: 0,   # Male
    2: 1    # Female
}

breastfeeding = {
    1: 0,   # No
    2: 1,   # Yes
    3: 2    # Unknown
}

varicella = {
    1: 0,   # No
    2: 1,   # Yes
    3: 2    # Unknown
}

group_map = {
    1: 0,   # Healthy
    2: 1    # MS
}

mri_mapping = {
    0: "negative",
    1: "positive"
}

# --------------------------
# Load dataset
# --------------------------
df = pd.read_csv("MLOPS\data\Dataset.csv")

print("🔍 Raw unique values:")
for col in ["Gender", "Breastfeeding", "Varicella", "group"]:
    print(f"{col}: {df[col].unique()}")

# --------------------------
# Drop useless column
# --------------------------
data = df.drop("Unnamed: 0", axis=1)

# --------------------------
# Apply mappings safely
# --------------------------
mapping_pairs = {
    "Gender": gender,
    "Breastfeeding": breastfeeding,
    "Varicella": varicella,
    "group": group_map,
    "Periventricular_MRI": mri_mapping,
    "Cortical_MRI": mri_mapping,
    "Infratentorial_MRI": mri_mapping,
    "Spinal_Cord_MRI": mri_mapping
}

for col, mapping_dict in mapping_pairs.items():
    data[col] = data[col].map(mapping_dict)

# --------------------------
# Drop NA rows (should be 0 now)
# --------------------------
na_count = data.isna().sum().sum()
print(f"Found {na_count} missing mapped values.")

data = data.dropna()

# --------------------------
# Normalize numeric columns
# --------------------------
numeric_cols = data.select_dtypes(include=["int64", "float64"]).columns

for col in numeric_cols:
    col_min = data[col].min()
    col_max = data[col].max()
    if col_min != col_max:
        data[col] = (data[col] - col_min) / (col_max - col_min)

# --------------------------
# Save cleaned file
# --------------------------
data.to_csv("data/cleaned_data.csv", index=False)

print("✔ Cleaned dataset saved successfully!")
