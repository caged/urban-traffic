from datetime import datetime, date

class TrafficFlow:
    """Takes traffic flow dat from the Here API and normalizes to a
       GeoJSON representation.

    Parameters
    ----------
    payload : dict
        raw payload from here api.

    Attributes
    ----------
    __raw : dict
        raw dict payload from here api

    """
    def __init__(self, payload):
        self.__raw = payload


    def features(self):
        """Yields GeoJSON Feature objects

        Returns
        -------
        dict
            GeoJSON Feature object as a MultiLineString.

        """
        return self.__parse_features()

    def __create_feature(self, roadway, flowitem):
        """Given a RoadWay and FlowItem, build a GeoJSON Feature

        Parameters
        ----------
        roadway : dict
            A Here RoadWay item.
        flowitem : dict
            A Here API FlowItem

        Returns
        -------
        dict
            yields a feature.

        """
        process_date = datetime.now().replace(second=0, microsecond=0)
        props = {}

        tmc = flowitem['TMC']
        cf  = flowitem['CF'][0]
        shp = flowitem['SHP']

        props['de'] = tmc['DE']
        props['pc'] = int(tmc['PC'])
        props['qd'] = tmc['QD']
        props['le'] = float(tmc['LE'])

        props['ty'] = cf['TY']
        props['sp'] = float(cf['SP'])
        props['su'] = float(cf['SU'])
        props['ff'] = float(cf['FF'])
        props['jf'] = float(cf['JF'])
        props['cn'] = float(cf['CN'])

        try:
            # Discard this for now.
            ss = cf['SSS']['SS']
        except KeyError as e:
            pass

        props['li'] = roadway['LI']
        props['roadway'] = roadway['DE']
        props['pbt'] = datetime.strptime(roadway['PBT'], '%Y-%m-%dT%H:%M:%SZ').replace(second=0, microsecond=0)
        props['processed'] = process_date
        coordinates = []


        for leg in shp:
            coords = leg['value'][0].strip()
            points = [[float(v) for v in reversed(c.split(','))] for c in coords.split(' ')]
            coordinates.append(points)

        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'MultiLineString',
                'coordinates': coordinates
            },
            'properties': props
        }

        return feature


    def __parse_features(self):
        # feature_collection = []
        # created = payload['CREATED_TIMESTAMP']
        # version = payload['VERSION']

        for roadways in self.__raw['RWS']:
            for rw in roadways['RW']:
                li = rw['LI']
                de = rw['DE']
                pbt = rw['PBT']

                for fis in rw['FIS']:
                    for fi in fis['FI']:
                        yield self.__create_feature(roadway=rw, flowitem=fi)
