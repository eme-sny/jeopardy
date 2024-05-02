from email.message import EmailMessage
import smtplib

def createEmail (sender, password, receiver, subject, body):

    em = EmailMessage()
    em['From'] = sender
    em['To'] = receiver
    em['Subject'] = subject
    em.set_content(body)

    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.login(sender,password)
    smtp.sendmail(sender, receiver, em.as_string( ))