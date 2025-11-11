import duckdb

# Connect to DuckDB
con = duckdb.connect()

# Step 1: Create a table from an existing Parquet file
con.execute("""
CREATE TABLE test_write AS 
SELECT * FROM 'C:/Users/powar/Desktop/final parquet/sample.parquet'
""")

# Step 2: Write the table back to a new Parquet file
con.execute("""
COPY test_write TO 'C:/Users/powar/Desktop/final parquet/output.parquet' (FORMAT PARQUET)
""")

print("Parquet file written successfully!")

# Step 3: Verify the contents of the newly written Parquet file
result = con.execute("SELECT * FROM 'C:/Users/powar/Desktop/final parquet/output.parquet' LIMIT 5").fetchall()

print("\nFirst 5 rows of the Parquet file:")
for row in result:
    print(row)
