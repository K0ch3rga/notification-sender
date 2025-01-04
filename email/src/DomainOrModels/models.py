from sqlalchemy import (
    TIMESTAMP,
    CheckConstraint,
    Column,
    Enum,
    Index,
    Integer,
    MetaData,
    PrimaryKeyConstraint,
    String,
    Table,
    text,
)

metadata_obj = MetaData()

mails_table = Table(
    "mails",
    metadata_obj,
    Column("Idx", Integer, primary_key=True),
    Column("From", String),
    Column("To", String),
    Column("Subject", String),
    Column("Text", String),
    Column("Status", String),
)

# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from database import Base
# class MailsOrm(Base):
#     __tablename__ = "mails2"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     Fro: Mapped[str]
#
#     # resumes: Mapped[list["ResumesOrm"]] = relationship(
#     #     back_populates="worker",
#     # )
#     #
#     # resumes_parttime: Mapped[list["ResumesOrm"]] = relationship(
#     #     back_populates="worker",
#     #     primaryjoin="and_(WorkersOrm.id == ResumesOrm.worker_id, ResumesOrm.workload == 'parttime')",
#     #     order_by="ResumesOrm.id.desc()",
#     # )