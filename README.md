# fix/61

https://github.com/elbuo8/sendgrid-django/issues/61

## Replication attempt
```
$ git clome https://github.com/jayhale/sendgrid-django-61.git

$ pip install -r requirements

$ pytest test.py
```

## Result
```
========================================= test session starts =========================================
platform darwin -- Python 3.6.2, pytest-3.2.2, py-1.4.34, pluggy-0.4.0
rootdir: /Users/james/Projects/sendgrid-django-61, inifile:
collected 3 items                                                                                      

test.py F.F

============================================== FAILURES ===============================================
______________________________ Issue61Tests.test_attachment_binary_type _______________________________

self = <test.Issue61Tests testMethod=test_attachment_binary_type>

    def test_attachment_binary_type(self):
        backend = SendGridBackend()
    
        attachments = (
            ('file.txt', b'File content', 'text/plain'),
        )
    
        mail = EmailMessage(
            subject='Email subject',
            body='Email body',
            from_email='webmaster@sink.sendgrid.net',
            to=('recipient@sink.sendgrid.net', ),
            attachments=attachments,
        )
    
        # Replicate backend sending
>       prepared_mail = backend._build_sg_mail(mail)

test.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
../../projects/sendgrid-django-61/.direnv/python-3.6.2/lib/python3.6/site-packages/sgbackend/mail.py:125: in _build_sg_mail
    base64_attachment = base64.b64encode(attachment[1])
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

s = 'File content', altchars = None

    def b64encode(s, altchars=None):
        """Encode the bytes-like object s using Base64 and return a bytes object.
    
        Optional altchars should be a byte string of length 2 which specifies an
        alternative alphabet for the '+' and '/' characters.  This allows an
        application to e.g. generate url or filesystem safe Base64 strings.
        """
>       encoded = binascii.b2a_base64(s, newline=False)
E       TypeError: a bytes-like object is required, not 'str'

../../projects/sendgrid-django-61/.direnv/python-3.6.2/lib/python3.6/base64.py:58: TypeError
______________________________ Issue61Tests.test_attachment_string_type _______________________________

self = <test.Issue61Tests testMethod=test_attachment_string_type>

    def test_attachment_string_type(self):
        backend = SendGridBackend()
    
        attachments = (
            ('file.txt', 'File content', 'text/plain'),
        )
    
        mail = EmailMessage(
            subject='Email subject',
            body='Email body',
            from_email='webmaster@sink.sendgrid.net',
            to=('recipient@sink.sendgrid.net', ),
            attachments=attachments,
        )
    
        # Replicate backend sending
>       prepared_mail = backend._build_sg_mail(mail)

test.py:53: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
../../projects/sendgrid-django-61/.direnv/python-3.6.2/lib/python3.6/site-packages/sgbackend/mail.py:125: in _build_sg_mail
    base64_attachment = base64.b64encode(attachment[1])
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

s = 'File content', altchars = None

    def b64encode(s, altchars=None):
        """Encode the bytes-like object s using Base64 and return a bytes object.
    
        Optional altchars should be a byte string of length 2 which specifies an
        alternative alphabet for the '+' and '/' characters.  This allows an
        application to e.g. generate url or filesystem safe Base64 strings.
        """
>       encoded = binascii.b2a_base64(s, newline=False)
E       TypeError: a bytes-like object is required, not 'str'

../../projects/sendgrid-django-61/.direnv/python-3.6.2/lib/python3.6/base64.py:58: TypeError
================================= 2 failed, 1 passed in 1.06 seconds ==================================
```

## Conclusion
Tests fail. Issue exists.