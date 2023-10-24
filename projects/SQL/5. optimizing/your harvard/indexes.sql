CREATE INDEX courses_department_index ON courses(department);
CREATE INDEX courses_number_index ON courses(number);
CREATE INDEX courses_semester_index ON courses(semester);
CREATE INDEX courses_id_index ON courses(id);
CREATE INDEX courses_title_index ON courses(title);

CREATE INDEX enrollments_course_id_index ON enrollments(course_id);
CREATE INDEX enrollments_students_id_index ON enrollments(student_id);

CREATE INDEX requirements_id_index ON requirements(id);

CREATE INDEX student_id_index ON students(id);


