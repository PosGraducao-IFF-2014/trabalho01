import SOAPpy
service_url = "http://footballpool.dataaccess.eu/data/info.wso"
namespace = "http://footballpool.dataaccess.eu"
client = SOAPpy.SOAPProxy(service_url,namespace)
print client.Cities()
print client.StadiumNames()