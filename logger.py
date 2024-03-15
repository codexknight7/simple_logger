import os
import datetime

"""
Konstantin Pankratov
2024-03-15
********************
The following class is an application logger.
It allows to save a record into a LOG file with 
Severity Level, Current Timestamp, and a Message.
Uder the following format:
[ERROR] - 2024-03-15 10:20:25 - An Error occured...

Example of usage:
*****
# import class
from logger import Logger

# instantiate object
app_logger = Logger("./log", "application.log")

# use logger inside the application
logger_object.info("This is an info message")
"""
class Logger(object):

    # Specify the directory path
    # for the LOG file
    file_path = "./log"
    file_name = "application.log"

    def __init__(self, file_path, file_name):
        self.file_path = file_path
        self.file_name = file_name

    def write_log(self, level, msg):
        # Create the directory if not exist
        if not os.path.exists(self.file_path):
            os.makedirs(self.file_path) 

        # Open file in Append mode and add message
        log_path = os.path.join(self.file_path, self.file_name)    
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(log_path, "a") as file:
            file.write("[{0}] - {1} : {2}\n".format(level, timestamp, msg))

    def critical(self, msg):
        self.write_log("CRITICAL", msg)

    def error(self, msg):
        self.write_log("ERROR", msg)

    def warn(self, msg):
        self.write_log("WARN", msg)

    def info(self, msg):
        self.write_log("INFO", msg)

    def debug(self, msg):
        self.write_log("DEBUG", msg)                