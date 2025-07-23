import logging

def get_logger(name: str):
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s %(name)s: %(message)s'
    )
    handler.setFormatter(formatter)
    if not logger.hasHandlers():
        logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger 