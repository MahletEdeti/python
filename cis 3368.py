import mysql.connector
from mysql.connector import Error


# creating a connection
def create_con(hostname, username, userpw, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=hostname,
            user=username,
            password=userpw,
            database=dbname
        )
        print("success")
    except Error as e:
        print(f'the {e} occurred')
    return connection


conn = create_con('cis3368fall.cew5xs3nurup.us-east-2.rds.amazonaws.com', 'mwedeti', 'admin2816', 'cis3368')
cursor = conn.cursor()


def execute_read_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f'the {e} occurred')


# output the Menu
def menu_1():
    menu = """MENU
    a – Add travel log
    d – Remove travel log
    u – Update travel log
    o – Output entire log in console
    s – Save travel log to database
    q – Quit
   choose an option:"""
    return menu


def main():
    while True:
        option = input()
        if option == 'a':  # if the user choose 'a' it will add an info
            travelyear = input("which year did you travel to?")
            tr_comment = input("Do you have any comment?")
            tr_revisit = input("Do you want to revisit?")
            sql = "insert into log(year,comment,revisit) VALUES (%s, %s, %s)"
            value = (travelyear, tr_comment, tr_revisit)
            cursor.execute(sql, value)
            conn.commit()
        elif option == 'd':  # user can remove by using year
            sql = "DELETE FROM log WHERE year = %s"
            del_year = input("which year do you want to remove?")
            value_2 = (del_year,)
            cursor.execute(sql, value_2)
        elif option == 'u':
            year_1 = 2022
            sql = "UPDATE log SET year = %s  WHERE  year > 2022" % year_1
            cursor.execute(sql)
            conn.commit()
        elif option == "o":
            cursor.execute("SELECT * FROM log")
            row = cursor.fetchall()
            for x in row:
                print(x)



print(menu_1())
print(main())
