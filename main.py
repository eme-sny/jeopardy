
from rules import *
from newEmail import * 
from writeEmail import *
from question import *

def main():
    # user has limited appempts to update email address
    tries = 0
    limit = 3 
    
    
    greet()
    new_email = email_input()
    email_errors = validate_email(new_email) 
    print_errors(email_errors)
    new_email = update_email(new_email, tries, limit)
    list = add_email(new_email)
    write_list(list)
    get_question()

if __name__ == "__main__": 
    main()