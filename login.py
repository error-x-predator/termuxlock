import os
def banner():
             os.system("clear")
             print('''\033[1;36;40m_                             _                _
	     | |_ ___ _ __ _ __ ___  _   ___  _| |__   __ _  ___| | _____ _ __
	     | __/ _ \ '__| '_ ` _ \| | | \ \/ / '_ \ / _` |/ __| |/ / _ \ '__|
	     | ||  __/ |  | | | | | | |_| |>  <| | | | (_| | (__|   <  __/ |
 	      \__\___|_|  |_| |_| |_|\__,_/_/\_\_| |_|\__,_|\___|_|\_\___|_|\033m[0m
                           \033[1;33;40mauthur by ukf\033[0m
              ''')
banner()
if not os.path.isfile("user.txt"):
	f=open("/data/data/com.termux/files/usr/etc/bash.bashrc","a")
	f.write("cd login;python login.py")
	f.close
	print("")
	print("")
	print("")
	user=input("\033[1;33;40mset username :\033[0m \033[1;32;40m")
	print("")
	print("")
	print("")
	pas=input("\033[1;33;40mset password :\033[0m \033[1;32;40m")
	f=open("user.txt","w")
	f.write(f"{user}\n")
	f.write(pas)
	f.close()
else:
	f=open("user.txt","r")
	username=f.readline()
	username=username.strip()
	password=f.readline()
	f.close
	while True:
		    try:
		      print("")
		      print("")
		      user=input("\033[1;33;40mEnter username:\033[0m \033[1;32;40m")
		      if user==username:
				       print("")
				       print("")
				       pas=input("\033[1;33;40mEnter password:\033[0m \033[1;32;40m")
				       if pas==password:
						      banner()
						      break
				       else:
		                            print("")
		                            print("")
		                            print("\033[1;31;40mtry again \033[0m")
		      else:
		           print("")
		           print("")
		           print("\033[1;31;40mtry again \033[0m")
		    except:
	        	   print("")
		           print("")
		           print("\033[1;31;40mtry again \033[0m")
