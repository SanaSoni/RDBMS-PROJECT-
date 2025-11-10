import mysql.connector as mycon

# --------------------------- LOGIN ---------------------------

def login(username, password):
    global cur
    global con
    try:
        con = mycon.connect(host="localhost", user=f"{username}", passwd=f"{password}")
        cur = con.cursor()
        cur.execute("use RDBMS")
    except:
        print("Incorrect Username or Password")
        exit()

username = input("username: ")
password = input("password: ")
login(username, password)

# --------------------------- OUTPUT ---------------------------

def output(data):
    if not data:
        print("(no rows)\n")
        return

    for row in data:
        for col in row:
            print(col, end="\t")
        print()
    print()

# --------------------------- INSERT FUNCTIONS ---------------------------

def add_assignment():
    a    = input("Assignment Number: ")
    name = input("Assignment Name: ")
    date = input("Due Date (YYYY-MM-DD): ")
    sub  = input("Subject: ")

    cur.execute(f"INSERT INTO Assignments VALUES({a},'{name}','{date}','{sub}')")
    con.commit()

    print("Inserted.\n")

def add_student():
    sid = input("Student ID: ")
    fn  = input("First Name: ")
    mn  = input("Middle Name (or blank): ") or None
    ln  = input("Last Name: ")
    dob = input("DOB (YYYY-MM-DD): ")
    ph  = input("Phone Number: ")
    a   = input("Assignment Number: ")

    cur.execute(f"INSERT INTO Student VALUES({sid},'{fn}','{mn}','{ln}','{dob}',{ph},{a})")
    con.commit()

    print("Inserted.\n")

def add_class():
    cid   = input("Class ID: ")
    cname = input("Class Name: ")
    t     = input("Timing: ")

    cur.execute(f"INSERT INTO Classes VALUES({cid},'{cname}','{t}')")
    con.commit()

    print("Inserted.\n")

def add_professor():
    pid = input("Professor ID: ")
    dep = input("Department: ")
    fn  = input("First Name: ")
    mn  = input("Middle Name (or blank): ") or None
    ln  = input("Last Name: ")
    ph  = input("Phone Number: ")
    a   = input("Assignment Number: ")
    cid = input("Class ID: ")

    cur.execute(
        f"INSERT INTO Professor VALUES({pid},'{dep}','{fn}','{mn}','{ln}',{ph},{a},{cid})"
    )
    con.commit()

    print("Inserted.\n")

def add_material():
    br  = input("Branch: ")
    pid = input("Professor ID: ")

    cur.execute(f"INSERT INTO Study_Material VALUES('{br}',{pid})")
    con.commit()

    print("Inserted.\n")

def add_quiz():
    qid = input("Quiz ID: ")
    m   = input("Marks: ")
    t   = input("Type: ")
    lb  = input("Leaderboard: ")
    tp  = input("Topic: ")
    dt  = input("Date (YYYY-MM-DD): ")

    cur.execute(f"INSERT INTO Quiz VALUES({qid},{m},'{t}',{lb},'{tp}','{dt}')")
    con.commit()

    print("Inserted.\n")

def add_enrollment():
    sid = input("Student ID: ")
    cid = input("Class ID: ")

    cur.execute(f"INSERT INTO Enrolls_in VALUES({sid},{cid})")
    con.commit()

    print("Inserted.\n")

# --------------------------- SEARCH ---------------------------

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

# --------------------------- DELETE ---------------------------

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

# --------------------------- DISPLAY ---------------------------

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

# --------------------------- MENUS ---------------------------

def display_menu():
    while True:
        print("1.Display Assignments")
        print("2.Display Students")
        print("3.Display Classes")
        print("4.Display Professors")
        print("5.Display Study Material")
        print("6.Display Quiz")
        print("7.Display Enrollments")
        print("0.Back")

        c = input("Enter choice: ")

        if   c == "1": display_assignments()
        elif c == "2": display_students()
        elif c == "3": display_classes()
        elif c == "4": display_professors()
        elif c == "5": display_material()
        elif c == "6": display_quiz()
        elif c == "7": display_enrollments()
        elif c == "0": break

def insert_menu():
    while True:
        print("1.Add Assignment")
        print("2.Add Student")
        print("3.Add Class")
        print("4.Add Professor")
        print("5.Add Study Material")
        print("6.Add Quiz")
        print("7.Add Enrollment")
        print("0.Back")

        c = input("Enter choice: ")

        if   c == "1": add_assignment()
        elif c == "2": add_student()
        elif c == "3": add_class()
        elif c == "4": add_professor()
        elif c == "5": add_material()
        elif c == "6": add_quiz()
        elif c == "7": add_enrollment()
        elif c == "0": break

def search_menu():
    while True:
        print("1.Search Student")
        print("2.Search Professor")
        print("3.Search Class")
        print("0.Back")

        c = input("Enter choice: ")

        if   c == "1": search_student()
        elif c == "2": search_professor()
        elif c == "3": search_class()
        elif c == "0": break

def delete_menu():
    while True:
        print("1.Delete Student")
        print("2.Delete Professor")
        print("3.Delete Class")
        print("0.Back")

        c = input("Enter choice: ")

        if   c == "1": delete_student()
        elif c == "2": delete_professor()
        elif c == "3": delete_class()
        elif c == "0": break

# --------------------------- MAIN MENU ---------------------------

def menu():
    while True:
        print("\n1.Display Records   2.Insert Records   3.Search Records   4.Delete Record   0.Exit")
        c = input("Enter choice: ")

        if   c == "1": display_menu()
        elif c == "2": insert_menu()
        elif c == "3": search_menu()
        elif c == "4": delete_menu()
        elif c == "0":
            print("Bye!!")
            break

menu()
