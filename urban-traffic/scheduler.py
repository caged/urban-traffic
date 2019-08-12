import os
from datetime import datetime
import psycopg2

from traffic_api import TrafficApi
from traffic_flow import TrafficFlow


def process_traffic_data():
    conn = psycopg2.connect(host='db',
                            dbname=os.environ['POSTGRES_DBNAME'],
                            user=os.environ['POSTGRES_USER'],
                            password=os.environ['POSTGRES_PASS'],
                            port=5432)

    cursor = conn.cursor()

    process_date = datetime.utcnow().replace(second=0, microsecond=0)
    traffic = TrafficApi(app_id=os.environ['APP_ID'],
                         app_code=os.environ['APP_CODE'])
    tf = traffic.flow_by_bbox(
        bbox=[45.391700, -122.826462, 45.657728, -122.347183]
    )

    for feature in tf.features():
        query = "INSERT INTO flow_items VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        props = feature['properties']
        cursor.execute(query, (
            props['li'],
            props['de'],
            props['roadway'],
            props['pc'],
            props['qd'],
            props['le'],
            props['ty'],
            props['sp'],
            props['su'],
            props['ff'],
            props['jf'],
            props['cn'],
            props['pbt'],
            process_date
        ))

    conn.commit()
    conn.close()
    print("Ran at {}".format(process_date))


process_traffic_data()
