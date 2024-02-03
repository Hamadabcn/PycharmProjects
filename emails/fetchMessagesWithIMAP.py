import imapclient
import pprint
import pyzmail

# connect to server
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)

# login to email
rec_email = "triumphbcn@gmail.com"
password = input(str('Please enter your password: '))

imapObj.login(rec_email, password)

# print all folders
pprint.pprint(imapObj.list_folders())

# select folder
imapObj.select_folder("INBOX", readonly=True)

# search in folder
UIDs = imapObj.search(['All'])
print(UIDs)

raw_messages = imapObj.fetch(UIDs,['BODY[]'])
# pprint.pprint(raw_messages)

message = pyzmail.PyzMessage.factory(raw_messages[2021][b'BODY[]'])  # '2021' is an email in my inbox
print(message.get_subject())  # this will get the subject of the email
print(message.get_addresses('from'))  # this will get who sent the email
print(message.get_addresses('to'))  # this will get to whom the email was sent

# get message body
print(message.text_part.get_payload().decode(message.text_part.charset))  # gets the text

print(message.html_part.get_payload().decode(message.text_part.charset))  # gets the html

imapObj.logout()
