import sqlite3

def init_db():
    conn = sqlite3.connect("jarvis.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        message TEXT
    )
    """)

    conn.commit()
    conn.close()
def save_message(message):
    conn = sqlite3.connect("jarvis.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO memory (message) VALUES (?)",
        (message,)
    )

    conn.commit()
    conn.close()
