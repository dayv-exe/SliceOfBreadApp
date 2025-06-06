# This function runs after the cognito sdk completes signup on client side
# user details like username and email and date joined will be added to db by this function
import os
import boto3


def get_table():
    dynamodb = boto3.resource("dynamodb")
    return dynamodb.Table(os.environ['USERS_TABLE'])

def handler(event, context, table=None):
    if table is None:
        # this allows for mock table to be injected for testing
        table = get_table()