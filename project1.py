import pandas as pd

file_path = "C:/Users/vedso/Desktop/data analyst/internship/decodelabs/Dataset for Data Analytics.xlsx"
df = pd.read_excel(file_path)

print("=" * 50)
print("DATASET INFORMATION")
print("=" * 50)

print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nMissing Values:")
print(df.isnull().sum())

if 'CouponCode' in df.columns:
    df['CouponCode'] = df['CouponCode'].fillna('NO_COUPON')

duplicate_rows = df.duplicated().sum()
print("\nDuplicate Rows Found:", duplicate_rows)

df = df.drop_duplicates()
if 'OrderID' in df.columns:

    duplicate_ids = df['OrderID'].duplicated().sum()
    print("\nDuplicate Order IDs:", duplicate_ids)

    if duplicate_ids > 0:
        df = df.drop_duplicates(subset='OrderID')

if 'Date' in df.columns:
    try:
        df['Date'] = pd.to_datetime(df['Date'])
        print("\nDate format corrected successfully.")
    except Exception as e:
        print("Date Conversion Error:", e)

print("\nVerification Report")
print("Missing Values:")
print(df.isnull().sum())
print("\nDuplicate Rows:",
      df.duplicated().sum())
if 'OrderID' in df.columns:
    print("Duplicate Order IDs:",
          df['OrderID'].duplicated().sum())

output_file = "Cleaned_Dataset.xlsx"
df.to_excel(output_file,
            index=False)
print("\nCleaned dataset saved as:",
      output_file)
print("\nPROJECT COMPLETED SUCCESSFULLY")
