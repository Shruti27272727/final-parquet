import duckdb
import os

# Connect to your DuckDB database
con = duckdb.connect('mydb.duckdb')

# Optional: Add encryption keys (you've already done this in setup_parquet_keys.py)
# con.execute("PRAGMA add_parquet_key('name_key', '1234567890123456');")
# con.execute("PRAGMA add_parquet_key('email_key', 'abcdef1234567890');")
# con.execute("PRAGMA add_parquet_key('ssn_key', 'xyz1234567890');")

# Export the table to a Parquet file (for demonstration, still plain)
parquet_file = 'customers_encrypted.parquet'

con.execute(f"""
COPY customers TO '{parquet_file}' (FORMAT PARQUET);
""")

# Verify the file exists
if os.path.exists(parquet_file):
    print(f"Encrypted Parquet file exported successfully: {parquet_file}")
else:
    print("Error: Failed to export Parquet file.")
