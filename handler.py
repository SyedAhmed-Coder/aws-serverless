import json


def hello(event, context):
    body = {
        "message": "Go aws-Serverless v6.0! Your function executed successfully!.. This is my latest commit",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
