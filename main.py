from src.Infrastructure.services.databaseService import create_tables, select_all_mails
from src.Infrastructure.services.mail_service import send_email
from src.Infrastructure.configs.config import TO_EMAIL, FROM_EMAIL, PSSWD
from src.Infrastructure.services.kafkaService import consume_messages
from src.DomainOrModels.Mail import Email
# from querries.orm import create_tables,insert_mail

topic = 'email'
consume_messages(topic)


# sys.path.insert(1, os.path.join(sys.path[0], '..'))
create_tables()
# test_insert_mails()

email = Email(TO_EMAIL,
              FROM_EMAIL,
              subject="Какая то тема2",
              content="Какой то текст2")
send_email(
   email
)
select_all_mails()
