

import time
import datetime

import logging

def main():
    logging.basicConfig(filename='/var/log/python_daemon_example.log',level=logging.DEBUG)
    while(True):
        logging.debug("python example message : "+str(datetime.datetime.now()))
        time.sleep(60)

if __name__ == "__main__":
    main()

