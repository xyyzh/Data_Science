import unittest
from pathlib import Path
import os, sys, json
parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)
from src.compile_word_counts import *
from src.compute_pony_lang import *

class TasksTest(unittest.TestCase):
    def setUp(self):
        dir = os.path.dirname(__file__)
        self.mock_dialog = os.path.join(dir, 'fixtures', 'mock_dialog.csv')
        self.true_word_counts = os.path.join(dir, 'fixtures', 'word_counts.true.json')
        self.true_tf_idfs = os.path.join(dir, 'fixtures', 'tf_idfs.true.json')
        
        

    def test_task1(self):
        # use  self.mock_dialog and self.true_word_counts; REMOVE self.assertTrue(True) and write your own assertion, i.e. self.assertEquals(...)
        print("Test for task 1")
        # will ignore the num words >=5 condition
        with open(self.true_word_counts) as f:
            self.assertEqual(get_all_count_test(self.mock_dialog), json.load(f))
        print("Task 1 OK.")

    def test_task2(self):
        # use self.true_word_counts self.true_tf_idfs; REMOVE self.assertTrue(True) and write your own assertion, i.e. self.assertEquals(...)
        print("Test for task 2")
        with open(self.true_tf_idfs) as f:
            self.assertEqual(get_output(self.true_word_counts, 2), json.loads(f.read()))
        print("Task 2 OK.")
        
    
if __name__ == '__main__':
    unittest.main()