import datetime
from typing import List

import pandas as pd

def is_weekday(Date) -> bool:
  currentDateTime = datetime.datetime.now()
  year = currentDateTime.date().strftime("%Y")
  setDate = year + '-' + Date[0:2] + '-' + Date[2:]
  temp = pd.Timestamp(setDate)
  DayName = temp.day_name()
  print(Date)
  print("今天是"+DayName)
  if DayName=='Saturday' or DayName=='Sunday':
    print('是假日')
    return False
  else:
    print('是平日')
    return True

def get_previous_YearMonth() -> List[str]:
    today = datetime.date.today()
    YearMonthList = []

    for i in range(3):
        if today.day <= 15:
            # 6月10日 5月還沒出要取 4月 3月 2月
            month = today.month - (i + 2)
            year = today.year
            if month <= 0:
                month += 12
                year -= 1
        else:
            # 6月20日 5月 4月 3月
            month = today.month - (i + 1)
            year = today.year
            if month <= 0:
                month += 12
                year -= 1
                
        #西元轉民國年份後放入
        ROC_year = int(year) - 1911        
        YearMonthList.append((str(ROC_year) + '_' + str(month)))

    return YearMonthList
