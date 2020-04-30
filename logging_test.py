import logging

mylogger = logging.getLogger(__name__)

#loggin level - DEBUG, INFO, WARNING, ERROR, CRITICAL
# mylogger.setLevel(logging.INFO)

#콘솔
stream_hander = logging.StreamHandler()
mylogger.addHandler(stream_hander)

#폴더
file_handler = logging.FileHandler('my.log')
mylogger.addHandler(file_handler)

def logging_test(func):
    print("working")
    mylogger.warning("retrying %s", func.__name__)

def test():
    return None

if __name__ == "__main__":
    logging_test(test)