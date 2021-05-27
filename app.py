from flask import Flask

from Utils.SystemUtils import auto_email_apk

app = Flask(__name__)


@app.route('/say_hi')
def hello_world():
    return 'hello'


@app.route('/package/feeler')
def package_feeler():
    # 发起编译，执行编译脚本

    # 设置编译状态

    # 返回结果

    pass


@app.route('/email/send')
def send_email():
    auto_email_apk()
    return "end"
    pass


if __name__ == '__main__':
    app.run()

