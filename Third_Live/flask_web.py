from flask import Flask

app = Flask(__name__)


@app.route("/index")
def index():
    return "欢迎使用xxx系统"


@app.route("/login")
def login():
    return "欢迎登录"


if __name__ == '__main__':
    app.run()

