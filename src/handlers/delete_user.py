def handler(event, context):
    user_id = event["pathParameters"]["id"]
    repo.delete(user_id)
    return {"statusCode": 204} # No Content