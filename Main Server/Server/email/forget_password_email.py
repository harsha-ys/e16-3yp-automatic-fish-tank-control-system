import smtplib

from Server.email.config import GMAIL_APP_PASSWORD,GMAIL_USER
from Server.db.controllers.handlers import retrieve_user


async def forgetPasswordEmailSend(email):
    user=await retrieve_user(email)
    if not user:
        return
    password=user['password']
    sent_from = GMAIL_USER
    sent_to = [email,]
    sent_subject = "Your Password"
    sent_body = ("Hey, your password is!\n\n"
                +password+"\n"
                "\n"
                "Cheers,\n"
                "Fish Com\n")

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(sent_to), sent_subject, sent_body)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        server.sendmail(sent_from, sent_to, email_text)
        server.close()
        print('Email sent!')
        
    except Exception as exception:
        print("Error: %s!\n\n" % exception)