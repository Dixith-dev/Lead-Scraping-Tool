import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# GoDaddy email settings
smtp_server = 'smtpout.secureserver.net'
smtp_port = 465  # Use 587 if you prefer to use TLS
email_address = 'dixith@tabrobotics.com'  # Replace with your GoDaddy email address
email_password = "Dixith_008"  # Use an environment variable for the password

# Email content
subject = 'Save 30+ hours a week automating booking appointments'
body = """
Hey,

I hope you are doing good, Dixith this side.

We offer AI agents to businesses like yours to help you save over 30 hours a week booking appointments.

Our AI agents, implemented on your website, qualify your new customers, book appointments for you, and automatically save their details in your preferred CRM.

Here is a demo :- https://dixith-pamgolding-bot.hf.space/   
The demo is located on the bottom right corner.

Contact us if you want this implemented on your website. We have made a personal demo for you too.
"""

def send_email(recipient, subject, body):
    """Send an email to the recipient."""
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connecting using SSL
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(email_address, email_password)
        text = msg.as_string()
        server.sendmail(email_address, recipient, text)
        server.quit()
        print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email to {recipient}: {e}")

def main():
    with open('Send_emails\\emails.txt', 'r') as file:
        emails = [line.strip() for line in file.readlines()]

    for email in emails:
        send_email(email, subject, body)

if __name__ == "__main__":
    main()
