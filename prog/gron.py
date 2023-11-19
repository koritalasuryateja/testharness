import json
import sys

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

def gron(json_text):
    json_obj = json.loads(json_text)
    return "\n".join(flatten_json(json_obj))

def main():
    if len(sys.argv) > 1:
        json_file = sys.argv[1]
        if json_file == '-':
            json_input = sys.stdin.read()
        else:
            with open(json_file, 'r') as file:
                json_input = file.read()
    else:
        json_input = sys.stdin.read()

    try:
        print(gron(json_input))
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()

