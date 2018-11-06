def hello(event, context):
    try:
        return {
            'statusCode': 200,
            'body': "Hello"
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }


def resize_image(event, context):
    try:
        return {
            'statusCode': 200,
            'body': "Image re-sized!"
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
