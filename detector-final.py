import shutil
import tempfile
import os
import sqlite3
import requests as r
import time as t

while True:
    t.sleep(0)
    chrome_history_path = "C:\\Users\\k.s.varun chandra\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
    # print(chrome_history_path)
    temp_dir = tempfile.mkdtemp()
    temp_db_path = os.path.join(temp_dir, 'temp_history.db')
    shutil.copy(chrome_history_path, temp_db_path)

    conn = sqlite3.connect(temp_db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT url FROM urls ORDER BY last_visit_time DESC LIMIT 1")
    result = cursor.fetchone()

    # print(result[0])
    url = result[0]

    print(url)

    # history URL decode into HTML to text
    decode = r.get(url)
    output = decode.text

    # Instagram HTML decoder
    url_1 = 'https://www.instagram.com/'
    decode_1 = r.get(url_1)
    insta_1 = decode_1.text

    # To detect if 'instagram' exists in the history of the browser
    if 'instagram' in output:
        x = 1
        print(x)
        # if 'instagram' exists, verify it with the real Instagram URL
        if x == 1:
           if output[0:20] == insta_1[0:20]:
                y = 1
                print(y,' its a real instagram page ')
                
           else:
                y = 0
                print(y)
                if y == 0:
                    alert_path = 'C:\\Users\\k.s.varun chandra\\Desktop\\alert.vbs'
                    print('pyphishing page bro')
                    os.startfile(alert_path)
    else:
        print('0')
        
  
    
