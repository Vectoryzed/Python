import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


url = input('Enter url which retrieve XML from: ')
if len(url) < 1: quit()

#url = serviceurl + urllib.parse.urlencode({'address': address})
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
xml_tree = ET.fromstring(data)

num_list = list()

results = xml_tree.findall('.//count')
print("Number of counts:", len(results))
for item in results:
    cnt_retr = item.text
    print(cnt_retr)
    num_list.append(int(cnt_retr))

sumValue = sum(num_list)
print("The sum is:", sumValue)

