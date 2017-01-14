from Provider import ProviderPage


class ProviderImgUr(ProviderPage.ProviderPage):
    url_regex_list = ['property="og:video"\s+content="([^"]+)"', 'property="og:url"\s+content="([^"]+)"']

    def __init__(self, url):
        super(self.__class__, self).__init__(url, self.url_regex_list)
