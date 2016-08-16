from index_assessor.settings import DAEMON_INPUT, DAEMON_OUTPUT
import os
import time
import json

def process(data):
    return [{'text': 'first_item', 'id': 1}, {'text': 'second_item', 'id': 2}, {'text': 'third_item', 'id': 3}]

while True
    if os.path.exists(DAEMON_INPUT):
        with open(DAEMON_INPUT, 'r') as f:
            data = f.read()
        os.remove(DAEMON_INPUT)
        result = process(data)
        while os.path.exists(DAEMON_OUTPUT):
            time.sleep(1)
        with open(DAEMON_OUTPUT, 'w') as f:
            f.write(json.dumps(result))
    else:
        time.sleep(1)
