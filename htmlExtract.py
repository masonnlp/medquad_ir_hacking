# This file is to test out retrieving the URL from a dataset's XML file
# and then using Boilerpy to grab all the text

import os
from urllib.error import HTTPError

import lxml.etree as ET
from boilerpy3 import extractors

extractor = extractors.DefaultExtractor()
path = os.getcwd() + '/'
filelist = os.listdir(path)

def getUrl(tree):
    #file = open(dataset)
    #tree = ET.parse(file)
    root = tree.getroot()

    # Find the URL which is an attribute (url) of the <Document> tag
    return root.attrib['url']

def parseHtml(url,id,source, outputFile):
    try:
        content = extractor.get_content_from_url(url)
        file = open(outputFile, "a", encoding="utf-8")
        file.write(source + ": " + id + "\n" + content + "\n")
        file.close()
    except HTTPError:
        file = open(outputFile, "a", encoding="utf-8")
        file.write(source + ": " + id + "\n404: Not Found\n")
        file.close
    except ConnectionError:
        print("Connection error")

def main():
    for dataset in [f for f in os.listdir(path+'MedQuAD/') if f.endswith("QA") or f.endswith("XML")]:
        print(dataset)
        for xml_file in [f for f in os.listdir(path+'MedQuAD/' + dataset + '/') if f.endswith(".xml")]:
            tree = ET.parse(os.path.join(path+'MedQuAD/' + dataset + '/', xml_file))
            root = tree.getroot()
            url = root.attrib['url']
            id = root.attrib['id']
            source = root.attrib['source']
            print(source + ": " + id)
            parseHtml(url, id, source, "htmlExtraction.txt")

if __name__ == "__main__":
    main()