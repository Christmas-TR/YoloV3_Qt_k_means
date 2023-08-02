"""Perform test request"""
import pprint

import requests

DETECTION_URL = "http://localhost:5000/v1/object-detection/yolov5s"
TEST_IMAGE = "D:\CV2\qt_show\\v3_chen\qt5_yolov3-main\street.jpg"

image_data = open(TEST_IMAGE, "rb").read()

response = requests.post(DETECTION_URL, files={"image": image_data}).json()

pprint.pprint(response)
