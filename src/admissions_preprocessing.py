"""
admissions_preprocessing.py
Milestone 1 - Data Preprocessing Phase
Assigned dataset: admissions.csv
Author: Nafisa

Follows the team checklist:
1. Check for duplicates
2. Handle missing values
3. Verify data types
4. Standardize date formats
5. Remove extra spaces
6. Check for invalid values
(Column names and IDs kept unchanged, as agreed by the team)
"""

import pandas as pd

# ---------------------------------------------------------
# 1. Load the dataset
# ---------------------------------------------------------
admissions = pd.read_csv("data/raw/admissions.csv")

print("Initial shape:", admissions.shape)
print(admissions.head())
admissions.info()

# ---------------------------------------------------------
# 2. Check for duplicates
# ---------------------------------------------------------
print("\nFull duplicate rows:", admissions.duplicated().sum())
print("Duplicate Admission_IDs:", admissions["Admission_ID"].duplicated().sum())

# ---------------------------------------------------------
# 3. Handle missing values
# ---------------------------------------------------------
print("\nMissing values per column:")
print(admissions.isnull().sum())

admissions = admissions.dropna(subset=["Admission_ID", "Patient_ID", "Doctor_ID"])

# ---------------------------------------------------------
# 4. Verify / fix data types
# ---------------------------------------------------------
admissions["Admission_Date"] = pd.to_datetime(admissions["Admission_Date"])
admissions["Discharge_Date"] = pd.to_datetime(admissions["Discharge_Date"])

print("\nData types after conversion:")
print(admissions.dtypes)

# ---------------------------------------------------------
# 5. Standardize text columns / remove extra spaces
# ---------------------------------------------------------
text_columns = ["Admission_ID", "Patient_ID", "Doctor_ID", "Department_ID", "Status"]
for col in text_columns:
    admissions[col] = admissions[col].str.strip()

admissions["Status"] = admissions["Status"].str.title()

# ---------------------------------------------------------
# 6. Check for invalid values
# ---------------------------------------------------------
print("\nUnique Status values:", admissions["Status"].unique())

invalid_dates = admissions[admissions["Discharge_Date"] < admissions["Admission_Date"]]
print("Rows with Discharge_Date before Admission_Date:", len(invalid_dates))

# ---------------------------------------------------------
# 7. Derived field: Length of Stay
# ---------------------------------------------------------
admissions["Length_of_Stay_Days"] = (
    admissions["Discharge_Date"] - admissions["Admission_Date"]
).dt.days

print("\nLength of Stay summary:")
print(admissions["Length_of_Stay_Days"].describe())

# ---------------------------------------------------------
# 8. Save the cleaned dataset
# ---------------------------------------------------------
admissions.to_csv("data/processed/admissions_clean.csv", index=False)
print("\nSaved cleaned file to data/processed/admissions_clean.csv")
print("Final shape:", admissions.shape)