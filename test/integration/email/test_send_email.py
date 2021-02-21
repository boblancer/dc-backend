import unittest
import easyimap
import sys
sys.path.append('/dc-backend/email')
import server

class TestSendEmail(unittest.TestCase):

    def test_send_email(self, email='toonkunggs@gmail.com', password='gvtmqzqtwhwhdpjh'):
        imapper = easyimap.connect('imap.gmail.com', email, password)
        senders = []
        titles = []
        for mail_id in imapper.listids(limit = 20):
            mail = imapper.mail(mail_id)
            senders.append(mail.from_addr)
            titles.append(mail.title)
        imapper.quit()
        self.assertTrue('toonkunggs@gmail.com' in senders and 'Your fortune cookie today' in titles)

if __name__ == '__main__':
    unittest.main()





