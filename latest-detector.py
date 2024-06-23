import shutil
import tempfile
import os
import sqlite3
import requests as r
import time as t

# Function to check if a URL is a search engine query
def is_search_query(url):
    search_keywords = ['google.', 'bing.com', 'yahoo.', 'duckduckgo.', 'search.', 'yandex.', 'baidu.']
    for keyword in search_keywords:
        if keyword in url:
            return True
    return False

while True:
    t.sleep(0)
    chrome_history_path = "C:\\Users\\k.s.varun chandra\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
    temp_dir = tempfile.mkdtemp()
    temp_db_path = os.path.join(temp_dir, 'temp_history.db')
    shutil.copy(chrome_history_path, temp_db_path)

    conn = sqlite3.connect(temp_db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT url FROM urls ORDER BY last_visit_time DESC LIMIT 1")
    result = cursor.fetchone()

    url = result[0]

    print(url)

    # Check if the URL is a search engine query
    if is_search_query(url):
        print(f"{url} is a search engine query, skipping.")
        continue

    decode = r.get(url)
    output = decode.text

    # Instagram HTML decoder
    url_1 = 'https://www.instagram.com/'
    decode_1 = r.get(url_1)
    insta_1 = decode_1.text

    try:
        response = r.get(url, timeout=10)

        if 200 <= response.status_code < 300:
            if response.url.startswith('https://'):
                print(f"The website {url} is safe and has a valid SSL certificate.")
                if 'instagram' in url:
                    x = 1
                    if x == 1:
                        if output[0:20] == insta_1[0:20]:
                            y = 1
                            print(y, ' its a real Instagram page ')
                        else:
                            y = 0
                            print(y)
                            if y == 0:
                                alert_path = 'C:\\Users\\k.s.varun chandra\\Desktop\\alert.vbs'
                                print('Phishing page detected!')
                                os.startfile(alert_path)
                else:
                    continue
            else:
                print(f"The website {url} is accessible but does not use HTTPS (SSL/TLS).")
                alert_path = 'C:\\Users\\k.s.varun chandra\\Desktop\\alert.vbs'
                print('Phishing page detected!')
                os.startfile(alert_path)
        else:
            print(f"The website {url} returned a non-successful status code: {response.status_code}")
            alert_path = 'C:\\Users\\k.s.varun chandra\\Desktop\\alert.vbs'
            print('Phishing page detected!')
            os.startfile(alert_path)
    except r.exceptions.RequestException as e:
        print(f"An error occurred while trying to access the website {url}: {e}")
        print(f"The website {url} may not be safe.")
        alert_path = 'C:\\Users\\k.s.varun chandra\\Desktop\\alert.vbs'
        print('Phishing page detected!')
        os.startfile(alert_path)
