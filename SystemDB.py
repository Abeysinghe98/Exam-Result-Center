from tkinter import*

# import mysql.connector as mysql
import itertools

# Check the database connection
# import FROM as FROM
# import FROM as FROM
# import INNER as INNER
# import JOIN as JOIN
import mysql.connector
import sql as sql
from mysql.connector import Error

# Exception handling
try:
    conn=mysql.connector.connect(host='localhost', user='root', password='')
    if conn.is_connected():
        print("Successfully Connected")
except Error as e:
    print("Oopss..!")
    print(e)

# open database connection
conDict = {'host': 'localhost', 'database': 'db 1', 'user': 'root', 'password': ''}

db = mysql.connector.connect(**conDict)

# Prepare a cursor object using cursor() method.
cursor = db.cursor()


def calcGpa(reg, sem):           # Calculate One Semester GPA for all student

    table_name = sem
    print( table_name)
    cursor.execute(f"SELECT sem.result, crt.credits FROM {table_name} as sem INNER JOIN credit_table as crt ON sem.sub_code = crt.sub_code WHERE sem.stu_ar = {reg}")

    # Fetch results using fetchall() method.

    data = cursor.fetchall()

    # calculate Grade and GPA
    gpa = 0.00
    tot = 0
    tot_credit = 0

    for item in data:
        gpv = 0.00
        # print(item)
        if item[0] == "A+":
            gpv = 4.00
        elif item[0] == "A":
            gpv = 4.00
        elif item[0] == "A-":
            gpv = 3.70
        elif item[0] == "B+":
            gpv = 3.30
        elif item[0] == "B":
            gpv = 3.00
        elif item[0] == "B-":
            gpv = 2.70
        elif item[0] == "C+":
            gpv = 2.30
        elif item[0] == "C":
            gpv = 2.00
        elif item[0] == "C-":
            gpv = 1.70
        elif item[0] == "D+":
            gpv = 1.30
        elif item[0] == "D":
            gpv = 1.00
        elif item[0] == "E":
            gpv = 0.00

        tot = gpv * item[1] + tot
        # print("TOT :", round(tot, 4))

        tot_credit = item[1] + tot_credit
        # print("Total Credit :", tot_credit)

    gpa = (tot / tot_credit)
    print("GPA : ", round(gpa, 4))
    gpa = round(gpa, 4)
    return gpa


def calcSemGPA(sem):     # Calculate One Semester GPA for all students
    sem_gpalist = []

    cursor.execute(f"SELECT DISTINCT stu_ar FROM {sem}")

    ar = cursor.fetchall()
    print(ar)
    for item in ar:
        g_list = calcGpa(item[0], sem)
        sem_gpalist.append(g_list)
    print(sem_gpalist)

    # db.close()


# calcSemGPA("yr1_sem1_table")
# sem by sem

#
# def calcTotGPA():     # Calculate Final GPA of one student
#     final_gpa = []
#
#     for i in ("yr1_sem1_table", "yr1_sem2_table", "yr2_sem1_table", "yr2_sem2_table"):
#
#


def calcFinalgpa(reg):       # calculate Final GPA of one student
    final_tot = 0.0
    final_totcredit = 0
    final_gpa = 0.0

    for i in ("yr1_sem1_table", "yr1_sem2_table", "yr2_sem1_table", "yr2_sem2_table"):

        table_name = i
        # print(table_name)
        cursor.execute(f"SELECT sem.result, crt.credits FROM {table_name} as sem INNER JOIN credit_table as crt ON sem.sub_code = crt.sub_code WHERE sem.stu_ar = {reg}")
        # print(table_name)
        # Fetch results using fetchall() method.

        data = cursor.fetchall()

        # calculate Grade and GPA
        tot = 0
        tot_credit = 0

        for item in data:
            gpv = 0.00
            # print(item)
            if item[0] == "A+":
                gpv = 4.00
            elif item[0] == "A":
                gpv = 4.00
            elif item[0] == "A-":
                gpv = 3.70
            elif item[0] == "B+":
                gpv = 3.30
            elif item[0] == "B":
                gpv = 3.00
            elif item[0] == "B-":
                gpv = 2.70
            elif item[0] == "C+":
                gpv = 2.30
            elif item[0] == "C":
                gpv = 2.00
            elif item[0] == "C-":
                gpv = 1.70
            elif item[0] == "D+":
                gpv = 1.30
            elif item[0] == "D":
                gpv = 1.00
            elif item[0] == "E":
                gpv = 0.00

            tot = gpv * item[1] + tot
            # print("TOT :", round(tot, 4))

            tot_credit = item[1] + tot_credit
            # print("Total Credit :", tot_credit)


        final_tot = final_tot + tot
        # print("Final TOT :", final_tot, "TOT : ", tot)
        final_totcredit = final_totcredit + tot_credit
        # print("Final Credit :", final_totcredit, "Credit :", tot_credit)

    final_gpa = (final_tot / final_totcredit)
    # print("Final GPA : ", round(final_gpa, 4))
    final_gpa = round(final_gpa, 4)
    return final_gpa


final_gpalist= []
ar = []
value = []

def calcAllgpa():          # Calculate GPA for all student

    sem = "yr1_sem1_table"

    cursor.execute(f"SELECT DISTINCT stu_ar FROM {sem}")


    ar = cursor.fetchall()
    # print(ar)
    for item in ar:
        all_gpa = calcFinalgpa(item[0])
        final_gpalist.append(all_gpa)
    # print(final_gpalist)

 # value = []
    # print(value)

    for (i,x) in zip(ar, final_gpalist):
        tup = (i[0], x)
        # print(tup)
        value.append(tup)

    # print(value)



#
# def calcRank():
#     calcAllgpa()
#     # ar = cursor.fetchall()
#         # l = (i[0],x)
#         # value.append(y);
#
#     # print(value)


# sql = []
#
#
def manageGPAtable():
    # print(value)
    sql1 = "DELETE FROM final_gpatable"

    cursor.execute(sql1)

    db.commit()

    # print(cursor.rowcount, "record(s) deleted")

    sql = "INSERT INTO final_gpatable(stu_ar, final_gpa) VALUES (%s, %s)"

    cursor.executemany(sql, value)

    db.commit()

    # print(cursor.rowcount, "was inserted.")


def calcClass():  # calculate class of all students

    x = "SELECT * FROM final_gpatable"

    cursor.execute(x)

    store = cursor.fetchall()

    print(store)

    for i in store:
        y = i[1]
        print(y)

        if 4.00 >= y >= 3.70:
            c = "First Class "
        elif 3.70 > y >= 3.30:
            c = "Second Upper Class"
        elif 3.30 > y >= 3.00:
            c = "Second Lower Class"
        else:
            c = "General Degree"

        print(c)


def calcOneClass(reg):   # calculate class of one student

    cursor.execute(f"SELECT final_gpa FROM final_gpatable WHERE  stu_ar = {reg}")
    p = cursor.fetchall()
    print(p[0][0])
    y = p[0][0]

    if 4.00 >= y >= 3.70:
        c = "First Class "
    elif 3.70 > y >= 3.30:
        c = "Second Upper Class"
    elif 3.30 > y >= 3.00:
        c = "Second Lower Class"
    else:
        c = "General Degree"

    print(c)


# calcRank()

calcAllgpa()

calcClass()

manageGPAtable()

calcOneClass(96301)

# calcFinalgpa(96453)
db.close()


