import smtplib
import os
import webbrowser
msg ="""From: chandru,\n
        To: Santa,\n
        Sub:Shortlisted,\n

        hi, we are very lucky to have u in our company.
        but ,for the application process we charged 2,800 rs from ur bank account.
        thank u for appling.....
        welcome again
        '<a href="tel:7824847809">click here to call</a>'
        """
apppassword ='ecdzmpcbphlvpmkt'
smtpobj=smtplib.SMTP_SSL('smtp.gmail.com',465)
smtpobj.login('schandru16203@gmail.com',apppassword)
smtpobj.sendmail('schandru16203@gmail.com','2001721033016@mcc.edu.in',msg)
print('Done')