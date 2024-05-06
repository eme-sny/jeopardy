from emails.validateEmail import *
import os
import csv
import sys

# user provides email address
def email_input ():
    email = input("Type your email address: ")
    print()
    return email 

# user confirms email 
def review_email (email):
    # user reviews email 
    user_check = input("Is this correct:  " + email + "?     (y/n)\n" )
    print()
    return user_check

# user can update email with a limited number of tries 
# need to update this to use regular expression 
def update_email (email, tries, limit):
    while tries < limit - 1: 
        is_correct = review_email(email)
        if is_correct == "y": 
            up_email = email
            break
        elif is_correct == "n": 
            up_email = email_input()
            tries += 1
            is_email_valid = validate_email(up_email) 
            if is_email_valid == True:
                break
            else:
                update_email(up_email, tries, limit - tries)
        else: 
            print("Invalid input")
            sys.exit()
    return up_email




# add item to file if file exists 
def check_list_for_email(email, email_list):
    if does_email_list_exist(email_list) == True:
        with open(email_list, 'r') as file: 
            inFile = file.read().splitlines()
            if email in inFile: 
                print("Email already in list")
            else:
                add_email_to_list (email, email_list)

    else:
        add_email_to_list(email, email_list)

# adds an item to a csv file 
def add_email_to_list (email, email_list):
    email = str(email)
    with open (email_list, "a") as file:
        file.write(email + "\n")
    print("Item added")

# check if file exists and return boolean 
def does_email_list_exist(email_list):
    return os.path.isfile(email_list)






# write email list csv to list object prior to sending the email 
def from_csv_to_list (email_file):
    with open(email_file, 'r') as file:
        emails = csv.reader(file)
        list_of_emails = list(emails)
    return list_of_emails