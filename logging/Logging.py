#logging
import logging
import logging.config
import traceback
import time
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
from pythonjsonlogger import jsonlogger


# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.debug("this is a debug message")
logging.info("this is an info message")
logging.warning("this is a warning message")
logging.error("this is an error message")
logging.critical("this is a critical message")

import Helper

sampleLogger = logging.getLogger("sample")
sampleLogger.info("this is message from sample")

stream_h = logging.StreamHandler()
file_h = logging.FileHandler("../logs/file.log")

stream_h.setLevel(logging.DEBUG)
file_h.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

file_logger = logging.getLogger("file")
file_logger.propagate = False
file_logger.addHandler(stream_h)
file_logger.addHandler(file_h)

#start to log
file_logger.debug("debug message will only be in stream")
file_logger.info("info message will be in both stream and file")
#


logging.config.fileConfig("../logs/logging.conf")
# logging.config.dictConfig("../logs/logging.conf")

complexLogger = logging.getLogger("complexExample")
complexLogger.debug("this is a debug message")
complexLogger.info("this is an info message")
complexLogger.warning("this is a warning message")
complexLogger.error("this is an error message")
complexLogger.critical("this is a critical message")

try:
    a = [1,2,3,4]
    val = a[5]
except IndexError as e:
    complexLogger.error(e, exc_info=True)



try:
    x = 10/0
except:
    complexLogger.error("unknown error happen %s", traceback.format_exc())

rotateHandler = RotatingFileHandler("../logs/rotate.log", maxBytes=2000, backupCount=5)
rotateLogger = logging.getLogger("rotate_log")
rotateLogger.setLevel(logging.INFO)
rotateLogger.addHandler(rotateHandler)
for _ in range(10000):
    rotateLogger.info("hello world")


#s, m, h, d, midnight,w0
timeRotateHandle = TimedRotatingFileHandler("../logs/time.log", when='s', interval=5, backupCount=5)
timeRotateLogger = logging.getLogger("time_log")
timeRotateLogger.setLevel(logging.INFO)
timeRotateLogger.addHandler(timeRotateHandle)
for _ in range(10):
    timeRotateLogger.info("hello world")
    time.sleep(1)

#pip install python-json-logger
jlogger = logging.getLogger("json_logger")
jLogHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
jLogHandler.setFormatter(formatter)
jlogger.addHandler(jLogHandler)
jlogger.info({
    "msg": "this is a json message"
})




