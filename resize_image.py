import boto3
from wand.image import Image


def resize_image(event):
    print(event)
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key_path = event['Records'][0]['s3']['object']['key']

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    obj = s3.Object(bucket_name=bucket_name, key=key_path)
    response = obj.get()
    data = response['Body'].read()

    filename = key_path.split('/')[1]
    new_key_path = "media/" + filename

    with Image(blob=data) as image:
        resized_image = resize(image)
        print('re-sizing...')
        resized_data = resized_image.make_blob()

    bucket.put_object(Key=new_key_path, Body=resized_data)

    print('resize_image() worked!')


def resize(image):
    resize_width, resize_height = 600, 600

    if resize_width == image.width and resize_height == image.height:
        return image

    original_ratio = image.width / float(image.height)
    resize_ratio = resize_width / float(resize_height)

    # Use original ration
    if original_ratio > resize_ratio:
        # If width is larger, we base the resize height as a function of the ratio of the width
        resize_height = int(round(resize_width / original_ratio))
    else:
        # Otherwise, we base the width as a function of the ratio of the height
        resize_width = int(round(resize_height * original_ratio))

    #
    if ((image.width - resize_width) + (image.height - resize_height)) < 0:
        filter_name = 'mitchell'
    else:
        filter_name = 'lanczos2'

    image.resize(width=resize_width, height=resize_height, filter=filter_name, blur=1)

    return image
