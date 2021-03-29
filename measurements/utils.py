from django.contrib.gis.geoip2 import GeoIP2
#Helper fuction

def get_geo(ip):
    g = GeoIP2()
    country = g.country(ip)
    city = g.city(ip)
    lat, lon = g.lat_lon(ip)
    return country, city, lat, lon

def get_center_coodinates(latA, longA, latB=None, longB=None):
    cord = (latA, longA)
    if latB:
        cord = [(latA + latB) / 2, (longA + longB) / 2]
    return cord

