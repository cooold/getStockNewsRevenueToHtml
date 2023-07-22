import os
import json
from typing import List

def get_text(path: str) -> str:
    temp = ''
    if os.path.exists(path):
       with open(path, 'r' ,encoding="utf-8") as file:
          temp = file.read()
    else:
        print(path + "檔案不存在")
        input("按下任意鍵表示了解此情況......")
    return temp

def get_text_split(path: str) -> List[str]:
    if os.path.exists(path):
        with open(path, 'r' ,encoding="utf-8") as file:
          temp = file.read()
          temp = temp.split()
    else:
        print(path + "檔案不存在")
        input("按下任意鍵表示了解此情況......")
    return temp

def get_textLines(path: str) -> List[str]:
    if os.path.exists(path):
        with open(path, 'r' ,encoding="utf-8") as file:
          temp = file.readlines()
    else:
        print(path + "檔案不存在")
        input("按下任意鍵表示了解此情況......")
    return temp

def removeOldFile(path: str) -> None:
    if os.path.isfile(path):
        os.remove(path)
        print(path + "已刪除")
    else:
       print("找不到" + path)
       input("按下任意鍵表示了解此情況......")

def makedirs(path: str) -> None:
    if os.path.isdir(path):
        print(path+'資料夾已經存在')
    else:
      os.makedirs(path)
      print(path+'資料夾建立成功')
      input("按下任意鍵表示了解此情況......")

def writeFile(path,context: str) -> None:
    with open(path,"a",encoding="utf-8") as file:
        file.write(str(context))
    print(path + " 已寫入")

def dictToJson(saveStockListToJson,savepath):

    if os.path.exists(savepath + '.json'):
        removeOldFile(savepath + '.json')
    with open(savepath + '.json', 'w') as fp:
        json.dump(saveStockListToJson, fp)
    print(savepath + '.json 成功儲存')

def CompareHistoricalHighText(file_a, file_b, file_c):
    # 讀取 A.txt
    with open(file_a, 'r', encoding='utf-8') as f_a:
        lines_a = set(f_a.readlines())

    # 讀取 B.txt
    with open(file_b, 'r', encoding='utf-8') as f_b:
        lines_b = set(f_b.readlines())

    # 找出新增的股票
    diff_lines = lines_a - lines_b
    print('今日歷史新高新增')
    print(diff_lines)

    # 將新增的股票加入 B.txt
    with open(file_b, 'a', encoding='utf-8') as f_b:
        for line in diff_lines:
            f_b.write(line)

    # 將不同的新增的股票保存到 C.txt
    with open(file_c, 'a', encoding='utf-8') as f_c:
        for line in diff_lines:
            f_c.write(line)
    
    #排序
    sort_txt_by_first_value(file_b)
    sort_txt_by_first_value(file_c)

#排序diff過的順序
def sort_txt_by_first_value(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()

    # 按股票代號排序
    sorted_lines = sorted(lines, key=lambda line: int(line.split()[0]))

    if os.path.exists(file_path):
        removeOldFile(file_path)

    with open(file_path, 'a', encoding='utf-8') as sorted_file:
        for line in sorted_lines:
            sorted_file.write(line + '\n')

    print(f"已經排序：{file_path}")