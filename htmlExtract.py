# This file is to test out retrieving the URL from a dataset's XML file
# and then using Boilerpy to grab all the text

# TODO: Develop way to get continuously grab URL and output contents for multiple dataset files

import lxml.etree as ET
from boilerpy3 import extractors
extractor = extractors.ArticleExtractor()

def getUrl(dataset):
    file = open(dataset)
    tree = ET.parse(file)
    root = tree.getroot()

    # Find the URL which is an attribute (url) of the <Document> tag
    return root.attrib['url']

def parseHtml(url, outputFile):
    content = extractor.get_content_from_url(url)

    file = open(outputFile, "a")
    file.write(content)
    file.close()

def main():
    url = getUrl("0000001_1.xml")
    parseHtml(url, "htmlOutput.txt")

if __name__ == "__main__":
    main()