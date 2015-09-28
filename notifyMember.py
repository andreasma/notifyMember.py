from plone import api

portal = api.portal.get()

users = api.user.get_users()

for f in users:
  id = f.getProperty('id')
  name = f.getProperty('fullname')
  email = f.getProperty('email')
  
  api.portal.send_email(
    recipient=email,
    subject='New LibreOffice Extensions and Templates Website',
    body='''We created a new LibreOffice extensions and templates 
          website and set up an account for you. Please go to 
          Login for the new site under ... and ask for a reset 
          of your password. You will get an email with a link 
          to reset your password then''',
    )
