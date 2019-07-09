import re
''' A python CLI application to send email to specific individuals '''


def register(emailAddress, *args):
    match = re.match(
        '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', emailAddress)
    while match is None:
        #
        print("Your Email is {}".format(emailAddress),
              "Is not a valid email, please try again")
        emailAddress = input("Please Enter Your Email Address Again: ")
        break
    # register(emailAddress, args)

    # else:
    print("Welcome to the 21st {}, {}".format(first_name, second_name),
          "further information being sent to your email")


emailAddress = input("Enter your  Email Address: ")
first_name = input("Enter Your First Name: ")
second_name = input("Enter Your Second Name: ")
args = [first_name, second_name]
register(emailAddress, args)
