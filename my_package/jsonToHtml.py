import copy
import os
import sys 
sys.path.append("..") 
from my_package import file_operations
from my_package import date_calculator

def jsonToHtml(ToHtmlJson, savePath,title, Market = True):
    #舊的刪除
    if os.path.exists(savePath):
        file_operations.removeOldFile(savePath)

    sortIndexOfStockDict(ToHtmlJson)
    makeHtml(ToHtmlJson, savePath, title)
    
uptitleHtml = file_operations.get_text('F:/dayWork_ver4/combine/addTitle_1.txt')
upHtml = file_operations.get_text('F:/dayWork_ver4/combine/addUp_2.txt')
downHtml = file_operations.get_text('F:/dayWork_ver4/combine/addDown_3.txt')

displayHrefs = {}
DictIndexHtml = []

#放的網址
def getDisplaytHref(number, name):
    googleSerch = number + '+' + name
    displayHrefs['goodinfo'] = 'https://goodinfo.tw/tw/ShowK_Chart.asp?STOCK_ID=' + number +'&CHT_CAT2=DATE'
    displayHrefs['googleNews'] = 'https://www.google.com.tw/search?q=' + googleSerch +'&tbm=nws'
    displayHrefs['wantgooEps'] = 'https://www.wantgoo.com/stock/' + number + '/financial-statements/eps'

