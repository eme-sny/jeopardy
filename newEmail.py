from validateEmail import *

receivers = []

# user provides email address
def email_input ():
    email = input("Type your email address: ")
    print()
    return email 

# user confirms email 
def review_email (email):
    # user reviews email 
    user_check = input("Let's make sure I got that right. Your email address is " + email + "\nRight? (y/n)\n" )
    print()
    return user_check

# user can update email with a limited number of tries 
def update_email (email, tries, limit):
    while tries < limit - 1: 
        is_correct = review_email(email)
        if is_correct == "y": 
            up_email = email
            print("Great!")
            break
        elif is_correct == "n": 
            up_email = email_input()
            tries += 1
            email_errors = validate_email(up_email) 
            print_errors(email_errors)
            update_email(up_email, tries, limit - tries)
        else: 
            print("Invalid input")
            up_email = email_input()
            tries += 1 
            email_errors = validate_email(up_email) 
            print_errors(email_errors)
            update_email(up_email, tries, limit - tries)
    return up_email

# add email address to a list of email addresses 
# uses a set to avoid duplicates 
def add_email (email):
    with open("email_list.csv", "a") as file:
        file.write(email)


# read csv into list 
def email_dupes(email):
    with open("email_list.csv", 'r') as file: 
        receivers = file.read().splitlines()
        print(receivers)
    if email in receivers: 
        print("Email already in list")
    else:
        add_email(email)
        print("Email added")
