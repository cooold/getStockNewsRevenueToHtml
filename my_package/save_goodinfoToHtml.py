import os
import pandas as pd
import sys 
sys.path.append("..") 
from my_package import file_operations
from my_package import base_webScraping

def saveGoodinfoToHtml(headers: str, url: str, savePath: str) :
    res = base_webScraping.getRequests(headers, url)

    if base_webScraping.checkRequestsSuccess(res):
        pass
    else:
        print("爬取失敗，公開資訊觀測站沒有回應")
        input("按下任意鍵表示了解此情況......")
    
    soup = base_webScraping.resToParser(res)

    if os.path.exists(savePath):
        file_operations.removeOldFile(savePath)
    file_operations.writeFile(savePath, str(soup))
