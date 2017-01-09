import json


def load_data(filepath):
    with open(filepath,'r',encoding='utf-8') as json_to_parse:
        json_to_parse = json.loads(json_to_parse.read())
    return json_to_parse


def pretty_print_json(data):
    data = json.dumps(data,sort_keys=True,indent=4,ensure_ascii=False)
    return data

if __name__ == '__main__':
    json_content = load_data(input("Enter json-file path: "))
    print ('Pretty print: \n', pretty_print_json(json_content))
