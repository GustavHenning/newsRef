#!/usr/bin/python
import sqlite3

def main():
    conn = sqlite3.connect('../db/summaries.db')
    c = conn.cursor()
    rows = c.execute('SELECT * FROM summaries')
    for row in rows:
        #print row[0] #url
        print row[1].encode("utf-8")
        #print row[2] #date
    conn.close()

if __name__=='__main__':
    main()
