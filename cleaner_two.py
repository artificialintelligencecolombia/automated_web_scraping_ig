import csv

def clean_csv_and_save_usernames(input_file, output_csv, output_txt):
    """
    Cleans a CSV file by removing duplicate rows based on the 'username' column and creates two output files:
    1. A CSV file with unique usernames and corresponding data (three columns).
    2. A TXT file with only unique usernames.

    Args:
        input_file (str): Path to the input CSV file.
        output_csv (str): Path to the output CSV file (with three columns).
        output_txt (str): Path to the output TXT file (with usernames only).
    """

    unique_usernames = set()
    cleaned_rows = []

    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Save the header
        cleaned_rows.append(header)  # Keep the header in the output CSV

        for row in reader:
            username = row[0].strip()  # Assuming 'username' is the first column
            if '...' not in username and username not in unique_usernames:
                unique_usernames.add(username)
                cleaned_rows.append(row)

    # Write the unique usernames to the TXT file
    with open(output_txt, 'w', encoding='utf-8') as txtfile:
        for username in unique_usernames:
            txtfile.write(f"{username}\n")

    # Write the unique rows (with all three columns) to the CSV file
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(cleaned_rows)

# Example usage
input_file = "./instagram_usernames2.csv"
output_csv = "cleaned_instagram_list4.csv"  # CSV with all three columns
output_txt = "api_usernames_list4.txt"  # TXT with only usernames
clean_csv_and_save_usernames(input_file, output_csv, output_txt)
