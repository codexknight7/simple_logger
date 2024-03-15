from logger import Logger

app_logger = Logger("./log", "application.log")

for i in range(4):
    app_logger.critical("log message {}".format(i))
    