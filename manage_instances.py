import boto.ec2
import os

try:
    # import credentials and region from credentials.py - see readme for format
    from credentials import aws_id, aws_key, aws_region
except ImportError:
    print "Credentials missing. Please see readme for information."
    raise SystemExit

try:
    # create session with the desired EC2 region
    ec2 = boto.ec2.connect_to_region(aws_region, aws_access_key_id=aws_id, aws_secret_access_key=aws_key)
    # test credentials
    ec2.get_all_instances()
except Exception:
    print "EC2 test failed. Please check AWS_ID, AWS_KEY and associated permissions. More information is in the readme."
    raise SystemExit

def check_key(instance_keypair):
    # check keypair
    check_key = ec2.get_key_pair(instance_keypair)

    # returns true if key exists, false if it does not
    if check_key != None:
        return True
    else:
        return False

def create_key(instance_keypair):
    # creates a key with the given name and returns the location
    key = ec2.create_key_pair(instance_keypair)
    name = instance_keypair + '.pem'
    pem = open(name, 'w')
    pem.write(key.material)
    pem.close
    cwd = os.getcwd()
    path = cwd + '/' + name
    return path

def create_instance(instance_size, instance_ami, instance_keypair, instance_metadata=None):
    # call the check_key function, inform user if key is created
    if check_key(instance_keypair):
        print "The key {} already exists, therefore it will be used.".format(instance_keypair)
    else:
        key = create_key(instance_keypair)
        print "Specified key was not found, therefore is has been created at {}".format(key)

    # read instance metadata if requested
    user_data = None
    if instance_metadata != None:
        with open(instance_metadata, 'r') as metadata:
            user_data=metadata.read()

    # create vm with specified params
    instance = ec2.run_instances(image_id=instance_ami, key_name=instance_keypair, instance_type=instance_size, user_data=user_data)
    return instance
