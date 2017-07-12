# archivewrapper - wraps a spider into an archive
# scans web.archive.org every our since the latest hour available.
# stops when it has caught up with the database or reaches oldest timestamp

OLDEST_TIMESTAMP_RANGE="20000101000000" # first jan 2000, 00:00:00
ARCHIVE_AVAILABLE_URL_PREFIX="http://archive.org/wayback/available?url="

latestArchivedTimestamp=""
currentTimestamp=""

# fetches the latest archived entry's timestamp
def fetchLatest(baseurl):


# returns the timestamp of the precise our since the supplied timestamp.
def lastHourSince(timestamp):

# returns the latest timestamp of the website url, None if not available.
def latestTimestamp(url):

def spider(searchurl, baseurl, regex, dryrun):

def main(searchurl, baseurl, regex, dryrun):
    currentTimestamp = latestTimestamp(baseurl)
    if currentTimestamp is None:
        print "Spider for " + baseurl + " cannot find latest timestamp"
        return
    # check if latest timestamp differs from latest archived
    fetchLatest(baseurl)
    # if it doesn't then exit
    if (latestArchivedTimestamp == currentTimeStamp):
        print "Spider for " + baseurl + " has no new archives to parse"
        return

    # else spider the current timestamp
    spider(searchurl, baseurl, regex, dryrun, currentTimeStamp)
    # and repeat until a known timestamp is found
    # or we reach oldest allowed
    while(lastestArchivedTimeStamp == currentTimestamp ||
        currentTimestamp > OLDEST_TIMESTAMP_RANGE):
        spider(searchurl, baseurl, regex, dryrun, currentTimeStamp)
        currentTimeStamp = lastHourSince(currentTimeStamp)


if __name__=='__main__':
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))
