import mysql.connector
from mysql.connector import Error


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
        if option == 'a':
            travelyear = input("which year did you travel to?")
            tr_comment = input("Do you have any comment?")
            tr_revisit = input("Do you want to revisit?")
            sql = "insert into log(year,comment,revisit) VALUES (%s, %s, %s)"
            value = (travelyear, tr_comment, tr_revisit)
            cursor.execute(sql, value)
            conn.commit()
        elif option == 'd':
            sql = "DELETE FROM log WHERE year = %s"
            del_year = input("which year do you want to remove?")
            value_2 = (del_year,)
            cursor.execute(sql, value_2)
            conn.commit()
        elif option == 'u':
            new_amount = input("which year do you want to update?")
            update_year_query = """
            UPDATE year
            SET year = %s
            WHERE year > 1985""" % (new_amount)
            execute_query(conn, update_year_query)

            #sql = "UPDATE log SET year = %s WHERE year = %s"
            #year_1 = input("which year do you want to update?")
            #year_2 = input("To what year do you want to change it?")
            #value_3 = (year_1, year_2)
            #cursor.execute(sql, value_3)
            #conn.commit()
        elif option == "o":
            cursor.execute("SELECT * FROM log")
            row = cursor.fetchall()
            for x in row:
                print(x)
        elif option == "s":
            conn.commit()
        elif option == "q":
            print()
            break


print(menu_1())
print(main())

