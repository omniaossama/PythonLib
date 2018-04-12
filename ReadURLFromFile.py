from urllib.parse import urlparse

url_list = open('C:\Python\list.txt', 'r').read().split(",")
#print(url_list)
# loop for each url
i=0
for url in url_list:
    i=i+1
    hostname = urlparse(url).netloc
    protocol= urlparse(url).scheme
    print( str(i) + ") HostName:" + hostname + ' - Scheme:' + protocol )
    