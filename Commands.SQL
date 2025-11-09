CREATE TABLE Assignments
(
  Assignment_number INT NOT NULL,
  Assignment_name varchar(20) NOT NULL,
  Due_Date date NOT NULL,
  Subject varchar(20) NOT NULL,
  PRIMARY KEY (Assignment_number)
);

CREATE TABLE Student
(
  student_id INT NOT NULL,
  First_name varchar(20) NOT NULL,
  Middle_name varchar(20),
  Last_name varchar(20) NOT NULL,
  DOB date NOT NULL,
  phone_number_ INT NOT NULL,
  Assignment_number INT NOT NULL,
  PRIMARY KEY (student_id),
  FOREIGN KEY (Assignment_number) REFERENCES
  Assignments(Assignment_number)
);

CREATE TABLE Classes
(
  Class_id INT NOT NULL,
  Class_name varchar (20) NOT NULL,
  Timing varchar(6) NOT NULL,
  PRIMARY KEY (Class_id)
);

CREATE TABLE Professor
(
  Professor_id INT NOT NULL,
  Department VARCHAR(20) NOT NULL,
  First_name VARCHAR(20) NOT NULL,
  Middle_name VARCHAR(20),
  Last_Name_ VARCHAR(20) NOT NULL,
  Phone_number_ INT NOT NULL,
  Assignment_number INT NOT NULL,
  Class_id INT NOT NULL,
  PRIMARY KEY (Professor_id),
  FOREIGN KEY (Assignment_number) REFERENCES Assignments(Assignment_number),
  FOREIGN KEY (Class_id) REFERENCES Classes(Class_id)
);

CREATE TABLE Study_Material
(
  Branch varchar(20) NOT NULL,
  Professor_id INT NOT NULL,
  FOREIGN KEY (Professor_id) REFERENCES Professor(Professor_id)
);

CREATE TABLE Quiz
(
  Quiz_id INT NOT NULL,
  Quiz_marks INT NOT NULL,
  Quiz_type varchar(20) NOT NULL,
  Leader_Board INT NOT NULL,
  Quiz_topic varchar(20) NOT NULL,
  Quiz_date date NOT NULL,
  PRIMARY KEY (Quiz_id)
);

CREATE TABLE Enrolls_in
(
  student_id INT NOT NULL,
  Class_id INT NOT NULL,
  PRIMARY KEY (student_id, Class_id),
  FOREIGN KEY (student_id) REFERENCES Student(student_id),
  FOREIGN KEY (Class_id) REFERENCES Classes(Class_id)
);