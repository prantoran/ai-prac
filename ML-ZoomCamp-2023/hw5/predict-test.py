#!/usr/bin/env python
# coding: utf-8

import requests

# host = 'localhost'
host = '0.0.0.0'
port = 9696
# port = 80
url = f"http://{host}:{port}/predict"

print("url:", url)


client = {"job": "unknown", "duration": 270, "poutcome": "failure"}
response = requests.post(url, json=client).json()

print(response)