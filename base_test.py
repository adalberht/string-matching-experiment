import unittest
import os
from base import StringMatchingTestCases, StringMatchingTestCase

class TestStringMatchingTestCasesClass(unittest.TestCase):
    def test_load_and_dump(self):
        test_cases = StringMatchingTestCases()
        test_cases.insert(pattern='abcd', text='abc')
        test_cases.insert(pattern='abbb', text='hahahaha')


        test_cases.dump_to_json_file('test_dump.json')

        new_test_case = StringMatchingTestCases()
        new_test_case.load_from_json_file('test_dump.json')

        self.assertEqual(
            dict(test_cases.test_cases),
            dict(new_test_case.test_cases)
        )
        os.remove("test_dump.json")

if __name__ == '__main__':
    unittest.main()
