import smtpd
import asyncore

#sa https://pymotw.com/2/smtpd/

class CustomSMTPServer(smtpd.SMTPServer):
    
    def process_message(self, peer, mailfrom, rcpttos, data):
        print 'Primanje poruke sa    :', peer
        print 'Poruka adresirana sa  :', mailfrom
        print 'Poruka adresirana za  :', rcpttos
        print 'Duzina poruke         :', len(data)
        return

server = CustomSMTPServer(('127.0.0.1', 1025), None)

asyncore.loop()