import smtplib
import ssl
import platform
import socket
import colorama
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from concurrent.futures import ThreadPoolExecutor
colorama.init()

def clear():
	if platform == "linux":
		os.system('clear')
	else:
		os.system('cls')


class SMTPChecker:
	def __init__(self):
		self.banner = """\x1b[34;1m███████╗███╗   ███╗████████╗██████╗  \x1b[31;1m    ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗\n\x1b[34;1m██╔════╝████╗ ████║╚══██╔══╝██╔══██╗ \x1b[31;1m   ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝\n\x1b[34;1m███████╗██╔████╔██║   ██║   ██████╔╝ \x1b[31;1m   ██║     ███████║█████╗  ██║     █████╔╝ \n\x1b[34;1m╚════██║██║╚██╔╝██║   ██║   ██╔═══╝  \x1b[31;1m   ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ \n\x1b[34;1m███████║██║ ╚═╝ ██║   ██║   ██║      \x1b[31;1m   ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗\n\x1b[34;1m╚══════╝╚═╝     ╚═╝   ╚═╝   ╚═╝      \x1b[31;1m    ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝\n\n\n\t\t\t\x1b[34m    | \x1b[37m@scarlettaowner \x1b[34m| \x1b[37mv1.3  \x1b[34m|\n\t\t\t\x1b[34m    |    \x1b[37mSCARLETTA    \x1b[34m| \x1b[37mTOOLS \x1b[34m|\n\x1b[0m\n        """
		self.smtp = ""
		self.receiver = ""
		self.threads = 5
		self.context = ssl._create_unverified_context()
	def clear(self):
		os.system('cls' if os.name == 'nt' else 'clear')

	def save_valid(self, i):
		with open('good.txt', 'a+') as file:
			file.write(i+"\n")

	def create_message(self, smtp):
		host, port, user, pssw = smtp.split('|')
		return f"""<!DOCTYPE html><html><head></head><body><center><h1>📧 SCARLETTA SMTP CHECKER 📧</h1> <br><font color="00c4ff"><h2>SMTP Works</h2></font><br><br></center><font color="black" size="5"><font color="red">Host => </font>{host}<br></font><font color="black" size="5"><font color="red">Port => </font>{port}<br></font><font color="black" size="5"><font color="red">User => </font>{user}<br></font><font color="black" size="5"><font color="red">Pass => </font>{pssw}<br></font><font color="black" size="5"><font color="red">Mailer Format =></font>{host}|{port}|{user}|{pssw}<br></font><br><br><br><center><a href="https://t.me/tutorials_zone"><button style="background-color: #4CAF50; border: none; color: white; padding: 14px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer">JOIN CHANNEL</button></a><h6>Made By @f4c3r100</h6><br></center></body></html>\r\n""".format(host=host, port=port, user=user, pssw=pssw, smtp=smtp)

	def send_email(self, smtp, receiver):
		host, port, user, pssw = smtp.split('|')
		message = self.create_message(smtp)

		msg = MIMEMultipart('alternative')
		msg['Subject'] = "📧 SMTP CHECKER | SCARLETTA 📧"
		msg['From'] = user
		msg['To'] = receiver
		eee = MIMEText(message, 'html')
		msg.attach(eee)
		try:
			print(f"\n\x1b[37m[\x1b[33m-\x1b[37m] Attempting to connect to SMTP server: \x1b[33m{host}\x1b[37m:\x1b[33m{port} with user \x1b[33m{user}\x1b[0m")
			if port == "465":
				smtp_server = smtplib.SMTP_SSL(host, port, context=self.context)
			else:
				smtp_server = smtplib.SMTP(host, port)
				smtp_server.starttls(context=self.context)
			smtp_server.login(user, pssw)
			smtp_server.sendmail(msg['From'], msg['To'], msg.as_string())
			smtp_server.quit()
			print(f"\x1b[37m[\x1b[32m*\x1b[37m] \x1b[32mEmail successfully sent to {receiver} using {host}:{port}\x1b[0m")
			self.save_valid(smtp)
		except smtplib.SMTPAuthenticationError:
			print(f"\x1b[37m[\x1b[31m!\x1b[37m] \x1b[31mAuthentication failed for {user} on {host}:{port}\x1b[0m")
		except smtplib.SMTPConnectError:
			print(f"\x1b[37m[\x1b[31m!\x1b[37m] \x1b[31mFailed to connect to {host}:{port}\x1b[0m")
		except smtplib.SMTPException as e:
			print(f"\x1b[37m[\x1b[31m!\x1b[37m] \x1b[31mSMTP error occurred: {e}\x1b[0m")
		except socket.gaierror as e:
			print(f"\x1b[37m[\x1b[31m!\x1b[37m] \x1b[31mSocker error occurred: {e}\x1b[0m")
		except Exception as e:
			print(f"\x1b[37m[\x1b[31m!\x1b[37m] \x1b[31mOther error occurred: {e}\x1b[0m")
	def main(self):
		self.clear()
		print(self.banner)
		self.smtps = input("\x1b[37m[\x1b[36mSCARLETTA \x1b[37m| \x1b[36mSMTP\x1b[37m] Input your SMTPs \x1b[37m(\x1b[35mf.e smtp.txt\x1b[37m): ")
		self.receiver = input("\x1b[37m[\x1b[36mSCARLETTA \x1b[37m| \x1b[36mSMTP\x1b[37m] Your Email \x1b[37m(\x1b[35mf.e test@gmx.de\x1b[37m): ")
		threads = input("\x1b[37m[\x1b[36mSCARLETTA \x1b[37m| \x1b[36mSMTP\x1b[37m] Input your Threads \x1b[37m(\x1b[35mf.e 10\x1b[37m): ")
		
		if os.path.exists(self.smtps):
			with open(self.smtps, "r") as smtp_file:
				smtp_list = smtp_file.readlines()
			if int(threads) >= len(smtp_list):
				self.threads = len(smtp_list)
			elif int(threads) >= 30:
				self.threads = 30
			else:
				self.threads = threads
				with ThreadPoolExecutor(max_workers=int(self.threads)) as executor:
					futures = [executor.submit(self.send_email, smtp.strip(), self.receiver) for smtp in smtp_list]
		else:
			print(f"\x1b[37m[\x1b[31m!\x1b[37m] \x1b[31mError, path {self.smtps} does not exists.\x1b[0m")


if __name__ == '__main__':
	checker = SMTPChecker()
	checker.main()