import os
from datetime import datetime
from traffic_api import TrafficApi
import json
from xml.etree import ElementTree

def say_hello(message="Hello World"):
    traffic = TrafficApi(app_id=os.environ['APP_ID'],
                         app_code=os.environ['APP_CODE'])
    # data = traffic.flow_by_bbox(bbox=[45.391700,-122.826462,45.657728,-122.347183])
    with open('flow-formatted.json') as f:
        raw_data = f.read()
        data = json.loads(raw_data)
        print(data['RWS'][0]['RW'][0])
    # for roadway in data.roadways():
    #     print(roadway['DE'])
    # print(datetime.now(), message)


say_hello()
