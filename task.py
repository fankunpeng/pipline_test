# -*- coding:utf8 -*-
from flask import Flask
import json
app = Flask(__name__)

# test
@app.route('/')
def hello_world():
    return json.dumps('again in master7')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

