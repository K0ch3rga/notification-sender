import os
import sys

from src.Infrastructure.services.databaseService import create_tables, select_all_mails
from src.Infrastructure.services.mail_service import send_email
from src.Infrastructure.configs.config import TO_EMAIL, FROM_EMAIL, PSSWD
from src.Infrastructure.services.kafkaService import consume_messages
from src.DomainOrModels.Mail import Email
# from querries.orm import create_tables,insert_mail
from src.Infrastructure.services.kafkaService import consumer

sys.path.insert(1, os.path.join(sys.path[0], '..'))
topic = 'email'


while True:
    try:
        msg = consume_messages(topic)
        create_tables()
        email = Email(msg["address"],
                      FROM_EMAIL,
                      msg["title"],
                      msg["message"])
        send_email(
            email
        )
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

