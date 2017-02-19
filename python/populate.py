#!/usr/bin/python
# -*- coding: utf-8 -*-
from pyteaser import SummarizeUrl
import sqlite3, time, sys
from datetime import date
# takes 1 argument, the url. If the url is already inside the db, quit
# else, insert it and it's summary.

def main(url):
    # open db connection
    conn = sqlite3.connect('../db/summaries.db')
    c = conn.cursor()
    # check if exists

    u = (url,)
    rows = c.execute('SELECT COUNT(*) FROM summaries WHERE url=?', u).fetchone()
    if (rows[0] != 0):
        #print url + " was found in db"
        conn.close()
        return

    # add the new article
    summaries = SummarizeUrl(url)
    if summaries is None:
        conn.close()
        return
    sums = " ".join(summaries).replace('\n', '. ')

    stage = (url, sums, date.today())
    c.execute('INSERT INTO summaries VALUES (?,?,?)', stage)

    # save & close
    conn.commit()
    conn.close()

    # delay so we dont overflow the site
    print url + " added"
    time.sleep(5)


if __name__=='__main__':
    sys.exit(main(sys.argv[1]))
