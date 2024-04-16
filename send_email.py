import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set up the SMTP server details
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # TLS port
sender_email = os.environ['SENDER_EMAIL']
sender_password = os.environ['SENDER_PASSWORD']

# Create a message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = os.environ['RECIPIENT_EMAIL']
message['Subject'] = os.environ['EMAIL_SUBJECT']

email_count = os.environ["EMAIL_COUNT"]

# Add body to email
body = os.environ['EMAIL_BODY']
message.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

# Login to Gmail
server.login(sender_email, sender_password)

# Send the email
for _ in range(int(email_count)):
    server.send_message(message)

# Quit the server
server.quit()

print("Email sent successfully!")
