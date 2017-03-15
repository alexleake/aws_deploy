# About

Example script to create a machine in AWS using the boto library.

# Instructions

Create an AWS service account with the appropriate permissions to create a machine in EC2.

Add the details for this account (AWS ID, SECRET KEY) in a file called "credentials.py":

```
aws_id=''
aws_key=''
aws_region='eu-west-1'
```

Once complete install the python requirements:

```
pip install -r requirements.txt
```

And run the sample application (if you want to):
```
python nodejs_quickstart.py
```
