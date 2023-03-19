```
CREATE DATABASE assignment_project;
# User SQL Query

INSERT INTO `homeworks_teacher`(teacher_id, fname, lname, birthday, email, phone, password) VALUES(1,'Admin', 'Admin', '1995-02-22', 'Admin', '0904751326', 'Admin');
INSERT INTO `homeworks_teacher`(teacher_id, fname, lname, birthday, email, phone, password) VALUES(2,'Admin2', 'Admin2', '1995-02-22', 'Admin2', '0904751326', 'Admin2');
INSERT INTO `homeworks_teacher`(teacher_id, fname, lname, birthday, email, phone, password) VALUES(3,'Admin3', 'Admin3', '1995-02-22', 'Admin3', '0904751326', 'Admin3');
INSERT INTO `homeworks_teacher`(teacher_id, fname, lname, birthday, email, phone, password) VALUES(4,'Admin4', 'Admin4', '1995-02-22', 'Admin4', '0904751326', 'Admin4');

INSERT INTO `homeworks_subject`(subject_id,name, description, credit, teacher_id) VALUES(1,'คณิตศาสตร์ ', '', 3, 1);
INSERT INTO `homeworks_subject`(subject_id,name, description, credit, teacher_id) VALUES(2,'วิทยาศาสตร์ ', '', 3, 2);
INSERT INTO `homeworks_subject`(subject_id,name, description, credit, teacher_id) VALUES(3,'อังกฤษ', '', 3, 3);
INSERT INTO `homeworks_subject`(subject_id,name, description, credit, teacher_id) VALUES(4,'ไทย', '', 3, 4);
INSERT INTO `homeworks_subject`(subject_id,name, description, credit, teacher_id) VALUES(5,'พละ', '', 3, 1);
INSERT INTO `homeworks_subject`(subject_id,name, description, credit, teacher_id) VALUES(6,'สุขศึกษา', '', 3, 3);
INSERT INTO `homeworks_subject`(subject_id,name, description, credit, teacher_id) VALUES(7,'ดณตรี', '', 3, 3);
INSERT INTO `homeworks_subject`(subject_id,name, description, credit, teacher_id) VALUES(8,'เปียโน', '', 3, 3);
INSERT INTO `homeworks_subject`(subject_id,name, description, credit, teacher_id) VALUES(9,'Science', '', 3, 3);
INSERT INTO `homeworks_subject`(subject_id,name, description, credit, teacher_id) VALUES(10,'Mathematic', '', 3, 3);
INSERT INTO `homeworks_subject`(subject_id,name, description, credit, teacher_id) VALUES(11,'ENS', '', 3, 3);
INSERT INTO `homeworks_subject`(subject_id,name, description, credit, teacher_id) VALUES(12,'สังคมศึกษา ศาษนาและวัฒนธรรม', '', 3, 3);
INSERT INTO `homeworks_subject`(subject_id,name, description, credit, teacher_id) VALUES(13,'ประวัติศาครื', '', 3, 3);
INSERT INTO `homeworks_subject`(subject_id,name, description, credit, teacher_id) VALUES(14,'Social Study', '', 3, 3);
INSERT INTO `homeworks_subject`(subject_id,name, description, credit, teacher_id) VALUES(15,'จีน', '', 3, 3);
INSERT INTO `homeworks_subject`(subject_id,name, description, credit, teacher_id) VALUES(16,'Computer', '', 3, 3);
INSERT INTO `homeworks_subject`(subject_id,name, description, credit, teacher_id) VALUES(17,'Stem', '', 3, 3);
INSERT INTO `homeworks_subject`(subject_id,name, description, credit, teacher_id) VALUES(18,'แนะแนว', '', 3, 3);

INSERT INTO `homeworks_grade`(grade_id,name, num) VALUES(1,'ประถมศึกษา', 1);
INSERT INTO `homeworks_grade`(grade_id,name, num) VALUES(2,'ประถมศึกษา', 2);
INSERT INTO `homeworks_grade`(grade_id,name, num) VALUES(3,'ประถมศึกษา', 3);
INSERT INTO `homeworks_grade`(grade_id,name, num) VALUES(4,'ประถมศึกษา', 4);
INSERT INTO `homeworks_grade`(grade_id,name, num) VALUES(5,'ประถมศึกษา', 5);
INSERT INTO `homeworks_grade`(grade_id,name, num) VALUES(6,'ประถมศึกษา', 6);

INSERT INTO `homeworks_room`(room_id,num, grade_id, subject_id) VALUES(1,1, 4, 1);
INSERT INTO `homeworks_room`(room_id,num, grade_id, subject_id) VALUES(2,1, 4, 2);

INSERT INTO `homeworks_student`(student_id,fname, lname, phone, birthday, email, room) VALUES(3,'Adminpage', 'str01', '0823416383', '2013-03-13', 'Adminpagestr01', 1);
INSERT INTO `homeworks_student`(student_id,fname, lname, phone, birthday, email, room) VALUES(4,'Adminpage', 'str02', '0823416383', '2013-03-13', 'Adminpagestr02', 2);

select * from homeworks_teacher
```
