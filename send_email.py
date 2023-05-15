import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    smtp_server = 'server_smtp'
    smtp_port = 587
    smtp_username = 'adresa_de_email'
    smtp_password = 'parola'

    sender_email = 'adresa_de_email'
    recipient_email = request.form['recipient']
    subject = request.form['subject']
    message_text = request.form['message']

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    message.attach(MIMEText(message_text, 'plain'))

    smtp_server = smtplib.SMTP(smtp_server, smtp_port)
    smtp_server.starttls()
    smtp_server.login(smtp_username, smtp_password)
    smtp_server.sendmail(sender_email, recipient_email, message.as_string())
    smtp_server.quit()

    return 'E-mailul a fost trimis cu succes!'

if __name__ == '__main__':
    app.run()
