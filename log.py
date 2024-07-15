import re

def log(i):
    f = open("logfile.txt", "a")
    f.write(str(i))
    f.write("\n")
    f.close()
    count()

def login():
    i="Iam a nonce"
    log(i)


def count():
    f = open("logfile.txt","r")
    Lines=f.readlines()
    print(Lines)
    f.close()


login()