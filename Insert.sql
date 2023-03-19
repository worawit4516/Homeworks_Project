-- select host, user from mysql.user;

-- create database assignment_project;
-- -- drop database assignment_project;
use assignment_project;
select * from Homeworks_stu_homework;
show tables;  

-- DELETE FROM Homeworks_homework WHERE homework_id = 3;

INSERT INTO `Homeworks_teacher`(teacher_id, fname, lname, birthday, email, phone, password) VALUES(1,'Sarah', 'Moore', '1990-02-20', 'sarah.moor@gmail.com', '0912356478', '');
INSERT INTO `Homeworks_teacher`(teacher_id, fname, lname, birthday, email, phone, password) VALUES(2,'Emily', 'Smith', '1995-02-22', 'emily.smit@gmail.com', '0904751326', '');

INSERT INTO `Homeworks_subject`(subject_id,name, description, credit, teacher_id) VALUES(1,'คณิตศาสตร์ 1', '', 3, 1);
INSERT INTO `Homeworks_subject`(subject_id,name, description, credit, teacher_id) VALUES(2,'วิทยาศาสตร์ 1', '', 3, 2);

INSERT INTO `Homeworks_grade`(grade_id,name, num) VALUES(1,'ประถมศึกษา', 1);
INSERT INTO `Homeworks_grade`(grade_id,name, num) VALUES(2,'ประถมศึกษา', 2);
INSERT INTO `Homeworks_grade`(grade_id,name, num) VALUES(3,'ประถมศึกษา', 3);
INSERT INTO `Homeworks_grade`(grade_id,name, num) VALUES(4,'ประถมศึกษา', 4);
INSERT INTO `Homeworks_grade`(grade_id,name, num) VALUES(5,'ประถมศึกษา', 5);
INSERT INTO `Homeworks_grade`(grade_id,name, num) VALUES(6,'ประถมศึกษา', 6);

INSERT INTO `Homeworks_room`(room_id,num, grade_id, subject_id) VALUES(1,1, 4, 1);
INSERT INTO `Homeworks_room`(room_id,num, grade_id, subject_id) VALUES(2,1, 4, 2);

INSERT INTO `Homeworks_student`(student_id,fname, lname, birthday, email, phone, room_id) VALUES(1,'Bob', 'Migon', '2013-07-30', 'bob.migo@gmail.com', '0826547891', 1);
INSERT INTO `Homeworks_student`(student_id,fname, lname, birthday, email, phone, room_id) VALUES(2,'Mae', 'Pooka', '2013-09-17', 'mae.pook@gmail.com', '0824561372', 1);
