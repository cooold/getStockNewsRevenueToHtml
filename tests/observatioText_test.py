import unittest

def read_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

class TxtFileTestCase(unittest.TestCase):

    #每一行三個資料 1101 台xx 櫃
    def test_txt_file_fields(self):
        file_path = 'F:/dayWork_ver4/observation.txt'
        
        lines = read_txt_file(file_path)
        
        for line in lines:
            fields = line.split()
            self.assertEqual(len(fields), 3, f"Line '{line}' does not have three fields")
    
    #第一個 為四位數字
    def test_first_element_is_four_digit(self):
        file_path = 'F:/dayWork_ver4/observation.txt'
        
        lines = read_txt_file(file_path)
        
        for line in lines:
            first_element = line.split()[0]
            self.assertTrue(first_element.isdigit() and len(first_element) == 4, f"First element '{first_element}' in line '{line}' is not a four-digit number")
    
    #最後一個為上市或上櫃
    def test_last_element_is_correct(self):
        file_path = 'F:/dayWork_ver4/observation.txt'

        lines = read_txt_file(file_path)

        for line in lines:
            last_element = line.split()[2]
            self.assertTrue(last_element == "櫃" or last_element == "市", f"Second element '{last_element}' in line '{line}' is not '櫃' or '市'")
    

if __name__ == '__main__':
    unittest.main()
