import urllib.request
import json

url = 'https://newsapi.org/v1/articles?source={}&apiKey=abdae41567894d36b2ecfd46ef20ee78'
news = '''The news is from {}.
The Author is {}.
The title is {}.
Description: {}.
Link to website: {} \n'''
categoriesList = ['business', 'entertainment', 'gaming', 'general', 'music', 'science-and-nature', 'sport',
                  'technology']

with open('Sources.Json', 'r') as SourceFile:
    sourceDictionary = json.loads(SourceFile.read())
    sourceDictionary = dict(sourceDictionary)
    SourceFile.close()


def getNewsData(source):
    urllib.request.urlretrieve(url.format(source), 'DataFile.Json')


def openCategoryText(category):
    open(category + '.txt', encoding='utf8')


def getDicData(source):
    return sourceDictionary[source]


def retrieveDataFile():
    with open('DataFile.Json', encoding='utf8') as newsData:
        return json.loads(newsData.read())


for categories in categoriesList:
    sourceLists = getDicData(categories)
    with open(categories + '.txt', 'r+', encoding='utf8') as newsText:
        for x in sourceDictionary[categories]:
            try:
                getNewsData(x)
                jsonData = retrieveDataFile()
                articlesDictionary = jsonData['articles']
                Source = jsonData['source']
                for i in articlesDictionary:
                    newsText.write(news.format(Source, i['author'], i['title'], i['description'], i['url']))
                print('Done '+ x)
            except Exception:
                continue
        newsText.close()

input()