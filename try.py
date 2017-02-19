#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyteaser import SummarizeUrl
from scipy import spatial
import re, math
from collections import Counter

#http://stackoverflow.com/questions/15173225/how-to-calculate-cosine-similarity-given-2-sentence-strings-python
WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)


url = 'http://www.svt.se/kultur/bjorn-granath-har-avlidit'
summaries = SummarizeUrl(url)

sums = " ".join(summaries)
print sums.replace('\n', '')

url2 = 'https://www.svd.se/bjorn-granath-ar-dod/om/kultur:scen'
summaries2 = SummarizeUrl(url2)

sums2 = " ".join(summaries2)
print sums2.replace('\n', '')

url3 = 'https://www.dn.se/kultur-noje/bjorn-granath-ar-dod/'
summaries3 = SummarizeUrl(url3)

sums3 = " ".join(summaries3)
print sums3.replace('\n', '')

vector1 = text_to_vector(sums)
vector2 = text_to_vector(sums2)
vector3 = text_to_vector(sums3)

print 'Cosine:', get_cosine(vector1, vector2)
print 'Cosine:', get_cosine(vector1, vector3)
print 'Cosine:', get_cosine(vector2, vector3)


#result = 1 - spatial.distance.cosine(sums, sums)
#print result
