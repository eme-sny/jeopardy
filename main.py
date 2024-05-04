from jeopardy.rules import *
from addToList import * 
from jeopardy.jeopardy import *
from jeopardy.jeopardyVars import *
from emails.validateEmail import *
from emails.createEmail import *
import sys


def main():
    # user has limited appempts to update email address
    tries = 0
    limit = 3 
    question_email_subject = ("Today's Question")
    answer_email_subject = ("Today's Answer")
    
    # get user's email address
    #greet()
    new_email = email_input()

    # check email address for errors and print errors 
   # email_errors = validate_email(new_email) 
    if validate_email(new_email) == True:
        # user confirms email and upates if needed
        #new_email = update_email(new_email, tries, limit)
        # check for email in list, if not already in list add it
        check_csv_for_item(new_email, email_filename)
        # read email csv file and store emails in list
        email_list = from_csv_to_list(email_filename)
    else:
        sys.exit()


    # save api response with question and answers 
    # parse api response 
    # save question and answer choices in email formatted string 
    email_bodies = get_question()
    question = email_bodies[0]
    answer = email_bodies[1]

    # send email with question 
    # this will be scheduled for start of day 
    createEmail(email_sender, email_password, email_list, question_email_subject, question)

    # send email with answer 
    # this will be scheduled for end of day 
    createEmail(email_sender, email_password, email_list, answer_email_subject, answer)


if __name__ == "__main__": 
    main()