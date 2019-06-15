import smtplib
import email.utils
from email.mime.text import MIMEText

# sa https://pymotw.com/2/smtpd/
msg = MIMEText('Ovo je tijelo poruke.')
msg['Subject'] = 'Testna poruka'
msg['To'] = email.utils.formataddr(('Recipient', 'tino@andrijic.com'))
msg['From'] = email.utils.formataddr(('Author', 'tino@totohost.hr'))

server = smtplib.SMTP('127.0.0.1', 1025)
server.set_debuglevel(True) 
try:
    server.sendmail('tino@andrijic.com', ['tino@totohost.hr'], msg.as_string())
finally:
    server.quit()