from __future__ import print_function
import multiprocessing
import sys
import os
import time
import signal
import re
import json
import ctypes
try:
    from colorama import Fore, Style
except ImportError:
    print("[!] Please install module colorama : pip3 install colorama")
    sys.exit()

try:
    import itertools
except ImportError:
    print("[!] Please install module itertools : pip3 install itertools")
    sys.exit()

try:
    import requests
except ImportError:
    print("[!] Please install module requests : pip3 install requests")
    sys.exit()

try:
    import random
except ImportError:
    print("[!] Please install module random : pip3 install random")
    sys.exit()

try:
    import traceback
except ImportError:
    print("[!] Please install module traceback : pip3 install traceback")
    sys.exit()

try:
    import configparser
except ImportError:
    print("[!] Please install module configparser : pip3 install configparser")
    sys.exit()

try:
    import urllib3
except ImportError:
    print("[!] Please install module urllib3 : pip3 install urllib3")
    sys.exit()

from multiprocessing import Pool, freeze_support, active_children
from os import path
from multiprocessing.pool import INIT
import datetime

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

config = configparser.ConfigParser()
resume = '.session'
config.read(resume)

with open('token.txt') as f:
    lines = f.readlines()

if path.exists('token.txt') is False:
    print("[!] Recheck token.txt file then re run this tool.")
    sys.exit()

for tok in lines:
    if 'LOMPAT' not in tok:
        print("[!] You cant use this token on this scanner! Recheck token.txt file then re run this tool.")
        sys.exit()

with open('token.txt', 'r') as f:
    token = f.readline().strip()

# Global counters
gmail = 0
yahoo = 0
hotmail = 0
aol = 0
icloud = 0
earthlink = 0
sbcglobal = 0
comcast = 0
verizon = 0
chin1 = 0
attnet = 0
tonline = 0
mailru = 0
yandex = 0
cox = 0
gmx = 0
bellsouth = 0
qq = 0
chin2 = 0
libero = 0
webde = 0
zoho = 0
bad = 0
good = 0


def logo():
    logo = f"""
{Fore.MAGENTA}$$\\       $$$$$$\\  $$\\      $$\\ $$$$$$$\\   $$$$$$\\ $$$$$$$$\\ 
{Fore.MAGENTA}$$ |     $$  __$$\\ $$$\\    $$$ |$$  __$$\\ $$  __$$\\__$$  __|
{Fore.MAGENTA}$$ |     $$ /  $$ |$$$$\\  $$$$ |$$ |  $$ |$$ /  $$ |  $$ |   
{Fore.MAGENTA}$$ |     $$ |  $$ |$$\\$$\\$$ $$ |$$$$$$$  |$$$$$$$$ |  $$ |   
{Fore.MAGENTA}$$ |     $$ |  $$ |$$ \\$$$  $$ |$$  ____/ $$  __$$ |  $$ |   
{Fore.MAGENTA}$$ |     $$ |  $$ |$$ |\\$  /$$ |$$ |      $$ |  $$ |  $$ |   
{Fore.MAGENTA}$$$$$$$$\\ $$$$$$  |$$ | \\_/ $$ |$$ |      $$ |  $$ |  $$ |   
{Fore.MAGENTA}\\________|\\______/ \\__|     \\__|\\__|      \\__|  \\__|  \\__|{Fore.WHITE} by {Fore.GREEN}W3LL.STORE\n"""
    for line in logo.split('\n'):
        print(line)
        time.sleep(0.15)


def menu():
    clearConsole()
    logo()
    print(Fore.WHITE)
    print(Fore.WHITE + '[' + Fore.CYAN + 'MENU' + Fore.WHITE + ']')
    print('')
    print('[' + Fore.YELLOW + '1' + Fore.WHITE + '] Validate Emails')
    print('[' + Fore.YELLOW + '2' + Fore.WHITE + '] Validate Emails 365')
    print('[' + Fore.YELLOW + '3' + Fore.WHITE + '] Sort Emails')
    print('[' + Fore.YELLOW + '4' + Fore.WHITE + '] Sort Combos')
    print('[' + Fore.YELLOW + '5' + Fore.WHITE + '] Remove Duplicated Emails')
    print('')
    print('[' + Fore.YELLOW + 'CTRL + C' + Fore.WHITE + '] Go Back To This Menu')
    print('')


def write_file():
    config.write(open(resume, 'w'))


def filelist():
    arr = os.listdir()
    print('')
    print(Fore.YELLOW + 'All files' + Fore.WHITE + '/' + Fore.YELLOW + 'directory' + Fore.WHITE + ':')
    print('')
    for alldir in arr:
        print(Fore.CYAN + alldir + Fore.WHITE)
    print('')


def init_worker():
    signal.signal(signal.SIGINT, signal.SIG_IGN)


