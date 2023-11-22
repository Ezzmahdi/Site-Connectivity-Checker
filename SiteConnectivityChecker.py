import urllib.request as urllib

url = input('Url you want to check: ')

try:
    response = urllib.urlopen(url)
    print('The response code was:', response.getcode())
except urllib.URLError as e:
    print('Error:', e)
