import duckdb
import pandas as pd

# Path to your CSV file and DuckDB database file
csv_file = "test_report_with_timestamp.csv"
db_file = "my_duckdb_data1.db"

# Connect to DuckDB and create a database file
con = duckdb.connect(database=db_file, read_only=False)

# Read CSV data into a DataFrame
df = pd.read_csv(csv_file)
print("CSV data loaded successfully:", df.head())  # Check if CSV data is loaded

# Register DataFrame as a table in DuckDB
con.register("test_data", df)
print("Table 'test_data' registered successfully.")

# Optionally, you can query or manipulate the data
# For example, print the first 5 rows
result = con.execute("SELECT * FROM test_data LIMIT 5")
print(result.fetch_df())

# Close the connection
con.close()
