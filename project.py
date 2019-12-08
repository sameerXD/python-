def regf():
  dict={'NAME':"",'EML':"",'NUM':"",'AGE':"",'PASS':""}
  dict['NAME'] = input("your name sir:\t")
  dict['EML'] = input("your email address sir:\t")
  dict['NUM'] = input("your contact number sir:\t")
  dict['AGE'] = input("your age sir:\t")
  dict['PASS'] = input("your password sir:\t")
  if dict['NAME']=="" or dict['EML']=="" or dict['NUM']=="" or dict['AGE']=="" or dict['PASS']=="":
      print("wrong registration information")
      print("returning to mainframe")
      regf()

regf()	
  
