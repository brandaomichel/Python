import boto3
import io

s3 = boto3.resource(
    service_name = 's3',
    region_name='sa-east-1',
    aws_access_key_id='',
    aws_secret_access_key=''
)

bucket = 'miche-python'
prefix = 'images/'

for obj_s3 in s3.Bucket(bucket).objects.filter(Prefix=prefix):
    if obj_s3.key.endswith('jpg') or obj_s3.key.endswith('JPG'):
        # print(obj_s3)
        file_name = obj_s3.key.split('/')[1]
        print(file_name)

        # Salvar imagem em Disco
        body = obj_s3.get()['Body'].read()
        imagem = io.BytesIO(body)
        with open(file_name, 'wb') as f:
            f.write(imagem.getbuffer())

