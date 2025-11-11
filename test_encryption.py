import duckdb

# Connect to your DuckDB database
con = duckdb.connect('mydb.duckdb')

# First, try reading the encrypted Parquet file WITHOUT keys
print("Read without keys (this should fail or return gibberish):")
try:
    df_no_keys = con.execute("SELECT * FROM 'customers_encrypted.parquet';").fetchdf()
    print(df_no_keys)
except Exception as e:
    print("Error reading without keys:", e)

# Now, add the encryption keys
con.execute("PRAGMA add_parquet_key('name_key', '1234567890123456');")   # 16 chars
con.execute("PRAGMA add_parquet_key('email_key', 'abcdef1234567890');")  # 16 chars
con.execute("PRAGMA add_parquet_key('ssn_key', '0987654321123456');")    # 16 chars


# Try reading the file WITH keys
print("\nRead with keys (should show proper data):")
df_with_keys = con.execute("SELECT * FROM 'customers_encrypted.parquet';").fetchdf()
print(df_with_keys)
