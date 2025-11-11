import duckdb
import os

# Connect to your DuckDB database
con = duckdb.connect('mydb.duckdb')

# Path to your Parquet file
parquet_file = 'customers_parquet.parquet'

# Check if file exists
if os.path.exists(parquet_file):
    # Read the exported Parquet file
    df = con.execute(f"SELECT * FROM '{parquet_file}';").fetchdf()
    
    # Show the data
    print("Parquet file contents:")
    print(df)
else:
    print(f"Error: Parquet file '{parquet_file}' does not exist.")
