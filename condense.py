import subprocess
import sys
import os

# Check if pandas is installed, and install it if not
try:
    import pandas as pd
except ImportError:
    print("Pandas not found. Installing pandas...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
    import pandas as pd

def main():
    # Check if a file name is provided via command line arguments
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = 'Registration Badge Printing.xlsx'

    # Determine file type and load the spreadsheet
    file_ext = os.path.splitext(input_file)[1].lower()
    if file_ext == '.csv':
        df = pd.read_csv(input_file)
    elif file_ext in ['.xls', '.xlsx']:
        df = pd.read_excel(input_file)
    else:
        print("Unsupported file format. Please provide a CSV or Excel file.")
        return

    # Output Lunch Metrics
    print("Lunch Metrics:\n")
    print(df['Lunch'].value_counts())
    print()
    print(df['Lunch Purchase'].value_counts())
    print()
    total_lunches = df['Lunch'].value_counts().get('1 "Included" - Not Picked Up', 0) + df['Lunch Purchase'].value_counts().get('1 "Yes Please" - Not Picked Up', 0)
    print('Total Lunches:', total_lunches)

    # Condense Lunch numbers
    lunch = df['Lunch Purchase'].fillna(df['Lunch'])
    lunch.fillna('No Lunch', inplace=True)

    lunch.replace(['1 "Included" - Not Picked Up', '1 "Yes Please" - Not Picked Up'], "Yes", inplace=True)
    lunch.replace(['1 "No Thank you" - Not Picked Up', 'No Lunch'], "No", inplace=True)

    # Output Condensed Lunch Metrics
    print("Condensed Lunch Metrics:")
    print(lunch.value_counts())

    # Update table
    df.drop(columns=['Lunch Purchase', 'Lunch'], inplace=True)
    df['Lunch Included'] = lunch

    # Generate output file name
    base_name, ext = os.path.splitext(input_file)
    output_file = f"{base_name}_condensed.csv"    

    # Save to file
    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    main()