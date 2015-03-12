from SOAPpy import *
service_url = "http://chennaiemergency.co.in/sree/s2.php"
namespace = "urn:ChnEmergency"
chennai_emergency = SOAPProxy(service_url,namespace)
latitude = floatType(11)
longitude = floatType(12.1)
print chennai_emergency.police(latitude,longitude)
print chennai_emergency.fire(latitude,longitude)
print chennai_emergency.hospital(latitude,longitude)