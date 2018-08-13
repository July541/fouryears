from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

class EmailSender:
    def __init__(self, from_addr=None, password=None, to_addr=None,
                smtp_server=None, from_name=None, to_name=None, subject=None, msg=''):
        self.from_addr = from_addr
        self.password = password
        self.to_addr = to_addr
        self.smtp_server = smtp_server
        self.from_name = from_name
        self.to_name = to_name
        self.subject = subject

        self.msg = msg

    def _fromat_addr(self, name, addr):
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def send(self):
        # todo: add empty check

        self.msg = MIMEText(self.msg, _charset='utf-8')
        self.msg['From'] = self._fromat_addr(self.from_name, self.from_addr)
        self.msg['To'] = self._fromat_addr(self.to_name, self.to_addr)
        self.msg['Subject'] = Header(self.subject, 'utf-8').encode()

        server = smtplib.SMTP(self.smtp_server, 25)
        
        server.set_debuglevel(1)

        server.login(self.from_addr, self.password)
        server.sendmail(self.from_addr, [self.to_addr], self.msg.as_string())
        server.quit()