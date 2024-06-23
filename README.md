# Phishing Domain Detector

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction
Phishing Domain Detector is a Python-based tool designed to identify and flag potentially malicious domains based on the browsing history from Google Chrome. The tool checks if a visited site mimics a legitimate site like Instagram to alert the user of potential phishing.

## Features
- **Browser History Access:** Access and read the latest URL from Google Chrome's browsing history.
- **Real-time Detection:** Check if the visited site mimics a legitimate site like Instagram.
- **Alert System:** Alert the user if a phishing page is detected.

## Installation
To install the Phishing Domain Detector, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/phishing-domain-detector.git
    cd phishing-domain-detector
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Alert Script (Optional):**
   Create a `alert.vbs` file on your desktop with the following content:
    ```vbs
    x=msgbox("Phishing alert! This page may not be legitimate.", 0+48, "Phishing Alert")
    ```

## Usage
To use the Phishing Domain Detector, run the following Python script:

```python
import shutil
import tempfile
import os
import sqlite3
import requests as r
import time as t

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

    decode = r.get(url)
    output = decode.text

    url_1 = 'https://www.instagram.com/'
    decode_1 = r.get(url_1)
    insta_1 = decode_1.text

    if 'instagram' in output:
        x = 1
        print(x)
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
