def log(i):
    f = open("logfile.txt", "a")
    f.write(i)
    f.write("\n")
    f.close()

def login():
    i=0
    a=False
    while a == False: #while password for user != password entered, i+=1
        i+=1
        a = True
    log(i)

login()