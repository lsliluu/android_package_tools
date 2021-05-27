#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
Author : dev.hezf
Date   : 2021/5/28 0:35
File   : Email.py
Ver    : v0.0.1
Email  : dev.hezf@139.com
Desc   : 邮件相关类
"""
import yagmail


class Email:

    yag = yagmail.SMTP(
        host='smtp.139.com', user='18959137976@139.com',
        password='ccdb794a0a6899e9b700', smtp_ssl=True)

    def sendmail(self, receivers, title, msg ):
        """
        发送邮件

        Arguments:
            msg {str} -- 邮件正文
            title {str} -- 邮件标题
            receivers {list} -- 邮件接收者，数组
        """
        try:
            self.yag.send(receivers, title, msg)
            print("邮件发送成功")

        except BaseException as e:
            print(e)
            print("Error: 无法发送邮件")

    # def send_mail_with_attachments(self, receivers, title, msg):
    #     """
    #     发送邮件
    #
    #     Arguments:
    #         msg {str} -- 邮件正文
    #         title {str} -- 邮件标题
    #         receivers {list} -- 邮件接收者，数组
    #     """
    #     try:
    #         self.yag.send(receivers, title, msg, './SystemUtils.py')
    #         print("邮件发送成功")
    #
    #     except BaseException as e:
    #         print(e)
    #         print("Error: 无法发送邮件")
