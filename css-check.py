import requests
from bs4 import BeautifulSoup

# Replace 'url' with the website link you want to fetch CSS from
url = 'https://www.instagram.com'

try:
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract CSS links from the webpage
        css_links = []
        for link in soup.find_all('link', rel='stylesheet'):
            css_links.append(link['href'])

        # Extract inline CSS styles
        inline_styles = []
        for style in soup.find_all('style'):
            inline_styles.append(style.get_text())

        # Print the CSS links and inline styles
        print("CSS Links:")
        for link in css_links:
            print(link)
            

        print("\nInline Styles:")
        for style in inline_styles:
            print(style)
            if 'instagram' in style:
                print("11111111111111111111111111")
            else:
                print('000000000000000000000')
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
