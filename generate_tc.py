import json
import random

from typing import Dict
from collections import namedtuple

from base import *

ALPHABET_CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generate_test_case(pattern_length: int, text_length: int, number_of_matches = 1) -> StringMatchingTestCase:
    pattern = "".join([random.choice(ALPHABET_CHARACTERS) for _ in range(pattern_length)])
    text = [random.choice(ALPHABET_CHARACTERS) for _ in range(text_length - pattern_length * number_of_matches)]
    for _ in range(number_of_matches):
        text.append(pattern)
    random.shuffle(text)
    text = "".join(text)
    return StringMatchingTestCase(pattern=pattern, text=text)

def generate_test_cases(pattern_length: int, text_length: int, number_of_test_cases: int = 1):
    return [generate_test_case(pattern_length, text_length) for _ in range(number_of_test_cases)]

DESIRED_TEST_CASES = [
    # Fixed pattern_length
    {'pattern_length': 10, 'text_length': 10, 'number_of_test_cases': 5},
    {'pattern_length': 10, 'text_length': 100, 'number_of_test_cases': 5},
    {'pattern_length': 10, 'text_length': 1000, 'number_of_test_cases': 5},
    {'pattern_length': 10, 'text_length': 10000, 'number_of_test_cases': 5},
    {'pattern_length': 10, 'text_length': 100000, 'number_of_test_cases': 5},

    # Fixed text_length
    {'pattern_length': 1, 'text_length': 1000, 'number_of_test_cases': 5},
    {'pattern_length': 2, 'text_length': 1000, 'number_of_test_cases': 5},
    {'pattern_length': 4, 'text_length': 1000, 'number_of_test_cases': 5},
    {'pattern_length': 8, 'text_length': 1000, 'number_of_test_cases': 5},
    {'pattern_length': 16, 'text_length': 1000, 'number_of_test_cases': 5},
    {'pattern_length': 32, 'text_length': 1000, 'number_of_test_cases': 5},
    {'pattern_length': 64, 'text_length': 1000, 'number_of_test_cases': 5},
    {'pattern_length': 128, 'text_length': 1000, 'number_of_test_cases': 5},
    {'pattern_length': 256, 'text_length': 1000, 'number_of_test_cases': 5},
    {'pattern_length': 512, 'text_length': 1000, 'number_of_test_cases': 5},
    
    # Fixed pattern_length + text_length
    {'pattern_length': 256, 'text_length': 256, 'number_of_test_cases': 5},
    {'pattern_length': 230, 'text_length': 282, 'number_of_test_cases': 5},
    {'pattern_length': 200, 'text_length': 312, 'number_of_test_cases': 5},
    {'pattern_length': 128, 'text_length': 384, 'number_of_test_cases': 5},
]

def main():
    test_cases = StringMatchingTestCases()

    for group in DESIRED_TEST_CASES:
        result = generate_test_cases(**group)
        for tc in result:
            test_cases.insert_test_case(tc)

    test_cases.dump_to_json_file('input2.json')

if __name__ == '__main__':
    main()
