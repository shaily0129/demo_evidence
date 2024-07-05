import csv
import glob
from datetime import datetime

# File paths
input_csv = "test_report*.csv"
output_csv = "test_report_with_timestamp.csv"

# Read the CSV file
with open(input_csv, mode="r") as infile:
    reader = csv.reader(infile)
    rows = list(reader)

# Get the current date and time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Add the date and time to the header
rows[0].extend(["date", "time"])
for row in rows[1:]:
    row.extend([current_time.split()[0], current_time.split()[1]])

# Write the updated rows to a new CSV file
with open(output_csv, mode="w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerows(rows)

print(f"CSV file updated with date and time: {output_csv}")
