import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
csv_file = 'sample.csv'

# Read the CSV file
try:
    data = pd.read_csv(csv_file)

    # Display the content of the CSV file
    print("CSV Content:")
    print(data)
except FileNotFoundError:
    print(f"Error: The file '{csv_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print("My name is Anubhav Pandey")