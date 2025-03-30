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
    API_ID = int(os.getenv("API_ID", "22182189"))
    API_HASH = os.getenv("API_HASH", "5e7c4088f8e23d0ab61e29ae11960bf5")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    sudo = os.getenv("SUDO")
    SUDO = []
    if sudo:
        SUDO = make_int(sudo) 
 

