import os
import sqlite3
import time

# Specify the path to Chrome's history database
chrome_history_path = "C:\\Users\\k.s.varun chandra\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"

# Check if the history database file exists
if not os.path.isfile(chrome_history_path):
    print("Chrome history database file not found.")
    exit(1)

while True:
    # Connect to the Chrome history database
    conn = sqlite3.connect(chrome_history_path)
    cursor = conn.cursor()

    # Query the history data for the most recently opened link
    cursor.execute("SELECT url FROM urls ORDER BY last_visit_time DESC LIMIT 1")
    result = cursor.fetchone()

    # Print the most recently opened website link
    if result:
        print("Most recently opened link:", result[0])
    else:
        print("No browser history found.")

    # Close the database connection
    conn.close()

    # Wait for a while before checking again (e.g., every 60 seconds)
    time.sleep(60)
