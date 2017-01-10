import json
import os
import argparse

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath,'r',encoding='utf-8') as json_file:
        return json.load(json_file)



def pretty_print_json(data):
    print (json.dumps(data,sort_keys=True,indent=4,
           ensure_ascii=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='...')
    parser.add_argument('path', help='Enter filepath to your JSON')
    arg = parser.parse_args()
    json_content = load_data(arg.path)
pretty_print_json(json_content)
