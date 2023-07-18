import pandas as pd

# Read the data from the Excel file
xlsx_file = '/Users/femisokoya/Documents/GitHub/Rough-sleeping/result.xlsx'
df = pd.read_excel(xlsx_file)

# Melt the dataframe
melted_df = df.melt(
    id_vars=['Local authority ONS code', 'Local authority', 'Region', 'Region ONS code'],
    value_vars=['Female 2017', 'Male 2017', 'Not known 2017', 'Total 2017',
                'Female 2018', 'Male 2018', 'Not known 2018', 'Total 2018',
                'Female 2019', 'Male 2019', 'Not known 2019', 'Total 2019',
                'Female 2020', 'Male 2020', 'Not known 2020', 'Total 2020',
                'Female 2021', 'Male 2021', 'Not known 2021', 'Total 2021',
                'Female 2022', 'Male 2022', 'Not known 2022', 'Total 2022'],
    var_name='Period',
    value_name='Numerical'
)

# Remove rows with blank cells
melted_df = melted_df.dropna(subset=['Local authority ONS code', 'Local authority', 'Region', 'Region ONS code', 'Numerical'])

# Convert the 'Numerical' column to integers
melted_df['Numerical'] = melted_df['Numerical'].astype(int)

# Save the cleaned dataframe to a new CSV file
output_path = 'result1.csv'
melted_df.to_csv(output_path, index=False)

print(f"Results saved to {output_path}")
