import requests
from bs4 import BeautifulSoup

def getRequests(headers: str, url: str,encod='utf-8') -> str:
    res = requests.get(url, headers=headers)
    res.encoding = encod
    return res

def checkRequestsSuccess(res: str) -> bool:
    isSuccess = False
    if res.status_code == 200:
        print("篩選網站成功回應")
        isSuccess = True
    else:
        print("爬取失敗，伺服器沒有回應")
        isSuccess = False

    return isSuccess
    
def resToParser(res: str) -> str:
    soup = BeautifulSoup(res.text,"html.parser")
    return soup