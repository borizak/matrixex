# THIS IS A PSEUDO-TEST ROUTINE
from spear.flights import TLV_AIRPORT

tlv =  TLV_AIRPORT()

tlv.pull()

all_flights = tlv.all()

to_berlin = tlv.search(destination = 'Berlin')
from_london = tlv.search(origin = 'London')

print(to_berlin)
print(from_london)