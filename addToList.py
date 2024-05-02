from emails.validateEmail import *
import os
import csv

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
# need to update this to use regular expression 
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

# adds an item to a csv file 
def add_item_to_csv (item, csv):
    with open (csv, "a") as file:
        file.write("\n" + item)
    print("Item added")
        
# add item to file if file exists 
def check_csv_for_item(item, csv):
    if does_file_exist == True:
        with open(csv, 'r') as file: 
            inFile = file.read().splitlines()
            if item in inFile: 
                print("Item already in list")
            else:
                add_item_to_csv (item, csv)

    else:
        add_item_to_csv(item, csv)

# check if file exists and return boolean 
def does_file_exist(csv):
    return os.path.isfile(csv)

# write csv to list 
def from_csv_to_list (file):
    with open(file, 'r') as file:
        items = csv.reader(file)
        list_of_items = list(items)
    print(list_of_items)
    return(list_of_items)