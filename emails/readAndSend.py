import ezgmail

print(ezgmail.EMAIL_ADDRESS)  # this will send back my email

# this to send emails
# ezgmail.send('triumphbcn@gmail.com', 'Test line', 'Test body of the email', ['test.jpg', 'test1.jpg'])

# get the unread messages
# unreadMessages = ezgmail.unread()  # this will return an object from gmail thread (conversation threads)
#
# print(ezgmail.summary(unreadMessages))  # this will read the unread emails
# print(len(unreadMessages))

# you can get the first unread email by:
# index 0 first email (if there are more than one email, and you want to get the first one you have to add .messages)
# first of the first email
# print(unreadMessages[0].messages[0])
# print(unreadMessages[0].messages[0].subject)  # this will return only the subject
# print(unreadMessages[0].messages[0].body)  # this will return the body
# print(unreadMessages[0].messages[0].timestamp)  # this will return the time the email was received
# print(unreadMessages[0].messages[0].sender)  # this will show was sent the message
# print(unreadMessages[0].messages[0].recipient)  # to whom was it delivered

# now we are going to use something different from .unread and it called recent
recentThread = ezgmail.recent()
print(len(recentThread))

recentMessages = ezgmail.recent(maxResults=50)  # this will bring the last 50 unread messages
print(len(recentThread))

# search for an email
resultThread = ezgmail.search('MongoDB')  # this will search for a specific sender
print(len(resultThread))

