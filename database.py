from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData

DATABASE_URL = "mysql+pymysql://user:ahmed@127.0.0.1:3306/assignment-5"

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

metadata = MetaData()

users_table = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(50), nullable=False, unique=True),
    Column('email', String(100), nullable=False, unique=True),
    Column('age', Integer)
)
