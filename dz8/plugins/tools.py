import json
from .keyboard import  citys

with open('numbers.json', 'r', encoding = 'utf-8') as f:
    data = json.load(f)

def get_region(number):
    for region in data:
        fromre = int(f"7{region['abcdef']}{region['ranges']['from']}")
        to = int(f"7{region['abcdef']}{region['ranges']['to']}")
        if number >= fromre and number <= to:
            for k, v in citys.items():
                if v in region['region']:
                    date = region
                    return k, date