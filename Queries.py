import mysql.connector as mycon

username = input("username: ")
password = input("password: ")
con = mycon.connect(host="localhost", user=f"{username}", passwd=f"{password}")
cur = con.cursor()
cur.execute("SHOW DATABASES")
for dbname in cur:
    if("RDBMS" in dbname):
        continue
    else:
        cur.execute("Create database RDBMS")

#OUTPUT
def output(data):
    if not data:
        print("(no rows)\n")
        return

    for row in data:
        for col in row:
            print(col, end="\t")
        print()
    print()

#insert
def add_assignment():
    ano = input("Assignment Number: ")
    name = input("Assignment Name: ")
    date = input("Due Date (YYYY-MM-DD): ")
    sub  = input("Subject: ")
    cur.execute(f"INSERT INTO Assignments VALUES({ano},'{name}','{date}','{sub}')")
    con.commit()
    print("Inserted.\n")

def add_student():
    sid = input("Student ID: ")
    fn = input("First Name: ")
    mn = input("Middle Name (or blank): ") or None
    ln = input("Last Name: ")
    dob = input("DOB (YYYY-MM-DD): ")
    ph = input("Phone Number: ")
    a = input("Assignment Number: ")
    cur.execute(f"INSERT INTO Student VALUES({sid},'{fn}','{mn}','{ln}','{dob}',{ph},{a})")
    con.commit()
    print("Inserted.\n")

def add_class():
    cid = input("Class ID: ")
    cname = input("Class Name: ")
    t = input("Timing: ")
    cur.execute(f"INSERT INTO Classes VALUES({cid},'{cname}','{t}')")
    con.commit()
    print("Inserted.\n")

def add_professor():
    pid = input("Professor ID: ")
    dep = input("Department: ")
    fn = input("First Name: ")
    mn = input("Middle Name (or blank): ") or None
    ln = input("Last Name: ")
    ph = input("Phone Number: ")
    a = input("Assignment Number: ")
    cid = input("Class ID: ")

    cur.execute(
        f"INSERT INTO Professor VALUES({pid},'{dep}','{fn}','{mn}','{ln}',{ph},{a},{cid})"
    )
    con.commit()

    print("Inserted.\n")

def add_material():
    br = input("Branch: ")
    pid = input("Professor ID: ")
    cur.execute(f"INSERT INTO Study_Material VALUES('{br}',{pid})")
    con.commit()
    print("Inserted.\n")

def add_quiz():
    qid = input("Quiz ID: ")
    m = input("Marks: ")
    t = input("Type: ")
    lb = input("Leaderboard: ")
    tp = input("Topic: ")
    dt = input("Date (YYYY-MM-DD): ")
    cur.execute(f"INSERT INTO Quiz VALUES({qid},{m},'{t}',{lb},'{tp}','{dt}')")
    con.commit()
    print("Inserted.\n")

def add_enrollment():
    sid = input("Student ID: ")
    cid = input("Class ID: ")
    cur.execute(f"INSERT INTO Enrolls_in VALUES({sid},{cid})")
    con.commit()
    print("Inserted.\n")

#search
def search_student():
    sid = input("Student ID: ")
    cur.execute(f"SELECT * FROM Student WHERE student_id={sid}")
    output(cur.fetchall())

def search_professor():
    pid = input("Professor ID: ")
    cur.execute(f"SELECT * FROM Professor WHERE Professor_id={pid}")
    output(cur.fetchall())

def search_class():
    cid = input("Class ID: ")
    cur.execute(f"SELECT * FROM Classes WHERE Class_id={cid}")
    output(cur.fetchall())

#delete
def delete_student():
    sid = input("Student ID to delete: ")
    cur.execute(f"DELETE FROM Student WHERE student_id={sid}")
    con.commit()
    print("Deleted.\n")

def delete_professor():
    pid = input("Professor ID to delete: ")
    cur.execute(f"DELETE FROM Professor WHERE Professor_id={pid}")
    con.commit()
    print("Deleted.\n")

def delete_class():
    cid = input("Class ID to delete: ")
    cur.execute(f"DELETE FROM Classes WHERE Class_id={cid}")
    con.commit()
    print("Deleted.\n")

#display
def display_assignments():
    cur.execute("SELECT * FROM Assignments")
    output(cur.fetchall())

def display_students():
    cur.execute("SELECT * FROM Student ORDER BY student_id")
    output(cur.fetchall())

def display_classes():
    cur.execute("SELECT * FROM Classes ORDER BY Class_id")
    output(cur.fetchall())

def display_professors():
    cur.execute("SELECT * FROM Professor ORDER BY Professor_id")
    output(cur.fetchall())

def display_material():
    cur.execute("SELECT * FROM Study_Material")
    output(cur.fetchall())

def display_quiz():
    cur.execute("SELECT * FROM Quiz")
    output(cur.fetchall())

def display_enrollments():
    cur.execute("SELECT * FROM Enrolls_in")
    output(cur.fetchall())


def display():
    while True:
        print("\n1)Assignments\t\t2)Students\t\t3)Classes\t\t4)Professors\t\t5)Study Material\t\t6)Quiz\t\t7)Enrollments\t\t0)Back\n(1/2/3/4/0): ")
        c2 = input("Enter choice: ")
        if c2 == "1": 
            display_assignments()
        elif c2 == "2": 
            display_students()
        elif c2 == "3": 
            display_classes()
        elif c2 == "4": 
            display_professors()
        elif c2 == "5": 
            display_material()
        elif c2 == "6": 
            display_quiz()
        elif c2 == "7": 
            display_enrollments()
        elif c2 == "0": 
            break

def insert():
    while True:
        print("\n1)Assignments\t\t2)Students\t\t3)Classes\t\t4)Professors\t\t5)Study Material\t\t6)Quiz\t\t7)Enrollments\t\t0)Back\n(1/2/3/4/0): ")
        c3 = input("Enter choice: ")
        if c3 == "1": 
            add_assignment()
        elif c3 == "2": 
            add_student()
        elif c3 == "3": 
            add_class()
        elif c3 == "4": 
            add_professor()
        elif c3 == "5": 
            add_material()
        elif c3 == "6": 
            add_quiz()
        elif c3 == "7": 
            add_enrollment()
        elif c3 == "0": 
            break

def search():
    while True:
        print("1)Student\t\t2)Professor\t\t3)Class\t\t0)Back\n(1/2/3/0): ")
        c4 = input("Enter choice: ")
        if c4 == "1": 
            search_student()
        elif c4 == "2": 
            search_professor()
        elif c4 == "3": 
            search_class()
        elif c4 == "0": 
            break

def delete():
    while True:
        print("1)Student\t\t2)Professor\t\t3)Class\t\t0)Back")
        c5 = input("Enter choice: ")
        if c5 == "1": 
            delete_student()
        elif c5 == "2": 
            delete_professor()
        elif c5 == "3": 
            delete_class()
        elif c5 == "0": 
            break


def menu():
    while True:
        print("\n1)Display\t\t2)Insert\t\t3)Search\t\t4)Delete\t\t0)Exit\n(1/2/3/4/0): ")
        c1 = input("Choice: ")
        if   c1 == "1": 
            display()
        elif c1 == "2": 
            insert()
        elif c1 == "3": 
            search()
        elif c1 == "4": 
            delete()
        elif c1 == "0":
            print("Bye!!")
            break
menu()
