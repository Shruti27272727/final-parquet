import duckdb
import pandas as pd

# Connect to database
con = duckdb.connect('mydb.duckdb')

# Optional: Drop the table if it exists
con.execute("DROP TABLE IF EXISTS customers;")

# Create your DataFrame (replace with your real data)
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com'],
    'ssn': ['123-45-6789', '987-65-4321', '111-22-3333']
}
df = pd.DataFrame(data)

# Create customers table from DataFrame
con.execute("CREATE TABLE customers AS SELECT * FROM df;")

print("Customers table created successfully.")
