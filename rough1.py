import pandas as pd

# Read from the Excel worksheet
xlsx_file = '/Users/femisokoya/Documents/GitHub/Rough-sleeping/result.xlsx'
df = pd.read_excel(xlsx_file)

# Convert numeric columns to integers
numeric_columns = ['Local authority ONS code', 'Local authority', 'Region', 'Region ONS code', 'Female 2017', 'Male 2017', 'Not known 2017', 'Total 2017', 'Female 2018', 'Male 2018', 'Not known 2018', 'Total 2018', 'Female 2019', 'Male 2019', 'Not known 2019', 'Total 2019', 'Female 2020', 'Male 2020', 'Not known 2020', 'Total 2020', 'Female 2021', 'Male 2021', 'Not known 2021', 'Total 2021', 'Female 2022', 'Male 2022', 'Not known 2022', 'Total 2022']

for column in numeric_columns:
    if column in df.columns:
        df[column] = pd.to_numeric(df[column], errors='coerce').fillna(0).astype(int)

# Initialize a new DataFrame to store the extracted values
extracted_df = pd.DataFrame(columns=['Local authority ONS code', 'Local authority', 'Region', 'Region ONS code', 'Year', 'Female', 'Male', 'Not known', 'Total'])

# Define the sets of columns to extract
column_sets = [[0, 1, 2, 3, 4, 5, 6, 7, 7],  # Set 0
               [0, 1, 2, 3, 8, 9, 10, 11, 11],  # Set 1
               [0, 1, 2, 3, 12, 13, 14, 15, 15],  # Set 2
               [0, 1, 2, 3, 16, 17, 18, 19, 19],  # Set 3
               [0, 1, 2, 3, 20, 21, 22, 23, 23],  # Set 4
               [0, 1, 2, 3, 24, 25, 26, 27, 27]  # Set 5
               ]

# Define the corresponding year values for each set
year_values = [2017, 2018, 2019, 2020, 2021, 2022]

# Loop through the column sets and extract the values
for i, columns in enumerate(column_sets):
    extracted_values = df.iloc[:, columns].copy()
    extracted_values.columns = ['Local authority ONS code', 'Local authority', 'Region', 'Region ONS code', 'Year', 'Female', 'Male', 'Not known', 'Total']  # Update the column headers
    extracted_values['Year'] = year_values[i]  # Update the 'Year' column with the corresponding year value
    
    # Test and assign default values if 'Local authority ONS code', 'Local authority', or 'Region ONS code' are missing
    extracted_values['Local authority ONS code'] = extracted_values['Local authority ONS code'].fillna('E00000000')
    extracted_values['Local authority'] = extracted_values['Local authority'].fillna('No relevant LA')
    extracted_values['Region ONS code'] = extracted_values['Region ONS code'].fillna('E11111111')
    
    # Print each extracted value before storing
    for index, row in extracted_values.iterrows():
        print("Extracted Values:")
        print(f"Local authority ONS code: {row['Local authority ONS code']}")
        print(f"Local authority: {row['Local authority']}")
        print(f"Region: {row['Region']}")
        print(f"Region ONS code: {row['Region ONS code']}")
        print(f"Year: {row['Year']}")
        print(f"Female: {row['Female']}")
        print(f"Male: {row['Male']}")
        print(f"Not known: {row['Not known']}")
        print(f"Total: {row['Total']}")
        print("\n")
    
    extracted_df = pd.concat([extracted_df, extracted_values], ignore_index=True)

# Save the results to a new CSV file
output_path = 'result1.csv'
extracted_df.to_csv(output_path, index=False)

print(f"Results saved to {output_path}")
