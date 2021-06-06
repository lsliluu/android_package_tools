from flask import g


def execute_doc_shell():
    pass


def execute_shell():
    # 执行脚本
    from pip._internal import commands
    (status, output) = commands.getstatusoutput('sh hello.sh')
    # 调用发送邮件
    send_email(status, output)
    pass


def send_email(status, output):
    if status == 0:
        # 获取成功邮件模板

        # 获取apk附件
        pass
    else:
        # 获取失败邮件模板

        # 将output输出成日志文件，放到邮件附件中发送

        pass
    # 释放全局变量
    g.packaging_sign = False
    pass
