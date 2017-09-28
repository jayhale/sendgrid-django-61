import os

from django.conf import settings
from django.core.mail import EmailMessage
from django.test import SimpleTestCase as TestCase
from sgbackend import SendGridBackend

settings.configure(SENDGRID_API_KEY=os.environ.get('SENDGRID_API_KEY'))
RECIPIENT=os.environ.get('TEST_RECIPIENT', 'recipient@sink.sendgrid.net')


class Issue61Tests(TestCase):
    def test_attachment_binary_type(self):
        backend = SendGridBackend()

        attachments = (
            ('file.txt', b'File content', 'text/plain'),
        )

        mail = EmailMessage(
            subject='Email subject',
            body='Email body',
            from_email='webmaster@sink.sendgrid.net',
            to=(RECIPIENT, ),
            attachments=attachments,
        )

        # Replicate backend sending
        prepared_mail = backend._build_sg_mail(mail)

        # Send to SendGrid
        response = backend.sg.client.mail.send.post(request_body=prepared_mail)
        self.assertEqual(
            response.status_code,
            202
        )

    def test_attachment_string_type(self):
        backend = SendGridBackend()

        attachments = (
            ('file.txt', 'File content', 'text/plain'),
        )

        mail = EmailMessage(
            subject='Email subject',
            body='Email body',
            from_email='webmaster@sink.sendgrid.net',
            to=(RECIPIENT, ),
            attachments=attachments,
        )

        # Replicate backend sending
        prepared_mail = backend._build_sg_mail(mail)

        # Send to SendGrid
        response = backend.sg.client.mail.send.post(request_body=prepared_mail)
        self.assertEqual(
            response.status_code,
            202
        )

    def test_attachment_image_type(self):
        backend = SendGridBackend()

        with open(os.path.join(os.path.dirname(__file__), 'octocat.png'), 'rb') as f:
            img = f.read()

        attachments = (
            ('octocat.png', img, 'image/png'),
        )
        
        mail = EmailMessage(
            subject='Email subject',
            body='Email body',
            from_email='webmaster@sink.sendgrid.net',
            to=(RECIPIENT, ),
            attachments=attachments,
        )

        # Replicate backend sending
        prepared_mail = backend._build_sg_mail(mail)

        # Send to SendGrid
        response = backend.sg.client.mail.send.post(request_body=prepared_mail)
        self.assertEqual(
            response.status_code,
            202
        )
