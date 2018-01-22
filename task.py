# -*- coding:utf8 -*-
from flask import Flask
import json
app = Flask(__name__)

#
# 第八次构建test
# 第9次构建test
@app.route('/')
def hello_world():
    return json.dumps('in task one 5')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