def makeHtml(stockDict, savepath, title):
    #title = today + 'Observation'

    #放入標題上半部
    tempHtml = uptitleHtml
    #寫入標題
    tempHtml += '<title>'+ title + '</title>'

    tempHtml += upHtml

    #放入日期 提供其他連結的日期
    tempHtml += '<p id="thisDate" style="font-size: 20px; text-align: center;">' + title[:4] + '</p>'
    
    for indexStock in DictIndexHtml:
        
        #拿網址
        getDisplaytHref(stockDict[str(indexStock)]['number'], stockDict[str(indexStock)]['name'])

        tempHtml += '<table class="table table-bordered table-striped table-hover-yw table-sticky mt-5" style="padding: 0px;">'
        tempHtml += '<thead class="thead-light text-mid tableFloatingHeaderOriginal">'
        tempHtml += '<tr><th colspan="9" width="100%" style="font-size: 20px;">' + stockDict[str(indexStock)]['number'] + ' '+  stockDict[str(indexStock)]['name'] +'</th></tr></thead>'

        #放新聞
        for indexNews in range(len(stockDict[str(indexStock)]['news'])):
            tempHtml += '<tbody class="rt" monthlyrevenue=""><tr monthlyrevenue-item="" class=""><td class="cr" c-model="yearDate">'
            tempHtml += '<a href=' +stockDict[str(indexStock)]['news'][str(indexNews)]['saveHref'] + ' target="_blank" style="font-size: 16px;">'
            tempHtml += stockDict[str(indexStock)]['news'][str(indexNews)]['saveTitle'] + '</a>'
            tempHtml += '<p style="font-size: 16px;">' + stockDict[str(indexStock)]['news'][str(indexNews)]['saveTimes'] + '</p></td></tr></tbody>'
        tempHtml += '</table>'

        #放網址
        tempHtml += '<table class="table table-bordered table-striped table-hover-yw table-sticky" style="padding: 0px;">'
        tempHtml += '<thead class="thead-light text-mid tableFloatingHeaderOriginal">'
        tempHtml += '<tr>'
        
        for displayName, displayHref in displayHrefs.items():
            tempHtml += '<td class="cr" c-model="yearDate">'
            tempHtml += '<a href=' + displayHref + ' target="_blank" style="font-size: 16px;">'
            tempHtml += displayName + '</a></td>'
        tempHtml += '</tr></thead>'

        #月營收格式
        tempHtml += '<table class="table table-bordered table-striped table-hover-yw table-sticky" style="padding: 0px;">'
        tempHtml += '<thead class="thead-light text-mid tableFloatingHeaderOriginal">'
        tempHtml += '<tr><th rowspan="2">年度/月份</th><th colspan="4" width="50%">營業收入</th><th colspan="3" width="40%">累計營業收入</th></tr>'
        tempHtml += '<tr><th>當月營收</th><th>上月比較%</th><th>去年同月營收</th><th>去年同月增減%</th><th>當月累計營收</th><th>去年累計營收</th><th>前期比較%</th></tr></thead>'
        tempHtml += '<tbody class="rt" monthlyrevenue="">'
        
        #放月營收
        for indexMonthlyRevenue, MonthlyRevenue in stockDict[str(indexStock)]['monthlyRevenue'].items():
            tempHtml += '<tr monthlyrevenue-item="" class="">'
            tempHtml += '<td class="cr" c-model="yearDate">' + indexMonthlyRevenue + '</td>'
            tempHtml += '<td c-model="monthRevenue">' + MonthlyRevenue['當月營收'] + '</td>'

            if(MonthlyRevenue['上月比較增減(%)'][0] == '-'):
                tempHtml += '<td c-model-dazzle="class:classOfPreMonthRevenueDiff,html:preMonthRevenueDiff" class="dn">' + MonthlyRevenue['上月比較增減(%)'] + '</td>'
            else:
                tempHtml += '<td c-model-dazzle="class:classOfPreMonthRevenueDiff,html:preMonthRevenueDiff" class="up">' + MonthlyRevenue['上月比較增減(%)'] + '</td>'

            tempHtml += '<td c-model="preYearMonthRevenue">' + MonthlyRevenue['去年當月營收'] + '</td>'
            if(MonthlyRevenue['去年同月增減(%)'][0] == '-'):
                tempHtml += '<td c-model-dazzle="class:classOfPreYearMonthRevenueDiff,html:preYearMonthRevenueDiff" class="dn">' + MonthlyRevenue['去年同月增減(%)'] + '</td>'
            else:
                tempHtml += '<td c-model-dazzle="class:classOfPreYearMonthRevenueDiff,html:preYearMonthRevenueDiff" class="up">' + MonthlyRevenue['去年同月增減(%)'] + '</td>'
            tempHtml += '<td c-model="monthTotalRevenue">' + MonthlyRevenue['當月累計營收'] + '</td>'
            tempHtml += '<td c-model="preYearTotalRevenue">' + MonthlyRevenue['去年累計營收'] + '</td>'

            if(MonthlyRevenue['前期比較增減(%)'][0] == '-'):
                tempHtml += '<td c-model-dazzle="class:classOfPreTotalRevenueDiff,html:preTotalRevenueDiff" class="dn">' + MonthlyRevenue['前期比較增減(%)'] +'</td></tr>'
            else:
                tempHtml += '<td c-model-dazzle="class:classOfPreTotalRevenueDiff,html:preTotalRevenueDiff" class="up">' + MonthlyRevenue['前期比較增減(%)'] +'</td></tr>'
    tempHtml += downHtml

        #儲存
    file_operations.writeFile(savepath,tempHtml)


def  sortIndexOfStockDict(stockDict):
    global DictIndexHtml
    stockDictCopy = copy.deepcopy(stockDict)
    #最新月份
    lastMonth = date_calculator.get_previous_YearMonth()
    print('排序依照營收' + lastMonth[0])

    #遍歷沒有營收 加入假資料置頂
    for key, value in stockDictCopy.items():
        if(len(value['monthlyRevenue']) < 1):
             value['monthlyRevenue'].setdefault(lastMonth[0], {})['前期比較增減(%)'] = 1000000

    dayLookDictIndex = sorted((stockDictCopy.items()), key=lambda x: float(x[1]['monthlyRevenue'][lastMonth[0]]['前期比較增減(%)']), reverse=True)

    if(len(DictIndexHtml) !=0):
        DictIndexHtml.clear()
    for i in dayLookDictIndex:
        DictIndexHtml.append(i[0])


