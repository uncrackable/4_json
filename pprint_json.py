import json
import os
import argparse


def load_data(filepath):
    if not os.path.exists(filepath):
        return 'No such file in directory'
    with open(filepath, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def pretty_print_json(data):
    return json.dumps(data, sort_keys=True, indent=4,
                      ensure_ascii=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='JSON pretty print script')
    parser.add_argument('-f', '--file', required='True',
                        help='filepath to your JSON')
    args = parser.parse_args()
    json_content = load_data(args.file)
    print(pretty_print_json(json_content))
