import urllib2

query=urllib2.unquote('?$filter=Request/Filter%20eq%20%27TRI.TO%20AND%20LEN%20NOT%20RITV%27&$top=25&$select=uniqueIdentifier,pnacDate,versionCreated,headline,RCS,Products,BodyLanguage,BodyType,HeadlineLanguage,State,ErrorMessage')

for s in query.split('&'):
   print s+'\n'

