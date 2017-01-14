import logging


def get(name='main', level=logging.WARNING):
    formatter = logging.Formatter('%(asctime)s - %(module)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    log = logging.getLogger(name)
    log.setLevel(level)

    if not log.hasHandlers():
        log.addHandler(handler)

    return log
