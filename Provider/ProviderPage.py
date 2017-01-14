import abc

import requests
import re


class ProviderPage(object):
    __metaclass__ = abc.ABCMeta

    org_url = ""
    url_regex_list = ""
    html = ""

    def __init__(self, org_url=None, url_regex=None):
        self.org_url = org_url
        self.url_regex_list = url_regex
        self.html = self.get_html(org_url)

    def get_html(self, url=None):
        if url is None:
            url = self.org_url

        req = requests.get(url)
        return req.text

    def get_full_filename(self):
        return self.get_download_url().rsplit('/')[-1]

    def get_file_ext(self):

        # sometime there can be url params like a.gif?noredirect
        extension_with_url_param = self.get_full_filename().rsplit('.')[-1]
        return extension_with_url_param.split('?')[0]

    def get_filename(self):
        return self.get_full_filename().rsplit('.', 1)[0]

    def get_filename_with_ext(self):
        return self.get_filename() + '.' + self.get_file_ext()

    def get_download_url(self):

        # sometimes the file is linked directly
        if self.html.find('<head') == -1:
            return self.org_url

        # return the first hit of the given patterns
        for entry in self.url_regex_list:
            match = re.search(entry, self.html)

            if match is not None:
                break

        return match.group(1)
