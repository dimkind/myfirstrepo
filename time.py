import datetime
import logging
import schedule
class Workflow:
    def logSetup():
        logger = logging.getLogger('testlog')
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(fmt='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                                      datefmt = '%m-%d-%y %H:%M:%S')
        fh = TimedRotatingFileHandler('/Documents/projects/python/testlog.log', when='S', interval=5)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger