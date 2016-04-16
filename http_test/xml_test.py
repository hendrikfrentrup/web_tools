from xml.dom import minidom

test_xml="""
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<feed xml:base="https://apac1.mobile13.cp.thomsonreuters.com/msf1.0/data/" xmlns:d="http//schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://www.w3.org/2005/Atom">
 <title type="text">NewsArticles</title>
 <id>https://apac1.mobile13.cp.thomsonreuters.com/msf1.0/data/NewsArticles</id>
 <updated>2013-01-30T14:22:38Z</updated>
 <link rel="self" title="NewsArticles" href="NewsArticles" />
 <entry>
  <id>https://apac1.mobile13.cp.thomsonreuters.com/msf1.0/data/</id>
 </entry>
 </feed>"""

xmldoc = minidom.parse('test.xml')#test_xml)
itemlist = xmldoc.getElementsByTagName('feed')
print len(itemlist)
print itemlist[0].attributes['base'].value
for s in itemlist :
    print s.attributes['base'].value
