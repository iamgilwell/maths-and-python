import re
import getpass

''' A python CLI application to send email to specific individuals '''


def register(emailAddress, *args):
    print(len(args))
    # password = ''
    # password2 = ''
    global password, password2

    print(password)

    while(password != password2):
        print(password, password2)
        print("The password are not the same, please try again")
        password = getpass.getpass(prompt="Enter Password: ")
        password2 = getpass.getpass(prompt="Confirm Password: ")
    else:
        match = re.match(
            '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', emailAddress)

        while match is None:
            #
            print("Your Email is {}".format(emailAddress),
                  "Is not a valid email, please try again")
            emailAddress = input("Please Enter Your Email Address Again: ")
            match = re.match(
                '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', emailAddress)
        # register(emailAddress, args)
  # print(args[2])

    # if args['password'] == args['password2']:
    #     print("Your password did not match, please try again")
    #     password = getpass.getpass(prompt="Enter Password: ")
    #     password2 = getpass.getpass(prompt="Confirm Password: ")

    # else:
    print("Welcome to the 21st {}, {}".format(first_name, second_name),
          "further information being sent to your email")


first_name = input("Enter Your First Name: ")
second_name = input("Enter Your Second Name: ")
emailAddress = input("Enter your  Email Address: ")
password = getpass.getpass(prompt="Enter Password: ")
password2 = getpass.getpass(prompt="Confirm Password: ")
args = [first_name, second_name, password, password2]
register(*args)
