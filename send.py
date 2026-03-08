"""
Email Automation Script
Send emails with Python
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender, password, recipient, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())
    
    print(f"Email sent to {recipient}")

if __name__ == "__main__":
    send_email(
        'your@email.com',
        'your_password',
        'to@email.com',
        'Subject',
        'Body'
    )
