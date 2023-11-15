import datetime
import time
import sys
import os


def read_file(filename):
    with open(filename, mode='rb') as f:
        print(filename)
        while True:
            #time.sleep(0.001)
            data = f.read(1024)
            if not data:
                print(filename, "done ###############")
                break


def main():
    begin = datetime.datetime.now()
    files = ['../files/file{}.bin'.format(i) for i in range(1, 11)]
    for file in files:
        read_file(file)
    print(datetime.datetime.now() - begin)

main()
