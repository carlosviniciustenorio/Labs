import json

import pytest

from hello_world import app


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
        "body": '{ "test": "body"}',
        "resource": "/{proxy+}",
        "requestContext": {
            "resourceId": "123456",
            "apiId": "1234567890",
            "resourcePath": "/{proxy+}",
            "httpMethod": "POST",
            "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
            "accountId": "123456789012",
            "identity": {
                "apiKey": "",
                "userArn": "",
                "cognitoAuthenticationType": "",
                "caller": "",
                "userAgent": "Custom User Agent String",
                "user": "",
                "cognitoIdentityPoolId": "",
                "cognitoIdentityId": "",
                "cognitoAuthenticationProvider": "",
                "sourceIp": "127.0.0.1",
                "accountId": "",
            },
            "stage": "prod",
        },
        "queryStringParameters": {"foo": "bar"},
        "headers": {
            "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
            "Accept-Language": "en-US,en;q=0.8",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-SmartTV-Viewer": "false",
            "CloudFront-Is-Mobile-Viewer": "false",
            "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
            "CloudFront-Viewer-Country": "US",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Upgrade-Insecure-Requests": "1",
            "X-Forwarded-Port": "443",
            "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
            "X-Forwarded-Proto": "https",
            "X-Amz-Cf-Id": "aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==",
            "CloudFront-Is-Tablet-Viewer": "false",
            "Cache-Control": "max-age=0",
            "User-Agent": "Custom User Agent String",
            "CloudFront-Forwarded-Proto": "https",
            "Accept-Encoding": "gzip, deflate, sdch",
        },
        "pathParameters": {"proxy": "/examplepath"},
        "httpMethod": "POST",
        "stageVariables": {"baz": "qux"},
        "path": "/examplepath",
    }


@pytest.fixture()
def sqs_message():
    return {
        "Records": [
            {
                "messageId": "1e1e8b06-bc5f-4c4e-8d7f-1d9d8b6377f3",
                "receiptHandle": "AQEBFzLzFZ3K2sECRnGzV2Xa5fp7C4s1Z2FPzznWVZDrKY9SloFHJZZpGDCROw8/Uh+cFcGVuXYQThDJh1iwKNXKnA==",
                "body": json.dumps({
                    "ContratacaoId": "12345",
                    "NomeCliente": "João Silva",
                    "CodigoPessoa": "789456",
                    "ClienteDocumento": "123.456.789-00",
                    "CaminhoPdfBucket": "s3://meu-bucket/documento.pdf",
                    "ValorContrato": 15000.0,
                    "ClienteEmail": "joao.silva@email.com",
                    "ClienteTelefone": "+55 11 98765-4321"
                }),
                "attributes": {
                    "ApproximateReceiveCount": "1",
                    "SentTimestamp": "1634224747423",
                    "SenderId": "AIDAEXAMPLE",
                    "ApproximateFirstReceiveTimestamp": "1634224747424"
                },
                "messageAttributes": {
                    "correlationId":"1234-5678-9012-3456"
                },
                "md5OfBody": "e99a18c428cb38d5f260853678922e03",
                "eventSource": "aws:sqs",
                "eventSourceARN": "arn:aws:sqs:us-east-1:123456789012:minha-fila",
                "awsRegion": "us-east-1"
            },
            {
                "messageId": "1e1e8b06-bc5f-4c4e-8d7f-1d9d8b6377f4",
                "receiptHandle": "AQEBFzLzFZ3K2sECRnGzV2Xa5fp7C4s1Z2FPzznWVZDrKY9SloFHJZZpGDCROw8/Uh+cFcGVuXYQThDJh1iwKNXKnA==",
                "body": json.dumps({
                    "ContratacaoId": "12346",
                    "NomeCliente": "Paulo",
                    "CodigoPessoa": "789456",
                    "ClienteDocumento": "123.456.789-00",
                    "CaminhoPdfBucket": "s3://meu-bucket/documento.pdf",
                    "ValorContrato": 15000.0,
                    "ClienteEmail": "joao.silva@email.com",
                    "ClienteTelefone": "+55 11 98765-4321"
                }),
                "attributes": {
                    "ApproximateReceiveCount": "1",
                    "SentTimestamp": "1634224747423",
                    "SenderId": "AIDAEXAMPLE",
                    "ApproximateFirstReceiveTimestamp": "1634224747424"
                },
                "messageAttributes": {
                    "correlationId": "1234-5678-9012-3457"
                },
                "md5OfBody": "e99a18c428cb38d5f260853678922e03",
                "eventSource": "aws:sqs",
                "eventSourceARN": "arn:aws:sqs:us-east-1:123456789012:minha-fila",
                "awsRegion": "us-east-1"
            }
        ]
    }

def test_lambda_handler_from_apiGtw(apigw_event):

    ret = app.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] == "This message is from api gateway process"


def test_lambda_handler_from_sqs(sqs_message):
    response = app.lambda_handler(sqs_message, "")
    data = json.loads(response["body"])
    assert response["statusCode"] == 200
    assert data["message"] == "Is from SQS"