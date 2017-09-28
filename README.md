# fix/61

https://github.com/elbuo8/sendgrid-django/issues/61

## Replication
```
$ git clome https://github.com/jayhale/sendgrid-django-61.git@88dcf909d0067f85fc2bf8d9e5244464a434f045

$ pip install -r requirements.txt

$ pytest test.py
```

Results in test failure, the issue exists.

## Resolution
```
$ git clone https://github.com/jayhale/sendgrid-django-61

$ pip install -r requirements.txt

$ export TEST_RECIPIENT='recipient@sink.sendgrid.com'

$ pytest test.py
```

Tests pass, issue resolved by https://github.com/elbuo8/sendgrid-django/pull/70
