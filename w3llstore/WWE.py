import multiprocessing
import sys
import os
import time
import signal
import random
import re

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

from multiprocessing import Pool, freeze_support, active_children
from os import path
from multiprocessing.pool import INIT
import datetime

config = configparser.ConfigParser()
resume = '.session'
config.read(resume)

with open('token.txt') as f:
    lines = f.readlines()

if path.exists('token.txt') is False:
    print("[!] Recheck token.txt file then re run this tool.")
    sys.exit()

for tok in lines:
    if 'WWE' not in tok:
        print("[!] You cant use this token on this scanner! Recheck token.txt file then re run this tool.")
        sys.exit()

with open('token.txt', 'r') as f:
    token = f.readline().strip()


def logo():
    logo = f"""
{Fore.MAGENTA}$$\\      $$\\ $$\\      $$\\ $$$$$$$$\\ 
{Fore.MAGENTA}$$ | $\\  $$ |$$ | $\\  $$ |$$  _____|
{Fore.MAGENTA}$$ |$$$\\ $$ |$$ |$$$\\ $$ |$$ |      
{Fore.MAGENTA}$$ $$ $$\\$$ |$$ $$ $$\\$$ |$$$$$\\    
{Fore.MAGENTA}$$$$  _$$$$ |$$$$  _$$$$ |$$  __|   
{Fore.MAGENTA}$$$  / \\$$$ |$$$  / \\$$$ |$$ |      
{Fore.MAGENTA}$$  /   \\$$ |$$  /   \\$$ |$$$$$$$$\\ 
{Fore.MAGENTA}\\__/     \\__|\\__/     \\__|\\________|{Fore.WHITE} by {Fore.GREEN}W3LL.STORE\n"""
    for line in logo.split('\n'):
        print(line)
        time.sleep(0.15)


def menu():
    clearConsole()
    logo()
    print(Fore.WHITE)
    print(Fore.WHITE + '[' + Fore.CYAN + 'MENU' + Fore.WHITE + ']')
    print('')
    print('[' + Fore.YELLOW + '1' + Fore.WHITE + '] Xtract Only Business Emails')
    print('[' + Fore.YELLOW + '2' + Fore.WHITE + '] Xtract All Emails')
    print('[' + Fore.YELLOW + '3' + Fore.WHITE + '] Xtract Office365 Emails')
    print('[' + Fore.YELLOW + '4' + Fore.WHITE + '] Remove Duplicated Emails')
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


