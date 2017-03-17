from manage_instances import create_instance 
from manage_elb import create_http_elb, register_instance_elb

# create two instances
instance_1 = create_instance('m1.small', 'ami-fe133998', 'nodejs_server', 'nodejs_hello.sh')
instance_2 = create_instance('m1.small', 'ami-fe133998', 'nodejs_server', 'nodejs_hello.sh')

# create an ELB
elb_zones = [ 'eu-west-1a', 'eu-west-1b', 'eu-west-1c' ]
elb = create_http_elb('nodejs', elb_zones) 

# add our two instances to the ELB
register_instance_elb(instance_1.instances[0].id, elb)
register_instance_elb(instance_2.instances[0].id, elb)

# print connection information
print "nodejs example will be available shortly at this URL: {}...".format(elb.dns_name)
