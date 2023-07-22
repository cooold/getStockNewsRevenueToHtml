import unittest
import datetime
from unittest.mock import patch
import sys 
sys.path.append("..") 
from my_package import date_calculator

class TestIsWeekdayOrHoliday(unittest.TestCase):
    
    #是平日還是假日
    def test_is_weekday_or_holiday(self):
        current_date = datetime.datetime.now().date()
        weekday = current_date.weekday()
        
        result = date_calculator.is_weekday_or_holiday()
        if (weekday < 5):
            self.assertEqual(result, "平日")
        else:
            self.assertEqual(result, "假日")
    
    '''
    #得出正確格式
    @patch('datetime.date')
    def test_get_previous_YearMonth(self, mock_date):
        mock_date.today.return_value = datetime.date(2023, 6, 1)
        result = date_calculator.get_previous_YearMonth()
        self.assertEqual(result, ['112_4','112_3','112_2'])
    '''
    


if __name__ == '__main__':
    unittest.main()