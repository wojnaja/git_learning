#! /usr/bin/python3
from time import time
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%Y %B %d %H:%M:%S")
crontest = open("/home/wojnaja/learning/testfile.txt", "a")
crontest.write("\nLog entry " + current_time )
crontest.close()

 