import csv
import smtplib
import os
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def email_login(smtp_server_name, smtp_port, sender_email, password):
    server = smtplib.SMTP(host=smtp_server_name, port=smtp_port)
    server.connect(host=smtp_server_name, port=smtp_port)
    server.starttls()
    server.login(user=sender_email, password=password)
    return server

def send_email(sender_email, password, eventtitle, firstname, surname, receiver_email, filename):
    subject = eventtitle + ' tickets'
    fullname = firstname + ' ' + surname
    filename = 'tickets/' + filename

    content = f'''
    Hi {fullname},

    Here is your ticket for {eventtitle}.

    Thank you
    '''

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    body = MIMEText(content, 'plain')
    msg.attach(body)

    with open(filename, 'rb') as f:
        attachment = MIMEApplication(f.read(), Name=basename(filename))
        attachment['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))
    msg.attach(attachment)

    smtp_server_name = 'smtp.gmail.com'
    smtp_port = 587
    server = email_login(smtp_server_name, smtp_port, sender_email, password)

    server.send_message(msg, from_addr=sender_email, to_addrs=[receiver_email])
    server.quit()

    print('EMAIL SENT TO ' + fullname + filename)

def tickets_to_stack():
    files = os.listdir('tickets')
    ticket_stack = []
    for file in files:
        ticket_stack.append(file)
    
    return ticket_stack

def main():
    csv_filename = 'example.csv'
    sender_email = 'example@gmail.com'
    password = 'example'
    eventtitle = 'Title'
    attachment = ''

    ticket_stack = tickets_to_stack()
    print(ticket_stack)

    with open(csv_filename, mode='r') as file:
        csv_file = csv.reader(file)
        next(csv_file)

        for line in csv_file:
            #firstname = 3rd, aka [2]
            firstname = line[2]
            #surname = 4th, aka [3]
            surname = line[3]
            #email = 5th, aka [4]
            receiver_email = line[4]
            #print(line[2] + ' ' + line[3] + ' Email: ' + line[4])
            attachment = ticket_stack.pop()

            send_email(sender_email, password, eventtitle, firstname, surname, receiver_email, attachment)
            print('Number of tickets: ' + str(len(ticket_stack)))

    #UNCOMMENT FOR DEBUG
    #print('Number of tickets: ' + str(len(ticket_stack)))

if __name__=="__main__":
    main()