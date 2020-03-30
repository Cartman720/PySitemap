import urllib.request
from urllib.parse import urlsplit, urlunsplit, urljoin, urlparse
import re

class Crawler:

	def __init__(self, url, exclude=None, no_verbose=False):
	
		self.url = self.normalize(url)
		self.host = urlparse(self.url).netloc
		self.exclude = exclude
		self.no_verbose = no_verbose
		self.found_links = []
		self.visited_links = [self.url]

	def start(self):
		self.crawl(self.url)

		return self.found_links


	def crawl(self, url):
		if not self.no_verbose:
			print("Parsing " + url)
		try:
			response = urllib.request.urlopen(url)
		except:
			print('404 error')
			return
		
		page = str(response.read())

		pattern = '<a [^>]*href=[\'|"](.*?)[\'"].*?>'

		found_links = re.findall(pattern, page)
		links = []

		for link in found_links:
			is_url = self.is_url(link)

			if is_url:
				is_internal = self.is_internal(link)

				if is_internal:
					self.add_url(link, links, self.exclude)
					self.add_url(link, self.found_links, self.exclude)

		for link in links:
			if link not in self.visited_links:
				link = self.normalize(link)

				self.visited_links.append(link)
				self.crawl(urljoin(self.url, link))

	def add_url(self, link, link_list, exclude_pattern=None):
		link = self.normalize(link)

		if link:			
			not_in_list = link not in link_list

			excluded = False

			if exclude_pattern:
				excluded = re.search(exclude_pattern, link)

			if not_in_list and not excluded:
				link_list.append(link)
			

	def normalize(self, url):
		scheme, netloc, path, qs, anchor = urlsplit(url)
		return urlunsplit((scheme, netloc, path, qs, anchor))

	def is_internal(self, url):
		host = urlparse(url).netloc
		return host == self.host or host == ''	

	def is_url(self, url):
		scheme, netloc, path, qs, anchor = urlsplit(url)
		
		if url != '' and scheme in ['http', 'https', '']:
			return True 
		else:
			return False
