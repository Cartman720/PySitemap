import argparse
from crawler import Crawler
import ssl                                                                                                                                  

# monkey patch ssl
#ssl.match_hostname = lambda cert, hostname: hostname == cert['subjectAltName'][0][1]
ssl.match_hostname = lambda cert, hostname: True



# initializing parameters
parser = argparse.ArgumentParser(description="Sitemap generator")
parser.add_argument('--url', action="store", default="", help="For example https://www.finstead.com")
parser.add_argument('--exclude', action="store", default="", help="regex pattern to exclude. For example 'symbol/info' will exclude https://www.finstead.com/symbol/info/ORCL")
parser.add_argument('--no-verbose', action="store_true", default="", help="print verbose output")
parser.add_argument('--output', action="store", default="sitemap.xml", help="File path for output, if file exists it will be overwritten")
parser.add_argument('--domain', action="store", default="", help="include subdomains of domain in search")
# parsing parameters
args = parser.parse_args()
url = args.url

found_links = []

# initializeing crawler
crawler = Crawler(url, exclude=args.exclude, domain=args.domain, no_verbose=args.no_verbose);

# fetch links
links = crawler.start()


#write into file
with open(args.output, "w") as file: 
	file.write('<?xml version="1.0" encoding="UTF-8"?>\n\t<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

	for link in links:
		file.write("\n\t\t<url>\n\t\t\t<loc>\n\t\t\t\t{0}\n\t\t\t</loc>\n\t\t</url>".format(link))

	file.write('</urlset>')


