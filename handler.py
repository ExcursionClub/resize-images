from resize_image import resize_image


def handle_resize_image(event, context):
    resize_image(event)
    print('handle_resize called')
