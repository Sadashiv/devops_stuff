import smtplib

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.ehlo()
print(smtp_obj.ehlo())
#smtp_obj.starttls()
print(smtp_obj.starttls())

import getpass
#kaxt oxva fzqj pvkt
email = 'abc@gmail.com'
password='*****************' #use app password from gmail
smtp_obj.login(email, password)

from_address = 'abc@gmail.com'
to_address = 'xyz@gmail.com'
subject = "Test email"
message = "Hello how are you"
msg = "Subject: "+subject+'\n'+message
smtp_obj.sendmail(from_address, to_address, msg)
#imaplib to receive email

