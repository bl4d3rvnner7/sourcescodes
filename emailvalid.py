import requests,threading,os
from colorama import init,Fore,Back,Style
init(convert=True)
hotlook=0
office365=0
gmailify=0
invalid=0
def Hotlookify(email):
    global hotlook,invalid
    try:
        link='https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress='+email+'&_=1604288577990'
        data=''
        header = {'Accept': '*/*', 'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36', 'Connection': 'close', 'Host': 'odc.officeapps.live.com', 'Accept-Encoding': 'gzip, deflate', 'Referer': 'https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0', 'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8', 'canary': 'BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c', 'uaid': 'd06e1498e7ed4def9078bd46883f187b', 'Cookie': 'xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354'}
        response=requests.get(link,data=data,headers=header).text
        if 'MSAccount' in response:
                hotlook+=1
                open('Hotmail_Outlook.txt','a+').write(email+"\n")
        else:
            invalid+=1
    except:
        invalid+=1
        pass
def Gmailify(gmail):
    global gmailify,invalid
    try:
        request=requests.get(f"https://mail.google.com/mail/gxlu?email={gmail}")
        if request.cookies.get_dict()["COMPASS"]:
            gmailify+=1
            open('Gmail_Service.txt','a+').write(gmail+"\n")
    except:
        invalid+=1
        pass
def Officely(email):
    global office365,invalid
    try:
        header={'User-Agent': 'Microsoft Office/16.0 (Windows NT 10.0; Microsoft Outlook 16.0.12026; Pro)', 'Accept': 'application/json'}
        payload={"Username":"%s"} % email
        response=requests.get('https://login.microsoftonline.com/common/GetCredentialType',data=payload)
        if '"IfExistsResult":0,' in response.text:
            office365+=1
            open("office365.txt",'a+').write(email+"\n")
        elif '"IfExistsResult":1,' in response.text:
            invalid+=1
    except:
        invalid+=1
        pass
def Checking(email):
    Officely(email)
    if "gmail" in email:Gmailify(email)
    if "hotmail" in email or "outlook" in email:Hotlookify(email)
def Status():
    global gmailify,office365,hotlook,invalid
    while True:
        print(f"{Fore.GREEN}  [=] Valid > Office365({office365}) ~ Gmail_Service({gmailify}) ~ Hotmail&Outlook({hotlook}) |{Fore.RED} Invalid({invalid})",end="\r")
if __name__=='__main__':
    banner="         .                                                      .\n        .n                   .                 .                  n.\n  .   .dP                  dP                   9b                 9b.    .\n 4    qXb         .       dX                     Xb       .        dXp     t\ndX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb\n9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP\n 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP\n  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'\n    `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'\n        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~\n                        )b.  .dbo.dP'`v'`9b.odb.  .dX(\n                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.\n                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb\n                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb\n                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP\n                     `'      9XXXXXX(   )XXXXXXP      `'\n                              XXXX X.`v'.X XXXX\n                              XP^X'`b   d'`X^XX\n                              X. 9  `   '  P )X\n                              `b  `       '  d'\n                               `             '\n                               Cosmic X - Mail_Check"
    os.system("cls")
    os.system("clear")
    print(Fore.RED+banner+Fore.RESET)
    file=input(f" {Fore.GREEN} [+] Input mail list: ")
    xxx=[]
    with open(file,encoding="utf-8",errors="ignore")as list:
        for line in list.readlines():
            if len(line)>3:
                xxx.append(line.strip())
    stat=threading.Thread(target=Status,daemon=True).start()
    for gmail in xxx:
        threading.Thread(target=Checking,args=(gmail,)).start()
