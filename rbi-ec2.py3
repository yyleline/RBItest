import boto3
ec2 = boto3.resource('ec2')

outfile = open('ec2-keypair.pem','w')
key_pair = ec2.create_key_pair(KeyName='ec2-keypair')
#ami-08b11fc5bd2026dee


#Create Instance
instances_y = ec2.create_instances(
     ImageId='ami-08b11fc5bd2026dee',
     MinCount=1,
     MaxCount=2,
     InstanceType='t2.micro',
     KeyName='ec2-keypair'
 )


#Terminate Instance
ids = ['i-0278a3bba3826ca5a']
ec2.instances.filter(InstanceIds = ids).terminate() 
