import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

def send_email(receiver_email, subject, message, image_path, attachment_path):  
      
    smtp_server = 'smtp.office365.com'
    smtp_port = 587
    username = 'email.com'
    password = 'password'
    
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = username
    # msg['To'] = receiver_email
    msg['To'] = ', '.join(receiver_email)
    msg['Subject'] = subject

    # Create an HTML message body
    html_message = f"""
    <html>
        <body>
            <h1>{subject}</h1>
            <p>{message}</p>
            <p>This is a <b>bold</b> text example.</p>
            <p>This is an <i>italic</i> text example.</p>
            <p>This is a <a href="https://www.example.com">link</a> example.</p>
            <img src="cid:image1" alt="Image">
        </body>
    </html>
    """

    # Attach the HTML message body
    msg.attach(MIMEText(html_message, 'html'))
    
    # Add the image part
    with open(image_path, 'rb') as image_file:
        image_part = MIMEImage(image_file.read())
        image_part.add_header('Content-ID', '<image1>')
        msg.attach(image_part)
 
    # # Add the file attachment
    # with open(attachment_path, 'rb') as attachment_file:
    #     attachment_part = MIMEApplication(attachment_file.read())
    # attachment_part.add_header('Content-Disposition', 'attachment', filename='attachment.pdf')
    # msg.attach(attachment_part)
    
    # Create a SMTP session
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(msg)

# Provide the necessary details for your email
receiver_email_list = ['receiver.email.com']
subject = 'Hello from Python!'
message = 'This is a test email sent using Python.'
image_path = '/Users/ronyip/Projects/Toppwork/email sender/hunghing.jpg'  
attachment_path = '/Users/ronyip/Projects/Toppwork/email sender/ZKG_A2101-onepage.pdf'

# Call the send_email function
send_email(receiver_email_list, subject, message, image_path, attachment_path)