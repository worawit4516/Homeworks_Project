# Create your views here.
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from Homeworks.models import Student, Student_has_Homework, Teacher, Subject, Room
from Homeworks.models import Homework

# Get homework
def get_all_homeworks_teacher(request):
    teacher = request.session['user']
    print(f'Teacher id : {teacher}')

    Homeworks = Homework.objects.filter(teacher=teacher)
    print(f'Homework  : {Homeworks }')
    Teachers = Teacher.objects.all()
    Subjects = Subject.objects.all()
    Rooms = Room.objects.all()
    context = {
        'Homeworks': Homeworks,
        'Teachers': Teachers,
        'Subjects': Subjects,
        'Rooms': Rooms
    }
    print(Homeworks)
    return render(request, 'homeworks_teacher.html', context)

def get_all_homeworks_student(request):
    student = request.session['user']
    print(f'Student id : {student}')

    stu_homeworks = Student_has_Homework.objects.select_related(
        'homework').filter(status="InProgress", student=student)
    print(f'Homework  : { stu_homeworks}')

    context = {
        'stu_homeworks': stu_homeworks
    }
    return render(request, 'homeworks_student.html', context)

# Add, Delete, Submit homework
def add_student_homework(students_in_room):
    homework = Homework.objects.last()
    for student in students_in_room:
        new_stu_homework = Student_has_Homework(
            status="InProgress", student=student, homework=homework)
        new_stu_homework.save()

def add_homework(request):
    homework_description = request.POST['description']
    score = request.POST['score']
    subject = Subject.objects.get(subject_id=request.POST['subject_id'])
    teacher = Teacher.objects.get(teacher_id=request.POST['teacher_id'])
    room = Room.objects.get(room_id=request.POST['room_id'])
    deadline = request.POST['dead_line']

    students_in_room = Student.objects.filter(room=request.POST['room_id'])

    new_Homework = Homework(homework_description=homework_description, score=score,
                            subject=subject, teacher=teacher, deadline=deadline, room=room)
    new_Homework.save()
    add_student_homework(students_in_room)
    return HttpResponseRedirect(reverse('homeworks'))

def add_student_homework(students_in_room):
    homework = Homework.objects.last()
    for student in students_in_room:
        new_stu_homework = Student_has_Homework(
            status="InProgress", student=student, homework=homework)
        new_stu_homework.save()

def delete_homework(request,id):
    homework_to_delete = id
    Homework.objects.filter(pk=homework_to_delete ).delete()
    Student_has_Homework.objects.filter(homework=homework_to_delete).delete()
    return HttpResponseRedirect(reverse('homeworks'))

def edit_homework(request,id):
    homework_to_edit = id
    homework = Homework.objects.get(pk=homework_to_edit)
    homework_description = request.POST['description']
    score = request.POST['score']
    deadline = request.POST['dead_line']
    
    homework.homework_description = homework_description
    homework.score  =  score 
    homework.deadline = deadline
    homework.save()
    return HttpResponseRedirect(reverse('homeworks'))

def submit_homework(request, id):
    stu_homework_submit = Student_has_Homework.objects.get(stu_hw_id=id)
    stu_homework_submit.status = 'Success'
    stu_homework_submit.save()
    return HttpResponseRedirect(reverse('student_homeworks'))

# Login
def homepage(request):
    return render(request, 'login.html')

def login(request):
    if Teacher.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
        user = Teacher.objects.filter(
            email=request.POST['email'], password=request.POST['password']).values_list('teacher_id', flat=True)
        userId = list(user)
        request.session['user'] = userId[0]
        return redirect('homework/teacher_homeworks')
    elif Teacher.objects.filter(email=request.POST['email'],  birthday=request.POST['password']).exists():
        user = Teacher.objects.filter(
            email=request.POST['email'], birthday=request.POST['password']).values_list('teacher_id', flat=True)
        userId = list(user)
        request.session['user'] = userId[0]
        return redirect('homework/teacher_homeworks')
    elif Student.objects.filter(email=request.POST['email'], birthday=request.POST['password']).exists():
        user = Student.objects.filter(
            email=request.POST['email'], birthday=request.POST['password']).values_list('student_id', flat=True)
        userId = list(user)
        request.session['user'] = userId[0]
        return redirect('homework/student_homeworks')
    else:
        return render(request, 'login.html')
    
# Signup
def signup_teacher(request):
    return render(request, 'signup_teacher.html')

def signup_student(request):
    return render(request, 'signup_student.html')

def add_new_teacher(request):
    fname= request.POST['fname']
    lname = request.POST['lname']
    birthday = request.POST['birthday']
    email = request.POST['email']
    phone = request.POST['phone']
    password = request.POST['password']   

    new_teacher = Teacher(fname= fname, lname = lname, birthday= birthday, email= email, phone= phone, password= password,)
    new_teacher.save()
    return render(request, 'login.html')

def add_new_student(request):
    fname= request.POST['fname']
    lname = request.POST['lname']
    birthday = request.POST['birthday']
    email = request.POST['email']
    phone = request.POST['phone']
    room = request.POST['room']   

    new_student = Student(fname= fname, lname = lname, birthday= birthday, email= email, phone= phone, room= room,)
    new_student.save()
    return render(request, 'login.html')