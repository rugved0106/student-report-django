from django.db import models

# Model for Department
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model for Student (Roll can be considered as unique student record)
class Student(models.Model):
    roll_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True, default="default@vu.edu.in")  
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.roll_number} - {self.name}"
    
class Subject(models.Model):
    s_name = models.CharField(max_length=100)

# Model for Student Report
class StudentReport(models.Model):
    roll = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    age = models.IntegerField()

    def __str__(self):
        return f"Report of {self.roll.name} (Roll: {self.roll.roll_number})"
    
class Student_marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()
    
    def __str__(self):
        return f"{self.student.name} - {self.subject.s_name}"

    def Meta():
        unique_together = ['student', 'subject']
