from plone import api

portal = api.portal.get()

users = api.user.get_users()

f = open('message.txt')
message = f.read()

for g in users:
  id = g.getProperty('id')
  name = g.getProperty('fullname')
  email = g.getProperty('email')
  
  api.portal.send_email(
    recipient=email,
    subject='New LibreOffice Extensions and Templates Website',
    body=message,
    )
