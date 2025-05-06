import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Optional


class EmailClien:
    def __init__(
            self,
            login: str,
            password: str,
            smtp_server: str = 'smtp.gmail.com',
            smtp_port: int = 587,
            imap_server: str = 'imap.gmail.com'
    ):
        self.login = login
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.imap_server = imap_server

    def send_email(self, subject: str, message: str, recipients: List[str]) -> None:
        """Send an email with the given subject and message to the recipients."""
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as smtp_conn:
            smtp_conn.ehlo()
            smtp_conn.starttls()
            smtp_conn.ehlo()
            smtp_conn.login(self.login, self.password)
            smtp_conn.sendmail(self.login, recipients, msg.as_string())

    def receive_latest_email(self, header: Optional[str] = None) -> email.message.Message:
        """
        Fetch the latest email matching the header. If no header is specified, fetch the latest email.

        Returns:
            email.message.Message: Parsed email message object.
        """
        with imaplib.IMAP4_SSL(self.imap_server) as imap_conn:
            imap_conn.login(self.login, self.password)
            imap_conn.select('inbox')

            criterion = f'(HEADER Subject "{header}")' if header else 'ALL'
            result, data = imap_conn.uid('search', None, criterion)

            if not data[0]:
                raise ValueError('No emails found with the specified header')

            latest_email_uid = data[0].split()[-1]
            result, data = imap_conn.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]

        return email.message_from_bytes(raw_email)


if __name__ == '__main__':
    client = EmailClien(
        login='login@gmail.com',
        password='qwerty'
    )

    # Send email.
    client.send_email(
        subject='Subject',
        message='Message',
        recipients=['vasya@email.com', 'petya@email.com']
    )

    # Recieve latest email.
    try:
        latest_email = client.receive_latest_email()
        print('From:', latest_email['From'])
        print('Subject:', latest_email['Subject'])
    except ValueError as err:
        print('Error:', err)
