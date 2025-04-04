import os
import pandas as pd

def check_file():
    file_path = 'world_population.xlsx'
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"ERROR: File '{file_path}' not found in the current directory.")
        print(f"Current directory: {os.getcwd()}")
        print("Files in current directory:")
        for file in os.listdir('.'):
            print(f"  - {file}")
        return False
    
    # Try to read the file
    try:
        df = pd.read_excel(file_path)
        print(f"SUCCESS: File '{file_path}' found and loaded successfully.")
        print(f"File size: {os.path.getsize(file_path)} bytes")
        print(f"Number of rows: {len(df)}")
        print(f"Columns: {list(df.columns)}")
        print("\nFirst 5 rows of data:")
        print(df.head())
        return True
    except Exception as e:
        print(f"ERROR: Could not read the file: {e}")
        return False

if __name__ == "__main__":
    print("Checking world_population.xlsx file...")
    check_file() 