import boto3
import io
import psycopg2

s3 = boto3.resource(
    service_name = 's3',
    region_name='sa-east-1',
    aws_access_key_id='',
    aws_secret_access_key='/'
)

bucket = 'miche-python'
prefix = 'images/'

con = psycopg2.connect(
    host='database-1..rds.amazonaws.com',
    database='postgres',
    user='postgres',
    password='TesteCurso1'
)

cur = con.cursor()
con.autocommit = True
id = 1

for obj_s3 in s3.Bucket(bucket).objects.filter(Prefix=prefix):
    if obj_s3.key.endswith('jpg') or obj_s3.key.endswith('JPG'):
        # print(obj_s3)
        file_name = obj_s3.key.split('/')[1]
        cur.cursor()
        cur.execute(f"insert into arquivo (idarquivo, nomedoarquivo) values({id}, {file_name})")
        id += 1

con.close()


