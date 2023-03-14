from django.urls import path
from Homeworks import views

urlpatterns = [
    path('teacher_homeworks', views.get_all_homeworks_teacher, name='homeworks'),
    path('student_homeworks', views.get_all_homeworks_student, name='student_homeworks'),
    path('add_homework', views.add_homework, name='add_homework'),
    path('', views.homepage, name='homapage'),
    path('login', views.login, name='login'),
    path('signup_teacher', views.signup_teacher, name='Signup_teacher'),
    path('signup_student', views.signup_student, name='Signup_student'),
    path('add_new_teacher', views.add_new_teacher, name='add_new_teacher'),
    path('add_new_student', views.add_new_student, name='add_new_student'),
    path('delete/<int:id>', views.delete_homework, name='delete'),
    path('submit/<int:id>', views.submit_homework, name='submit'),
    path('edit/<int:id>', views.edit_homework, name='edit'),
]