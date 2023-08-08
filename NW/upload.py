import boto3 as to3

def s3_connection():
    try:
        s3 = to3.client(
            service_name="s3",
            region_name="ap-northeast-2",
            aws_access_key_id="AKIA5WAXLOULLNN23SGK",
            aws_secret_access_key="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",
        )
    except Exception as e:
        print(e)
    else:
        print("s3 bucket connected!")
        return s3
s3=s3_connection()

try:
    s3.upload_file("2023-07-15#04h08m25s.mp4","sjmama1","2023-07-15#04h08m25s.mp4")
except Exception as e:
    print(e)