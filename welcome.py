import re
import getpass
import psycopg2
from datetime import datetime as dt

''' A python CLI application to send email to specific individuals '''


def register(*args):

    global password, password2, emailAddress
    match = re.match(
        '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', emailAddress)

    while(password != password2):
        print(password, password2)
        print("The password are not the same, please try again")
        password = getpass.getpass(prompt="Enter Password: ")
        password2 = getpass.getpass(prompt="Confirm Password: ")
    #
    while match is None:
        print("Your email is ++++++++++++++:{}".format(emailAddress))
        print("Your Email is {}".format(emailAddress),
              "Is not a valid email, please try again")
        emailAddress = input("Please Enter Your Email Address Again: ")
        match = re.match(
            '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', emailAddress)

    print("Welcome to the 21st {}, {}".format(first_name, second_name),
          "further information being sent to your email")
    data = (first_name, second_name, emailAddress, password)
    #print("This is the data", data)
    # return data

    try:
        connection = psycopg2.connect(user="postgres",
                                      password="",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="welcome")

        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        # dt = datetime.now()
        # print(dt)
        print(connection.get_dsn_parameters(), "\n")
        print("This is data from REGISTER+++++++++++++++++++++", data)
        print(dt.now())
        postgres_insert_query = """ INSERT INTO users (first_name, second_name, emailAddress,password) VALUES (%s,%s,%s,%s)"""
        record_to_insert = (data)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into mobile table")

        # Print PostgreSQL version
        # cursor.execute("SELECT version();")
        # record = cursor.fetchone()
        # print("You are connected to - ", record, "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


first_name = input("Enter Your First Name: ")
second_name = input("Enter Your Second Name: ")
emailAddress = input("Enter your  Email Address: ")
password = getpass.getpass(prompt="Enter Password: ")
password2 = getpass.getpass(prompt="Confirm Password: ")
args = [first_name, second_name, password, password2]
register(*args)
