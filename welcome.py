import re
import getpass
import psycopg2
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


first_name = input("Enter Your First Name: ")
second_name = input("Enter Your Second Name: ")
emailAddress = input("Enter your  Email Address: ")
password = getpass.getpass(prompt="Enter Password: ")
password2 = getpass.getpass(prompt="Confirm Password: ")
args = [first_name, second_name, password, password2]
register(*args)


try:
    connection = psycopg2.connect(user="postgres",
                                  password="",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="welcome")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
