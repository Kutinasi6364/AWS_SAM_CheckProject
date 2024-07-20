# S3にファイルがアップロードされたのを検知してTextractを実行する
import boto3
import json


def lambda_handler(event, context):
    s3 = boto3.client("s3")
    textract = boto3.client("textract")

    for record in event["Records"]:
        print("record: " + str(record))
        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]
        print("bucket: " + str(bucket))
        print("key: " + str(key))

        if "/" not in key:
            response = textract.detect_document_text(
                Document={"S3Object": {"Bucket": bucket, "Name": key}}
            )

            textracted_text = ""
            for item in response["Blocks"]:
                if item["BlockType"] == "LINE":
                    textracted_text += item["Text"] + "\n"

            output_key = f"extracted/{key.split('/')[-1]}.txt"
            print("output_key: " + str(output_key))
            s3.put_object(Bucket=bucket, Key=output_key, Body=textracted_text)
