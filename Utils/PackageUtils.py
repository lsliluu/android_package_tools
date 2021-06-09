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
    packaging_sign = False
    # 调用发送邮件
    # send_email(status, output)
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
