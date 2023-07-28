from . import file_operations

#全域變數
global_headers = {'user-agent':  file_operations.get_text('../data_web/headers.txt') }
global_class_time = file_operations.get_text_split('../data_web/時間Class.txt')
global_class_media = file_operations.get_text_split('../data_web/媒體Class.txt')
global_class_title = file_operations.get_text_split('../data_web/標題Class.txt')
global_class_href= file_operations.get_text_split('../data_web/連結Class.txt',)
global_get_dayURL = file_operations.get_text('../data_web/要得網址.txt')
global_get_InvestmentTrust_URL1 = file_operations.get_text('../data_web/投信第一日上市.txt')
global_get_InvestmentTrust_URL2 = file_operations.get_text('../data_web/投信第一日上櫃.txt')
global_get_historicalHigh_URL = file_operations.get_text('../data_web/歷史新高.txt')
global_html_df_index = int(file_operations.get_text('../data_web/html_df_index.txt'))



