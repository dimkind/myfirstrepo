import logging

def write_log(text, file):
    f = open(file, 'a')  # 'a' will append to an existing file if it exists
    f.write("{}\n".format(text))  # write the text to the logfile and move to next line
    return

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

logging.info('an info messge')
# 2017-05-25 00:58:28 INFO     an info messge
logging.debug('a debug message is not shown')

logfile = r"C:\Users\ddimkin\Documents\GitHub\myfirstrepo\testlog.txt"  # name of my log file


# Some code here

# Other code here
print("do that")
write_log("do something else", logfile)

# Even more code here
print("do that")
write_log("do something else", logfile)