def allemail(IPs, IPin, THREAD):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        'Accept-Encoding': 'gzip, deflate'
    }
    
    if 'http' in IPs:
        response = requests.get(IPs, headers=headers, allow_redirects=True, timeout=3)
    else:
        response = requests.get('http://' + IPs + '/', headers=headers, allow_redirects=True, timeout=3)
    
    emails = re.findall(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', response.text)
    email = list(dict.fromkeys(emails))
    halo = ''
    
    # List of patterns to filter out invalid emails
    filters = [
        'godaddy.', '.png', '.gif', '.jpg', '.gov', '.sch', '.edu', '.svg', '.jpeg',
        'example', '.doc', 'font', '.xls', '.ico', '.html', '.htm', '.sch.', '.ac.',
        'email.', 'you', 'javascript', 'test', 'debug', 'drupal', 'collage', 'apache',
        'bootstrap', 'u003', 'wixpress.', 'wix.', 'domain', 'webp', 'sentry.', '.x',
        'site.', 'address.', 'whois.', 'aspx', '.asp', 'education', '.css', '.js'
    ]
    
    for emailval in email:
        is_filtered = False
        for f in filters:
            if f in emailval:
                is_filtered = True
                break
        
        if is_filtered or re.findall(r'^[-!$%^&*()_+|~=`{}\[\]\:;<>?,\.\/](\.*?)', emailval):
            print('[' + Fore.RED + '-' + Fore.WHITE + '] ' + IPs + Fore.YELLOW + ' > ' + Fore.RED + emailval + Fore.WHITE)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
        else:
            print('[' + Fore.GREEN + '+' + Fore.WHITE + '] ' + IPs + Fore.YELLOW + ' > ' + Fore.GREEN + emailval + Fore.WHITE)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            halo = halo + emailval + '\n'
    
    with open('W3LL_EMAILS.txt', 'a+') as save:
        save.write(halo)


def emailbusiness(IPs, IPin, THREAD):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        'Accept-Encoding': 'gzip, deflate'
    }
    
    if 'http' in IPs:
        response = requests.get(IPs, headers=headers, allow_redirects=True, timeout=3)
    else:
        response = requests.get('http://' + IPs + '/', headers=headers, allow_redirects=True, timeout=3)
    
    emails = re.findall(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', response.text)
    email = list(dict.fromkeys(emails))
    halo = ''
    
    # Filters for generic/common emails (personal email providers)
    filters = [
        'godaddy.', '.png', '.gif', '.jpg', '.gov', '.sch', '.edu', '.svg', '.jpeg',
        'example', '.doc', 'font', '.xls', '.ico', '.html', '.htm', '.sch.', '.ac.',
        'email.', 'you', 'javascript', 'test', 'debug', 'drupal', 'collage', 'apache',
        'bootstrap', 'u003', 'wixpress.', 'wix.', 'domain', 'webp', 'sentry.', '.x',
        'site.', 'address.', '126.', '163.', 'aol.', 'att.net', 'bellsouth.', 'comcast.',
        'earthlink.', 'gmail.', 'gmx.', 'hotmail.', 'live.', 'outlook.', 'icloud.',
        'mail.com', 'mail.ru', 'qq.', 'sbcglobal.', 't-online.', 'verizon.', 'yahoo.',
        'yandex.', 'msn.', 'whois.', 'google.', 'orange.', 'aspx', '.asp', 'contact',
        'contato', 'education', 'enquiries', 'enquiry', 'hello', 'info@', 'mail@',
        'marketing@', 'office@', 'webmaster@', 'booking', 'event', 'customercare@',
        'cs@', 'support', 'service', 'reservation', 'reception', 'question', 'privacy',
        'ontact', 'noreply', 'no-reply', 'inquiry', 'customer', 'client', '.css', '.js'
    ]
    
    for emailval in email:
        is_filtered = False
        for f in filters:
            if f in emailval:
                is_filtered = True
                break
        
        if is_filtered or re.findall(r'^[-!$%^&*()_+|~=`{}\[\]\:;<>?,\.\/](\.*?)', emailval):
            print('[' + Fore.RED + '-' + Fore.WHITE + '] ' + IPs + Fore.YELLOW + ' > ' + Fore.RED + emailval + Fore.WHITE)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
        else:
            print('[' + Fore.GREEN + '+' + Fore.WHITE + '] ' + IPs + Fore.YELLOW + ' > ' + Fore.GREEN + emailval + Fore.WHITE)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            halo = halo + emailval + '\n'
    
    with open('W3LL_EMAILS.txt', 'a+') as save:
        save.write(halo)


def emailbusiness365(IPs, IPin, THREAD):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        'Accept-Encoding': 'gzip, deflate'
    }
    
    if 'http' in IPs:
        response = requests.get(IPs, headers=headers, allow_redirects=True, timeout=3)
    else:
        response = requests.get('http://' + IPs + '/', headers=headers, allow_redirects=True, timeout=3)
    
    emails = re.findall(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', response.text)
    email = list(dict.fromkeys(emails))
    halo = ''
    
    # Filters for generic/common emails
    filters = [
        'godaddy.', '.png', '.gif', '.jpg', '.gov', '.sch', '.edu', '.svg', '.jpeg',
        'example', '.doc', 'font', '.xls', '.ico', '.html', '.htm', '.sch.', '.ac.',
        'email.', 'you', 'javascript', 'test', 'debug', 'drupal', 'collage', 'apache',
        'bootstrap', 'u003', 'wixpress.', 'wix.', 'domain', 'webp', 'sentry.', '.x',
        'site.', 'address.', '126.', '163.', 'aol.', 'att.net', 'bellsouth.', 'comcast.',
        'earthlink.', 'gmail.', 'gmx.', 'hotmail.', 'live.', 'outlook.', 'icloud.',
        'mail.com', 'mail.ru', 'qq.', 'sbcglobal.', 't-online.', 'verizon.', 'yahoo.',
        'yandex.', 'msn.', 'whois.', 'google.', 'orange.', 'aspx', '.asp', 'contact',
        'contato', 'education', 'enquiries', 'enquiry', 'hello', 'info@', 'mail@',
        'marketing@', 'office@', 'webmaster@', 'booking', 'event', 'customercare@',
        'cs@', 'support', 'service', 'reservation', 'reception', 'question', 'privacy',
        'ontact', 'noreply', 'no-reply', 'inquiry', 'customer', 'client', '.css', '.js'
    ]
    
    for emailval in email:
        is_filtered = False
        for f in filters:
            if f in emailval:
                is_filtered = True
                break
        
        if is_filtered or re.findall(r'^[-!$%^&*()_+|~=`{}\[\]\:;<>?,\.\/](\.*?)', emailval):
            print('[' + Fore.RED + '-' + Fore.WHITE + '] ' + IPs + Fore.YELLOW + ' > ' + Fore.RED + emailval + Fore.WHITE)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
        else:
            # Check if email is valid Office365 account
            headers365 = {
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55',
                'Content-type': 'application/json; charset=UTF-8'
            }
            params = (('mkt', 'en-US'),)
            data = f'{{"username":"{emailval}"}}'
            response365 = requests.post('https://login.microsoftonline.com/common/GetCredentialType', headers=headers365, params=params, data=data)
            
            if 'IfExistsResult":0' in response365.text and 'IsSignupDisallowed":true' in response365.text:
                print('[' + Fore.GREEN + '+' + Fore.WHITE + '] ' + IPs + Fore.YELLOW + ' > ' + Fore.GREEN + emailval + Fore.WHITE)
                config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
                write_file()
                halo = halo + emailval + '\n'
            else:
                print('[' + Fore.RED + '-' + Fore.WHITE + '] ' + IPs + Fore.YELLOW + ' > ' + Fore.RED + emailval + Fore.WHITE)
                config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
                write_file()
    
    with open('W3LL_EMAILS.txt', 'a+') as save:
        save.write(halo)


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


def wweall():
    clearConsole()
    logo()
    print(Fore.WHITE + '[ ' + Fore.CYAN + 'W3LL WEB EMAIL XTRACTOR' + Fore.WHITE + ' ]')
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
                    cleango = p.apply_async(allemail, args=(i, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'EXTRACTING COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'W3LL_EMAILS.txt' + Fore.WHITE)
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
                    cleango = p.apply_async(allemail, args=(i, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'EMAIL XTRACTOR HAS COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'W3LL_EMAILS.txt' + Fore.WHITE)
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
                cleango = p.apply_async(allemail, args=(i, IPin, THREAD))
            else:
                a = 0
                time.sleep(THREAD)
        p.close()
        p.join()
        
        os.remove('.session')
        end_time = datetime.datetime.now()
        long = end_time - start_time
        pot = str(long).split('.')
        print(Fore.WHITE + 'EMAIL XTRACTOR HAS COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'W3LL_EMAILS.txt' + Fore.WHITE)
        time.sleep(3)


def wwebusiness():
    clearConsole()
    logo()
    print(Fore.WHITE + '[ ' + Fore.CYAN + 'W3LL WEB EMAIL XTRACTOR' + Fore.WHITE + ' ]')
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
                    cleango = p.apply_async(emailbusiness, args=(i, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'EXTRACTING COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'W3LL_EMAILS.txt' + Fore.WHITE)
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
                    cleango = p.apply_async(emailbusiness, args=(i, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'EMAIL XTRACTOR HAS COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'W3LL_EMAILS.txt' + Fore.WHITE)
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
                cleango = p.apply_async(emailbusiness, args=(i, IPin, THREAD))
            else:
                a = 0
                time.sleep(THREAD)
        p.close()
        p.join()
        
        os.remove('.session')
        end_time = datetime.datetime.now()
        long = end_time - start_time
        pot = str(long).split('.')
        print(Fore.WHITE + 'EMAIL XTRACTOR HAS COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'W3LL_EMAILS.txt' + Fore.WHITE)
        time.sleep(3)


def wwebusiness365():
    clearConsole()
    logo()
    print(Fore.WHITE + '[ ' + Fore.CYAN + 'W3LL WEB EMAIL365 XTRACTOR' + Fore.WHITE + ' ]')
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
                    cleango = p.apply_async(emailbusiness365, args=(i, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'EXTRACTING COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'W3LL_EMAILS.txt' + Fore.WHITE)
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
                    cleango = p.apply_async(emailbusiness365, args=(i, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'EMAIL XTRACTOR HAS COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'W3LL_EMAILS.txt' + Fore.WHITE)
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
                cleango = p.apply_async(emailbusiness365, args=(i, IPin, THREAD))
            else:
                a = 0
                time.sleep(THREAD)
        p.close()
        p.join()
        
        os.remove('.session')
        end_time = datetime.datetime.now()
        long = end_time - start_time
        pot = str(long).split('.')
        print(Fore.WHITE + 'EMAIL XTRACTOR HAS COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'W3LL_EMAILS.txt' + Fore.WHITE)
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
                wwebusiness()
            elif int(option) == 2:
                wweall()
            elif int(option) == 3:
                wwebusiness365()
            elif int(option) == 4:
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