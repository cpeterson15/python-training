import urllib.parse
import urllib.request

values = {'q': 'python programming tutorials'}

data = urllib.parse.urlencode(values)
url = 'https://www.google.com/search?' + data

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"
req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req)
resp_data = resp.read()

print(resp_data)

