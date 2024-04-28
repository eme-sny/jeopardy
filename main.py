
import csv
#import pandas as pd 

# get email address 
def greet ():
    print("Hello! Welcome to Jeapordy.\nOnce a day I'll send you a Jeapordy question, and later I'll follow up with the answer.")
    print()
    print("First, I'll need your email address.")

def email_input ():
    email = input("Type your email address: ")
    print()
    return email 


# validate email address 
# must have one '@'
# must have at least one '.'
# must be > or equal to 3 characters
# only contains letters, numbers, dashes, or underscores - loop through and check 
# contains at least on letter or number - loop through and count (for effieciency, stop once we find one)
def validate_email (email):
    error_count = 0
    error_set = set(())
    char1_count = 0
    char2_count = 0

    if len(email) < 3:
        error_count = error_count + 1 
        error_set = list(("Not enough characters"))
    for c in email:
        if c == "@":
            char1_count += 1  
            if char1_count > 1: 
                error_count += 1
                error_set.add("Too many @ symbols")
        elif c == ".":
            char2_count += 1
        elif not (c.isalpha()) and not (c.isnumeric()) and c != '-' and c != '/':
            error_set.add("Invalid character: " + c) 
    if char1_count < 1:
        error_set.add("Missing character: @")
    if char2_count < 1:
        error_set.add("Missing character: .")
    return error_set 

def print_errors (error_set): 
    if len(error_set) == 0:
        print("Thank you! Your email adddress is valid")
    else: 
        error_count = len(error_set)
        print("Your email address has " + str(error_count) + " errors:")
        for error in error_set: 
            print(error) # need to add something after this to make sure emails that aren't valid are not stored 
        print("Try again.... ")

def review_email (email):
    # user reviews email 
    user_check = input("Let's make sure I got that right. Your email address is " + email + "\nRight? (y/n)\n" )
    print()
    return user_check

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

# add email address to a list of eamil addresses 
# will there only ever be one email address? write to file to it keeps a running list 
def add_email (email):
    em_list = set()
    em_list.add(email)
    return em_list

def write_list (emails):
    filename = "email_list.csv"
    with open(filename, 'w') as csvfile: 
        writer = csv.writer(csvfile)
        for email in emails: 
            writer.writerow([email])





# send verificatoin email 

# user verifies email 




#ideas ... user can upload one or more email address via csv 
#remove email from list if get a undelivered response 



def main():
    tries = 0
    limit = 3 
    
    greet()
    new_email = email_input()
    email_errors = validate_email(new_email) 
    print_errors(email_errors)
    new_email = update_email(new_email, tries, limit)
    list = add_email(new_email)
    write_list(list)

if __name__ == "__main__": 
    main()