import smtplib
import os
from email.message import EmailMessage


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = os.environ['LAUNDRALARM_USER']
    msg['from'] = user
    password = os.environ['LAUNDRALARM_PASSWORD']

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()


if __name__ == '__main__':
    email_alert("Hey", "Hello world", "3478605680@vtext.com")
