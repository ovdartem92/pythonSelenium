from __future__ import print_function

import base64
import os.path

import allure
from bs4 import BeautifulSoup
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from framework.utils.utils import get_project_root

CONFIG_PATH = fr"{get_project_root()}\\framework\\gmail_client\\"
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://mail.google.com/']


@allure.step("[Gmail Client] Authorize an gmail, return client")
def __authorize():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(CONFIG_PATH + 'token.json'):
        creds = Credentials.from_authorized_user_file(CONFIG_PATH + 'token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CONFIG_PATH + 'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(CONFIG_PATH + 'token.json', 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)


@allure.step("[Gmail Client] Print label")
def print_label():
    service = __authorize()
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])


@allure.step("[Gmail Client] Get message by subject")
def get_message_by_subject(subject_message):
    service = __authorize()
    result = service.users().messages().list(userId='me').execute()
    messages = result.get('messages')
    for msg in messages:
        # Get the message from its id
        txt = service.users().messages().get(userId='me', id=msg['id']).execute()

        # Use try-except to avoid any Errors
        try:
            # Get value of 'payload' from dictionary 'txt'
            payload = txt['payload']
            headers = payload['headers']

            # Look for Subject and Sender Email in the headers
            for d in headers:
                if d['name'] == 'Subject' and d['value'] == subject_message:
                    subject = d['value']

            # The Body of the message is in Encrypted format. So, we have to decode it.
            # Get the data and decode it with base 64 decoder.
            parts = payload.get('parts')[0]
            data = parts['body']['data']
            data = data.replace("-", "+").replace("_", "/")
            decoded_data = base64.b64decode(data)

            # Now, the data obtained is in lxml. So, we will parse
            # it with BeautifulSoup library
            soup = BeautifulSoup(decoded_data, "lxml")
            return {
                "Subject": subject,
                "Message": soup.body(),
            }
        except:
            pass


@allure.step("[Gmail Client] Delete all messages")
def delete_all_messages():
    service = __authorize()
    result = service.users().messages().list(userId='me').execute()
    messages = result.get('messages')
    if messages is None:
        return
    ids = []
    for msg in messages:
        # Get the message from its id
        ids.append(msg["id"])
    service.users().messages().batchDelete(userId="me", body={"ids": ids}).execute()


if __name__ == '__main__':
    delete_all_messages()
