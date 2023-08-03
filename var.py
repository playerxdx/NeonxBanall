import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

class Var:
    API_ID = int(os.getenv("API_ID", "14029604"))
    API_HASH = os.getenv("API_HASH", "80c20ae3166c904aa2137523564d46df")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "6291254699:AAGewmWje5-ctZOf5V5UIbMhyazvsG4UI3U")
    sudo = os.getenv("5845522410")
    SUDO = []
    if sudo:
        SUDO = make_int(sudo)
