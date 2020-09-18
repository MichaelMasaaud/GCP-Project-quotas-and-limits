from google.oauth2.service_account import Credentials
from googleapiclient import discovery
import gspread
from google.cloud import bigquery
import pprint
import urllib3

gc = gspread.service_account(filename='sa.json')
file = gc.open('quota')

worksheet = file.worksheet(title='quota_limit_usage')

CLIENT_SECRETS_FILE_PATH = "sa.json"
AUTH_SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
table_id = 'quota.quota_usage'
base_credentials = Credentials.from_service_account_file(CLIENT_SECRETS_FILE_PATH,scopes=AUTH_SCOPES)
project_id = 'ivory-strategy-236322'

client = bigquery.Client(credentials=base_credentials, project=project_id)


service1 = discovery.build('cloudresourcemanager', 'v1', credentials=base_credentials)
service = discovery.build('compute','v1',credentials=base_credentials)
req = service1.projects()
res = req.list().execute()
worksheet.insert_row(['project Name', 'Metric Name ', 'Current Usage', 'Max limit per project', 'Utilization %'])
for i in range(len(res['projects'])):
    project = (res['projects'][i]['projectId'])
    request = service.projects().get(project=project).execute()
    for j in range(len(request['quotas'])):
        metric = request['quotas'][j]['metric']
        usage = request['quotas'][j]['usage']
        limit = request['quotas'][j]['limit']
        test = ('{0:.2f}%'.format((usage / limit * 100)))
        table = client.get_table(table_id)
        rows_to_insert = [(u'project_Name', project), (u'Metric_Name', metric), (u'Current Usage', usage), (u'Max_project', limit), (u'Utilization %', test)]
        client.insert_rows(table,rows_to_insert)
