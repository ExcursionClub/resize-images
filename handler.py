def handle_hello(event, context):
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


def handle_resize_image(event, context):
    print('handle_resize called')
