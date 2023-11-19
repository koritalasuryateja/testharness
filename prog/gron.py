import json
import sys
import argparse

def flatten_json(obj, path=''):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from flatten_json(v, f"{path}{k}.")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from flatten_json(v, f"{path}{i}.")
    else:
        path = path.rstrip('.')
        value = json.dumps(obj)
        yield f"{path} = {value}"

def gron(json_text, base_object='json'):
    json_obj = json.loads(json_text)
    return "\n".join([f"{base_object} = {{"]] + list(flatten_json(json_obj, f"{base_object}.")) + ["}"])

def main():
    parser = argparse.ArgumentParser(description='A Python implementation of the gron utility.')
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                        help='A filename to read from. If omitted, will read from STDIN.')
    parser.add_argument('--obj', help='Specify the base object name.')

    args = parser.parse_args()

    if args.file.name == '<stdin>':
        json_input = sys.stdin.read()
    else:
        with open(args.file.name, 'r') as file:
            json_input = file.read()

    try:
        base_object = args.obj if args.obj else 'json'
        print(gron(json_input, base_object))
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()


