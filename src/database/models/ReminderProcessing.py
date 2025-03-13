import sqlalchemy as sa 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ExpirationReminderProcessing(Base):
    __tablename__ = 'ExpirationReminderProcessing'
    
    ReminderId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)  
    ContractID = sa.Column(sa.Integer, nullable=False)                       
    IsExpReminderSent = sa.Column(sa.Boolean, nullable=False)                   
    ExpReminderDate = sa.Column(sa.Date, nullable=False)

class StartReminderProcessing(Base):
    __tablename__ = 'StartReminderProcessing'

    ReminderId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)  
    ContractID = sa.Column(sa.Integer, nullable=False)                       
    IsStartReminderSent = sa.Column(sa.Boolean, nullable=False)                   
    StartReminderDate = sa.Column(sa.Date, nullable=False)

class AutoRenewalReminderProcessing(Base):
    __tablename__ = 'AutoRenewalReminderProcessing'

    ReminderId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)  
    ContractID = sa.Column(sa.Integer, nullable=False)                       
    IsAutoReminderSent = sa.Column(sa.Boolean, nullable=False)     
    AutoReminderDate = sa.Column(sa.Date, nullable=False)             