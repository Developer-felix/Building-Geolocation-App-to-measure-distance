I got "GeocoderInsufficientPrivileges: Non-successful status code 403"

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="measurements")

This is how i solved The error

"GeocoderInsufficientPrivileges" error - try to use 'Photon' instead of 'Nominatim'

from geopy.geocoders import Photon
geolocator = Photon(user_agent="measurements")
