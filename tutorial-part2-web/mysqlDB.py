import time
import urllib.request

from bs4 import BeautifulSoup
from dbconnect import connection

req = urllib.request.urlopen('http://www.nationaljournal.com/politics?rss=1')

xml = BeautifulSoup(req, 'xml')

c, conn = connection()

for item in xml.findall('link')[3:]:
    url = item.text
    c.execute("INSERT INTO links (time, link) VALUES (%s, %s)",
              (time.time(), url))
    conn.commit()

conn.close()
