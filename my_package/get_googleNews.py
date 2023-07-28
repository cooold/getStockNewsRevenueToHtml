import copy
import time
import sys 
sys.path.append("..") 
from my_package import base_webScraping

from my_package import global_class_href
from my_package import global_class_media
from my_package import global_class_time
from my_package import global_class_title

def googleNewsURL(b):
    a ='https://www.google.com.tw/search?q='
    c = '&tbm=nws'
    googleURL = a + b + c
    return googleURL

class stockInfo():
    number = ""
    name = ""
    news = []
    #listedOrOtc = ''
    monthly_revenue = {
        '當月營收' : '0',
        '上月營收' : '0',
        '去年當月營收' : '0',
        '上月比較增減(%)' : '0',
        '去年同月增減(%)' : '0',
        '當月累計營收' : '0',
        '去年累計營收' : '0',
        '前期比較增減(%)' : '0'
    }

#json
#最後轉json的
saveStockListToJson = {}
#個股的所有新聞資料 往上放
saveStockToJson = {}
#一則新聞的資料 往上放
saveStockNewsToJson = {}
#建構單筆的新聞資料
saveNews = {}
stockInfoList = []
#整理營收
stockMonthly_revenueList ={}
stockInfo = stockInfo()

#爬google新聞
def GoogleWebcrawle(headers, stock):
    times = 0
    c = stock.split()
    stockInfo.number = c[0]
    stockInfo.name = c[1]

    #if(len(c) >= 3):
    #    stockInfo.listedOrOtc = c[2]
    #else:
    #    stockInfo.listedOrOtc = '無市場資料'

    stockInfoList.append(copy.deepcopy(stockInfo))
    saveStockToJson['number'] = stockInfo.number
    saveStockToJson['name'] = stockInfo.name
    #saveStockToJson['市場'] = stockInfo.listedOrOtc
    url = googleNewsURL(c[0] + ' ' + c[1])
    request = base_webScraping.getRequests(headers, url)

    if base_webScraping.checkRequestsSuccess(request):
        pass
    else:
        print("爬取失敗，公開資訊觀測站沒有回應")
        input("按下任意鍵表示了解此情況......")

    soup = base_webScraping.resToParser(request)

    #過濾奇摩
    span_tagsYahoo =soup.find_all("div", class_= [global_class_media])
    #過濾時間
    span_tagsTime =soup.find_all("div", class_= [global_class_time])
    #過濾標題
    span_tagsTitle =soup.find_all("div", class_= [global_class_title])
    #過濾連結
    span_tagsHref =soup.find_all("a", class_= [global_class_href])

    count = 0
    titleCount = 0
    for span_tag in span_tagsYahoo:
        if "奇摩" not in span_tag.span.string and 'LINE' not in span_tag.span.string:
            saveTimes = str(span_tagsTime[times].span.string)
            try:
                saveTitle = str(span_tagsTitle[titleCount].string)
            except:
                saveTitle = "取得標題失敗"

            if '盤中速報' not in saveTitle and '盤中股價' not in saveTitle and '盤後速報' not in saveTitle:
                saveHref = str(span_tagsHref[times]["href"])
                saveNews['saveTitle'] = saveTitle
                saveNews['saveTimes'] = saveTimes
                saveNews['saveHref'] = saveHref
                saveStockNewsToJson[count] = copy.deepcopy(saveNews)
                count += 1

        times += 1
        titleCount += 2
    print(str(c)+'新聞完成')

#讀取路徑開始爬
def startGet(headers, all_twse_months, lookStocks):    
    
    saveStockListToJson.clear()
    #開始爬
    print(lookStocks)

    for i in range(len(lookStocks)):
        print('剩餘'+str(len(lookStocks)-i)+'檔股票')
        time.sleep(2)
        #抓google
        GoogleWebcrawle(headers, lookStocks[i])

        #放入字典
        saveStockToJson['news'] = copy.deepcopy(saveStockNewsToJson)
        saveStockNewsToJson.clear()

        #整理公開資訊 
        #取出
        for key, value in all_twse_months.items():
            for monthTime, twse in value.items():
                if not twse[twse['公司 代號'] == stockInfo.number].empty:
                    want = twse[twse['公司 代號'] == stockInfo.number]
                    stockInfo.monthly_revenue['當月營收'] = str(want['當月營收'].values[0])
                    stockInfo.monthly_revenue['上月營收'] = str(want['上月營收'].values[0])
                    stockInfo.monthly_revenue['當月營收'] = str(want['當月營收'].values[0])
                    stockInfo.monthly_revenue['去年當月營收'] = str(want['去年當月營收'].values[0])
                    stockInfo.monthly_revenue['上月比較增減(%)'] = str(want['上月比較 增減(%)'].values[0])
                    stockInfo.monthly_revenue['去年同月增減(%)'] = str(want['去年同月 增減(%)'].values[0])
                    stockInfo.monthly_revenue['當月累計營收'] = str(want['當月累計營收'].values[0])
                    stockInfo.monthly_revenue['去年累計營收'] = str(want['去年累計營收'].values[0])
                    stockInfo.monthly_revenue['前期比較增減(%)'] = str(want['前期比較 增減(%)'].values[0])
                    stockMonthly_revenueList[monthTime] = copy.deepcopy(stockInfo.monthly_revenue)
                    
        saveStockToJson['monthlyRevenue'] = copy.deepcopy(stockMonthly_revenueList)
        stockMonthly_revenueList.clear()
        saveStockListToJson[i] = copy.deepcopy(saveStockToJson)
        saveStockToJson.clear()
        print(stockInfo.number + stockInfo.name + '完成')

    stockInfoList.clear()
    return saveStockListToJson

