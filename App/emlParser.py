def emailParser(path):
    from email import policy
    from email.parser import BytesParser

    msg = BytesParser(policy=policy.default).parse(path)

    subject = msg['subject']

    text_content = msg.get_body(preferencelist=('plain')).get_content()

    return subject + text_content