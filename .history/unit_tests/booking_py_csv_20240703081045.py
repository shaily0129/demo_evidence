import subprocess
import datetime
import csv

# Path to your test file
test_file_path = (
    "/Users/shailygoyal/Desktop/demo_evidence/unit_tests/test_holiday_booking.py"
)

# Current date and time formatted as YYYY-MM-DD HH:MM:SS
current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Filename for textual coverage report
coverage_txt_filename = f"coverage_report_{current_datetime}.txt"

# Directory name for HTML coverage report
coverage_html_directory = f"htmlcov_{current_datetime}"

# Command to run coverage with unittest
coverage_command = f"coverage run -m unittest {test_file_path}"
subprocess.run(coverage_command, shell=True, check=True)

# Generate textual coverage report
coverage_report_command = f"coverage report -m > {coverage_txt_filename}"
subprocess.run(coverage_report_command, shell=True, check=True)

# Generate HTML coverage report
coverage_html_command = f"coverage html -d {coverage_html_directory}"
subprocess.run(coverage_html_command, shell=True, check=True)

# Prepare data for CSV file
csv_filename = "test_run_history.csv"
header = ["Test File", "Coverage Report", "HTML Report", "Date and Time"]
data_row = [
    test_file_path,
    coverage_txt_filename,
    coverage_html_directory,
    current_datetime,
]

# Write to CSV file
with open(csv_filename, mode="a", newline="") as f:
    writer = csv.writer(f)
    if f.tell() == 0:
        writer.writerow(header)  # Write header if the file is empty
    writer.writerow(data_row)

print(f"Coverage reports generated with timestamp: {current_datetime}")
print(f"Details written to {csv_filename}")
