import os
from datetime import datetime
from traffic_api import TrafficApi
from traffic_flow import TrafficFlow
import json
from xml.etree import ElementTree


def process_traffic_data():
    process_date = datetime.now().replace(second=0, microsecond=0)
    traffic = TrafficApi(app_id=os.environ['APP_ID'],
                         app_code=os.environ['APP_CODE'])
    tf = traffic.flow_by_bbox(
        bbox=[45.391700, -122.826462, 45.657728, -122.347183]
    )
    for feature in tf.features():
        print(feature)


process_traffic_data()
