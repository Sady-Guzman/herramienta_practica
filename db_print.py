import sqlite3

def print_table(cursor, table_name):
    # Query all data from the specified table
    cursor.execute(f"SELECT * FROM {table_name};")
    
    # Fetch the column headers
    headers = [description[0] for description in cursor.description]
    
    # Fetch all rows from the query result
    rows = cursor.fetchall()
    
    # Print table name
    print(f"\nTABLE: {table_name}")
    print("=" * (len(table_name) + 8))
    
    # Print the headers
    print("\t".join(headers))
    
    # Print the rows
    for row in rows:
        print("\t".join(map(str, row)))


# Connect to the database
conn = sqlite3.connect("catalogo.db")  # Replace with your database file
cursor = conn.cursor()

# Enable foreign key constraints
cursor.execute("PRAGMA foreign_keys = ON;")
# Print data for each table
for table in ["piezas", "parametros", "trapecios"]:
    print_table(cursor, table)

# Commit the transaction (if needed)
conn.commit()

# Close the connection
conn.close()