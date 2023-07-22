import json
import datetime
import time
import sys 
sys.path.append("..") 
#folder
from my_package import file_operations
from my_package import date_calculator
from my_package import get_goodinfoStockToText
from my_package import save_goodinfoToHtml
from my_package import get_monthly_revenue
from my_package import get_googleNews
from my_package import jsonToHtml
#global variables
from my_package import global_headers
from my_package import global_get_dayURL
from my_package import global_get_historicalHigh_URL
from my_package import global_get_InvestmentTrust_URL1
from my_package import global_get_InvestmentTrust_URL2


def main():

    #問日期
    print('請輸入日期')
    today = input()
    #沒有的話取今日
    if(today == ''):
        today = datetime.datetime.now().strftime("%m%d")


    #儲存路徑
    saveNewHistoricalHighPath ='F:/dayWork_ver4/historicalHigh/' + today + '.txt'
    lookPath = 'F:/dayWork_ver4/look/' + today + '.txt'
    observationPath = 'F:/dayWork_ver4/observation.txt'
    historicalHighPath = 'F:/dayWork_ver4/historicalHigh.txt'
    saveNewHistorical_diff_HighPath ='F:/dayWork_ver4/historicalHigh/' + today + '_diff.txt'

    #平日抓 假日不抓goodinfo
    #if(date_calculator.is_weekday(today)):
    #print('今日是平日')

    get_goodinfoStockToText.getGoodinfoToRawText(global_headers, global_get_historicalHigh_URL, saveNewHistoricalHighPath, 'historicalHigh')
    print('新增歷史新高個股資料')
    time.sleep(12)

    get_goodinfoStockToText.getGoodinfoToRawText(global_headers, global_get_dayURL, lookPath, 'look')
    print('儲存每日個股資料')
    time.sleep(8)

    save_goodinfoToHtml.saveGoodinfoToHtml(global_headers, global_get_historicalHigh_URL, 'F:/dayWork_ver4/otherLook/'+ today + '歷史新高.html')
    print('儲存每日歷史新高網頁')
    time.sleep(13)

    save_goodinfoToHtml.saveGoodinfoToHtml(global_headers, global_get_InvestmentTrust_URL1, 'F:/dayWork_ver4/otherLook/'+ today + '投信上市.html')
    print('儲存每日投信上市網頁')
    time.sleep(8)

    save_goodinfoToHtml.saveGoodinfoToHtml(global_headers, global_get_InvestmentTrust_URL2, 'F:/dayWork_ver4/otherLook/'+ today + '投信上櫃.html')
    print('儲存每日投信上櫃網頁')
    
    #每日新的, 原有, 新增差異
    file_operations.CompareHistoricalHighText(saveNewHistoricalHighPath, historicalHighPath, saveNewHistorical_diff_HighPath)

    #整理observation
    file_operations.sort_txt_by_first_value(observationPath)
    
    #抓營收
    twse_months = date_calculator.get_previous_YearMonth()
    print('抓取營收' + str(twse_months))
    all_twse_monthsRevenue = get_monthly_revenue.getAllRevenue(global_headers, twse_months)
    print('取得月營收完成')

    #google爬蟲

    #HistoricalHigh 目前沒有營收
    HistoricalHighStocks = file_operations.get_textLines(historicalHighPath)
    HistoricalStocksNewsAndRevenue_dict = get_googleNews.startGet(global_headers, all_twse_monthsRevenue, HistoricalHighStocks)
    file_operations.dictToJson(HistoricalStocksNewsAndRevenue_dict, 'F:/dayWork_ver4/historicalHigh/' + today)

    #look
    lookStocks = file_operations.get_textLines(lookPath)
    lookStocksNewsAndRevenue_dict = get_googleNews.startGet(global_headers, all_twse_monthsRevenue, lookStocks)
    file_operations.dictToJson(lookStocksNewsAndRevenue_dict, 'F:/dayWork_ver4/look/' + today)

    #observation
    observationStocks = file_operations.get_textLines(observationPath)
    observationStocksNewsAndRevenue_dict = get_googleNews.startGet(global_headers, all_twse_monthsRevenue, observationStocks)
    file_operations.dictToJson(observationStocksNewsAndRevenue_dict, 'F:/dayWork_ver4/observation/' + today)

    #製作成html
    dayHistoricalHighStocks = file_operations.get_text('F:/dayWork_ver4/historicalHigh/' + today + '.json')
    dayHistoricalHighStocksJson = json.loads(dayHistoricalHighStocks)
    jsonToHtml.jsonToHtml(dayHistoricalHighStocksJson, 'F:/dayWork_ver4/dayHtml/' + today + 'dayHistoricalHigh.html', today + 'dayHistoricalHigh', Market = False)

    dayLook = file_operations.get_text('F:/dayWork_ver4/look/' + today + '.json')
    dayLookJson = json.loads(dayLook)
    jsonToHtml.jsonToHtml(dayLookJson, 'F:/dayWork_ver4/dayHtml/' + today + 'Day.html', today + 'Day')

    observationLook = file_operations.get_text('F:/dayWork_ver4/observation/' + today + '.json')
    observationJson = json.loads(observationLook)
    jsonToHtml.jsonToHtml(observationJson, 'F:/dayWork_ver4/dayHtml/' + today + 'Observation.html', today + 'Observation')

    input("Html完成")


if __name__ == "__main__":
    main()