
# get email address 
def email_input ():
    print("Hello! Welcome to Jeapordy.\nOnce a day I'll send you a Jeapordy question, and later I'll follow up with the answer.")
    print()
    print("First, I'll need your email address.")
    email = input("Where should I send your Jeapordy question? ")
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
    else: 
        for c in email:
            if c == "@":
                char1_count = char1_count + 1  
                if char1_count > 1: 
                    error_count += 1
                    error_set.add("Too many @ symbols")
            elif c == ".":
                char2_count += 1
            elif not (c.isalpha()) and not (c.isnumeric()) and c != '-' and c != '/':
                error_set.add("Invalid character: " + c) 
    if char1_count < 1:
        error_set.add("Missing character: @")
    elif char2_count < 1:
        error_set.add("Missing character: .")
    return error_set 

def print_errors (error_set): 
    if len(error_set) == 0:
        print("Thank you! Your email adddress is valid")
    else: 
        error_count = len(error_set)
        print("Your email address has " + str(error_count) + " errors:")
        for error in error_set: 
            print(error)

# user can correct address if needed 
#user_check = input("Let's make sure I got that right. Your email address is " + email + "\nRight?" )

# send verificatoin email 

# user verifies email 

# add email address to a list of eamil addresses 



#ideas ... user can upload one or more email address via csv 
#remove email from list if get a undelivered response 



def main():
    new_email = email_input()
    email_errors = validate_email(new_email)
    print_errors(email_errors)


if __name__ == "__main__": 
    main()