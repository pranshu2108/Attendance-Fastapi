from fastapi import FastAPI,HTTPException,Depends,status
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine
from models import *
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime
from typing import List
# import json

import models
from models import *

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


class AttendanceBase(BaseModel):
    emp_id: int
    name: str
    time: datetime
    status: str

class employees(BaseModel):
    id: int
    name: str
    email: str


class attendance(BaseModel):
    id :int
    emp_id: int
    time :datetime
    status: str   


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    


db = SessionLocal()

@app.post('/addemp',response_model=employees,status_code=status.HTTP_201_CREATED)
def add_Emp(emp:employees):
    newPerson = models.employees(
        id=emp.id,
        name= emp.name,
        email = emp.email,
    )

    find_person = db.query(models.employees).filter(models.employees.id==emp.id).first()

    if find_person is not None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="employees with this id already exist")


    db.add(newPerson)
    db.commit()

    return newPerson


@app.post('/addattendance',response_model=attendance,status_code=status.HTTP_201_CREATED)
def add_attendance(att:attendance):
    newatt = models.attendance(
        id=att.id,
        emp_id=att.emp_id,
        time = att.time,
        status = att.status
    )

    find_att = db.query(models.attendance).filter(models.attendance.emp_id==att.emp_id).first()

    if find_att is not None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="employees with this id already exist")


    db.add(newatt)
    db.commit()

    return newatt

@app.get('/getallattendance', response_model=list[attendance] ,status_code=status.HTTP_200_OK)
def getAllatt():
    getAll_att = db.query(models.attendance).all()
    return getAll_att

@app.get("/attendance/{emp_id}", response_model=List[attendance])
def read_attendance(emp_id: int,):

    attendances = db.query(models.attendance).filter(models.attendance.id == emp_id).all()
    return attendances

# @app.get("/attendance/{emp_id}")
# def read_attendance(emp_id: int):
#     db_employee = db.query(attendance).filter(attendance.id == emp_id).first()
#     if db_employee is None:
#         raise HTTPException(status_code=404, detail="Employee not found")
    
#     return db_employee.attendance

# @app.post("/employees/", response_model=EmployeeInDB)
# def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
#     db_employee = employee(name=employee.name, email=employee.email, phone=employee.phone)
#     db.add(db_employee)
#     db.commit()
#     db.refresh(db_employee)
#     return db_employee

# @app.post("/attendance/", response_model=AttendanceInDB)
# def create_attendance(attendance: AttendanceCreate, db: Session = Depends(get_db)):
#     db_employee = db.query(employees).filter(employees.id == attendance.emp_id).first()
#     if db_employee is None:
#         raise HTTPException(status_code=404, detail="Employee not found")
    
#     db_attendance = attendance(emp_id=attendance.emp_id, name=attendance.name, time=attendance.time, status=attendance.status)
#     db.add(db_attendance)
#     db.commit()
#     db.refresh(db_attendance)
#     return db_attendance

# @app.get("/employees/{employee_id}/attendance", response_model=List[AttendanceInDB])
# def read_attendance(employee_id: int, db: Session = Depends(get_db)):
#     db_employee = db.query(employees).filter(employees.id == employee_id).first()
#     if db_employee is None:
#         raise HTTPException(status_code=404, detail="Employee not found")
    
#     return db_employee.attendance


# @app.post("/courses/")
# def create_course(course: Course):
#     db.add(course)
#     db.commit()
#     db.refresh(course)
#     return course

# @app.get("/courses/{course_id}")
# def read_course(course_id: int):
#     course = db.query(Course).filter(Course.id == course_id).first()
#     if course is None:
#         raise HTTPException(status_code=404, detail="Course not found")
#     return course

# @app.put("/courses/{course_id}")
# def update_course(course_id: int, course: Course):
#     db_course = db.query(Course).filter(Course.id == course_id).first()
#     if db_course is None:
#         raise HTTPException(status_code=404, detail="Course not found")
#     db_course.name = course.name
#     db_course.teacher_id = course.teacher_id
#     db_course.time_slot = course.time_slot
#     db_course.capacity = course.capacity
#     db.commit()
#     return db_course

# @app.delete("/courses/{course_id}")
# def delete_course(course_id: int):
#     course = db.query(Course).filter(Course.id == course_id).first()
#     if course is None:
#         raise HTTPException(status_code=404, detail="Course not found")
#     db.delete(course)
#     db.commit()
#     return {"message": "Course deleted"}

# @app.get("/courses/")
# def read_courses(skip: int = 0, limit: int = 100):
#     courses = db.query(Course).offset(skip).limit(limit).all()
#     return courses

# @app.post("/teachers/")
# def create_teacher(teacher: Teacher):
#     db.add(teacher)
#     db.commit()
#     db.refresh(teacher)
#     return teacher