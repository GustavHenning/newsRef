import spider, sys


def main(dryrun):
    print dryrun
    # source, baseurl, regex on valid article links
    spider.main('http://www.dn.se','http://www.dn.se', '^/(nyheter|debatt|ekonomi|insidan|sport|sthlm)/(.+-.+-.+)/$', dryrun) # three layers of article words
    spider.main('http://www.svd.se','http://www.svd.se', '^/(.+-.+)/', dryrun) # the first words are connected by hyphens
    spider.main('http://www.svt.se/nyheter', 'http://www.svt.se', '^(/\w+)+(.+-.+)', dryrun) #one or more categories and then hyphen sentences

if __name__=='__main__':
    sys.exit(main(sys.argv[1]))
