import pandas as pd # pyright: ignore[reportMissingModuleSource]

df = pd.read_csv("creditcard.csv")

print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

duplicate_count = df.duplicated().sum()
print("\nDuplicate Rows:", duplicate_count)

df = df.drop_duplicates()

print("\nShape After Removing Duplicates:", df.shape)

df.to_csv("clean_creditcard.csv", index=False)

print("\nDataset cleaned and saved as clean_creditcard.csv")