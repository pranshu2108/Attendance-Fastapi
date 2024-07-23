from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy import Column, Integer, String , ForeignKey
from sqlalchemy import DateTime
from datetime import datetime

class employees(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    emp = relationship("attendance", back_populates="attendance")

class attendance(Base):
    __tablename__ = 'attendance'
    id = Column(Integer, primary_key=True,index=True)
    emp_id = Column(Integer, ForeignKey('employees.id'))
    time = Column(DateTime, default=datetime.utcnow)
    status = Column(String)

    attendance = relationship("employees", back_populates="emp")
    
