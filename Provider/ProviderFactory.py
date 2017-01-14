from Provider import ProviderGfycat
from Provider import ProviderImgUr


class ProviderFactory:

    @staticmethod
    def get_instance(url):
        provider = None

        if "gfycat.com" in url:
            provider = ProviderGfycat.ProviderGfycat(url)
        elif "imgur.com" in url:
            provider = ProviderImgUr.ProviderImgUr(url)

        return provider
