import unittest
from pathlib import Path
import os, sys
parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)
from src.clean import *

class CleanTest(unittest.TestCase):
    def setUp(self):
       # You might want to load the fixture files as variables, and test your code against them. Check the fixtures folder.
       self.dr = os.path.dirname(__file__)


    def test_title(self):
       # Just an idea for a test; write your implementation
       print("\n check#1: Posts that don’t have either “title” or “title_text” should be removed.")
       fixture1_path = os.path.join(self.dr, 'fixtures', 'test_1.json')
       with open(fixture1_path) as f:
           obj = f.readline()
           self.fixture_1 = json.loads(obj)
       self.assertEqual(bool(validate_title(self.fixture_1)), False)
       print("\n check#1 ok")
       
    def test_datetime(self):
        print("\n check#2: createdAt dates that don’t pass the ISO datetime standard should be removed.")
        fixture2_path = os.path.join(self.dr, 'fixtures', 'test_2.json')
        with open(fixture2_path) as f:
            obj = f.readline()
            self.fixture_2 = json.loads(obj) 
        self.assertEqual(bool(standardize_time(self.fixture_2)), False)
        print("\n check#2 ok")
        
    def test_validity(self):
        print("\n check#3: Any lines that contain invalid JSON dictionaries should be ignored.")
        fixture3_path = os.path.join(self.dr, 'fixtures', 'test_3.json')
        with open(fixture3_path) as f:
            self.fixture_3 = f.readline()
        self.assertEqual(bool(remove_invalid(self.fixture_3)), False)
        print("\n check#3 ok")
        
    def test_author(self):
        print("\n check#4: Any lines for which author is null, N/A or empty.")
        fixture4_path = os.path.join(self.dr, 'fixtures', 'test_4.json')
        with open(fixture4_path) as f:
             obj = f.readline()
             self.fixture_4 = json.loads(obj)
        self.assertEqual(bool(filter_author(self.fixture_4)), False)
        print("\n check#4 ok")
        
    def test_totalcount(self):
        print("\n check#5: total_count is a string containing a cast-able number, total_count is cast to an int properly.")
        fixture5_path = os.path.join(self.dr, 'fixtures', 'test_5.json')
        with open(fixture5_path) as f:
             obj = f.readline()
             self.fixture_5 = json.loads(obj)
        self.assertEqual(bool(cast_int(self.fixture_5)), False)
        print("\n check#5 ok")
        
    def test_tags(self):
        print("\n check#6: The tags field gets split on spaces when given a tag containing THREE words.")
        fixture6_path = os.path.join(self.dr, 'fixtures', 'test_6.json')
        with open(fixture6_path) as f:
            obj = f.readline()
            self.fixture_6 = json.loads(obj) 
        self.assertEqual(len(tag_split(self.fixture_6)["tags"]), 4)
        print("\n check#6 ok")
        
        
if __name__ == '__main__':
    unittest.main()