# reddit-downloader
Download objects from reddit

## Usage
```
python3 main.py --help
usage: main.py [-h] -r REDDIT [-d DIRECTORY] [-c [COUNT]] [-s [SLEEP]]
               [-u [USER_AGENT]]

optional arguments:
  -h, --help            show this help message and exit
  -r REDDIT, --reddit REDDIT
                        name of the reddit to download
  -d DIRECTORY, --directory DIRECTORY
                        path to the download-directory
  -c [COUNT], --count [COUNT]
                        number of elements to download
  -s [SLEEP], --sleep [SLEEP]
                        sleep in seconds between requests
  -u [USER_AGENT], --user_agent [USER_AGENT]
                        user-agent to use for requests
```

## Example
```
python3 main.py --reddit gifs --count 2 --directory downloads
```

## Troubleshooting
* Provider not found
 The domain is currently not supported, you can add one in the provider-directory.
 Also the `ProviderFactory` must be extended.