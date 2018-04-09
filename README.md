# Apple Store App ID Script
Apple Store App ID Script

The purpose of this script is to read a csv of Apple app ids and output a csv with the parameters

Requirements: python 2.7

iTunes ID
Bundle Id
App Name
Publisher Name
Primary Category

This script uses Apple's search API here: 
https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/#lookup

Steps to execute script:

1. Download the zip file from https://github.com/edwardho/applestoredata

2. Unzip the file and move the folder to your /Desktop directory
 
3. Navigate to Desktop/applestoredata/ and edit the file iosappids.csv and include all the app ids you want to look up

    Make sure to only include app ids, one per row

    Save the file

4. Open terminal/cmd and enter the command:

    cd Desktop/applestoredata/

5. Enter the command below to run the script on your csv input file:

    python iosappscraper.py

6. Within the same folder, you should see an output file called "iosscraperoutput.csv" which includes the data per app id
