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
    valid_arguments = ["--new-email",
                       "--send",
                       "--question",
                       "--answer"]

    args = sys.argv

    
    if args[1] == valid_arguments[0]:
        # get user's email address
        greet()
        new_email = email_input()
        if validate_email(new_email) == True:
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
            with open (answer_filename, "r") as file:
                #### FIX: issue reading answer from file and into email body 
                answer = csv.reader(file)
                list_of_answers = list(answer)
                answer = str(list_of_answers[0])
            createEmail(email_sender, email_password, email_list, answer_email_subject, answer)
    else:
        print("Invalid argument")
        sys.exit()

    
if __name__ == "__main__": 
    main()