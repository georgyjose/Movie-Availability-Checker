import sys
import requests
import json

BOT_TOKEN = "Add your Telegram Bot token here"
BOT_CHAT_ID = 'Add your Telegram Chat Id here'

def telegram_bot_sendmessage(message):
    send_text = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage?chat_id=' + BOT_CHAT_ID + '&parse_mode=Markdown&text=' + message
    response = requests.get(send_text)

def check_movie_open(pvr_url, force_message=False):
    response = requests.post(pvr_url)
    if response.status_code == 200:
        response_json = response.json()
        #print(response_json)
        if response_json.get('msg') == "No Sessions Available.":
            if force_message:
                telegram_bot_sendmessage("No tickets available in PVR Website. "
                                         "This is a forced message")
            return
        else:
            response_string = json.dumps(response_json).lower()
            if '4dx' in response_string:
                telegram_bot_sendmessage("4DX tickets available in PVR Website")
            elif 'atmos' in response_string:
                telegram_bot_sendmessage("Dolby Atmos tickets available in PVR Website")
            elif 'gold' in response_string:
                telegram_bot_sendmessage("Gold tickets available in PVR Website")
            else:
                telegram_bot_sendmessage("Normal tickets available in PVR Website")

def check_ticket_available_on_date(pvr_url, date):
    response = requests.post(pvr_url)
    if response.status_code == 200:
        # a.get('output').get('cinemas')[0].get('childs')[0].get('sws')[0].get('s')[0]
        response = response.json()
        cinemas = response.get('output', {}).get('cinemas', [])
        for cinema in cinemas:
            childs = cinema.get('childs',[])
            for child in childs:
                exit()
                # sws = child.get('sws', [])
                # for sw in sws:
                #     s = sw.get('s', [])
                #     for micro_s in s:
                #         print(micro_s)
                #         exit()


# vikram_url = "https://api1.pvrcinemas.com/PVRCinemasCMS/api/content/msessionsnew?city=Kochi&mid=NHO00018305&lat&lng&av&pt"
# doctor_strange_url="https://api1.pvrcinemas.com/PVRCinemasCMS/api/content/msessionsnew?city=Kochi&mid=NHO00018048&lat&lng&av&pt"
# fantastic_beasts_url = "https://api1.pvrcinemas.com/PVRCinemasCMS/api/content/msessionsnew?city=Kochi&mid=NHO00019135&lat&lng&av&pt"
# rrr_url = "https://api1.pvrcinemas.com/PVRCinemasCMS/api/content/msessionsnew?city=Kochi&mid=NHO00015492&lat&lng&av&pt"
ps1_url = "https://api1.pvrcinemas.com/PVRCinemasCMS/api/content/msessionsnew?city=Kochi&mid=NHO00018009&lat&lng&av&pt"

if 'force-message' in sys.argv:
    check_movie_open(ps1_url, force_message=True)
else:
    check_movie_open(ps1_url)

# check_ticket_available_on_date(vikram_url, None)
