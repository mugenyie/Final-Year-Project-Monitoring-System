# Student Project Monitoring System

[![Build Status](https://travis-ci.com/mugenyie/fyp.svg?branch=develop)](https://travis-ci.com/mugenyie/fyp)

## Admin API
```json
POST: http://127.0.0.1:5000/api/v1/admin/
Body
{
	"email": "ecmugenyi@gmail.com",
	"name": "Emmanuel C. Mugenyi",
	"password": "1234",
	"phonenumber": "0787744279"
}
Reponse
{
    "data": {
        "email": "ecmugenyi@gmail.com",
        "id": "caf70370-b0d5-4774-8dad-1f9f22b835c0",
        "name": "Emmanuel C. Mugenyi",
        "phonenumber": "0787744279",
        "user_role_name": "ADMIN",
        "user_role_value": 1
    },
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTc2ODk4NTcsImlhdCI6MTU1NzYwMzQ1NywidXNlcl9pZCI6ImNhZjcwMzcwLWIwZDUtNDc3NC04ZGFkLTFmOWYyMmI4MzVjMCIsInVzZXJfcm9sZSI6MX0.mqOcaor4hzrYmwDVzbuuEKUdxbALOtdJHoVE6h3-CJc"
}

GET: http://127.0.0.1:5000/api/v1/admin/<string:user_id>
headers - api-token
Reponse
{
    "email": "ecmugenyi@gmail.com",
    "id": "caf70370-b0d5-4774-8dad-1f9f22b835c0",
    "name": "Emmanuel C. Mugenyi",
    "phonenumber": "0787744279",
    "user_role_name": "ADMIN",
    "user_role_value": 1
}

GET: http://127.0.0.1:5000/api/v1/admin/
GET: http://127.0.0.1:5000/api/v1/admin/me
POST: http://127.0.0.1:5000/api/v1/admin/login
Body
{
	"email": "ecmugenyi@gmail.com",
	"password": "1234"
}
Response
{
    "api-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTc2OTA2NzcsImlhdCI6MTU1NzYwNDI3NywidXNlcl9pZCI6ImNhZjcwMzcwLWIwZDUtNDc3NC04ZGFkLTFmOWYyMmI4MzVjMCIsInVzZXJfcm9sZSI6MX0.qMLFwxfVcMEA2EC1XJViydUb8XSrBTgwv1cP7k10dNM",
    "data": {
        "email": "ecmugenyi@gmail.com",
        "id": "caf70370-b0d5-4774-8dad-1f9f22b835c0",
        "name": "Emmanuel C. Mugenyi",
        "phonenumber": "0787744279",
        "user_role_name": "ADMIN",
        "user_role_value": 1
    }
}
```


## Student API
```json
POST: http://127.0.0.1:5000/api/v1/student/
Body
{
  "course": "Computer Science",
  "email": "ecmugenyi@gmail.com",
  "name": "Emmanuel C. Mugenyi",
  "password": "1234",
  "phonenumber": "256787744279",
  "student_number": "214000080"
}
POST: http://127.0.0.1:5000/api/v1/student/login
Body
{
  "email": "ecmugenyi@gmail.com",
  "password": "1234"
}
Reponse
{
    "api-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTc2OTEyMjUsImlhdCI6MTU1NzYwNDgyNSwidXNlcl9pZCI6ImEzMGE1NTQ1LWE4NWMtNDEzZi05YTE1LTQzNmZlMGQwOGRmZSIsInVzZXJfcm9sZSI6MH0.uEh0S1fK0lsjARsPZeHSuMSEZeRUy76vOLVtrtQP6VE",
    "user": {
        "course": "CSC",
        "email": "ecmugenyi@gmail.com",
        "group_id": null,
        "id": "a30a5545-a85c-413f-9a15-436fe0d08dfe",
        "name": "Emmanuel Mugenyi",
        "phonenumber": "256787744279",
        "project_id": null,
        "student_number": "214000080",
        "supervisor_id": null,
        "user_role_name": "STUDENT",
        "user_role_value": 0
    }
}
GET: http://127.0.0.1:5000/api/v1/student/
Reponse
[
    {
        "course": "CSC",
        "email": "ecmugenyi@gmail.com",
        "group_id": null,
        "id": "a30a5545-a85c-413f-9a15-436fe0d08dfe",
        "name": "Emmanuel Mugenyi",
        "phonenumber": "256787744279",
        "project_id": null,
        "student_number": "214000080",
        "supervisor_id": null,
        "user_role_name": "STUDENT",
        "user_role_value": 0
    }
]
GET: http://127.0.0.1:5000/api/v1/student/<string:user_id>
GET: http://127.0.0.1:5000/api/v1/student/me
```

## Supervisor API
```json
POST: http://127.0.0.1:5000/api/v1/supervisor/
Body
{
	"department": "Computer Science",
	"email": "ecmugenyi@gmail.com",
	"name": "Emmanuel C. Mugenyi",
	"password": "1234",
	"phonenumber": "0787744279",
	"title": "Dr. / Prof."
}
GET: http://127.0.0.1:5000/api/v1/supervisor/
Reponse
[
    {
        "created_on": "2019-05-11T20:10:15.687193+00:00",
        "department": "Computer Science",
        "email": "ecmugenyi@gmail.com",
        "id": "93cf3b1f-96ec-4c94-bdc0-d0f0d88db728",
        "modified_on": "2019-05-11T20:10:15.687193+00:00",
        "name": "Emmanuel C. Mugenyi",
        "phonenumber": "0787744279",
        "title": "Dr. / Prof.",
        "user_role_name": "SUPERVISOR",
        "user_role_value": 2
    }
]

POST: http://127.0.0.1:5000/api/v1/supervisor/login
Response:
{
    "api-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTc2OTIzNjAsImlhdCI6MTU1NzYwNTk2MCwidXNlcl9pZCI6IjkzY2YzYjFmLTk2ZWMtNGM5NC1iZGMwLWQwZjBkODhkYjcyOCIsInVzZXJfcm9sZSI6Mn0.dEDR4H7WL4MOVIHUXJee5Ev_zPZ6eKlNyoRKBj4QlQs",
    "user": {
        "created_on": "2019-05-11T20:10:15.687193+00:00",
        "department": "Computer Science",
        "email": "ecmugenyi@gmail.com",
        "id": "93cf3b1f-96ec-4c94-bdc0-d0f0d88db728",
        "modified_on": "2019-05-11T20:10:15.687193+00:00",
        "name": "Emmanuel C. Mugenyi",
        "phonenumber": "0787744279",
        "title": "Dr. / Prof.",
        "user_role_name": "SUPERVISOR",
        "user_role_value": 2
    }
}
GET: http://127.0.0.1:5000/api/v1/supervisor/me
```

## API BaseUrl
[API](https://csc-fypms.herokuapp.com/)