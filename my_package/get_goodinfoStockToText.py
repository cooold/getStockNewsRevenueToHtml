import os
import pandas as pd
import sys 
sys.path.append("..") 
from my_package import file_operations
from my_package import base_webScraping
from my_package import global_html_df_index

#儲存篩選後個股txt
def getGoodinfoToRawText(headers: str, url: str, savepath: str) -> None:
    res = base_webScraping.getRequests(headers, url)

    if base_webScraping.checkRequestsSuccess(res):
        pass
    else:
        print("爬取失敗，公開資訊觀測站沒有回應")
        input("按下任意鍵表示了解此情況......")

    html_df = pd.read_html(res.text)

    print(len(html_df))
    #刪除原有資料夾內html_df 另存html_df 判斷暫存
    file_operations.delete_files_in_folder('F:/dayWork_ver4/tempGoodinfoText/html_df')
    for i in range(len(html_df)):
        file_operations.writeFile('F:/dayWork_ver4/tempGoodinfoText/html_df/' + str(i) + '.txt', str(html_df[i]))
    
    df = html_df[global_html_df_index]
    
    selected_columns = ['代號', '名稱'] 
    df = df[selected_columns] 

    # 過濾 '代號	名稱' 這一行
    df = df[df['代號'] != '代號']

    # 過濾 '代號' 欄位中只有四位數字的資料
    df = df[df['代號'].str.match(r'^\d{4}$')]

    saveTxt = ''
    for index, row in df.iterrows():
        code = row['代號']
        name = row['名稱']
        print(f'代號: {code}, 名稱: {name}')
        saveTxt += code + ' ' + name + '\n'
    
    if os.path.exists(savepath):
        file_operations.removeOldFile(savepath)

    file_operations.writeFile(savepath, saveTxt)