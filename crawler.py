import urllib.request
import re

class Crawler:

	def __init__(self, url, exclude=None, no_verbose=False):
		self.url = url
		self.exclude = exclude
		self.no_verbose = no_verbose
		self.found_links = []
		self.visited_links = []

	def start(self):
		self.crawl(self.url)

		return self.found_links


	def crawl(self, url):
		if not self.no_verbose:
			print(url)

		response = urllib.request.urlopen(url)
		page = str(response.read())

		pattern = '<a [^>]*href=[\'|"](.*?)[\'"].*?>'

		found_links = re.findall(pattern, page)
		links = []

		for link in found_links:
			self.add_url(link, links, self.exclude)
			self.add_url(link, self.found_links)

		for link in links:
			if link not in self.visited_links:
				self.visited_links.append(link)
				self.crawl("{0}{1}".format(self.url, link))

	def add_url(self, link, link_list, exclude_pattern=None):
		link = link.rstrip("/")

		if link:
			url_parts = link.split("://")

			not_in_list = link not in link_list
			is_internal_link = link[0] is "/" or link.startswith(self.url) 
			excluded = False

			if exclude_pattern:
				excluded = re.search(exclude_pattern, link)

			if not_in_list and is_internal_link and not excluded:
				link_list.append(link)
			

			
