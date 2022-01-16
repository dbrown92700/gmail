#!/usr/bin/python3
#
# Gmail integration requires an account with "Less Secure App Access" enabled
# in the security settings.  Consider using a dedicated gmail account for this
# app.
#

import smtplib
import sys

def send_email(local_user, local_password, plaintext_name, to, subject, body, mail_server, mail_port):

    # Defines function to send email using generic SMTP service
    # local_password is currently not implemented and requires a server without authentication

    try:
        server = smtplib.SMTP(mail_server, mail_port)
        server.ehlo()
    except:
        raise Exception('something went wrong with login')

    if type(to) == list:
        email_to = ', '.join(to)
    else:
        email_to = to

    email_text = f'From: "{plaintext_name}" <{local_user}>\n'
    email_text += f'Reply-To: "{plaintext_name}" <{local_user}>\n'
    email_text += f'To: {email_to}\n'
    email_text += f'Subject: {subject}\n\n{body}'''

    print(email_text)

    try:
        server.sendmail(local_user, to, email_text)
        print('Email sent.')
    except:
        raise Exception('something went wrong with email send')

    server.close()


def send_gmail(gmail_user, gmail_password, to, subject, body, plaintext_name='Gmail User'):

    # Defines function to send e-mail using gmail service.  Requires gmail account settings
    # to allow "Less secure apps" or login will be rejected.

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', port=465, source_address=('',0))
        server.ehlo()
        server.login(gmail_user, gmail_password)
    except Exception as e:
        print(f'Something went wrong with login...\n{e}')
        exit()

    if type(to)==list:
        email_to = ', '.join(to)
    else:
        email_to = to

    email_text = f'From: "{plaintext_name}" <{gmail_user}>\n'
    email_text += f'Reply-To: "{plaintext_name}" <{gmail_user}>\n'
    email_text += f'To: {email_to}\n'
    email_text += f'Subject: {subject}\n\n{body}'''

    print(email_text)

    try:
        server.sendmail(gmail_user, to, email_text)
        print('Email sent!')
    except:
        print('Something went wrong with email send...')

    server.close()

if __name__ == '__main__':
    #
    # send e-mail with cli
    # python3 gmail.py gmail_user@gmail.com password 'recipient1,recipient2,etc' 'email subject' 'email body' 'Plaintext Name'
    #
    send_gmail(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])