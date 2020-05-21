import json
from typing import Dict

from base import *

def run_experiment(test_cases: StringMatchingTestCases, pattern_key: str, text_key: str):
    print(f'Running Experiment for {pattern_key} and {text_key}')
    for tc in test_cases.test_cases[pattern_key][text_key]:
        print(tc)

def main():
    test_cases = StringMatchingTestCases('input.json')
    for pattern_len in test_cases.test_cases:
        for text_len in test_cases.test_cases[pattern_len]:
            run_experiment()

if __name__ == '__main__':
    main()