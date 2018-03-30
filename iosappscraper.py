import csv
import urllib2
import json

f = open('iosappids.csv')
fp = open('iosscraperoutput.csv', 'wb')
reader = csv.reader(f)
writer = csv.writer(fp, delimiter=',')

writer.writerows([['iTunes ID', 'Bundle Id', 'App Name', 'Publisher Name', 'Primary Category']])



for row in reader:

        try:
                response = urllib2.urlopen('http://itunes.apple.com/lookup?id=' + ', '.join(map(str, row))) # it's a file like object and works just like a file
                appjson = response.read()
                appdata = json.loads(appjson)

                if (appdata['resultCount'] != 0) :
                        aid = row[0]
                        #print apple id
                        bid = (appdata['results'][0]['bundleId'])
                        #print bid
                        pubname = (appdata['results'][0]['sellerName'])
                        #print pubname
                        appname = (appdata['results'][0]['trackName'])
                        #print appname
                        pgenre = (appdata['results'][0]['primaryGenreName'])
                        #print pgenre
                else:
                        aid = row[0]
                        bid = 'NULL'
                        pubname = 'NULL'
                        appname = 'NULL'
                        pgenre = 'NULL'

        except urllib2.HTTPError as e:
                aid = row[0]
                bid = 'NULL'
                pubname = 'NULL'
                appname = 'NULL'
                pgenre = 'NULL'

        writer.writerows([[aid, bid, appname.encode('utf-8'), pubname.encode('utf-8'), pgenre]])