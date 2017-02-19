#!/bin/bash

# entires innehåller ”
python ../python/showEntries.py > ./entries.txt

cat entries.txt | tr '[:punct:]' ' ' | tr 'A-Z' 'a-z' | tr -s ' ' | tr ' ' '\n' | sort | uniq -c | sort -rg > words.txt
