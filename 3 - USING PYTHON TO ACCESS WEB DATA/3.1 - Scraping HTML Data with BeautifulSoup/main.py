from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

num_list = list()

tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    print('Count:', tag.contents[0])
    num = tag.contents[0]
    num_list.append(int(num))

sum_val = sum(num_list)
print("Sum", sum_val)