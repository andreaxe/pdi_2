from sqlalchemy import Integer, ForeignKey, String, Column, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData

from main import username, password, database, hostname

metadata = MetaData()
engine = create_engine("mysql+pymysql://{}:{}@{}/{}".format(username, password, hostname, database))
Base = declarative_base()
metadata.bind = engine

metadata = MetaData()

dim = Table('dim', metadata,
    Column('id_dim',        Integer,    primary_key=True),
    Column('itempt_dim',    String(160), nullable=False),
    Column('itemen_dim',    String(160), key='email'),
    Column('desc_dim',      String(150), nullable=False),
    Column('wgt_dim',       Integer, nullable=False),
    Column('pri_dim',       Integer, nullable=False),
    Column('aut_dim',       String(150), nullable=False)
)

rdim = Table('rdim', metadata,
    Column('iddim_rdim',    Integer, ForeignKey("dim.id_dim"), primary_key=True),
    Column('iddimblg_rdim', Integer, ForeignKey("dim.id_dim"), primary_key=True),
)

# Clean database remove all data if exists and re-create tables
metadata.drop_all(engine)
metadata.create_all(engine)
