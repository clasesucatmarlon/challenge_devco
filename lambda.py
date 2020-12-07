import json
import boto3
import pandas as pd
import io

def lambda_handler(event, context):
    """ Read and extract data from an Excel file and store it in a csv file, using lambda aws 
    """
    s3 = boto3.client('s3', aws_access_key_id='AKIA3V6VSA7HPJGAYZ4T', aws_secret_access_key='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')
    if event:
        s3_records = event["Records"][0]
        bucket_name = str(s3_records["s3"]["bucket"]["name"])
        file_name = str(s3_records["s3"]["object"]["key"])
        file_obj = s3.get_object(Bucket=bucket_name, Key=file_name)
        file_content = file_obj["Body"].read()
        read_excel_data = io.BytesIO(file_content)
        df = pd.read_excel(read_excel_data)
        df = df.assign(dummy="dummy_value")
        df.to_cvs("/tmp/data.csv")
        s3_resource = boto3.resource("s3")
        s3_resource.Bucket("rekognit").upload_file("/tmp/data.csv", "data.csv")

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Conection Success!!!!')
    }
