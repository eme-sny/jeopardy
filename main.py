from jeopardy.rules import *
from addToList import * 
from jeopardy.jeopardy import *
from jeopardy.jeopardyVars import *
from emails.validateEmail import *
import os

def main():
    # user has limited appempts to update email address
    tries = 0
    limit = 3 
    
    greet()
    new_email = email_input()
    email_errors = validate_email(new_email) 
    print_errors(email_errors)
    new_email = update_email(new_email, tries, limit)
    check_csv_for_item(new_email, email_list)
    question = get_question()
   # sendEmail(question)
   # answer = get_answer()
   # sendEmail(answer)

    #jeopardyVars()

if __name__ == "__main__": 
    main()