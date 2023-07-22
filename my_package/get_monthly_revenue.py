import time
import pandas as pd
from my_package import base_webScraping
from typing import List


def getAllRevenue(headers: str, twse_months: List[str]) -> List[str]:
    #上市
    twseList_sii_0 = {}
    twseList_sii_1 = {}
    #上櫃
    twseList_otc_0 = {}
    twseList_otc_1 = {}
    for i in twse_months:
        temp1_0 = getRevenue(headers, i,'sii','0')
        time.sleep(5)
        print('取得上市_'+ i +'月營收')
        temp1_1 = getRevenue(headers, i,'sii','1')
        time.sleep(5)
        print('取得上市ky_'+ i +'月營收')
        temp2_0 = getRevenue(headers, i,'otc','0')
        time.sleep(5)
        print('取得上櫃_'+ i +'月營收')
        temp2_1 = getRevenue(headers, i,'otc','1')
        time.sleep(5)
        print('取得上櫃ky_'+ i +'月營收')
        twseList_sii_0[i] = temp1_0
        twseList_sii_1[i] = temp1_1
        twseList_otc_0[i] = temp2_0
        twseList_otc_1[i] = temp2_1

    allRevenue = {}
    allRevenue['twseList_sii_0'] = twseList_sii_0
    allRevenue['twseList_sii_1'] = twseList_sii_1
    allRevenue['twseList_otc_0'] = twseList_otc_0
    allRevenue['twseList_otc_1'] = twseList_otc_1

    return allRevenue

def getRevenue(headers, date, web, ky):
    url = 'https://mops.twse.com.tw/nas/t21/'+ web +'/t21sc03_'+ date +'_' + ky +'.html'
    print(url)
    res = base_webScraping.getRequests(headers, url, 'big5')
    #res.encoding = 'big5'

    if base_webScraping.checkRequestsSuccess(res):
        pass
    else:
        print("爬取失敗，公開資訊觀測站沒有回應")
        input("按下任意鍵表示了解此情況......")

    html_df = pd.read_html(res.text)
    # 剃除行數錯誤的表格,並將表格合併
    df = pd.concat([df for df in html_df if df.shape[1] == 11]) 
    # 設定表格的header 
    df.columns = df.columns.get_level_values(1)

    return df