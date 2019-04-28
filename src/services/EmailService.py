import smtplib, os

class EmailService:
    def __init__(self, from_, to_, subject, message):
        self.from_ = from_
        self.to_ = to_
        self.subject = subject
        self.message = message
    
    def send_email(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(os.getenv('SENDER_GMAIL'), os.getenv('SENDER_GMAIL_PASSWORD'))
        message = 'Subject: {}\n\n\n{}'.format(self.subject, self.message)
        server.sendmail(self.from_, self.to_, message)