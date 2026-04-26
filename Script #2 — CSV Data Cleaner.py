""" CSV/Excel Data Cleaner Script Author: Akshit Description: Cleans messy CSV or Excel files. - Removes completely blank rows - Strips extra spaces from text - Standardizes column names - Removes duplicate rows - Outputs a clean file """

import pandas as pd
import os

def clean_csv(input_file, output_file=None):
    """Cleans a CSV or Excel file and saves the result."""

    # Check if file exists
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        return

    # Read the file (works for both .csv and .xlsx)
    ext = os.path.splitext(input_file)[1].lower()
    if ext == '.xlsx' or ext == '.xls':
        df = pd.read_excel(input_file)
    else:
        df = pd.read_csv(input_file)

    print(f"\nOriginal: {len(df)} rows, {len(df.columns)} columns")
    print(f"Columns: {list(df.columns)}")
    print("-" * 40)

    # STEP 1: Clean column names
    # " First Name " → "first_name"
    df.columns = (df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('[^a-z0-9_]', '', regex=True)
    )
    print(f"✓ Column names standardized: {list(df.columns)}")

    # STEP 2: Remove completely blank rows
    before = len(df)
    df.dropna(how='all', inplace=True)
    print(f"✓ Blank rows removed: {before - len(df)}")

    # STEP 3: Strip extra spaces from text columns
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()
    print("✓ Extra spaces stripped from text")

    # STEP 4: Remove duplicate rows
    before = len(df)
    df.drop_duplicates(inplace=True)
    print(f"✓ Duplicate rows removed: {before - len(df)}")

    # STEP 5: Reset the row numbers (index)
    df.reset_index(drop=True, inplace=True)

    # Set output file name if not given
    if output_file is None:
        name, ext = os.path.splitext(input_file)
        output_file = f"{name}_cleaned{ext}"

    # Save the clean file
    if output_file.endswith('.xlsx'):
        df.to_excel(output_file, index=False)
    else:
        df.to_csv(output_file, index=False)

    print(f"\nClean file saved: {output_file}")
    print(f"Final: {len(df)} rows, {len(df.columns)} columns")

# ---- RUN THE SCRIPT ----
if __name__ == "__main__":
    print("=== CSV/Excel Data Cleaner v1.0 ===")
    input_path = input("Enter path to your CSV or Excel file: ")
    clean_csv(input_path.strip())