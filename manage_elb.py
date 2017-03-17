import boto.ec2.elb

from boto.ec2.elb import HealthCheck

try:
    # import credentials and region from credentials.py - see readme for format
    from credentials import aws_id, aws_key, aws_region
except ImportError:
    print "Credentials missing. Please see readme for information."
    raise SystemExit

try:
    # create session with the desired ELB region
    elb = boto.ec2.elb.connect_to_region(aws_region, aws_access_key_id=aws_id, aws_secret_access_key=aws_key)
except Exception:
    print "ELB test failed. Please check AWS_ID, AWS_KEY and associated permissions. More information is in the readme."
    raise SystemExit

def create_http_elb(name, zones):
    # Healthcheck - checks / for a 200
    hc = HealthCheck(interval=20,healthy_threshold=3,unhealthy_threshold=5,target='HTTP:80/')

    # port 80 - HTTP
    ports = [(80, 80, 'http')]

    # create LB and healthcheck - then return LB info
    lb = elb.create_load_balancer(name, zones, ports)
    lb.configure_health_check(hc)
    return lb

def register_instance_elb(instance, elb):
    # register this instance to an elb
    elb.register_instances(instance)
