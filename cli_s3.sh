#download folder
aws s3 cp s3://yyl-bucket/test RBItest --recursive
#upload
aws s3 cp /Users/yilingye/Desktop/wine.csv s3://yyl-bucket
#download
aws s3 cp s3://yyl-bucket/test/test1.jpg /Users/yilingye/Desktop
