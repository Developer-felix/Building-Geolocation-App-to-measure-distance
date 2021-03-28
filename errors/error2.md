country() missing 1 required positional argument: 'query'

This error was due to geoip2 had no geoip() and lat, lon had used d wich is not a positional argument
def get_geo(ip):
g = GeoIP2
country = g.country(ip)
city = g.city(ip)
lat, lon = d.lat_lon(ip)
return country, city, lat, lon

solutions were

def get_geo(ip):
g = GeoIP2()
country = g.country(ip)
city = g.city(ip)
lat, lon = g.lat_lon(ip)
return country, city, lat, lon
