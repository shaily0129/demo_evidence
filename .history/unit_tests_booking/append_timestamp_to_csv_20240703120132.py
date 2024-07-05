# import csv
# from datetime import datetime

# # File paths
# input_csv = "test_report.csv"
# output_csv = "test_report_with_timestamp.csv"

# # Read the CSV file
# with open(input_csv, mode="r") as infile:
#     reader = csv.reader(infile)
#     rows = list(reader)

# # Get the current date and time
# current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# # Add the date and time to the header
# rows[0].extend(["date", "time"])
# for row in rows[1:]:
#     row.extend([current_time.split()[0], current_time.split()[1]])

# # Write the updated rows to a new CSV file
# with open(output_csv, mode="w", newline="") as outfile:
#     writer = csv.writer(outfile)
#     writer.writerows(rows)

# print(f"CSV file updated with date and time: {output_csv}")

import csv

def generate_csv_report():
    csv_file = 'test_report.csv'

    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        for test_name, timings in TestHolidayBooking.test_timings.items():
            writer.writerow([test_name, timings['start_time'], timings['duration_seconds']])

if __name__ == '__main__':
    unittest.main()
    generate_csv_report()

