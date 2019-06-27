import sys
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from traffic_flow import TrafficFlow


class TrafficApi:

    def __init__(self, app_id, app_code, retries=5, backoff_factor=1,
                 status_forcelist=[502, 503, 504],
                 base_url='https://traffic.api.here.com/traffic'):
        """Interact with the Here API

        Args:
            app_id (str): The id of your registered Here application.
            app_code (str): The code for your registered Here application.
            retries (int): Number of retries to try when interacting with Here api.
            backoff_factor (int): Retry backoff.
            status_forcelist (list): List of statuses used to determine retry.
            base_url (str): The base url for the Here traffic API.

        Returns:
            type: Description of returned object.

        """
        self.app_id = app_id
        self.app_code = app_code
        self.base_url = base_url

        self.session = requests.Session()
        retries = Retry(total=retries, backoff_factor=backoff_factor,
                        status_forcelist=status_forcelist)
        self.session.mount('https://', HTTPAdapter(max_retries=retries))

    def flow_by_bbox(self, bbox, params={}):
        """Get TrafficFlow within a given bbox

        Args:
            bbox (list): [top, left, bottom, right].
            params (type): Additional query params to send to the Here API

        Returns:
            TrafficFlow: A TrafficFlow item representing a GeoJSON FeatureCollection.

        """
        bbox_formatted = f"{bbox[0]},{bbox[1]}; {bbox[2]},{bbox[3]}"
        params = {**{'bbox': bbox_formatted}, **params}
        return self.__flow(params=params)

    def __flow(self, params={}):
        flow = self.__get(f'{self.base_url}/6.2/flow.json', params)
        return TrafficFlow(payload=flow.json())

    def __get(self, url, params={}):
        default_params = {'app_id': self.app_id, 'app_code': self.app_code}
        payload = {**default_params, **params}
        # Hack to prevent escaping.  The HERE api can't handle url encoded
        # strings and requests automatically escapes dictionary items.
        payload_str = "&".join("%s=%s" % (k, v) for k, v in payload.items())
        try:
            r = requests.get(url, params=payload_str)
            r.raise_for_status()
            return r
        except requests.exceptions.HTTPError as err:
            print(err)
            sys.exit(1)
