#!/usr/bin/python
import sqlite3

def main():
    conn = sqlite3.connect('../db/summaries.db')
    c = conn.cursor()
    #c.execute('''DROP TABLE summaries''')
    c.execute('''CREATE TABLE summaries (url text, summary text, created_at date)''')
    conn.commit()
    conn.close()
    print 'database created'

if __name__=='__main__':
    main()
