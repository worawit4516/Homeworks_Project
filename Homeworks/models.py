from django.db import models

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=45 , null=False, blank=False)
    lname = models.CharField(max_length=45, null=False, blank=False)
    phone = models.CharField(max_length=10 , null=False, blank=False)
    birthday = models.DateField(null=False)
    email = models.CharField(max_length=45 , null=False, blank=False)
    password = models.CharField(max_length=20 , null=False, blank=False)

class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=65 , null=False, blank=False)
    credit = models.IntegerField(null=False, blank=False)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)

class Grade(models.Model):
    grade_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45 , null=False, blank=False)
    num = models.IntegerField(null=False, blank=False)


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    num = models.IntegerField(null=False, blank=False)
    grade = models.ForeignKey(Grade,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)


class Homework(models.Model):
    id = models.AutoField(primary_key=True)
    homework_name = models.CharField(max_length=45 , null=False, blank=False)
    homework_description = models.CharField(max_length=45, null=True)
    deadline = models.DateField(null=False)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    score = models.IntegerField(null=False, blank=False)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=45 , null=False, blank=False)
    lname = models.CharField(max_length=45, null=False, blank=False)
    phone = models.CharField(max_length=10 , null=False, blank=False)
    birthday = models.DateField(null=False)
    email = models.CharField(max_length=45 , null=False, blank=False)
    room = models.CharField(max_length=12 , null=False, blank=False)

class Student_has_Homework(models.Model):
    stu_hw_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    status = models.CharField(max_length=30, default='InProgress', null=False, blank=False)
    homework = models.ForeignKey(Homework,on_delete=models.CASCADE)

class Nofitication(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.CharField(max_length=12 , null=False, blank=False)
    start = models.DateField(null=False)
    deadline = models.DateField(null=False)
    stu_hw = models.ForeignKey(Student_has_Homework,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)

# class Stu_homework(models.Model):
#     homework_id = models.AutoField(primary_key=True)
#     homework_name = models.CharField(max_length=20 , null=True, blank=True)
#     homework_description = models.CharField(max_length=250 , null=True, blank=True)
#     homework_room = models.CharField(max_length=12 , null=True, blank=True)
#     homework_data = models.CharField(max_length=1200 , null=True, blank=True)