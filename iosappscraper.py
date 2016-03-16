import csv
import urllib2
import json

f = open('iosappids.csv')
fp = open('iosscraperoutput.csv', 'wb')
reader = csv.reader(f)
writer = csv.writer(fp, delimiter=',')

writer.writerows([['App ID', 'Publisher Name', 'App Name', 'Description', 'Primary Category']])

for row in reader:
    	response = urllib2.urlopen('http://itunes.apple.com/lookup?id=' + ', '.join(map(str, row))) # it's a file like object and works just like a file
    	appjson = response.read()
    	appdata = json.loads(appjson)
    	aid = appdata['results'][0]['artistId']
    	#print aid
    	pubname = (appdata['results'][0]['artistName'])
    	#print pubname
    	appname = (appdata['results'][0]['trackCensoredName'])
    	#print appname
    	desc = (appdata['results'][0]['description'])
    	#print desc
    	pcat = (appdata['results'][0]['primaryGenreName'])
    	#print pcat
    	#print '\n'
    	writer.writerows([[aid, pubname, appname, desc.encode('utf-8'),pcat]])

