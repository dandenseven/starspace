import sqlite3

def create_schema(db_groceries):
    conn = sqlite3.connect('db_groceries.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS my_schema.meats_table(
            id INTEGER PRIMARY KEY,
            column1 TEXT NOT NULL,
            column2 INTEGER
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS my_schema.frozen_table  (
            id INTEGER PRIMARY KEY,
            column1 TEXT NOT NULL,
            column2 TEXT
        );
    """)

    insert_query = """
        INSERT INTO meats_table (description, price, quantity)
        VALUES (:descripton, :price, :quantity);
    """



    insert_query = """
    INSERT INTO articles (title, description)
    VALUES (:title, :description);
    """

    for data in web_scraped_data:
        cursor.execute(insert_query, {'descriptio ': data['description'], 'price': data['price'], 'quantity': data['quantity']})

    # Create relationships (e.g., FOREIGN KEY)
    cursor.execute("""
        ALTER TABLE my_schema.another_table
        ADD CONSTRAINT fk_table1 FOREIGN KEY (column1) REFERENCES my_schema.meats_table (column1);
    """)

    conn.commit()
    conn.close()