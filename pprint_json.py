import json


def load_data(filepath):
    with open(filepath,'r',encoding='utf-8') as json_to_parse:
        return json.load(json_to_parse)



def pretty_print_json(data):
    print (json.dumps(data,sort_keys=True,indent=4,ensure_ascii=False))


if __name__ == '__main__':
    while True:
        filepath = input('Enter filepath for json file : ')
        if not filepath:
            print('Try again!')
        else:
            try:
                pretty_print_json(load_data(filepath))
                break
            except FileNotFoundError as e:
                print("Try better : %s" % (e.args[1]))


