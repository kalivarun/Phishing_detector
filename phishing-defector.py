import sqlite3
'''
# Specify the path to Chrome's history database
chrome_history_path = "C:\\Users\\k.s.varun chandra\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"

# Connect to the database
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
conn.close()'''


#2

'''import shutil
import tempfile
import os  # Add this import statement
import time as t 
# Specify the path to Chrome's history database

while True:

chrome_history_path = "C:\\Users\\k.s.varun chandra\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"

# Create a temporary copy of the database
temp_dir = tempfile.mkdtemp()
temp_db_path = os.path.join(temp_dir, 'temp_history.db')
shutil.copy(chrome_history_path, temp_db_path)

# Connect to the copied database
conn = sqlite3.connect(temp_db_path)
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

# Clean up the temporary files
shutil.rmtree(temp_dir)

detect = result[0]
if detect == 'https://zvodiac0012003.000webhostapp.com/index.php':
    print('this is a phishing link')
else:
    print('error')'''
    
    #while loop
'''while True:
     print(detect)
     t.sleep(3)

'''

#3 
import shutil
import tempfile
import os
import sqlite3
import time as t 

path = 'C:\\Users\\k.s.varun chandra\\Desktop\\alert.vbs'
path = os.path.realpath(path)


# Specify the path to Chrome's history database

while True:
    chrome_history_path = "C:\\Users\\k.s.varun chandra\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"

# Create a temporary copy of the database


    temp_dir = tempfile.mkdtemp()
    temp_db_path = os.path.join(temp_dir, 'temp_history.db')
    shutil.copy(chrome_history_path, temp_db_path)


    # Connect to the copied database
    conn = sqlite3.connect(temp_db_path)
    cursor = conn.cursor()

    # Query the history data for the most recently opened link
    cursor.execute("SELECT url FROM urls ORDER BY last_visit_time DESC LIMIT 1")
    result = cursor.fetchone()

    # Print the most recently opened website link
    if result:
        print("Most recently opened link:", result[0])

        detect = result[0]
        if detect == 'https://propecia-veterans-jesse-para.trycloudflare.com/login.html.php':
            print('This is a phishing link')
            t.sleep(1)
            os.startfile(path)
           
        else:
            print('No phishing detected')

    else:
        print("No browser history found.")

    # Close the database connection
    conn.close()

    # Wait for a while before checking again (e.g., every 5 seconds)
    t.sleep(0)
