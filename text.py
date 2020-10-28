import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
	msg = EmailMessage()
	msg.set_content(body)
	msg['subject'] = subject
	msg['to'] = to

	user = "laundralarmalert@gmail.com"
	msg['from'] = user
	password = "nqyyglqcbyqeaohq"

	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(user, password)
	server.send_message(msg)
	
	server.quit()


if _name_ == '__main__':
	email_alert("Hey", "Hello world", "3478605680@vtext.com")
