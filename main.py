
from rules import *
from newEmail import * 
from question import *
from jeopardyVars import *

def main():
    # user has limited appempts to update email address
    tries = 0
    limit = 3 
    
    greet()
    new_email = email_input()
    email_errors = validate_email(new_email) 
    print_errors(email_errors)
    new_email = update_email(new_email, tries, limit)
    email_dupes(new_email)
    #jeopardy = get_question()
    #jeopardyVars()

if __name__ == "__main__": 
    main()