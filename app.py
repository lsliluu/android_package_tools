from threading import Thread

from flask import Flask

from Utils.PackageUtils import get_packaging_sign

app = Flask(__name__)


@app.route('/say_hi')
def hello_world():
    return 'hello'


@app.route('/package/feeler')
def package_feeler():
    # result_dict 返回的参数
    result_dict = {}

    if not get_packaging_sign():
        # 如果没有在打包，则：

        # 发起编译，执行编译脚本，传递收件人等参数
        from Utils.PackageUtils import execute_shell
        # 创建线程，不指定参数
        thread = Thread(target=execute_shell)
        # 启动线程
        thread.start()

        result_dict['code'] = 0
        result_dict['msg'] = "打包服务已启动，稍候请注意查收邮件"
    else:
        # 如果正在打包就返回“占用异常"
        result_dict['code'] = -1
        result_dict['msg'] = "打包服务占用中，请稍候再试"
        pass

    # 返回结果
    print(result_dict)
    return result_dict
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

