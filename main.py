import argparse
import time

import Logger
from Downloader import Downloader
from Provider.ProviderFactory import ProviderFactory


def main(args):
    logger = Logger.get()
    download_count = args.count
    downloader = Downloader(args)

    while True:
        for cc in downloader.iterate_children():
            if download_count <= 0:
                exit()

            entry_id, entry_url = cc['data']['id'], cc['data']['url']
            provider = ProviderFactory.get_instance(entry_url)

            if provider is None:
                logger.error('Provider not found for url %s', entry_url)
                continue

            try:
                downloader.download(provider.get_download_url(), provider.get_filename_with_ext())
                download_count -= 1
                logger.debug("Files left to download: %s", download_count)

                time.sleep(args.sleep)
            except Exception as ex:
                logger.error('error: %s', ex)
            else:
                downloader.set_last_id(entry_id)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--reddit', required=True, help='name of the reddit to download')
    parser.add_argument('-d', '--directory', help='path to the download-directory')
    parser.add_argument('-c', '--count', help='number of elements to download', nargs='?', default=11, type=int)
    parser.add_argument('-s', '--sleep', help='sleep in seconds between requests', nargs='?', default=1, type=int)
    parser.add_argument('-u', '--user_agent', help='user-agent to use for requests', nargs='?',
                        default='reddit-downloader 1.0', type=str)

    main(parser.parse_args())
