import logging

logger = logging.getLogger(__name__)
logger.propagate = False
logger.info("this is message from helper")
