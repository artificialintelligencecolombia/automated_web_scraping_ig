import pandas as pd

def append_csv_to_excel(excel_file, csv_file, output_excel_file):
    # Load the Excel file into a DataFrame
    excel_df = pd.read_excel(excel_file)

    # Load the CSV file into a DataFrame
    csv_df = pd.read_csv(csv_file)

    # Merge both DataFrames on the 'username' column
    merged_df = pd.merge(excel_df, csv_df[['username', 'Category', 'Country']], on='username', how='left')

    # Write the result to a new Excel file
    merged_df.to_excel(output_excel_file, index=False)


excel_file = "./api_dataset4.xlsx"  # Replace with the path to your .xlsx file
csv_file = "./cleaned_instagram_list4.csv"       # Replace with the path to your .csv file
output_excel_file = "prefinal4.xlsx"  # The new Excel file with appended data

append_csv_to_excel(excel_file, csv_file, output_excel_file)
