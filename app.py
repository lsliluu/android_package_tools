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
    # auto_email_apk()
    from Utils.Email import Email
    email = Email()
    email.sendmail(['dev.hezf@139.com', 'hezf@newland.com.cn'], '关于Android编译apk', '您好：\n此邮件是发起Android编译后自动发送的通知邮件，请注意查看编译进展，请勿回复。\n祝工作顺利')
    return "end"
    pass


if __name__ == '__main__':
    app.run()

