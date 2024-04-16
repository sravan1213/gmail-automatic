# Email Sending Script

This Python script sends emails using the SMTP (Simple Mail Transfer Protocol) server. It is designed to be used with Gmail, but it can be modified to work with other SMTP servers as well.

## Prerequisites

Before running the script, make sure you have the following:

1. **Python**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).

2. **SMTP Server**: This script uses Gmail's SMTP server by default (`smtp.gmail.com`). If you're using a different SMTP server, you'll need to modify the `smtp_server` variable accordingly.

3. **Gmail Account**: You need a Gmail account to send emails. Make sure you have the sender's email address and password handy.

4. **Environment Variables**: This script uses environment variables for sensitive information like sender's email, password, recipient's email, etc. Set the following environment variables before running the script:
   - `SENDER_EMAIL`: Your Gmail email address.
   - `SENDER_PASSWORD`: Your Gmail account password.
   - `RECIPIENT_EMAIL`: Email address of the recipient.
   - `EMAIL_SUBJECT`: Subject of the email.
   - `EMAIL_BODY`: Body of the email.
   - `EMAIL_COUNT`: Number of emails to send (optional, defaults to 1).

## Usage

1. Clone this repository or download the script `send_email.py` to your local machine.

2. Set the required environment variables in your system. You can do this using the terminal/command prompt:

   ```bash
   export SENDER_EMAIL="your_email@gmail.com"
   export SENDER_PASSWORD="your_password"
   export RECIPIENT_EMAIL="recipient_email@example.com"
   export EMAIL_SUBJECT="Your Email Subject"
   export EMAIL_BODY="Your Email Body"
   export EMAIL_COUNT="5"  # Number of emails to send (optional)
   ```

3. Run the script using Python:

   ```bash
   python send_email.py
   ```

4. After execution, the script will send the specified number of emails to the recipient.

## Notes

- This script uses TLS (Transport Layer Security) to secure the connection to the SMTP server.
- Make sure to keep your Gmail account credentials secure and never share them in plain text.
- Depending on your email provider and security settings, you might need to allow less secure apps to access your Gmail account. You can do this in your Gmail account settings under "Security."
