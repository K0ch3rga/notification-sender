from sqlalchemy import insert, select, delete
from src.Infrastructure.Database.database import sync_engine
# from models import Workload, metadata_obj, resumes_table, workers_table
from src.DomainOrModels.models import metadata_obj, mails_table
def create_tables():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    sync_engine.echo = True

def insert_mail(email):
    with sync_engine.connect() as conn:

        stmt = insert(mails_table).values(
            [
                {"From": email.mailFrom, "To": email.mailTo,"Subject": email.subject, "Text": email.content, "Status": email.status},
            ]
        )
        conn.execute(stmt)
        conn.commit()
def select_all_mails():
    with sync_engine.connect() as conn:
        query = select(mails_table) # SELECT * FROM workers
        result = conn.execute(query)
        mails = result.all()
        print(f"{mails=}")

def delete_all_mails():
    with sync_engine.connect() as conn:
        stmt = delete(mails_table)
        conn.execute(stmt)
        conn.commit()
        print("All mails deleted")