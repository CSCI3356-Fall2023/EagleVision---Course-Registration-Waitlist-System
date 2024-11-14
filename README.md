# EagleVision - Course Registration & Waitlist System

EagleVision is a real-time course registration system built with Django and SQLite, featuring email alerts, priority-based waitlist sorting, and thread-safe auto-enrollment for conflict-free spot allocation.

## Features

- **Real-Time Registration**: Students can register for courses in real-time with immediate confirmation.
- **Priority-Based Waitlist**: Implements a priority system for waitlisted students to ensure fair enrollment.
- **Email Notifications**: Sends automated email alerts for registration confirmations and waitlist updates.
- **Thread-Safe Auto-Enrollment**: Ensures conflict-free spot allocation through thread-safe operations.



## Registration Page

![Registration Page](https://github.com/CSCI3356-Fall2023/EagleVision---Course-Registration-Waitlist-System/blob/main/assets/IMG_2409.JPG)


## Course List
![Course List](https://github.com/CSCI3356-Fall2023/EagleVision---Course-Registration-Waitlist-System/blob/main/assets/IMG_2413.JPG)

## Waitlist 
![Wait List](https://github.com/CSCI3356-Fall2023/EagleVision---Course-Registration-Waitlist-System/blob/main/assets/IMG_2412.JPG)







## Prerequisites

- **Python 3.x**
- **Git** (for cloning the repository)

## Installation

### 1. Clone the Repository

```bash
https://github.com/CSCI3356-Fall2023/EagleVision---Course-Registration-Waitlist-System.git
cd DjangoUnchained

```
### 2. Set up Local environment

Recommend using a venv

```bash
python3 -m venv venv
source venv/bin/activate
```

###3. Install all the requirements
```bash
pip install -r requirements.txt
```



## Running the application 
Set up the database by applying migrations:
```bash
python manage.py migrate
```
### 2. Create a Superuser (Optional)
If you want to access the Django admin panel:
```bash
python manage.py createsuperuser
```

## Run Server

```bash

python manage.py runserver

````
Locally, The application will be accessible at http://127.0.0.1:8000/.



### Usage
Access the Website: Open your web browser and navigate to http://127.0.0.1:8000/.

Register/Login: Create a new account or log in with existing BC credentials.

Browse Courses: View the list of available courses.

Register for Courses: Enroll in courses or join the waitlist if the course is full.

Receive Notifications: Check your email for registration confirmations and updates.

Admin Report: As an admin, you can check out the current analytics and registration for a specific course and can also go back to previous snapshot.



