import sqlite3
import config

# Function to establish connection to the database
def connect():
    connection = sqlite3.connect(config.DATABASE_NAME)
    return connection

# Function to create message history table
def create_message_history_table(connection):
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS message_history
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      sender_id TEXT,
                      message TEXT,
                      timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    connection.commit()
    cursor.close()

# Function to record incoming message in the database
def record_message(connection, sender_id, message):
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO message_history (sender_id, message)
                      VALUES (?, ?)''', (sender_id, message))
    connection.commit()
    cursor.close()

# Function to get predefined response from the database based on keywords
def get_response(keywords):
    # Implement query logic to retrieve response based on keywords
    pass
