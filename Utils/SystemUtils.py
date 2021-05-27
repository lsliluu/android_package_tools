def get_system_operating():
    pass


def auto_email_apk():
    print("abc")

    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header

    # 第三方 SMTP 服务
    mail_host = "smtp.139.com"  # 设置服务器
    mail_user = "18959137976@139.com"  # 用户名
    mail_pass = "ccdb794a0a6899e9b700"  # 口令

    sender = 'robot_hzf@139.com'
    receivers = ["hezf@newland.com.cn", "dev.hezf@139.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText('这是一封自动发送的测试软件，请勿回复。', 'plain', 'utf-8')

    message['From'] = Header("菜鸟教程", 'utf-8')
    message['To'] = Header("测试", 'utf-8')

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print
        "邮件发送成功"
    except smtplib.SMTPException:
        print
        "Error: 无法发送邮件"

    pass
