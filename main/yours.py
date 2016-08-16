from index_advisor.settings import DAEMON_INPUT, DAEMON_OUTPUT
import os
import time
import json

def your_function(text):
    while os.path.exists(DAEMON_INPUT):
        time.sleep(1)
    with open(DAEMON_INPUT, 'w') as f:
        f.write(text)
    while os.path.exists(DAEMON_OUTPUT):
        time.sleep(1)
    with open(DAEMON_OUTPUT, 'r') as f:
        res = f.read()

    res = json.loads(res)

    return res
