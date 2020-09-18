
from google.oauth2.service_account import Credentials
from googleapiclient import discovery
from google.cloud import bigquery



CLIENT_SECRETS_FILE_PATH = "sa.json"
AUTH_SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
table_id = '<project_id>.<dataset>.<tableid>'
base_credentials = Credentials.from_service_account_file(CLIENT_SECRETS_FILE_PATH,scopes=AUTH_SCOPES)
project_id = '<project_id>'

client = bigquery.Client(credentials=base_credentials, project=project_id)


service1 = discovery.build('cloudresourcemanager', 'v1', credentials=base_credentials)
service2 = discovery.build('compute','v1',credentials=base_credentials)
req = service1.projects()
res = req.list().execute()
table = client.get_table(table_id)

for p in res['projects'][0:5]:
    print(p['projectId'])
    request = service2.projects().get(project=p['projectId']).execute()
    for q in request['quotas']:
        metric = q['metric']
        usage = q['usage']
        limit = q['limit']
        rows_to_insert = [(p['projectId']), (metric), (usage), (limit)]
        errors = client.insert_rows(table, [rows_to_insert])
        if errors == []:
            print("New row have been added")
        print(metric, usage, limit, errors)

