# Mass emailing for Eventbrite
This script is used to send emails from a Gmail account containing the tickets to all attendees for an Eventbrite event.

## Requirements
1. python3
2. Gmail account

## How to use
1. Download this repository, navigate to the "eventbrite-mass-ticket-email"
2. Download all tickets from Eventbrite and add them to the "tickets" folder
3. Download the CSV file of all attendees with their information, and add it to the eventbrite-mass-ticket-email repo
4. Make sure the Gmail account you are sending this from has an app password; see https://support.google.com/accounts/answer/185833?hl=en for how to create one. You will also need 2 factor authentication.
5. In send.py in the repository, edit "csv_filename" to add the name of the Eventbrite CSV file, "sender_email" to the email of the account you will send from, "password" to add the aforementioned App Password on Gmail, and "eventtitle" to add the title of the event.
6. Open a terminal in Python, cd to "eventbrite-mass-ticket-email", run "python3 send.py".
