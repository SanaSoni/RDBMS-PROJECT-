CREATE TABLE Assignments
(
  Assignment_number INT NOT NULL,
  Assignment_name VARCHAR(50) NOT NULL,
  Due_Date DATE,
  Subject VARCHAR(50) NOT NULL,
  PRIMARY KEY (Assignment_number)
);

CREATE TABLE Student
(
  student_id INT NOT NULL,
  DOB DATE NOT NULL,
  First_name VARCHAR(50) NOT NULL,
  Middle_name VARCHAR(50),
  Last_name VARCHAR(50) NOT NULL,
  Student_phone_number INT NOT NULL,
  Assignment_number INT NOT NULL,
  PRIMARY KEY (student_id),
  FOREIGN KEY (Assignment_number) REFERENCES Assignments(Assignment_number)
);

CREATE TABLE Classes
(
  Class_id INT NOT NULL,
  Class_name VARCHAR(50) NOT NULL,
  Timing VARCHAR(50) NOT NULL,
  PRIMARY KEY (Class_id)
);

CREATE TABLE Quiz
(
  Quiz_id INT NOT NULL,
  Quiz_marks INT NOT NULL,
  Quiz_type VARCHAR(50) NOT NULL,
  Leader_Board VARCHAR(50),
  Quiz_topic VARCHAR(50),
  Quiz_date DATE NOT NULL,
  PRIMARY KEY (Quiz_id)
);

CREATE TABLE Professor
(
  Professor_id INT NOT NULL,
  Deptartment INT NOT NULL,
  First_name INT NOT NULL,
  Middle_name INT,
  Last_name INT NOT NULL,
  Professor_phone_number INT NOT NULL,
  Quiz_id INT NOT NULL,
  Assignment_number INT NOT NULL,
  Class_id INT NOT NULL,
  PRIMARY KEY (Professor_id),
  FOREIGN KEY (Quiz_id) REFERENCES Quiz(Quiz_id),
  FOREIGN KEY (Assignment_number) REFERENCES Assignments(Assignment_number),
  FOREIGN KEY (Class_id) REFERENCES Classes(Class_id)
);

CREATE TABLE Study_Material
(
  Year INT NOT NULL,
  Branch VARCHAR(50) NOT NULL,
  Subject VARCHAR(50) NOT NULL,
  Professor_id INT NOT NULL,
  FOREIGN KEY (Professor_id) REFERENCES Professor(Professor_id)
);

CREATE TABLE Enrolls_in
(
  student_id INT NOT NULL,
  Class_id INT NOT NULL,
  PRIMARY KEY (student_id, Class_id),
  FOREIGN KEY (student_id) REFERENCES Student(student_id),
  FOREIGN KEY (Class_id) REFERENCES Classes(Class_id)
);

CREATE TABLE gives
(
  student_id INT NOT NULL,
  Quiz_id INT NOT NULL,
  PRIMARY KEY (student_id, Quiz_id),
  FOREIGN KEY (student_id) REFERENCES Student(student_id),
  FOREIGN KEY (Quiz_id) REFERENCES Quiz(Quiz_id)
);