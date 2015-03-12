from SOAPpy import SOAPProxy

wsdlUrl = 'http://www.ebi.ac.uk/ws/services/WSDbfetch';
query = 'uniprot:wap_rat'
format = 'fasta'
style = 'raw'

server = SOAPProxy(wsdlUrl)

# Perform the query.
result = server.fetchData(query, format, style)

# Output the result.
print result