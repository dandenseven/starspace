import sqlite3

def create_schema(db_groceries):
    conn = sqlite3.connect(db_groceries)
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS my_schema.my_table (
            id INTEGER PRIMARY KEY,
            column1 TEXT NOT NULL,
            column2 INTEGER
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS my_schema.another_table (
            id INTEGER PRIMARY KEY,
            column1 TEXT NOT NULL,
            column2 TEXT
        );
    """)

    # Create relationships (e.g., FOREIGN KEY)
    cursor.execute("""
        ALTER TABLE my_schema.another_table
        ADD CONSTRAINT fk_table1 FOREIGN KEY (column1) REFERENCES my_schema.my_table (column1);
    """)

    conn.commit()
    conn.close()