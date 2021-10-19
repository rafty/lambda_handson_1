from aws_cdk import core as cdk
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_apigateway as apigw
from aws_cdk import aws_dynamodb as dynamo


class LambdaHandson1Stack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        table = dynamo.Table(
            self,
            'CountTable',  # Must be unique on the stack
            partition_key={
                'name': 'path',
                'type': dynamo.AttributeType.STRING
            }
        )

        # The code that defines your stack goes here
        counter_function = _lambda.Function(
            self,
            'CounterFunction',  # Must be unique on the stack
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset('api'),
            handler='counter.handler',
            environment={
                'COUNTER_TABLE_NAME': table.table_name
            }
        )

        table.grant_read_write_data(counter_function)

        apigw.LambdaRestApi(
            self,
            'CounterApi',
            handler=counter_function
        )

