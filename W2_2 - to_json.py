import json

def to_json(func):
    def json_f():
        return = json.dumps(func)
    return json_f


@to_json
def printer():
    return "propopopopoopo"

print(printer())