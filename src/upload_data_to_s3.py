import boto3
import argparse

#s3 = boto3.client('s3')
#input = '../data/data1.csv'
#bucket_name = 'nw-sichen'
#output = 'data1.csv'
#s3.upload_file(input, bucket_name, output)

def uploadtos3(args):
    s3 = boto3.client('s3')
    s3.upload_file(args.input_path, args.bucket_name, args.output_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Upload data to your own s3 bucket")

    parser.add_argument("--input_path", help="local file path")
    parser.add_argument("--bucket_name", help="bucket name")
    parser.add_argument("--output_path", help="destination file path")

    args = parser.parse_args()
    uploadtos3(args)
