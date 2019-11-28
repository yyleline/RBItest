import boto3
import logging
import os

#Upload
s3 = boto3.client('s3')
s3.upload_file("UBSprices.csv", "yyl-bucket", "UBSprices.csv")
# data = open('UBSprices.csv', 'rb')
# s3.Bucket('yyl-bucket').put_object(Key='UBSprices.csv', Body=data)



#Download
s3 = boto3.client('s3')
s3.download_file('yyl-bucket', 'test1.jpg','test1.jpg')





#Download folder
s3 = boto3.client('s3')
filepath = 'test/'
my_bucket = boto3.resource('s3').Bucket('yyl-bucket') 

for s3_object in my_bucket.objects.all():
    path, filename = os.path.split(s3_object.key)
    #print(s3_object.key)
    # print(s3_object)
    #print(path, filename)
    if s3_object.key[:len(filepath)] == filepath and len(s3_object.key) > len(filepath):
    	# print(s3_object.key, len(s3_object.key))
    	s3.download_file('yyl-bucket', path+'/'+filename, filename)
    	# print(filename)








