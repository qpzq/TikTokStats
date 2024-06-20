import requests
from bs4 import BeautifulSoup
import time
import re

def get_tiktok_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        scripts = soup.find_all('script')

        for script in scripts:
            if 'itemInfo' in str(script):
                # Extract playCount (views)
                view_pattern = r'"playCount":(\d+)'
                view_match = re.search(view_pattern, str(script))
                if view_match:
                    views = int(view_match.group(1))
                else:
                    views = None

                # Extract diggCount (hearts/likes)
                heart_pattern = r'"diggCount":(\d+)'
                heart_match = re.search(heart_pattern, str(script))
                if heart_match:
                    hearts = int(heart_match.group(1))
                else:
                    hearts = None

                # Extract shareCount (favorites)
                share_pattern = r'"shareCount":(\d+)'
                share_match = re.search(share_pattern, str(script))
                if share_match:
                    shares = int(share_match.group(1))
                else:
                    shares = None

                return views, hearts, shares

        return None, None, None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None, None, None

def format_number_with_commas(number):
    if number is None:
        return "N/A"
    else:
        # Format the number with commas and return
        return "{:,}".format(number)

banner = """
 ██████╗ ██████╗ ███████╗ ██████╗ 
██╔═══██╗██╔══██╗╚══███╔╝██╔═══██╗
██║   ██║██████╔╝  ███╔╝ ██║   ██║
██║▄▄ ██║██╔═══╝  ███╔╝  ██║▄▄ ██║
╚██████╔╝██║     ███████╗╚██████╔╝
 ╚══▀▀═╝ ╚═╝     ╚══════╝ ╚══▀▀═╝ 
"""

print(banner)

if __name__ == "__main__":
    tiktok_url = input(">  TikTok URL: ").strip()

    views, hearts, shares = get_tiktok_data(tiktok_url)

    if views is not None:
        print(f">  Views: {format_number_with_commas(views)}")
    else:
        print("Unable to fetch views. Please check your URL and try again.")

    if hearts is not None:
        print(f">  Hearts: {format_number_with_commas(hearts)}")
    else:
        print("Unable to fetch hearts. Please check your URL and try again.")

    if shares is not None:
        print(f">  Shares: {format_number_with_commas(shares)}")
    else:
        print("Unable to fetch shares. Please check your URL and try again.")

time.sleep(5)
