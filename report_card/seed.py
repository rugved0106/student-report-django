from report_card.models import Student
from report_card.models import Department
from report_card.models import Subject
from report_card.models import Student_marks
from faker import Faker
import random

fake = Faker()

def create_marks(n=100)-> None:
    try:
        students = list(Student.objects.all())
        subjects = list(Subject.objects.all())
        for i in range(n):
            student = random.choice(students)
            subject = random.choice(subjects)
            Student_marks.objects.create(
                subject = subject,
                student = student,
                marks = random.randint(20, 100)
            )
    except Exception as e:
        print(e)

def generate_random_user(n=10) -> None:
    try:
        # Ensure default departments exist
        default_departments = ["Computer Science", "Electronics", "Mechanical", "Civil", "IT"]
        for dept_name in default_departments:
            Department.objects.get_or_create(name=dept_name)

        departments = Department.objects.all()

        for _ in range(n):
            unique_number = random.randint(100000, 999999)  # 6-digit number
            roll_number = f"STD-VU-{unique_number}"  # Custom roll format
            name = fake.name()
            email = fake.unique.email() if random.random() > 0.1 else f"default{unique_number}@vu.edu.in"
            age = random.randint(18, 26)
            department = random.choice(departments)

            Student.objects.create(
                roll_number=roll_number,
                name=name,
                email=email,
                age=age,
                department=department
            )
        
        print(f"✅ {n} fake students with custom roll and default emails created successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")
