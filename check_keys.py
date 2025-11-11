import duckdb

# Connect to your DuckDB database
con = duckdb.connect('mydb.duckdb')

# List all registered Parquet encryption keys
keys = con.execute("SELECT * FROM pragma_key_list();").fetchall()

print("Registered keys:", keys)
