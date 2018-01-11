# -*- coding:utf8 -*-
from flask import Flask
import datetime
import json
app = Flask(__name__)

# test
@app.route('/')
def hello_world():
    now = datetime.datetime.now()
    now = json.dumps(now)
    return 'Hello World! {}'.format(now)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

