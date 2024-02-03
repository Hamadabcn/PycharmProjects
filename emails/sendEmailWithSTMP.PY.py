import smtplib

sender_email = "triumphbcn@gmail.com"
receiver_email = "triumphbcn@gmail.com"
password = input(str("Please Enter Your Password: "))
message = "Subject: Python message.\nHello, This message is sent using python"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)
print("Login Successful")
server.sendmail(sender_email, receiver_email, message)
print("Mail sent successfully", receiver_email)
server.quit()
