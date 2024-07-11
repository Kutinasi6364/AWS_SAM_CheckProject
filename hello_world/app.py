import json

# import requests


def lambda_handler(event, context):
    for rec in event["Records"]:
        print("アップロードされたファイルは: " + rec["s3"]["object"]["key"])
        print("アップロードされたバケットは: " + rec["s3"]["bucket"]["name"])
