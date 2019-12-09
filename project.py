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
        print("returning to mainframe................")
        regf()

    print("registration successful!!!!!!!")

    f=open("user.txt","a")
    f1=open("register.txt","a")

    filename="user.txt"
    filename1="register.txt"
    if not os.path.isfile(filename):
        print("no such file exist")
    else:
        f.write(dict['EML'])
        f.write(" ")
        f.write(dict['PASS'])
        f.write("\n")

        f1.write(dict['NAME'])
        f1.write(" ")
        f1.write(dict['NUM'])
        f1.write(" ")
        f1.write(dict['AGE'])

    main()

def login():
    import os.path
    user=input("give us your email adress:")
    password=input("giveus the password:")

    if not os.path.isfile("user.txt"):
        print("no such file exist")
    else:
      for line in open("user.txt","r").readlines():
          login=line.split()
          while user!=login[0] and password!=login[1]:
              print("wrong cresentials")
              user = input("give us your email adress: ")
              password = input("giveus the password: ")
          print("login success")

def main():
  print("welcome to the quiz")
  print("press 1 to login\npress 2 to register")
  n=int(input("\n"))
  if n==1:
    login()

  if n==2:
    regf()



main()
