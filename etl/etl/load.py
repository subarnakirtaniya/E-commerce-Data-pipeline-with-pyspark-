import psycopg2

def load_data(data):

    conn = psycopg2.connect(
        database="salesdb",
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()

    for row in data.collect():

        cursor.execute("""
        INSERT INTO daily_sales
        VALUES (%s,%s)
        """, (row['order_date'], row['daily_sales']))

    conn.commit()

    conn.close()
