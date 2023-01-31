from boto3 import resource
from boto3.dynamodb.conditions import Key

lis=[]
dynamodb_resource = resource('dynamodb')

def query_table(table_name, key=None, value=None):
    global total_items
    table = dynamodb_resource.Table(table_name)
    total_items = table.item_count

    if key is not None and value is not None:
        filtering_exp = Key(key).eq(value)
        return table.query(KeyConditionExpression=filtering_exp)

    raise ValueError('Parameters missing or invalid')


workspace_id=input("Enter workspace_id: ")
resp = query_table(
    table_name='decode-cx-study-details', 
    key='workspace_id', 
    value=workspace_id
)
items = resp.get('Items')


for i in range(0,total_items):
    items[i]["created_date"]=items[i]["created_date"].split(sep='T', maxsplit=1)
    items[i]["created_date"]=items[i]["created_date"][0]
    lis.append(items[i]["created_date"])

    #2022-10-16T12:38:48.805466+0000
    #2022-10-16T12:38:48.805466+0000
    