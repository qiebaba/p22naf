import smtplib
from email.mime.text import MIMEText
from email.header import Header

class SendEmail():
	def __init__(self):
		# 第三方 SMTP 服务
		self.mail_host = "smtp.qq.com"  # 设置服务器
		self.mail_user = "375578837"  # 用户名
		self.mail_pass = "jaop lnad npzg bgjf"  # 口令
		   # enwfdyukrrctbigc

	def send_mail(self):
		sender = '375578837@qq.com'
		receivers = ['jinbiao_yin@crfchina.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

		message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
		message['From'] = Header("test", 'utf-8')
		message['To'] = Header("测试", 'utf-8')

		subject = 'Python SMTP 邮件测试'
		message['Subject'] = Header(subject, 'utf-8')

		try:
			smtpObj = smtplib.SMTP()
			smtpObj.connect(self.mail_host, 465)  # 25 为 SMTP 端口号
			smtpObj.login(self.mail_user, self.mail_pass)
			smtpObj.sendmail(sender, receivers, message.as_string())
			print("邮件发送成功")
		except smtplib.SMTPException:
			print("Error: 无法发送邮件")


if __name__ == '__main__':
	sen = SendEmail()
	sen.send_mail()