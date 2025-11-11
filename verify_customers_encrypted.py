import duckdb
import os

con = duckdb.connect('mydb.duckdb')

parquet_file = 'customers_encrypted.parquet'

# Export table with footer key encryption
con.execute(f"""
COPY customers TO '{parquet_file}' (ENCRYPTION_CONFIG {{ footer_key: 'footer_key_name' }});
""")

if os.path.exists(parquet_file):
    print(f"Encrypted Parquet file exported successfully: {parquet_file}")
else:
    print("Error: Failed to export Parquet file.")
