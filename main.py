import os
import requests
from dotenv import load_dotenv
load_dotenv()


if __name__ == '__main__':
    url = f"https://api.miro.com/v1/boards/{os.getenv('MIRO_BOARD_ID')}/widgets/?widgetType=shape"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {os.getenv('MIRO_API_TOKEN')}"
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
