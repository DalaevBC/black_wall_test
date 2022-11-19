from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello():
    co = ""
    for i in range(10**4):
        co = f'{co}{i}'
    return f'{os.environ["APP"]}  {len(co)}'


@app.route("/health", methods=['POST'])
def health():
    return "True"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
