import re
''' A python CLI application to send email to specific individuals '''


def enter_email_address(emailAddress):
   # emailAddress = input("Enter your name: ")
    # print(inputEmail)

    #print("Your Email is {}".format(inputEmail))

    match = re.match(
        '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', emailAddress)

    if match == None:
        print("Your Email is {}".format(emailAddress),
              "Is not a valid email, please try again")
        emailAddress = input("Enter your name: ")
        enter_email_address(emailAddress)
        #raise ValueError('Bad Syntax')
    else:
        print("Welcome to the 21st, further information being sent to your email")


emailAddress = input("Enter your name: ")
enter_email_address(emailAddress)
