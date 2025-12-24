import pandas as pd
import os
from datetime import datetime

# Path to the folder containing Excel files
xlsx_folder = 'xlsxs'

# Get list of all Excel files in the folder
excel_files = [f for f in os.listdir(xlsx_folder) if f.endswith('.xlsx')]

# Create an empty list to store all dataframes
all_data = []

# Process each Excel file
for file in excel_files:
    # Read the Excel file
    df = pd.read_excel(os.path.join(xlsx_folder, file))
    
    # Add filename as a new column
    df['Archivo_Origen'] = file
    
    # Append to our list
    all_data.append(df)

# Concatenate all dataframes
consolidated_df = pd.concat(all_data, ignore_index=True)

# Create output filename with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_filename = f'consolidated_stock_{timestamp}.xlsx'

# Save to Excel
consolidated_df.to_excel(output_filename, index=False)

print(f"Consolidated file has been created: {output_filename}")
print(f"Total number of rows: {len(consolidated_df)}")