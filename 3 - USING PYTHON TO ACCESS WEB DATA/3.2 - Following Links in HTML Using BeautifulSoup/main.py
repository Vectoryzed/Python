import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

cnt = input("Enter count: ")
count = int(cnt);
pos = input("Enter position: ")
position = int(pos)

ind = 0
ind_2 = 0
ind_w = 0

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # print(tag.get('href', None))
    ind = ind + 1

    if (ind == position):
        link = tag.get('href', None)

        while ind_w != count:
            ind_2 = 0
            print("Retrieving:", link)
            html2 = urllib.request.urlopen(link, context=ctx).read()
            soup2 = BeautifulSoup(html2, 'html.parser')
            # print("ind_w:", ind_w)

            tags2 = soup2('a')
            for tag2 in tags2:
                # print("ind_2:", ind_2)
                ind_2 = ind_2 + 1
                if (ind_2 == position):
                    link = tag2.get('href', None)
                    break

            ind_w = ind_w + 1

        break
