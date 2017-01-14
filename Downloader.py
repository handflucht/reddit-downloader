import os
import json

import requests
import Logger


class Downloader:
    url_template = 'http://www.reddit.com/r/{0}/new.json?limit=25'
    url_id_template = 'http://www.reddit.com/r/{0}/new.json?limit=25&after=t3_{1}'

    def __init__(self, args):
        self.last_id = None
        self.args = args
        self.logger = Logger.get()

        # todo set as default-value in argparse
        self.download_dir = os.path.dirname(os.path.abspath(__file__))

        if args.directory is not None:
            self.download_dir += os.path.sep + args.directory
        else:
            self.download_dir += os.path.sep + args.reddit

        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)

    def set_last_id(self, last_id):
        self.last_id = last_id

    def download(self, url, path, append=True):
        self.logger.debug('downloading %s as %s', url, path)

        if append:
            path = os.path.join(self.download_dir, path)

        if os.path.isfile(path):
            self.logger.warning('file %s already exists', path)
            return

        request = requests.get(url, stream=True)

        with open(path, 'wb') as file:
            for data in request.iter_content(chunk_size=1024):
                file.write(data)

    def get_as_json(self):
        if not self.last_id:
            call_url = self.url_template.format(self.args.reddit)
        else:
            call_url = self.url_id_template.format(self.args.reddit, self.last_id)

        request = requests.get(call_url, headers={'User-Agent': self.args.user_agent})
        json_code = json.loads(request.text)

        if 'error' in json_code:
            raise Exception(json_code)

        return json_code

    def iterate_children(self):
        json = self.get_as_json()

        for child in json['data']['children']:
            yield child