def sortallcombo(IPs, IPin, THREAD):
    global bad
    try:
        os.mkdir('result')
    except FileExistsError:
        pass
    
    try:
        combo = IPs.split(':')
        mailcombo = combo[0].split('@')
        
        if '@' not in combo[0]:
            return
        
        if 'www.' in IPs:
            IPs = IPs.replace('www.', '')
            return
        
        # Gmail detection
        if ('@gmail' in combo[0] or '@googlemail' in combo[0] or '@GMail' in combo[0] or 
            '@gMail' in combo[0] or '@gmaiL' in combo[0] or '@gmAil' in combo[0] or 
            '@GoogleMail' in combo[0] or '@GMAil' in combo[0] or '@gMAIL' in combo[0]):
            global gmail
            gmail += 1
            print('[' + Fore.YELLOW + 'GMAIL' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/GMAIL.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Yahoo detection
        elif ('yahoo' in combo[0] or '@ymail' in combo[0] or '@rocketmail' in combo[0] or 
              '@YAHOO' in combo[0] or '@Yahoo' in combo[0] or '@YaHoo' in combo[0] or 
              '@YAHoo' in combo[0] or '@yAhoo' in combo[0] or '@yAHOO' in combo[0] or '@yahOo' in combo[0]):
            global yahoo
            yahoo += 1
            print('[' + Fore.YELLOW + 'YAHOO' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/YAHOO.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Hotmail/Outlook detection
        elif ('@hotmail' in combo[0] or '@live.' in combo[0] or '@outlook' in combo[0] or '@msn.' in combo[0] or
              '@OUTLOOK' in combo[0] or '@HOTMAIL' in combo[0] or '@MSN.' in combo[0] or '@LIVE.' in combo[0] or
              '@Outlook' in combo[0] or '@Msn.' in combo[0] or '@Live.' in combo[0] or '@Hotmail' in combo[0]):
            global hotmail
            hotmail += 1
            print('[' + Fore.YELLOW + 'HOTMAIL' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/HOTMAIL.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # AOL detection
        elif ('@aol.' in combo[0] or '@AOL.' in combo[0] or '@Aol.' in combo[0]):
            global aol
            aol += 1
            print('[' + Fore.YELLOW + 'AOL' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/AOL.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # iCloud detection
        elif ('@icloud' in combo[0] or '@iCloud' in combo[0] or '@mac.' in combo[0] or 
              '@ICLOUD' in combo[0] or '@Icloud' in combo[0] or '@Mac.' in combo[0] or '@MAC.' in combo[0]):
            global icloud
            icloud += 1
            print('[' + Fore.YELLOW + 'ICLOUD' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/ICLOUD.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Earthlink detection
        elif ('@earthlink' in combo[0] or '@Earthlink' in combo[0] or '@EarthLink' in combo[0] or '@EARTHLINK' in combo[0]):
            global earthlink
            earthlink += 1
            print('[' + Fore.YELLOW + 'EARTHLINK' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/EARTHLINK.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # SBCGlobal detection
        elif ('@sbcglobal' in combo[0] or '@SBCglobal' in combo[0] or '@SBCGLOBAL' in combo[0]):
            global sbcglobal
            sbcglobal += 1
            print('[' + Fore.YELLOW + 'SBCGLOBAL' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/SBCGLOBAL.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Comcast detection
        elif ('@comcast' in combo[0] or '@COMCAST' in combo[0] or '@Comcast' in combo[0]):
            global comcast
            comcast += 1
            print('[' + Fore.YELLOW + 'COMCAST' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/COMCAST.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Verizon detection
        elif ('@verizon.' in combo[0] or '@VERIZON.' in combo[0] or '@Verizon.' in combo[0]):
            global verizon
            verizon += 1
            print('[' + Fore.YELLOW + 'VERIZON' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/VERIZON.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # 163.com detection
        elif ('@163.' in combo[0]):
            global chin1
            chin1 += 1
            print('[' + Fore.YELLOW + '163' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/163.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # ATT detection
        elif ('@att.' in combo[0] or '@ATT.' in combo[0] or '@Att.' in combo[0]):
            global attnet
            attnet += 1
            print('[' + Fore.YELLOW + 'ATT' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/ATT.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # T-Online detection
        elif ('@t-online' in combo[0] or '@T-Online' in combo[0] or '@T-online' in combo[0] or '@T-ONLINE' in combo[0]):
            global tonline
            tonline += 1
            print('[' + Fore.YELLOW + 'T-ONLINE' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/T-ONLINE.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Mail.ru / Mail.com detection
        elif ('@mail.ru' in combo[0] or '@MAIL.RU' in combo[0] or '@Mail.ru' in combo[0] or
              '@mail.com' in combo[0] or '@MAIL.COM' in combo[0] or '@Mail.com' in combo[0]):
            global mailru
            mailru += 1
            print('[' + Fore.YELLOW + 'MAIL' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/MAIL-COM.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Yandex detection
        elif ('@yandex' in combo[0] or '@Yandex' in combo[0] or '@YANDEX' in combo[0]):
            global yandex
            yandex += 1
            print('[' + Fore.YELLOW + 'YANDEX' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/YANDEX.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Cox detection
        elif ('@cox.' in combo[0] or '@COX.' in combo[0] or '@Cox.' in combo[0]):
            global cox
            cox += 1
            print('[' + Fore.YELLOW + 'COX' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/COX.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # GMX detection
        elif ('@gmx.' in combo[0] or '@GMX.' in combo[0] or '@Gmx.' in combo[0]):
            global gmx
            gmx += 1
            print('[' + Fore.YELLOW + 'GMX' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/GMX.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Bellsouth detection
        elif ('@bellsouth' in combo[0] or '@Bellsouth' in combo[0] or '@BellSouth' in combo[0] or '@BELLSOUTH' in combo[0]):
            global bellsouth
            bellsouth += 1
            print('[' + Fore.YELLOW + 'BELLSOUTH' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/BELLSOUTH.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # QQ detection
        elif ('@qq.' in combo[0] or '@QQ.' in combo[0]):
            global qq
            qq += 1
            print('[' + Fore.YELLOW + 'QQ' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/QQ.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # 126.com detection
        elif ('@126.' in combo[0]):
            global chin2
            chin2 += 1
            print('[' + Fore.YELLOW + '126' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/126.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Libero detection
        elif ('@libero.' in combo[0] or '@Libero.' in combo[0] or '@LIBERO.' in combo[0]):
            global libero
            libero += 1
            print('[' + Fore.YELLOW + 'LIBERO' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/LIBERO.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Web.de detection
        elif ('@web.' in combo[0] or '@Web.' in combo[0] or '@WEB.' in combo[0]):
            global webde
            webde += 1
            print('[' + Fore.YELLOW + 'WEB.DE' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/WEB.DE.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Zoho detection
        elif ('@zoho.' in combo[0] or '@Zoho.' in combo[0] or '@ZOHO.' in combo[0]):
            global zoho
            zoho += 1
            print('[' + Fore.YELLOW + 'ZOHO' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/ZOHO.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Check for valid combo format
        if (len(mailcombo[0]) < 2 or len(mailcombo[1]) < 3 or len(IPs) < 8 or 
            '@' not in combo[0] or ':' not in IPs or ' ' in IPs or '﻿' in IPs or 
            '$HEX' in IPs or '__' in combo[0] or '?' in combo[0] or '!' in combo[0]):
            bad += 1
            print('[' + Fore.RED + 'BAD' + Fore.WHITE + '] ' + IPs)
            return
        
        # Good combo
        global good
        good += 1
        print('[' + Fore.GREEN + 'GOOD' + Fore.WHITE + '] ' + IPs)
        config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
        write_file()
        with open('result/GOOD.txt', 'a+') as save:
            save.write(IPs + '\n')
        
    except Exception as e:
        bad += 1
        print('[' + Fore.RED + 'BAD' + Fore.WHITE + '] ' + IPs)
    except KeyboardInterrupt:
        print('[' + Fore.YELLOW + '!' + Fore.WHITE + '] Program Quiting!')
        sys.exit()
    
    # Update console title with statistics
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(
            f'LOMPAT BY W3LL | Good - {good} | Bad - {bad} | Gmail - {gmail} | Yahoo - {yahoo} | '
            f'Hotmail - {hotmail} | Aol - {aol} | Icloud - {icloud} | Earthlink - {earthlink} | '
            f'Sbcglobal - {sbcglobal} | Comcast - {comcast} | Verizon - {verizon} | 163.com - {chin1} | '
            f'Att - {attnet} | T-online - {tonline} | Mail.com - {mailru} | Yandex - {yandex} | '
            f'Cox - {cox} | Gmx - {gmx} | Bellsouth - {bellsouth} | QQ - {qq} | 126.com - {chin2} | '
            f'Libero - {libero} | Web.de - {webde} | Zoho - {zoho}'
        )
    else:
        sys.stdout.write(
            f'\x1b]2;LOMPAT BY W3LL | Good - {good} | Bad - {bad} | Gmail - {gmail} | Yahoo - {yahoo} | '
            f'Hotmail - {hotmail} | Aol - {aol} | Icloud - {icloud} | Earthlink - {earthlink} | '
            f'Sbcglobal - {sbcglobal} | Comcast - {comcast} | Verizon - {verizon} | 163.com - {chin1} | '
            f'Att - {attnet} | T-online - {tonline} | Mail.com - {mailru} | Yandex - {yandex} | '
            f'Cox - {cox} | Gmx - {gmx} | Bellsouth - {bellsouth} | QQ - {qq} | 126.com - {chin2} | '
            f'Libero - {libero} | Web.de - {webde} | Zoho - {zoho}\x07'
        )


def lompat(IPs, IPin, THREAD):
    try:
        halo = ''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0'
        }
        params = (('email', IPs), ('key', '52d5d6dd-cd2b-4e5a-a76a-1667aea3a6fc'))
        response = requests.get('https://verify.gmass.co/verify', headers=headers, params=params)
        data = json.loads(response.text)
        
        if data['Valid']:
            print('[' + Fore.GREEN + '+' + Fore.WHITE + '] ' + IPs + Fore.YELLOW + ' > ' + Fore.GREEN + 'VALID' + Fore.WHITE)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            halo = IPs + '\n'
            with open('W3LL_EMAILS_VALID.txt', 'a+') as save:
                save.write(halo)
        else:
            print('[' + Fore.RED + '-' + Fore.WHITE + '] ' + IPs + Fore.YELLOW + ' > ' + Fore.RED + 'INVALID' + Fore.WHITE)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            halo = IPs + '\n'
            with open('W3LL_EMAILS_INVALID.txt', 'a+') as save:
                save.write(halo)
    except Exception:
        print('[' + Fore.RED + '-' + Fore.WHITE + '] ' + IPs + Fore.YELLOW + ' > ' + Fore.RED + 'INVALID' + Fore.WHITE)
    except KeyboardInterrupt:
        print('[' + Fore.YELLOW + '!' + Fore.WHITE + '] Program Quiting!')
        sys.exit()


def lompat365(IPs, IPin, THREAD):
    try:
        halo = ''
        user = IPs.split('@')
        
        # Filter out invalid emails
        filters = ['godaddy.', '.png', '.gif', '.jpg', '.gov', '.sch', '.edu', '.svg', '.jpeg',
                   'example', '.doc', 'font', '.xls', '.ico', '.html', '.htm', '.sch.', '.ac.',
                   'email.', 'you', 'javascript', 'test', 'debug', 'drupal', 'collage', 'apache',
                   'bootstrap', 'u003', 'wixpress.', 'wix.', 'domain', 'webp', 'sentry.', '.x',
                   'site.', 'address.', '126.', '163.', 'aol.', 'att.net', 'bellsouth.', 'comcast.',
                   'earthlink.', 'whois.', 'google.', 'orange.', 'aspx', '.asp', 'contact', 'contato',
                   'education', 'enquiries', 'enquiry', 'hello', 'info@', 'mail@', 'marketing@',
                   'office@', 'webmaster@', 'booking', 'event', 'customercare@', 'cs@', 'support',
                   'service', 'reservation', 'reception', 'question', 'privacy', 'ontact', 'noreply',
                   'no-reply', 'inquiry', 'customer', 'client']
        
        if (len(user[0]) > 30 or any(f in IPs for f in filters)):
            print('[' + Fore.RED + '-' + Fore.WHITE + '] ' + IPs + Fore.YELLOW + ' > ' + Fore.RED + 'INVALID' + Fore.WHITE)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            return
        
        # First validate with GMass
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0'
        }
        params = (('email', IPs), ('key', '52d5d6dd-cd2b-4e5a-a76a-1667aea3a6fc'))
        response = requests.get('https://verify.gmass.co/verify', headers=headers, params=params)
        data = json.loads(response.text)
        
        if data['Valid']:
            # Check Office365
            headers365 = {
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55',
                'Content-type': 'application/json; charset=UTF-8'
            }
            params365 = (('mkt', 'en-US'),)
            data365 = f'{{"username":"{IPs}"}}'
            response365 = requests.post('https://login.microsoftonline.com/common/GetCredentialType', headers=headers365, params=params365, data=data365)
            
            if 'IfExistsResult":0' in response365.text and 'IsSignupDisallowed":true' in response365.text:
                print('[' + Fore.GREEN + '+' + Fore.WHITE + '] ' + IPs + Fore.YELLOW + ' > ' + Fore.GREEN + 'VALID' + Fore.WHITE)
                config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
                write_file()
                halo = IPs + '\n'
            else:
                print('[' + Fore.RED + '-' + Fore.WHITE + '] ' + IPs + Fore.YELLOW + ' > ' + Fore.RED + 'INVALID' + Fore.WHITE)
                config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
                write_file()
        else:
            print('[' + Fore.RED + '-' + Fore.WHITE + '] ' + IPs + Fore.YELLOW + ' > ' + Fore.RED + 'INVALID' + Fore.WHITE)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
        
        with open('W3LL_EMAILS365.txt', 'a+') as save:
            save.write(halo)
    except KeyboardInterrupt:
        print('[' + Fore.YELLOW + '!' + Fore.WHITE + '] Program Quiting!')
        sys.exit()


def sortall(IPs, IPin, THREAD):
    try:
        os.mkdir('result')
    except FileExistsError:
        pass
    
    try:
        user = IPs.split('@')
        
        if 'www.' in IPs:
            IPs = IPs.replace('www.', '')
            return
        
        # Filter trash emails
        if (len(user[0]) > 20 or any(f in IPs for f in ['godaddy.', '.png', '.gif', '.jpg', '.gov', '.sch', '.edu',
            '.svg', '.jpeg', 'example', '.doc', 'font', '.xls', '.ico', '.html', '.htm', 'email.', 'you',
            'javascript', 'test', 'debug', 'drupal', 'collage', 'apache', 'bootstrap', 'u003', 'wixpress.',
            'wix.', 'domain', 'webp', 'sentry.', '.x', 'site.', 'address.', 'whois.', 'google.', 'orange.',
            'aspx', '.asp', 'contact', 'enquiry', 'hello', 'info@', 'mail@', 'marketing@', 'office@',
            'webmaster@', 'booking', 'event', 'customercare@', 'cs@', 'support', 'service', 'reservation',
            'reception', 'question', 'privacy', 'ontact', 'noreply', 'no-reply', 'inquiry', 'customer', 'client'])):
            print('[' + Fore.RED + 'TRASH' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/TRASH.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Filter patterns
        if (re.findall(r'(\\.*?)(0\\.0\\.|re-|user-|Response|r-|noreply|reply|hello|news|feedback|NoReply|replies|part|HTML|jpg|bounce|012|award|form|format|forum|hosted|hostmaster|info|partners|phishing|quotes|quote|why|your|shop|secretary|service|policy|orders|order|name|membership|editor|domains|digital|contact|content|complaints|community|collections|comments|advertising|advice|awards|careers|communications|compliance|enquires|found|here|help|honeypot|inquiries|inventories|tech|technicaltraining|treasurer|u00|view|welcome|available|online|paypal|person|press|product|project|properties|reservations|research|returns|search|studio|training|team|accounts|work|wordpress|access|subscriptions|sch|education|school|academy|college|academic|utoronto|uwinnipeg|ucalgary|teacher|umontreal|ubc|campus|educate|covid|pharmacy|website|customerservices|customer|enquiry|events|gouv|hpplaw\\.co\\.uk|magazine|email|email\\.|news|bounce|members|communications|comms|announcement|afibel|warrenmurton|music-minded|ukSEAD|marketo1|ac\\.uk|sch|gov\\.|college|education|edu\\.|academics|school|academy|utoronto|uwinnipeg|ucalgary|teacher|umontreal|ubc.ca|polymtl|uoguelph|dal.ca|your|campus|educate|covid|subscriptions|team|pharmacy|_@|me\\.|e-mail|onmicrosoft\\.com|image|abuse|wow\\.|virgin\\.|mimecast\\.|zoom\\.|courses|coupon|amazon|cp@|CP@|cs@|CS@|Cs@|customdev|Customer|CUSTOMER|Service|enquiries|Enquiries|equity|Events|event|notification|notice|Notice|office|offer|Office|microsoft\\.|operations|Operations|ops@|Ops@|OPS|postmaster|Postmaster|privacy|Privacy|promo|Promo|reservas|reservation|request|response|return|rewards|support|survey|test|tracking|unsubscribe|subscribe|imap|webex|xxx|x\\.|tdi\\.|t\\.|juno\\.|commercial|communication|company|comercial|hi@|hola|mail|rr|webmaster|contato|post|tiktok|web@\\.)', IPs) or
            re.findall(r'^[-!$%^&*()_+|~=`{}\[\]\:;<>?,\.\/](\.*?)', IPs) or
            re.findall(r'^mail|maintenance', IPs)):
            print('[' + Fore.RED + 'TRASH' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/TRASH.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Gmail detection
        if re.findall(r'(\\.*?)(gmail|GMAIL|Gmail|google|googlemail|GMail|gMail|gmaiL|gmAil|GoogleMail|GMAil|gMAIL)', IPs):
            print('[' + Fore.YELLOW + 'GMAIL' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/GMAIL.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Yahoo detection
        elif re.findall(r'(\\.*?)(yahoo|ymail|rocketmail|YAHOO|Yahoo|YaHoo|YAHoo|yAhoo|yAHOO|yahOo)', IPs):
            print('[' + Fore.YELLOW + 'YAHOO' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/YAHOO.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Hotmail detection
        elif re.findall(r'(\\.*?)(hotmail\\.|live\\.|outlook\\.|msn\\.|OUTLOOK\\.|HOTMAIL\\.|MSN\\.|LIVE\\.|Outlook\\.|Msn\\.|Live\\.|Hotmail\\.)', IPs):
            print('[' + Fore.YELLOW + 'HOTMAIL' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/HOTMAIL.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # AOL detection
        elif re.findall(r'(\\.*?)(aol\\.|AOL\\.|Aol\\.)', IPs):
            print('[' + Fore.YELLOW + 'AOL' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/AOL.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # iCloud detection
        elif re.findall(r'(\\.*?)(icloud\\.|iCloud\\.|mac\\.com|ICLOUD|Icloud)', IPs):
            print('[' + Fore.YELLOW + 'ICLOUD' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/ICLOUD.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Earthlink detection
        elif re.findall(r'(\\.*?)(earthlink\\.|Earthlink\\.)', IPs):
            print('[' + Fore.YELLOW + 'EARTHLINK' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/EARTHLINK.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # SBCGlobal detection
        elif re.findall(r'(\\.*?)(sbcglobal\\.com|sbcglobal\\.net|sbcglobal\\.|SBCglobal)', IPs):
            print('[' + Fore.YELLOW + 'SBCGLOBAL' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/SBCGLOBAL.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Comcast detection
        elif re.findall(r'(\\.*?)(comcast\\.|comcast\\.net|COMCAST|Comcast)', IPs):
            print('[' + Fore.YELLOW + 'COMCAST' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/COMCAST.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Verizon detection
        elif re.findall(r'(\\.*?)(verizon\\.net|verizon\\.com|VERIZON|Verizon)', IPs):
            print('[' + Fore.YELLOW + 'VERIZON' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/VERIZON.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # 163.com detection
        elif re.findall(r'(\\.*?)(163\\.net|163\\.com)', IPs):
            print('[' + Fore.YELLOW + '163' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/163.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # ATT detection
        elif re.findall(r'(\\.*?)(att\\.net|att\\.com)', IPs):
            print('[' + Fore.YELLOW + 'ATT' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/ATT.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # T-Online detection
        elif re.findall(r'(\\.*?)(t-online\\.|T-online|T-Online)', IPs):
            print('[' + Fore.YELLOW + 'T-ONLINE' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/T-ONLINE.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Mail.com / Mail.ru detection
        elif re.findall(r'(\\.*?)(mail\\.ru|mail\\.com)', IPs):
            print('[' + Fore.YELLOW + 'MAIL' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/MAIL-COM.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Yandex detection
        elif re.findall(r'(\\.*?)(yandex\\.|YANDEX|Yandex)', IPs):
            print('[' + Fore.YELLOW + 'YANDEX' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/YANDEX.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Cox detection
        elif re.findall(r'(\\.*?)(cox\\.net|COX\\.|Cox\\.)', IPs):
            print('[' + Fore.YELLOW + 'COX' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/COX.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # GMX detection
        elif re.findall(r'(\\.*?)(gmx\\.de|gmx\\.com|gmx\\.net|GMX\\.|Gmx\\.|gmx\\.)', IPs):
            print('[' + Fore.YELLOW + 'GMX' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/GMX.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Bellsouth detection
        elif re.findall(r'(\\.*?)(bellsouth\\.|BELLSOUTH|Bellsouth)', IPs):
            print('[' + Fore.YELLOW + 'BELLSOUTH' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/BELLSOUTH.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # QQ detection
        elif re.findall(r'(\\.*?)(qq\\.|QQ)', IPs):
            print('[' + Fore.YELLOW + 'QQ' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/QQ.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # 126.com detection
        elif re.findall(r'(\\.*?)(126\\.)', IPs):
            print('[' + Fore.YELLOW + '126' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/126.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Libero detection
        elif re.findall(r'(\\.*?)(libero\\.|LIBERO|Libero)', IPs):
            print('[' + Fore.YELLOW + 'LIBERO' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/LIBERO.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Web.de detection
        elif re.findall(r'(\\.*?)(web\\.de|WEB\\.DE|Web\\.de)', IPs):
            print('[' + Fore.YELLOW + 'WEB.DE' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/WEB.DE.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # American TLDs
        elif re.findall(r'(\\.*?)(\\.ac|\\.ag|\\.ai|\\.as|\\.biz\\.pr|\\.biz\\.tt|\\.bo|\\.bs|\\.bz|\\.cl|\\.co\\.ag|\\.co\\.bz|\\.co\\.cr|\\.co\\.dm|\\.co\\.gy|\\.co\\.lc|\\.co\\.ms|\\.co\\.ni|\\.co\\.tt|\\.co\\.ve|\\.co\\.vi|\\.com\\.ag|\\.com\\.ai|\\.com\\.ar|\\.com\\.bo|\\.com\\.bs|\\.com\\.bz|\\.com\\.co|\\.com\\.do|\\.com\\.ec|\\.com\\.gp|\\.com\\.gt|\\.com\\.gy|\\.com\\.hn|\\.com\\.ht|\\.com\\.jm|\\.com\\.kn|\\.com\\.lc|\\.com\\.ms|\\.com\\.mx|\\.com\\.ni|\\.com\\.pa|\\.com\\.pe|\\.com\\.pr|\\.com\\.py|\\.com\\.sv|\\.com\\.tt|\\.com\\.uy|\\.com\\.vc|\\.com\\.ve|\\.com\\.vi|\\.cr|\\.dm|\\.do|\\.ec|\\.gd|\\.gp|\\.gs|\\.gt|\\.gy|\\.hn|\\.ht|\\.info\\.ec|\\.kn|\\.lc|\\.mex\\.com|\\.ms|\\.mx|\\.net\\.ag|\\.net\\.bz|\\.net\\.co|\\.net\\.ec|\\.net\\.ht|\\.net\\.pr|\\.net\\.vc|\\.nom\\.ag|\\.nom\\.co|\\.north\\.am|\\.org\\.ag|\\.org\\.bz|\\.org\\.ht|\\.org\\.ms|\\.org\\.pr|\\.org\\.vc|\\.pa|\\.pe|\\.pr|\\.south\\.am|\\.sx|\\.tc|\\.tt|\\.us|\\.us\\.com|\\.us\\.org|\\.uy|\\.vc|\\.vg)+$', IPs):
            print('[' + Fore.GREEN + 'AMERICAN' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/AMERICAN.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Asian TLDs
        elif re.findall(r'(\\.*?)(\\.ac\\.nz|\\.ae|\\.ae\\.org|\\.af|\\.asia|\\.az|\\.bh|\\.biz\\.fj|\\.biz\\.id|\\.biz\\.ki|\\.biz\\.pk|\\.cc|\\.cn|\\.cn\\.com|\\.co\\.id|\\.co\\.in|\\.co\\.kr|\\.co\\.nz|\\.co\\.th|\\.th|\\.com\\.af|\\.com\\.az|\\.com\\.bd|\\.com\\.bh|\\.com\\.cn|\\.com\\.fj|\\.com\\.hk|\\.com\\.jo|\\.com\\.ki|\\.com\\.kz|\\.com\\.lk|\\.com\\.my|\\.com\\.nf|\\.com\\.ph|\\.com\\.pk|\\.com\\.ps|\\.com\\.sa|\\.com\\.sb|\\.com\\.sg|\\.com\\.tw|\\.com\\.vn|\\.com\\.vu|\\.cx|\\.edu\\.sg|\\.firm\\.in|\\.fm|\\.geek\\.nz|\\.gen\\.in|\\.gen\\.nz|\\.hk|\\.hk\\.com|\\.hk\\.org|\\.id|\\.idv\\.hk|\\.in|\\.in\\.net|\\.in\\.th|\\.inc\\.hk|\\.ind\\.in|\\.info\\.fj|\\.info\\.ki|\\.info\\.nf|\\.int\\.az|\\.io|\\.jo|\\.ki|\\.kiwi\\.nz|\\.kr|\\.kz|\\.la|\\.lk|\\.ltd\\.hk|\\.maori\\.nz|\\.mn|\\.mobi\\.ki|\\.my|\\.my\\.id|\\.name\\.fj|\\.ne\\.kr|\\.net\\.az|\\.net\\.cn|\\.net\\.fj|\\.net\\.in|\\.net\\.ki|\\.net\\.nf|\\.net\\.nz|\\.net\\.pk|\\.net\\.ps|\\.net\\.sb|\\.net\\.vn|\\.nf|\\.nu|\\.nz|\\.or\\.kr|\\.org\\.az|\\.org\\.cn|\\.org\\.fj|\\.org\\.hk|\\.org\\.in|\\.org\\.ki|\\.org\\.kz|\\.org\\.lk|\\.org\\.nz|\\.org\\.pk|\\.org\\.ps|\\.org\\.sb|\\.org\\.sg|\\.org\\.vn|\\.per\\.sg|\\.ph|\\.phone\\.ki|\\.pk|\\.pp\\.az|\\.pro\\.fj|\\.ps|\\.qa|\\.sa|\\.sa\\.com|\\.sb|\\.school\\.nz|\\.sg|\\.tk|\\.tl|\\.tm|\\.to|\\.tv|\\.tw|\\.vn|\\.vu|\\.web\\.id|\\.web\\.nf|\\.web\\.pk|\\.ws|\\.í•œêµ­|\\.å…¬å¸\\.é¦™æ¸¯|\\.ä¸­å›½|\\.é¦™æ¸¯|\\.Ø§Ù…Ø§Ø±Ø§Øª|\\.Ø§Ù„Ø³Ø¹ÙˆØ¯ÙŠØ©|\\.ç¶²çµ¡\\.é¦™æ¸¯|\\.çµ„ç¹”\\.é¦™æ¸¯|\\.Ù‚Ø·Ø±)+$', IPs):
            print('[' + Fore.GREEN + 'ASIAN' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/ASIA.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Netherlands
        elif re.findall(r'(\\.*?)(\\.co\\.nl|\\.nl)+$', IPs):
            print('[' + Fore.GREEN + 'NETHERLAND' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/NETHERLAND.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # United Kingdom
        elif re.findall(r'(\\.*?)(\\.uk\\.*?|\\.uk\\.com|\\.co\\.uk|\\.ltd\\.uk|\\.me\\.uk|\\.org\\.uk|\\.uk\\.net)+$', IPs):
            print('[' + Fore.GREEN + 'UNITED KINGDOM' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/UNITED-KINGDOM.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # France
        elif re.findall(r'(\\.*?)(\\.fr)+$', IPs):
            print('[' + Fore.GREEN + 'FRANCE' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/FRANCE.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Japan
        elif re.findall(r'(\\.*?)(\\.co\\.jp|\\.jp|\\.jp\\.net|\\.jp\\.com|\\.or\\.jp)+$', IPs):
            print('[' + Fore.GREEN + 'JAPAN' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/JAPAN.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Brazil
        elif re.findall(r'(\\.*?)(\\.tv\\.br|\\.net\\.br|\\.com\\.br|\\.br\\.com|\\.br)+$', IPs):
            print('[' + Fore.GREEN + 'BRAZIL' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/BRAZIL.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Canada
        elif re.findall(r'(\\.*?)(\\.ca)+$', IPs):
            print('[' + Fore.GREEN + 'CANADA' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/CANADA.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Australia
        elif re.findall(r'(\\.*?)(\\.asn\\.au|\\.au\\.biz|\\.au\\.info|\\.au\\.net|\\.id\\.au|\\.net\\.au|\\.com\\.au|\\.org\\.au|\\.au\\.)+$', IPs):
            print('[' + Fore.GREEN + 'AUSTRALIA' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/AUSTRALIA.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Germany
        elif re.findall(r'(\\.*?)(\\.com\\.de|\\.de|\\.de\\.com)+$', IPs):
            print('[' + Fore.GREEN + 'GERMAN' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/GERMAN.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Italy
        elif re.findall(r'(\\.*?)(\\.it)+$', IPs):
            print('[' + Fore.GREEN + 'ITALY' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/ITALY.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # European
        elif re.findall(r'(\\.*?)(\\.ac\\.im|\\.am|\\.at|\\.ba|\\.be|\\.bg|\\.biz\\.pl|\\.biz\\.tr|\\.by|\\.ch|\\.co\\.at|\\.co\\.ee|\\.co\\.gg|\\.co\\.gl|\\.co\\.hu|\\.co\\.il|\\.co\\.im|\\.co\\.je|\\.co\\.no|\\.co\\.rs|\\.com\\.es|\\.com\\.gl|\\.com\\.gr|\\.com\\.hr|\\.com\\.im|\\.com\\.mk|\\.com\\.mt|\\.com\\.pl|\\.com\\.pt|\\.com\\.ro|\\.com\\.ru|\\.com\\.se|\\.com\\.tr|\\.com\\.ua|\\.cz|\\.dk|\\.ee|\\.es|\\.eu|\\.eu\\.com|\\.fi|\\.gb\\.net|\\.gg|\\.gr|\\.gr\\.com|\\.hr|\\.hu|\\.hu\\.net|\\.ie|\\.im|\\.in\\.rs|\\.info\\.pl|\\.info\\.tr|\\.is|\\.je|\\.li|\\.lt|\\.ltd\\.co\\.im|\\.lu|\\.lv|\\.md|\\.mk|\\.mp|\\.mt|\\.net\\.im|\\.net\\.mt|\\.net\\.pl|\\.net\\.ru|\\.net\\.ua|\\.no|\\.nom\\.es|\\.or\\.at|\\.org\\.es|\\.org\\.il|\\.org\\.im|\\.org\\.mt|\\.org\\.pl|\\.org\\.ua|\\.pl|\\.plc\\.co\\.im|\\.pm|\\.pt|\\.re|\\.ro|\\.rs|\\.ru|\\.ru\\.com|\\.se|\\.se\\.net|\\.si|\\.sk|\\.su|\\.tf|\\.tv\\.tr|\\.ua|\\.web\\.tr|\\.wf|\\.Ñ€Ñ„)+$', IPs):
            print('[' + Fore.GREEN + 'EUROPEAN' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/EUROPEAN.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # African
        elif re.findall(r'(\\.*?)(\\.africa\\.com|\\.bi|\\.cd|\\.cg|\\.cm|\\.co\\.bi|\\.co\\.cm|\\.co\\.ke|\\.co\\.mg|\\.co\\.mw|\\.co\\.na|\\.co\\.ug|\\.co\\.za|\\.com\\.bi|\\.com\\.cm|\\.com\\.ly|\\.com\\.mg|\\.com\\.mw|\\.com\\.na|\\.com\\.ng|\\.com\\.sc|\\.coop\\.mw|\\.ly|\\.mg|\\.mu|\\.mw|\\.na|\\.net\\.cm|\\.net\\.mg|\\.net\\.za|\\.ng|\\.or\\.bi|\\.org\\.mg|\\.org\\.na|\\.org\\.za|\\.rw|\\.sc|\\.sh|\\.sl|\\.so|\\.st|\\.ug|\\.web\\.za|\\.za\\.com)+$', IPs):
            print('[' + Fore.GREEN + 'AFRICAN' + Fore.WHITE + '] ' + IPs)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/AFRICAN.txt', 'a+') as save:
                save.write(IPs + '\n')
            return
        
        # Default good
        else:
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            with open('result/GOOD.txt', 'a+') as save:
                save.write(IPs + '\n')
    except KeyboardInterrupt:
        print('[' + Fore.YELLOW + '!' + Fore.WHITE + '] Program Quiting!')
        sys.exit()


def input_num(word):
    try:
        thread = int(input(word))
    except ValueError:
        print(Fore.YELLOW + 'Please insert only a number value' + Fore.WHITE)
        return input_num(word)
    
    if thread < 1 or thread > 50:
        print(Fore.RED + 'Insert number that not under ' + Fore.YELLOW + '1' + Fore.RED + ' and more than ' + Fore.YELLOW + '50' + Fore.RED + '.' + Fore.WHITE)
        return input_num(word)
    return thread


def input_file():
    try:
        IPin = input(Fore.WHITE + 'Enter Your List: ' + Fore.YELLOW)
    except ValueError:
        return input_file()
    
    if path.exists(IPin) is False:
        print(Fore.RED + 'List ' + Fore.YELLOW + IPin + Fore.RED + ' is not found on your current directory.' + Fore.WHITE)
        return input_file()
    return IPin


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def lompatall():
    """Validate Emails - Main function"""
    clearConsole()
    logo()
    print(Fore.WHITE + '[ ' + Fore.CYAN + 'W3LL EMAIL VALIDATOR' + Fore.WHITE + ' ]')
    print('')
    
    if os.path.exists(resume):
        print('[' + Fore.YELLOW + '+' + Fore.WHITE + '] We Found A Session!')
        con = input('[' + Fore.YELLOW + '+' + Fore.WHITE + '] Do you want to continue session ? [y/n] ')
        
        if 'Y' in con or 'y' in con:
            IPin = config.get(token, 'list')
            fromlast = config.get(token, 'lastip')
            with open(IPin) as f:
                IPs = f.read().split(fromlast + '\n')[1].split()
            THREAD = int(config.get(token, 'thread'))
            start_time = datetime.datetime.now()
            print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'W3LL_EMAILS.txt' + Fore.WHITE)
            
            p = Pool(THREAD, init_worker)
            a = 0
            for i in IPs:
                if a != THREAD:
                    cleango = p.apply_async(lompat, args=(i, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            if os.path.exists(resume):
                os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'EMAIL VALIDATION COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'W3LL_EMAILS.txt' + Fore.WHITE)
            time.sleep(3)
        else:
            filelist()
            IPin = input_file()
            with open(IPin, 'r') as f:
                IPs = list(set(f.read().split()))
            THREAD = input_num(Fore.WHITE + 'Enter Your Thread [Max is 50]: ' + Fore.YELLOW)
            start_time = datetime.datetime.now()
            print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'W3LL_EMAILS.txt' + Fore.WHITE)
            
            p = Pool(THREAD, init_worker)
            a = 0
            for i in IPs:
                if a != THREAD:
                    cleango = p.apply_async(lompat, args=(i, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            if os.path.exists(resume):
                os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'EMAIL VALIDATION HAS COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'W3LL_EMAILS.txt' + Fore.WHITE)
            time.sleep(3)
    else:
        filelist()
        IPin = input_file()
        with open(IPin, 'r') as f:
            IPs = list(set(f.read().split()))
        THREAD = input_num(Fore.WHITE + 'Enter Your Thread [Max is 50]: ' + Fore.YELLOW)
        start_time = datetime.datetime.now()
        print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'W3LL_EMAILS.txt' + Fore.WHITE)
        
        p = Pool(THREAD, init_worker)
        a = 0
        for i in IPs:
            if a != THREAD:
                cleango = p.apply_async(lompat, args=(i, IPin, THREAD))
            else:
                a = 0
                time.sleep(THREAD)
        p.close()
        p.join()
        
        if os.path.exists(resume):
            os.remove('.session')
        end_time = datetime.datetime.now()
        long = end_time - start_time
        pot = str(long).split('.')
        print(Fore.WHITE + 'EMAIL VALIDATION HAS COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'W3LL_EMAILS.txt' + Fore.WHITE)
        time.sleep(3)


def lompatall365():
    """Validate Emails 365 - Main function"""
    clearConsole()
    logo()
    print(Fore.WHITE + '[ ' + Fore.CYAN + 'W3LL EMAIL365 VALIDATOR ' + Fore.WHITE + ' ]')
    print('')
    
    if os.path.exists(resume):
        print('[' + Fore.YELLOW + '+' + Fore.WHITE + '] We Found A Session!')
        con = input('[' + Fore.YELLOW + '+' + Fore.WHITE + '] Do you want to continue session ? [y/n] ')
        
        if 'Y' in con or 'y' in con:
            IPin = config.get(token, 'list')
            fromlast = config.get(token, 'lastip')
            with open(IPin) as f:
                IPs = f.read().split(fromlast + '\n')[1].split()
            THREAD = int(config.get(token, 'thread'))
            start_time = datetime.datetime.now()
            print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'W3LL_EMAILS365.txt' + Fore.WHITE)
            
            p = Pool(THREAD, init_worker)
            a = 0
            for i in IPs:
                if a != THREAD:
                    cleango = p.apply_async(lompat365, args=(i, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            if os.path.exists(resume):
                os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'EMAIL VALIDATION HAS COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'W3LL_EMAILS365.txt' + Fore.WHITE)
            time.sleep(3)
        else:
            filelist()
            IPin = input_file()
            with open(IPin, 'r') as f:
                IPs = list(set(f.read().split()))
            THREAD = input_num(Fore.WHITE + 'Enter Your Thread [Max is 50]: ' + Fore.YELLOW)
            start_time = datetime.datetime.now()
            print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'W3LL_EMAILS.txt' + Fore.WHITE)
            
            p = Pool(THREAD, init_worker)
            a = 0
            for i in IPs:
                if a != THREAD:
                    cleango = p.apply_async(lompat365, args=(i, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            if os.path.exists(resume):
                os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'EMAIL VALIDATION HAS COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'W3LL_EMAILS365.txt' + Fore.WHITE)
            time.sleep(3)
    else:
        filelist()
        IPin = input_file()
        with open(IPin, 'r') as f:
            IPs = list(set(f.read().split()))
        THREAD = input_num(Fore.WHITE + 'Enter Your Thread [Max is 50]: ' + Fore.YELLOW)
        start_time = datetime.datetime.now()
        print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'W3LL_EMAILS365.txt' + Fore.WHITE)
        
        p = Pool(THREAD, init_worker)
        a = 0
        for i in IPs:
            if a != THREAD:
                cleango = p.apply_async(lompat365, args=(i, IPin, THREAD))
            else:
                a = 0
                time.sleep(THREAD)
        p.close()
        p.join()
        
        if os.path.exists(resume):
            os.remove('.session')
        end_time = datetime.datetime.now()
        long = end_time - start_time
        pot = str(long).split('.')
        print(Fore.WHITE + 'EMAIL VALIDATION HAS COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'W3LL_EMAILS365.txt' + Fore.WHITE)
        time.sleep(3)


def sortallcountry():
    """Sort Emails - Main function"""
    clearConsole()
    logo()
    print(Fore.WHITE + '[ ' + Fore.CYAN + 'SORT ALL EMAILS' + Fore.WHITE + ' ]')
    print('')
    
    if os.path.exists(resume):
        print('[' + Fore.YELLOW + '+' + Fore.WHITE + '] We Found A Session!')
        con = input('[' + Fore.YELLOW + '+' + Fore.WHITE + '] Do you want to continue session ? [y/n] ')
        
        if 'Y' in con or 'y' in con:
            IPin = config.get(token, 'list')
            fromlast = config.get(token, 'lastip')
            with open(IPin) as f:
                IPs = f.read().split(fromlast + '\n')[1].split()
            THREAD = int(config.get(token, 'thread'))
            start_time = datetime.datetime.now()
            print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'W3LL_EMAILS.txt' + Fore.WHITE)
            
            p = Pool(THREAD, init_worker)
            a = 0
            for i in IPs:
                if a != THREAD:
                    cleango = p.apply_async(sortall, args=(i, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            if os.path.exists(resume):
                os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'SORTING COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'W3LL_EMAILS.txt' + Fore.WHITE)
            time.sleep(3)
        else:
            filelist()
            IPin = input_file()
            with open(IPin, 'r') as f:
                IPs = list(set(f.read().split()))
            THREAD = input_num(Fore.WHITE + 'Enter Your Thread [Max is 50]: ' + Fore.YELLOW)
            start_time = datetime.datetime.now()
            print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'W3LL_EMAILS.txt' + Fore.WHITE)
            
            p = Pool(THREAD, init_worker)
            a = 0
            for i in IPs:
                if a != THREAD:
                    cleango = p.apply_async(sortall, args=(i, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            if os.path.exists(resume):
                os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'SORTING HAS COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'W3LL_EMAILS.txt' + Fore.WHITE)
            time.sleep(3)
    else:
        filelist()
        IPin = input_file()
        with open(IPin, 'r') as f:
            IPs = list(set(f.read().split()))
        THREAD = input_num(Fore.WHITE + 'Enter Your Thread [Max is 50]: ' + Fore.YELLOW)
        start_time = datetime.datetime.now()
        print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'W3LL_EMAILS.txt' + Fore.WHITE)
        
        p = Pool(THREAD, init_worker)
        a = 0
        for i in IPs:
            if a != THREAD:
                cleango = p.apply_async(sortall, args=(i, IPin, THREAD))
            else:
                a = 0
                time.sleep(THREAD)
        p.close()
        p.join()
        
        if os.path.exists(resume):
            os.remove('.session')
        end_time = datetime.datetime.now()
        long = end_time - start_time
        pot = str(long).split('.')
        print(Fore.WHITE + 'SORTING HAS COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'W3LL_EMAILS.txt' + Fore.WHITE)
        time.sleep(3)


def sortallcombos():
    """Sort Combos - Main function"""
    clearConsole()
    logo()
    print(Fore.WHITE + '[ ' + Fore.CYAN + 'SORT ALL COMBOS' + Fore.WHITE + ' ]')
    print('')
    
    if os.path.exists(resume):
        print('[' + Fore.YELLOW + '+' + Fore.WHITE + '] We Found A Session!')
        con = input('[' + Fore.YELLOW + '+' + Fore.WHITE + '] Do you want to continue session ? [y/n] ')
        
        if 'Y' in con or 'y' in con:
            IPin = config.get(token, 'list')
            fromlast = config.get(token, 'lastip')
            with open(IPin, 'r', encoding='utf-8') as f:
                IPs = f.read().split(fromlast + '\n')[1].split()
            THREAD = int(config.get(token, 'thread'))
            start_time = datetime.datetime.now()
            print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'result folder' + Fore.WHITE)
            
            p = Pool(THREAD, init_worker)
            a = 0
            for i in IPs:
                if a != THREAD:
                    cleango = p.apply_async(sortallcombo, args=(i, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            if os.path.exists(resume):
                os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'SORTING COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'result folder' + Fore.WHITE)
            time.sleep(3)
        else:
            filelist()
            IPin = input_file()
            with open(IPin, 'r', encoding='utf-8') as f:
                IPs = list(set(f.read().split()))
            THREAD = 1
            start_time = datetime.datetime.now()
            print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'result folder' + Fore.WHITE)
            
            p = Pool(THREAD, init_worker)
            a = 0
            for i in IPs:
                if a != THREAD:
                    cleango = p.apply_async(sortallcombo, args=(i, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            if os.path.exists(resume):
                os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'SORTING HAS COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'result folder' + Fore.WHITE)
            time.sleep(3)
    else:
        filelist()
        IPin = input_file()
        with open(IPin, 'r', encoding='utf-8') as f:
            IPs = list(set(f.read().split()))
        THREAD = 1
        start_time = datetime.datetime.now()
        print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'result folder' + Fore.WHITE)
        
        p = Pool(THREAD, init_worker)
        a = 0
        for i in IPs:
            if a != THREAD:
                cleango = p.apply_async(sortallcombo, args=(i, IPin, THREAD))
            else:
                a = 0
                time.sleep(THREAD)
        p.close()
        p.join()
        
        if os.path.exists(resume):
            os.remove('.session')
        end_time = datetime.datetime.now()
        long = end_time - start_time
        pot = str(long).split('.')
        print(Fore.WHITE + 'SORTING HAS COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'result folder' + Fore.WHITE)
        time.sleep(3)


def Check_token():
    if path.exists('token.txt') is False:
        print('Token is invalid')
        time.sleep(3)
        sys.exit(0)
    
    with open('token.txt', 'r') as f:
        token = f.readline()
    
    now = datetime.datetime.now()
    stamp = datetime.datetime.timestamp(now)
    timer = str(stamp).split('.')
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0'
        }
        params = (('token', token), ('time', timer[0]))
        tokres = requests.get('https://w3ll.store/api/rev-tok', headers=headers, params=params, timeout=60)
        return tokres
    except Exception:
        print('[' + Fore.YELLOW + '!' + Fore.WHITE + '] Server Is Not Connected!')
        sys.exit()


def cleaning():
    """Remove duplicates from text files"""
    if os.name in ('nt', 'dos'):
        clearConsole()
        logo()
        print(Fore.WHITE + '[ ' + Fore.CYAN + 'Cleaning duplicates ' + Fore.WHITE + ']')
        filelist()
        result = input(Fore.WHITE + 'Enter your result name: ' + Fore.YELLOW)
        files = input_file()
        
        with open(result, 'w', encoding='latin-1') as outfile:
            with open(files, 'r', encoding='latin-1') as infile:
                sorted_file = sorted(infile.readlines())
            for line, _ in itertools.groupby(sorted_file):
                outfile.write(line)
        
        with open(result, 'r') as source:
            data = [(random.random(), line) for line in source]
        
        data.sort()
        
        with open(result, 'w') as target:
            for _, line in data:
                target.write(line)
        
        os.remove(files)
        print(Fore.WHITE + 'Success deleting all duplicate domains and saved on ' + Fore.YELLOW + result + Fore.WHITE + '')
        time.sleep(3)
    else:
        with open('.tempnya', 'w+') as f:
            pass
        
        clearConsole()
        logo()
        print(Fore.WHITE + '[ ' + Fore.CYAN + 'Cleaning duplicates ' + Fore.WHITE + ']')
        filelist()
        result = input(Fore.WHITE + 'Enter your result name: ' + Fore.YELLOW)
        files = input_file()
        
        os.system('cat ' + files + ' | sort > .1')
        os.system('cat .1 | uniq > .tempnya')
        os.system('cat .tempnya | shuf > ' + result)
        os.remove('.1')
        os.remove('.tempnya')
        os.remove(files)
        
        print(Fore.WHITE + 'Success deleting all duplicate domains and saved on ' + Fore.YELLOW + result + Fore.WHITE + '')
        time.sleep(3)


def main():
    try:
        while True:
            menu()
            option = input(Fore.WHITE + 'Enter Your Option: ' + Fore.YELLOW)
            
            if int(option) == 1:
                lompatall()
            elif int(option) == 2:
                lompatall365()
            elif int(option) == 3:
                sortallcountry()
            elif int(option) == 4:
                sortallcombos()
            elif int(option) == 5:
                cleaning()
            else:
                print(Fore.WHITE + '[ ' + Fore.RED + 'Please enter a valid option ' + Fore.WHITE + ']')
                time.sleep(3)
    except KeyboardInterrupt:
        main()
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)


if __name__ == '__main__':
    freeze_support()
    #tokres = Check_token()
    #if 'DAYS LEFT' in tokres.text:
    main()
    #else:
    #    print(Fore.RED + 'YOUR TOKEN IS INVALID' + Fore.WHITE)
    #    time.sleep(3)