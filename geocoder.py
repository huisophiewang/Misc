import geocoder
from geocoder import google
#import geocoder.google as gg

g = google('Mountain View, CA')
print g.latlng

#g = geocoder.google([45.15, -75.14], method='reverse')