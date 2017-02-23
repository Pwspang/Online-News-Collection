import os
import json
import urllib.request




def getSourceData(source):
    with urllib.request.urlopen(url.format(source)) as response:
        rawData = response.read()
        print(url.format(source))
        return json.loads(rawData)


url = 'https://newsapi.org/v1/sources?language=en&category={}'
categories = ['business', 'entertainment', 'gaming', 'general', 'music', 'science-and-nature', 'sport', 'technology']
sourceDictionary = {'business': [], 'entertainment': [], 'gaming': [], 'general': [], 'music': [],
                    'science-and-nature': [], 'sport': [], 'technology': []}

for j in categories:
    jsonData = getSourceData(j)
    sourceList = jsonData['sources']
    sourceDictionary.update(j='')
    for i in sourceList:
        sourceID = i['id']
        sourceDictionary[j].insert(0, sourceID)

with open('Sources.Json', 'w') as sourceFile:
    JsonData = json.dumps(sourceDictionary)
    sourceFile.write(JsonData)
    sourceFile.close()
