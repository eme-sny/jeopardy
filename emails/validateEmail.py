import re

# validate email address 
# must have one '@'
# must have at least one '.'
# must be > or equal to 3 characters
# only contains letters, numbers, dashes, or underscores - loop through and check 
# contains at least on letter or number - loop through and count (for effieciency, stop once we find one)
def validate_email (email):
   errors = []
#   validated_email = []
   char_count = len(email)
   at_char = 0
   per_char = 0
   validated_email = (re.findall(r"^\w{1,}[.|\w]{0,}[@]{1}[.|\w]{1,}[.]{1,}\w{1,}$", email))
   print(validated_email)
   if not validated_email:
       print("list is empty")

   for c in email:
       if c == "@":
           at_char =+ 1 
       elif c == ".":
           per_char =+ 1


   if len(validated_email) != 0:
       if validated_email[0] == email:
           print("Email address is valid. Adding to list....")
           return True
       else: 
           # to avoid throwing out valid email addresses 
           # an email address that doesn't match regex will still be added to the list 
           return True

   if not validated_email:
       errors.append("Email address has errors")
   if char_count < 3:
       errors.append("Too few characters")
   if char_count > 320:
       errors.append("Too many characters")
   if at_char == 0:
       errors.append("Missing @ symbol")
   if at_char > 1:
       errors.append("Too many @ symbols")
   if per_char == 0:
       errors.append("Missing . symbol")
       
   for e in errors:
       print(e)

   print("Try again.... ")
   return False






#def print_errors (error_set): 
#    if len(error_set) == 0:
#        print("Thank you! Your email adddress is valid")
#    else: 
#        error_count = len(error_set)
#        print("Your email address has " + str(error_count) + " errors:")
#        for error in error_set: 
#            print(error) # need to add something after this to make sure emails that aren't valid are not stored 
#        print("Try again.... ")