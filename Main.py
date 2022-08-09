import os
import data_access_s3
import boto3
from botocore.exceptions import ClientError



def upload_to_s3():
    """ Upload to S3 """
    s3_client = boto3.client('s3', aws_access_key_id = access_key,
                             aws_secret_access_key = access_secret)
    try:
        aws_access_key_id = access_key,
        aws_secret_access_key = access_secret
        response = s3_client.upload_file("upload_this_file.txt", 'siu-avb-bucket', 'upload_this_file.txt')
    except ClientError as e:
        print(e)
        return False
    return True


def download_from_s3():
    """ Download from S3 """
    try:
        s3_client = boto3.client('s3')
        s3_client.download_file('siu-avb-bucket', 'upload_this_file.txt', 'dn_upload_file.txt')
    except ClientError as e:
        print(e)
        return False
    return True;

