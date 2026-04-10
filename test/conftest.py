import pytest
import boto3
import os
from moto import mock_aws

@pytest.fixture(scope="function")
def aws_credentials():
    """Mocked AWS Credentials para que Boto3 no busque las reales."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "us-east-1"

@pytest.fixture(scope="function")
def dynamodb_mock(aws_credentials):
    """Fixture que levanta el mock de DynamoDB y crea la tabla para los tests."""
    with mock_aws():
        db = boto3.resource("dynamodb", region_name="us-east-1")
        table_name = "UsersTable"
        db.create_table(
            TableName=table_name,
            KeySchema=[{'AttributeName': 'user_id', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'user_id', 'AttributeType': 'S'}],
            ProvisionedThroughput={'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}
        )
        yield db # Aquí es donde el test se ejecuta