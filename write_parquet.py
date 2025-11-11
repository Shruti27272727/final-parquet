import duckdb

# Connect to DuckDB
con = duckdb.connect()

# Create a table from an existing Parquet file
con.execute("""
CREATE TABLE test_write AS 
SELECT * FROM 'C:/Users/powar/Desktop/final parquet/sample.parquet'
""")

# Write the table back to a new Parquet file
con.execute("""
COPY test_write TO 'C:/Users/powar/Desktop/final parquet/output.parquet' (FORMAT PARQUET)
""")

print("Parquet file written successfully!")
