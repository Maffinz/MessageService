import smtplib

from email.mime.text import MIMEText

port = 587

sender = 'testingservicees@gmail.com'
receiver = '9564679450@messaging.sprintpcs.com'

msg = MIMEText('Secured test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'testingservicees@gmail.com'
msg['To'] = 'whernan2598@gmail.com'

user = 'testingservicees@gmail.com'
password = 'akufwrdqnmrlwrfb'

with smtplib.SMTP("smtp.gmail.com", port) as server:

    server.starttls() # Secure the connection

    server.login(user, password)
    server.sendmail(sender, receiver, msg.as_string())
    print("mail successfully sent")
