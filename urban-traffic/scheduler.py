import os
from datetime import datetime
from traffic_api import TrafficApi


def say_hello(message="Hello World"):
    traffic = TrafficApi(app_id=os.environ['APP_ID'],
                         app_code=os.environ['APP_CODE'])
    data = traffic.flow_by_bbox(bbox=[45.391700,-122.826462,45.657728,-122.347183])
    print(data.json())
    print(datetime.now(), message)


say_hello()
