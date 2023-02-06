import json


def hello(event, context):
    body = {
        "message": "Go aws-Serverless v7.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
