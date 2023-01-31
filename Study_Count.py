from boto3 import resource
from boto3.dynamodb.conditions import Key, Attr

dynamodb_resource = resource('dynamodb')

# def query_table(table_name, key=None, value=None):
#     table = dynamodb_resource.Table(table_name)

#     if key is not None and value is not None:
#         filtering_exp = Key(key).eq(value)
#         return table.query(KeyConditionExpression=filtering_exp)

#     raise ValueError('Parameters missing or invalid')


# workspace_id=input("Enter workspace_id: ")
# resp = query_table(
#     table_name='decode-cx-study-details', 
#     key='workspace_id', 
#     value=workspace_id
# )
# items = resp.get('Items')


table = dynamodb_resource.Table("decode-cx-study-details")
def fun():
    res = table.query(
        KeyConditionExpression=Key('workspace_id').eq('01FSQ61M4D8M2S1ZEZK8KGG4RQ'),
        #FilterExpression=Attr('created_date').eq('2022-10-16T12:38:48.805466+0000')
        FilterExpression=Attr('created_date').begins_with('2022-10-16')

    )
    #print(res['Items'])
    items = res.get('Items')
    print(len(items))


fun()