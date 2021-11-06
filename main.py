import os
import requests
from dotenv import load_dotenv
load_dotenv()


def make_pair(x, y):
    return lambda n: x if n == 0 else y


def first(p):
    return p(0)


def second(p):
    return p(1)


if __name__ == '__main__':
    url = f"https://api.miro.com/v1/boards/{os.getenv('MIRO_BOARD_ID')}/widgets/?widgetType=shape"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {os.getenv('MIRO_API_TOKEN')}"
    }
    response = requests.request("GET", url, headers=headers)





    #вывод всех текстов
    for i in range(0,len(response.json()['data'])):
        p = make_pair(response.json()['data'][i]['id'], response.json()['data'][i]['text'])
        print(f'{first(p)} : {second(p)}')



    print('\n\n\n')

    url_widget = f"https://api.miro.com/v1/boards/{os.getenv('MIRO_BOARD_ID')}/widgets/?widgetType=line"
    response_widget = requests.request("GET", url_widget, headers=headers)

    #вывод всех текстов
    for i in range(0,len(response_widget.json()['data'])):
        p=make_pair(response_widget.json()['data'][i]['startWidget'],response_widget.json()['data'][i]['endWidget'])
        print(f'{first(p)} -> {second(p)}')

