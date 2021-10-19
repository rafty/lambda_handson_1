import json
import os
from decimal import Decimal
import boto3

# 環境変数
COUNTER_TABLE_NAME = os.environ['COUNTER_TABLE_NAME']

# boto3
dynamo = boto3.resource('dynamodb')
table = dynamo.Table(COUNTER_TABLE_NAME)


def decimal_encode(obj) -> object:
    if isinstance(obj, Decimal):
        return float(obj)


def handler(event, context):
    # event: dict type
    print('request: {}'.format(json.dumps(event)))

    table.update_item(
        Key={'path': event['path']},
        UpdateExpression='ADD calls :incr',
        ExpressionAttributeValues={':incr': 1}
    )

    response = table.get_item(
        Key={'path': event['path']},
        ConsistentRead=True
    )
    print('response: {}'.format(json.dumps(response, default=decimal_encode)))
    item = response['Item']

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': f'Api path "{event["path"]}": {item["calls"]} called.\n'
    }
    # return dict type
