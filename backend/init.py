from sqlalchemy import Column, String,Integer,VARCHAR,ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() 

class battery(Base):
    __tablename__ = 'battery'
    id = Column(Integer, primary_key=True, nullable=False)
    size = Column(VARCHAR(20))
    powerLeft = Column(Integer, nullable=False)
    status = Column(VARCHAR(20))
    masterSlotId = Column(Integer, ForeignKey('slot.id'))
    curUserId = Column(Integer, ForeignKey('ecycle.id'))

class cabinet(Base):
    __tablename__ = 'cabinet'
    id = Column(Integer, primary_key=True, nullable=False)
    pos = Column(VARCHAR(255))
    type = Column(VARCHAR(255))
    maxSlotNum = Column(Integer)
    companyId = Column(Integer, ForeignKey('company.id'), nullable=False)

class company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(VARCHAR(255))

class ecycle(Base):
    __tablename__ = 'ecycle'
    id = Column(Integer, primary_key=True, nullable=False)
    type = Column(VARCHAR(30))
    parameter = Column(VARCHAR(20))
    ownerId = Column(Integer, ForeignKey('owner.id'), nullable=False)

class owner(Base):
    __tablename__ = 'owner'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(VARCHAR(255))
    phone = Column(VARCHAR(20))
    address = Column(VARCHAR(255))

class slot(Base):
    __tablename__ = 'slot'
    id = Column(Integer, primary_key=True, nullable=False)
    masterId= Column(Integer, ForeignKey('cabinet.id'), nullable=False)
    maxNum = Column(Integer, nullable=False)
    type = Column(VARCHAR(20), nullable=False)


class workorder(Base):
    __tablename__ = 'workorder'
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(VARCHAR(255))
    content = Column(VARCHAR(255))

engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/ecbattery',echo=True)
DBSession = sessionmaker(bind=engine)