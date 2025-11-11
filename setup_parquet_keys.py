import duckdb

# Connect to a database (or create one)
con = duckdb.connect('mydb.duckdb')  # This will create mydb.duckdb in this folder

# Add your Parquet encryption keys
con.execute("PRAGMA add_parquet_key('footer_key_name', '1234567890123456');")
con.execute("PRAGMA add_parquet_key('column1_key', 'abcdef1234567890');")

# Verify the keys
keys = con.execute("SELECT * FROM pragma_key_list();").fetchall()
print("Current keys in database:", keys)
