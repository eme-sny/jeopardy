from trivia.rules import *
from addToList import * 
from trivia.trivia import *
from trivia.triviaVars import *
from emails.validateEmail import *
from emails.createEmail import *
import sys


def main():
    # user has limited appempts to update email address
    tries = 0
    limit = 3 
    question_email_subject = ("Today's Question")
    answer_email_subject = ("Today's Answer")
    valid_arguments = ["--new-email",
                       "--send",
                       "--question",
                       "--answer"]
    args = sys.argv
    
    if True:
        # get user's email address
        greet()
        new_email = email_input()
        validate_email(new_email)
        # user confirms email and upates if needed
        new_email = update_email(new_email, tries, limit)
        # check for email in list, if not already in list add it
        check_list_for_email(new_email, email_filename)
    elif args[1] == valid_arguments[1] and (args[2] == valid_arguments[2] or args[2] == valid_arguments[3]):
        email_list = from_csv_to_list(email_filename)
        if args[2] == valid_arguments[2]:
            q_email_body = get_question()
            question = q_email_body
            createEmail(email_sender, email_password, email_list, question_email_subject, question)
        elif args[2] == valid_arguments[3]:
            answer = read_answer_from_file(answer_filename)
            createEmail(email_sender, email_password, email_list, answer_email_subject, answer)
    else:
        print("Invalid argument")
        sys.exit()

    
if __name__ == "__main__": 
    main()