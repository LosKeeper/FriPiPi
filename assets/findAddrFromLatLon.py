import geocoder


def findAddrFromLatLon(lat, lon):
    g = geocoder.osm([lat, lon], method='reverse')
    return g.address
