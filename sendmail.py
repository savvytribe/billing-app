import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Setup port number and server name
smtp_port = 587  # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

# Set up the email lists
email_from = "from_user@gmail.com"
email_list = [
    "to_user1@gmail.com",
    "to_user2@gmail.com",
    "to_user3@gmail.com",
]

# Mail password (better to reference externally)
pswd = "SomePass123"


# Email subject
subject = "New email from Sender with attachments!!"


# Define the email function
def send_emails(email_list):
    for person in email_list:
        # Body of the email
        body = f"""
        line 1
        line 2
        line 3
        etc
        """

        # MIME object to define parts of the email
        msg = MIMEMultipart()
        msg["From"] = email_from
        msg["To"] = person
        msg["Subject"] = subject

        # Attach the body of the message
        msg.attach(MIMEText(body, "plain"))

        # Define the file to attach
        filename = "some_file.csv"

        # Open the file
        attachment = open(filename, "rb")

        # Encode as base 64
        attachment_package = MIMEBase("application", "octet-stream")
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header(
            "Content-Disposition", "attachment; filename= " + filename
        )
        msg.attach(attachment_package)

        # Cast as string
        text = msg.as_string()

        # Connect to server
        print("Connecting to server...")
        mail_server = smtplib.SMTP(smtp_server, smtp_port)
        mail_server.starttls()
        mail_server.login(email_from, pswd)
        print("Succesfully connected to server")
        print()

        # Send emails to "person" as list is iterated
        print(f"Sending email to: {person}...")
        mail_server.sendmail(email_from, person, text)
        print(f"Email sent to: {person}")
        print()

    # Close the port
    mail_server.quit()


# Run the function
send_emails(email_list)
