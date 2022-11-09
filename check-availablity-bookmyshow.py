import sys
import requests
import json
from bs4 import BeautifulSoup

BOT_TOKEN = "Add your Telegram Bot token here"
BOT_CHAT_ID = 'Add your Telegram Chat Id here'

def telegram_bot_sendmessage(message):
    send_text = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage?chat_id=' + BOT_CHAT_ID + '&parse_mode=Markdown&text=' + message
    response = requests.get(send_text)

def check_movie_open(url, force_message=False):

    movie_found = False

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        child_soup = soup.find_all('strong')
        for theatre in child_soup:
            theatre_name = theatre.contents[0].lower()
            if 'pvr' in theatre_name:
                if '4dx' in theatre_name:
                    telegram_bot_sendmessage("PVR 4DX tickets available in BookMyShow")
                    return
                elif 'atmos' in theatre_name:
                    telegram_bot_sendmessage("PVR Dolby Atmos tickets available in BookMyShow")
                    return
                elif 'gold' in theatre_name:
                    telegram_bot_sendmessage("PVR Gold tickets available in BookMyShow")
                    return
                else:
                    telegram_bot_sendmessage("PVR Normal tickets available in BookMyShow")
                    return
                movie_found = True
            elif 'shenoys' in theatre_name:
                telegram_bot_sendmessage("Shenoys tickets available in BookMyShow")
                return

        if force_message:
            telegram_bot_sendmessage("Movie not yet available in BookMyShow")
            return

    else:
        print(f"Kittunnilla: {response.status_code}")

ps1_url = "https://in.bookmyshow.com/buytickets/ponniyin-selvan-part-1-kochi/movie-koch-ET00323897-MT/20220930"
wakanda_url = "https://in.bookmyshow.com/buytickets/black-panther-wakanda-forever-3d-kochi/movie-koch-ET00342963-MT/20221111"

if 'force-message' in sys.argv:
    check_movie_open(wakanda_url, force_message=True)
else:
    check_movie_open(wakanda_url)

