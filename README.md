# resize-images
Resize images added to S3 bucket

## Install and setup Serverless credentials
```
npm install -g serverless
serverless config credentials --provider aws --key <key> --secret <secret>
```
Since CloudFormation is doing a lot it needs a lot of permissions.

## Deploy function as dev
```
sls deploy --stage dev && sls s3deploy
```
