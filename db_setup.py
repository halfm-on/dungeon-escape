import sqlite3

DB_NAME = "scores.db"


def create_tables(db_name=DB_NAME):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT NOT NULL,
            rounds_survived INTEGER NOT NULL,
            date TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()
    print("Scores table created successfully.")


if __name__ == "__main__":
    create_tables()