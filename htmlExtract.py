# This file is to test out retrieving the URL from a dataset's XML file
# and then using Boilerpy to grab all the text


import lxml.etree as ET
from boilerpy3 import extractors
extractor = extractors.ArticleExtractor()

# Need to parse the XML file
file = open("0000001_1.xml")
tree = ET.parse(file)
root = tree.getroot()

# Find the URL which is an attribute (url) of the <Document> tag
url = root.attrib['url']
file.close()

content = extractor.get_content_from_url(url)

file = open("htmlOutput.txt", "a")
file.write(content)
file.close()