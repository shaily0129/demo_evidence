import duckdb

def create_tables():
    conn = duckdb.connect("my-project/sources/new_booking/holiday_bookings.db")
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS bookings (
            request_id VARCHAR,
            name VARCHAR,
            country VARCHAR,
            age INTEGER,
            insurance BOOLEAN,
            booking_id VARCHAR,
            date DATE
        )
    """
    )
    conn.close()


if __name__ == "__main__":
    create_tables()
