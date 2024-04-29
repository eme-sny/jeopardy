import csv

# append new email address to csv  
def write_list (emails): #only do this is email is valid 
    filename = "email_list.csv"
    with open(filename, 'a') as csvfile: 
        writer = csv.writer(csvfile)
        for email in emails: 
            writer.writerow([email])

