import unittest, sys, os
import argparse
main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../caplog"))
# Add the directory containing main.py to the Python path
sys.path.append(main_dir)
import main
from datetime import datetime, timedelta


class TestMain(unittest.TestCase):
    def test_time_type(self):
        # Test valid time
        self.assertEqual(main.time_type('2020-01-01T00:00:00'), datetime(2020, 1, 1, 0, 0, 0))
        
        # Test today
        self.assertAlmostEqual(main.time_type('today'), datetime.now(), delta=timedelta(seconds=1))
        
        # Test yesterday
        self.assertAlmostEqual(main.time_type('yesterday'), datetime.now() - timedelta(days=1), delta=timedelta(seconds=1))
        
        # Test invalid time
        with self.assertRaises(argparse.ArgumentTypeError):
            main.time_type('invalid')



        
        # Test invalid time
        with self.assertRaises(argparse.ArgumentTypeError):
            main.time_type('invalid')
            
    def test_scrape_tags(self):
        # Test entry with tags
        self.assertEqual(main.scrape_tags('This is a test entry with @tag1 and @tag2'), '@tag1,@tag2')
        
        # Test entry without tags
        self.assertEqual(main.scrape_tags('This is a test entry without tags'), '')
        

if __name__ == '__main__':
    unittest.main()
