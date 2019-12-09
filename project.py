from random import sample
import os.path

def regf():


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
          game()

def game():


    print("welcome to the dice game")
    print("""
    choose a number between 1 to 6 
    we will roll the dice for you 
    if you choose the right option
    you will be rewarded with 
    $1000 1st turn will have no fine
    but consicutive turn will deplete $500
    if you answer 3 correct answers you 
    get a bonus point
    good luck! 
    """)

    procede = input("if you are in press yes: ")
    plus = 0
    minus =0
    while procede == 'yes' or procede == 'YES':
        s = [1, 2, 3, 4, 5, 6]
        k = sample(s, 1)

        ans = int(input("your choice:"))

        if k[0] == ans:
            print("right answer!! you earn 1000 rupees")
            plus += 1


        else:
            print("wrong anwer")
            minus+=1

        procede=input("do you want to play more: ")

    total = score(plus, minus)
    if total > 3000:
        total = lifeline(total)

    print("thank you for playing the game")
    rev = int(input("please review us out of five"))

    print("you won the total amount $",total)

def score(pls,min):
    profit=pls*1000

    if min<=1:
        loss =0
    else:
        loss=500*(min-1)

    total = profit-loss



    return total

def lifeline(total):
    n=0
    print("""you have recieved a life line
    you'll be asked for two more times
     but its like a freehit""")
    while n<=2:
        s = [1, 2, 3, 4, 5, 6]
        k = sample(s, 1)

        ans = int(input("your choice"))

        if ans==k[0]:
            print("correct answer")
            total=total+1000
            return total


def main():
  print("welcome to the quiz")
  print("press 1 to login\npress 2 to register")
  n=int(input("\n"))
  if n==1:
    login()

  if n==2:
    regf()



main()