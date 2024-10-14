import json
import requests


def lambda_handler(event, context):

    if event.get("requestContext", None) is not None:
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "This message is from api gateway process"
            }),
        }

    if event.get("Records", None) is not None:
        response = []
        for record in event['Records']:
            response.append(
                {
                    'messageId':record['messageId'],
                    'correlationId': record['messageAttributes']['correlationId'],
                    'body': record['body']
                }
            )

        return {

            "statusCode": 200,
            "body": json.dumps({
                "data": response,
                "message": "Is from SQS"
            }),
        }