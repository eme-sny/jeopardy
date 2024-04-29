
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