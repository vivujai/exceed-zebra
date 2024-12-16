from google.cloud import vision_v1
from google.cloud.vision_v1 import types
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'vision-project-207707-f84d39ceed76.json'

client = vision_v1.ImageAnnotatorClient()

def coldet(path):
    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision_v1.Image(content = content)
    response = client.image_properties(image = image)
    info = response.image_properties_annotation
    data = info.dominant_colors.colors

    total_red = 0
    total_green = 0
    total_blue = 0

    for stats in data:
        rgb_value = stats.color
        red = rgb_value.red
        green = rgb_value.green
        blue = rgb_value.blue
        total_red += red
        total_blue += blue
        total_green += green

    if total_red > total_blue and total_red > total_green:
        print("Red is the most dominant")

    if total_blue > total_red and total_blue > total_green:
        print("Blue is the most dominant")

    if total_green > total_blue and total_green > total_red:
        print("Green is the most dominant")

coldet('car.jpeg')
