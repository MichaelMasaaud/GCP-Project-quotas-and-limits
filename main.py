from google.oauth2.service_account import Credentials
from googleapiclient import discovery
import gspread
import pprint

gc = gspread.service_account(filename='sa.json')
file = gc.open('quota')

worksheet = file.worksheet(title='quota_limit_usage')

CLIENT_SECRETS_FILE_PATH = "sa.json"
AUTH_SCOPES = ['https://www.googleapis.com/auth/cloud-platform']

base_credentials = Credentials.from_service_account_file(CLIENT_SECRETS_FILE_PATH,scopes=AUTH_SCOPES)


service1 = discovery.build('cloudresourcemanager', 'v1', credentials=base_credentials)
service = discovery.build('compute','v1',credentials=base_credentials)

project = 'ivory-strategy-236322'
region = 'us-central1'



request = service.regions().get(project=project, region=region)
response = request.execute()

pprint.pprint(response)

