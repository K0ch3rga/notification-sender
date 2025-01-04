class Email:
    def __init__(self,mailTo , mailFrom, subject, content, status='Успешно'):
        self.subject = subject
        self.mailFrom = mailFrom
        self.mailTo = mailTo
        self.content = content
        self.status = status
