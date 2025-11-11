import duckdb

# Connect to the database (or create one if it doesn't exist)
con = duckdb.connect('mydb.duckdb')
print("Database connected successfully.")

# Add Parquet encryption keys (16-byte keys for AES-128)
con.execute("PRAGMA add_parquet_key('footer_key_name', '1234567890123456');")
con.execute("PRAGMA add_parquet_key('name_key', 'abcdef1234567890');")
con.execute("PRAGMA add_parquet_key('email_key', 'emailkey12345678');")
con.execute("PRAGMA add_parquet_key('ssn_key', 'ssnkey1234567890');")

print("Keys have been registered successfully.")
