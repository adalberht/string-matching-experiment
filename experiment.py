import json
from typing import Dict

from base import *
import time

from algorithms.kmp import kmp_match
from algorithms.z_algorithm import z_match
from algorithms.rabin_karp import rabin_karp_match

def measure_time(func, reps = 5):
    start = time.time()
    for i in range(reps):
        func()
    end = time.time()
    average_spent_time = (end - start) / reps
    return average_spent_time

def run_experiment_with(algo, test_cases):
    total_time = 0
    for tc in test_cases:
        wrapped_func = lambda: algo(tc.pattern, tc.text)
        total_time += measure_time(wrapped_func)
    average_time = total_time / len(test_cases)
    print (f"{algo.__name__} - Average time: {average_time * 1000} ms")

def run_experiment(test_cases: StringMatchingTestCases, pattern_key: str, text_key: str):
    print(f'Running Experiment for {pattern_key} and {text_key}')
    tcs = test_cases.test_cases[pattern_key][text_key]
    run_experiment_with(kmp_match, tcs)
    run_experiment_with(z_match, tcs)
    run_experiment_with(rabin_karp_match, tcs)

    print(f'--------------------------------------\n')



def main():
    test_cases = StringMatchingTestCases('input.json')
    for pattern_len in test_cases.test_cases:
        for text_len in test_cases.test_cases[pattern_len]:
            run_experiment(test_cases, pattern_len, text_len)

if __name__ == '__main__':
    main()