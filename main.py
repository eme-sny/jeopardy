from jeopardy.rules import *
from addToList import * 
from jeopardy.jeopardy import *
from jeopardy.jeopardyVars import *
from emails.validateEmail import *
from emails.createEmail import *
from datetime import date
import os


def main():
    # user has limited appempts to update email address
    tries = 0
    limit = 3 
    subject = ("Today's Question")
    
    # get user's email address
    greet()
    new_email = email_input()

    # check email address for errors and print errors 
    email_errors = validate_email(new_email) 
    print_errors(email_errors)

    # user confirms email and upates if needed 
    new_email = update_email(new_email, tries, limit)
    
    # check for email in list, if not already in list add it 
    check_csv_for_item(new_email, email_filename)
    # read email csv file and store emails in list 
    email_list = from_csv_to_list(email_filename)

    # get jeopardy question and answer 
    # this will happen once a day before sending question email  
    question = str(get_question()["question"])
    #answer = get_question()["answer"]
#
    # send email with question 
    # this will be scheduled for start of day 
    createEmail(email_sender, email_password, email_list, subject, question)

    # send email with answer 
    # this will be scheduled for end of day 
    #createEmail(email_sender, email_password, email_list, subject, question)

    

   # sendEmail(question)
   # answer = get_answer()
   # sendEmail(answer)

    #jeopardyVars()

if __name__ == "__main__": 
    main()