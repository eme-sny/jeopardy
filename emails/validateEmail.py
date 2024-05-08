import re
import sys

# validate email address 
# must have one '@'
# must have at least one '.'
# must be > or equal to 3 characters
# only contains letters, numbers, dashes, or underscores - loop through and check 
# contains at least on letter or number - loop through and count (for effieciency, stop once we find one)
def validate_email (email):
   errors = []
   char_count = len(email)
   at_char = 0
   per_char = 0
   validated_email = (re.findall(r"^\w{1,}[.|\w]{0,}[@]{1}[.|\w]{1,}[.]{1,}\w{1,}$", email))

   for c in email:
       if c == "@":
           at_char =+ 1 
       elif c == ".":
           per_char =+ 1

   if len(validated_email) != 0:
       if validated_email[0] == email:
           print("Email address is valid. Adding to list....")
      # else: 
      #     # to avoid throwing out valid email addresses 
      #     # an email address that doesn't match regex will still be added to the list 
      #     return True

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
    
   if errors: 
       print("Try again.... ")
       sys.exit()
