from flask import g


# 是否正在打包的标识
packaging_sign = False


def get_packaging_sign():
    return packaging_sign


def execute_doc_shell():
    pass


def execute_shell():
    global packaging_sign
    # 设置编译状态
    packaging_sign = True
    print(packaging_sign)
    # 执行脚本
    import subprocess
    (status, output) = subprocess.getstatusoutput('sh /home/hzf/workspace/auto_package_dir/auto_package_cmhnsjjf.sh')
    print(status)
    print(output)
    # 调用发送邮件
    send_email(status, output)
    # TODO 在邮件发送后才能继续下一轮编译，此处可以优化
    packaging_sign = False
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

    from Utils.Email import Email
    email = Email()
    email.send_mail_with_attachments(['dev.hezf@139.com', 'hezf@newland.com.cn'], '关于Android编译apk', '您好：\n此邮件是发起Android编译后自动发送的通知邮件，请注意查看编译进展，请勿回复。\n祝工作顺利')
    pass
