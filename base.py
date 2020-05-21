import json
from collections import namedtuple, defaultdict

class StringMatchingTestCase:
    def __init__(self, pattern: str, text: str):
        self.pattern = pattern
        self.text = text
    
    def __str__(self):
        return str({"pattern": self.pattern, "text": self.text})

    def __eq__(self, another):
        return str(self) == str(another)

    def serialize(obj):
        if isinstance(obj, StringMatchingTestCase):
            return {"pattern": obj.pattern, "text": obj.text}
        return ''

class StringMatchingTestCases:
    def __init__(self, json_file_name: str = None):
        self.test_cases = defaultdict(lambda: defaultdict(list))
        if json_file_name:
            self.load_from_json_file(json_file_name)

    def dump_to_json_file(self, file_name = 'input.json'):
        with open(file_name, 'w') as file:
            json.dump(self.test_cases, file, indent=4, default=StringMatchingTestCase.serialize)
            return True
        return False

    def load_from_json_file(self, file_name = 'input.json'):
        with open(file_name, 'r') as file:
            new_dict = json.load(file)
            for pattern_key in new_dict:
                for text_key in new_dict[pattern_key]:
                    entries = new_dict[pattern_key][text_key]
                    for entry in entries:
                        self.insert(
                            pattern=entry['pattern'],
                            text=entry['text']
                        )

    def get_pattern_key(self, pattern_length: int):
        return f'pattern_length={pattern_length}'

    def get_text_key(self, text_length: int):
        return f'text_length={text_length}'

    def get(self, pattern_length: int, text_length: int):
        pattern_key = self.get_pattern_key(pattern_length)
        text_key = self.get_text_key(text_length)
        if pattern_key not in self.test_cases:
            return []
        if text_key not in self.test_cases[pattern_key]:
            return []
        return self.test_cases[pattern_key][text_key]
    
    def insert_test_case(self, test_case: StringMatchingTestCase):
        pattern_key = self.get_pattern_key(len(test_case.pattern))
        text_key = self.get_text_key(len(test_case.text))
        self.test_cases[pattern_key][text_key].append(test_case)
        return test_case

    def insert(self, pattern: str, text: str):
        test_case = StringMatchingTestCase(pattern=pattern, text=text)
        return self.insert_test_case(test_case)
