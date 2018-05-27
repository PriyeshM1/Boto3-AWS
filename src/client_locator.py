import boto3


class ClientLocator:
    def __init__(self, client):
        self.client = boto3.client(client, region_name="eu-west-2")

    def get_client(self):
        return self.client


class EC2Client(ClientLocator):
    def __init__(self):
        super().__init__('ec2')

