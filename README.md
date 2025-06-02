# 🎓 Student Report and Rank Generation System

A Django-based web application that dynamically generates a list of students using the Faker library. It displays student details such as name, department, age, and roll number.
Clicking on a roll number opens the student's detailed report card page showing subject-wise scores, total marks, and rank. The student list is paginated for better readability 
and performance and also with search filters

## ✨ Features

- ✅ Automatically generate student data using the **Faker** library
- 📋 View all students with:
  - Name
  - Department
  - Age
  - Roll number (clickable)
- 📄 Detailed **report card page** for each student
  - Subject-wise scores
  - Total marks
  - Rank (calculated dynamically)
- 🔢 Real-time **rank generation** based on total marks
- 📄 **Pagination** implemented for student list
- 🛠️ Admin interface for monitoring students and scores

## 🧑‍💻 Tech Stack

- **Framework**: Django (Python)
- **Database**: SQLite (default Django DB)
- **Library**: [Faker](https://github.com/joke2k/faker) for generating fake student data
- **Frontend**: HTML, CSS (with Django Templates)
- **Pagination**: Django’s built-in pagination

🧪 Future Improvements
- Add authentication (admin/students)
- Export report cards as PDF

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/student-report-django.git
   cd student-report-django

2. **Install dependencies**

```bash
pip install -r requirements.txt
```


3. **Run migrations**
```bash 
python manage.py makemigrations
python manage.py migrate
```
4. **Run the development server**

```bash
python manage.py runserver
```

5. **Access the app**
Visit http://127.0.0.1:8000/ in your browser
