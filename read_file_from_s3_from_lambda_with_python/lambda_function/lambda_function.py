import boto3

s3 = boto3.client('s3')
bucket_name = 'yt-demo-1' # your bucket name
object_key = 'files/business_employment_data.csv' # your file path
    
def lambda_handler(event, context):

    try:
        
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        file_content = response['Body'].read().decode('utf-8')
        
        print(file_content)
        
        return {
            'statusCode': 200,
            'body': file_content
        }
    except Exception as e:
        print(f"Error reading file from S3: {e}")
        return {
            'statusCode': 500,
            'body': 'Internal Server Error'
        }
