def regf():
    import os.path
    dict = {'NAME': "", 'EML': "", 'NUM': "", 'AGE': "", 'PASS': ""}
    dict['NAME'] = input("your name sir:\t")
    dict['EML'] = input("your email address sir:\t")
    dict['NUM'] = input("your contact number sir:\t")
    dict['AGE'] = input("your age sir:\t")
    dict['PASS'] = input("your password sir:\t")
    if dict['NAME'] == "" or dict['EML'] == "" or dict['NUM'] == "" or dict['AGE'] == "" or dict['PASS'] == "":
        print("wrong registration information")
        print("returning to mainframe")
        regf()
    f=open("user.txt","a")
    filename="user.txt"
    if not os.path.isfile(filename):
        print("no such file exist")
    else:
        f.write(dict['EML'])
        f.write(" ")
        f.write(dict['PASS'])
        f.write("\n")

def login():
    user=input("give us your email adress")
    password=input("giveus the password:")
    for line in open("user.txt","r").readlines():
        login=line.split()
        if user==login[0] and password==login[1]:
            print("login successfull")
        else:
            print("wrong credentials")

login()
regf()

