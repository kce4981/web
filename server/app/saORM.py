import sqlalchemy as sa
import sqlalchemy.orm as orm
engine = sa.create_engine('sqlite3:///:memory:', echo=True)

Base = orm.declarative_base()
class User(Base):
    from sqlalchemy import Column, Integer, String

    __tableName__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    pass