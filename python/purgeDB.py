#!/usr/bin/python
import sqlite3
import datetime

# purges all entries older than a month

def main():
    conn = sqlite3.connect('../db/summaries.db')
    c = conn.cursor()
    oldest = datetime.datetime.now() + datetime.timedelta(-30) # 30 days back
    c.execute('DELETE * FROM summaries WHERE created_at < ' + oldest)
    conn.commit()
    conn.close()

if __name__=='__main__':
    main()
