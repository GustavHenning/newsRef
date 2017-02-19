#!/usr/bin/python

#spider used to find articles from a news website

import urllib2
from bs4 import BeautifulSoup
import re, sys, populate

def main(searchurl, baseurl, regex, dryrun):
    conn = urllib2.urlopen(searchurl)
    html = conn.read()

    soup = BeautifulSoup(html, "lxml")
    links = soup.find_all('a')

    regexp=re.compile(regex)
    
    for tag in links:
        link = tag.get('href',None)
        if link is not None and regexp.search(link):
            if dryrun is True:
                print baseurl + link
            else:
                populate.main(baseurl + link)

if __name__=='__main__':
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))
