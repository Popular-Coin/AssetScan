# https://developers.google.com/sheets/api/quickstart/python
from __future__ import print_function
import httplib2
import os

import sys
import psycopg2



from googleapiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

'''try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None'''

import boto3
# how to authenticate https://console.developers.google.com/apis/credentials?project=aqueous-charger-188403

conninfo=sys.argv[1]

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = os.path.abspath(__file__ + "/../../client_secret.json")
APPLICATION_NAME = 'Google Sheets API Python Quickstart'
rangepass="Sheet1!A1:B"


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if sys.version_info>(2,7    ,0):#flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def writetoS3():
	

	s3 = boto3.resource('s3', aws_access_key_id='aws_key', aws_secret_access_key='aws_sec_key')
	s3.Object('mybucket', 'sample.json').put(Body=open('data.json', 'rb'))
#key.set_contents_from_string(str) #to PUT your dicts' values directly.

    #See: http://boto.readthedocs.org/en/latest/ref/s3.html#module-boto.s3.key
def read_db_p():
    try:
        conn = psycopg2.connect(conninfo)
        cur = conn.cursor()

        cur.execute("select * from coinmarket_total")

        return cur.fetchone
    except psycopg2.Error as e:
        print (e)

def main():
    read_db_p()
    print (read_db_p())
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1UhiXbpMmP-fAK7r5dX5yPRoAhYuRd0-w9lUrdv0KKps'
    rangeName = rangepass#'Class Data!A2:E'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print(row)
            #print('%s, %s' % (row[0], row[4]))
    """
    

if __name__ == '__main__':
    main()