![image](https://github.com/user-attachments/assets/6c05ef52-bdec-4911-a12a-c5b0fc1c3d3b)# Attendance System

## Overview

The Attendance System is a modern application designed to track and manage attendance records efficiently. This system leverages Python's FastAPI for a high-performance API and PostgreSQL for robust and scalable data storage.

## Features

- **User Management**: Add, update, and delete users.
- **Attendance Tracking**: Mark attendance and view attendance history.
- **Reports**: Generate and export attendance reports.
- **Authentication**: Secure access with user authentication.

## Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: OAuth2 / JWT

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL 12+

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/attendance-system.git
   cd attendance-system
2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate

3. **Install Dependecies**

   ```bash
   pip install psycopg2 sqlalchemy alembic fastapi uvicorn

4. **Run Database Migration**
   
   ```bash
   alembic upgrade head

5. **Start the Application**

   ```bash
   uvicorn app.main:app --reload

## API Endpoints

### User Management

- **`POST /addemp`**: Create a new user.

### Attendance

- **`POST /attendance`**: Mark attendance for a user.
- **`GET /attendance/{user_id}`**: Get the attendance history for a specific user.


## Authentication

To access secured endpoints, use the OAuth2 authentication scheme with JWT tokens. Tokens can be obtained via the **`/token`** endpoint.

   
  
    
     

![image](https://github.com/user-attachments/assets/4e1f61be-baea-49da-a07f-f553708da08f)

![image](https://github.com/user-attachments/assets/04f54be6-3e1a-43d6-b0bb-82c5397a8d60)
