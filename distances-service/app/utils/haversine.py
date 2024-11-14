from math import radians, cos, sin, asin, sqrt, atan2


def haversine(lon1, lat1, lon2, lat2):
    EARTH_RADIUS = 6378  # in KM
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return EARTH_RADIUS * c
