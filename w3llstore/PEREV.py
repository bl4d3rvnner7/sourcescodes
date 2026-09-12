from __future__ import print_function
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
    import socket
except ImportError:
    print("[!] Please install module socket : pip3 install socket")
    sys.exit()

try:
    import random
except ImportError:
    print("[!] Please install module random : pip3 install random")
    sys.exit()

try:
    import struct
except ImportError:
    print("[!] Please install module struct : pip3 install struct")
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
    if 'PEREV' not in tok:
        print("[!] You cant use this token on this scanner! Recheck token.txt file then re run this tool.")
        sys.exit()

with open('token.txt', 'r') as f:
    token = f.readline().strip()


def logo():
    logo = f"""
{Fore.MAGENTA}$$$$$$$\\  $$$$$$$$\\ $$$$$$$\\  $$$$$$$$\\ $$\\    $$\\ 
{Fore.MAGENTA}$$  __$$\\ $$  _____|$$  __$$\\ $$  _____|$$ |   $$ |
{Fore.MAGENTA}$$ |  $$ |$$ |      $$ |  $$ |$$ |      $$ |   $$ |
{Fore.MAGENTA}$$$$$$$  |$$$$$\\    $$$$$$$  |$$$$$\\    \\$$\\  $$  |
{Fore.MAGENTA}$$  ____/ $$  __|   $$  __$$< $$  __|    \\$$\\$$  / 
{Fore.MAGENTA}$$ |      $$ |      $$ |  $$ |$$ |        \\$$$  /  
{Fore.MAGENTA}$$ |      $$$$$$$$\\ $$ |  $$ |$$$$$$$$\\    \\$  /   
{Fore.MAGENTA}\\__|      \\________|\\__|  \\__|\\________|    \\_/{Fore.WHITE} by {Fore.GREEN}W3LL.STORE\n"""
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


def menu():
    clearConsole()
    logo()
    print(Fore.WHITE)
    print(Fore.WHITE + '[' + Fore.CYAN + 'MENU' + Fore.WHITE + ']')
    print('')
    print('[' + Fore.YELLOW + '1' + Fore.WHITE + '] Reverse From File')
    print('[' + Fore.YELLOW + '2' + Fore.WHITE + '] Generate Ip')
    print('[' + Fore.YELLOW + '3' + Fore.WHITE + '] Convert Domain To IP')
    print('[' + Fore.YELLOW + '4' + Fore.WHITE + '] Check Active Domains')
    print('[' + Fore.YELLOW + '5' + Fore.WHITE + '] Check Ip Region')
    print('[' + Fore.YELLOW + '6' + Fore.WHITE + '] Cleaning Duplicates Txt')
    print('')
    print('[' + Fore.YELLOW + 'CTRL + C' + Fore.WHITE + '] Go Back To This Menu')
    print('')


def validate_ip(s):
    """Validate if a string is a valid IPv4 address"""
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


def con2ip(gen_array, gen, THREAD):
    """Convert domain to IP address"""
    try:
        domain2ip = socket.gethostbyname(gen_array)
        print(Fore.CYAN + str(gen_array) + Fore.WHITE + ' Convert To ' + Fore.GREEN + str(domain2ip) + Fore.WHITE)
        with open('UNCLEANED_IPS.txt', 'a+') as save:
            save.write(domain2ip + '\n')
        config['token'] = {'list': gen, 'thread': str(THREAD), 'lastip': gen_array}
        write_file()
    except KeyboardInterrupt:
        print('[' + Fore.YELLOW + '!' + Fore.WHITE + '] Program Quiting!')
        sys.exit()


def init_worker():
    signal.signal(signal.SIGINT, signal.SIG_IGN)


def is_registered(domain_name):
    """Check if a domain is registered/active"""
    try:
        resp = requests.get('http://' + domain_name)
        return resp.status_code == 200
    except:
        return False


def actdo(Domen, Domenin, THREAD):
    """Check active domain and save results"""
    try:
        halo = ''
        if is_registered(Domen) == False:
            print(Fore.RED + '[ BAD DOMAIN ] ' + Fore.WHITE + Domen)
            config['token'] = {'list': Domenin, 'thread': str(THREAD), 'lastip': Domen}
            write_file()
        else:
            print(Fore.GREEN + '[ GOOD DOMAIN ] ' + Fore.WHITE + Domen)
            halo = Domen + '\n'
            config['token'] = {'list': Domenin, 'thread': str(THREAD), 'lastip': Domen}
            write_file()
            with open('UNCLEANED_ACTIVE_DOMAINS.txt', 'a+') as save:
                save.write(halo)
    except KeyboardInterrupt:
        print('[' + Fore.YELLOW + '!' + Fore.WHITE + '] Program Quiting!')
        sys.exit()


def pro(IPs, IPin, THREAD):
    """Reverse IP to domains - calls external API"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0'
        }
        params = (('ip', IPs), ('token', token))
        response = requests.get('http://45.138.172.83/reverse.php', headers=headers, params=params)
        url = response.text.split()
        urls = list(dict.fromkeys(url))
        halo = ''
        for domains in urls:
            print(Fore.GREEN + '[+] ' + Fore.WHITE + IPs + Fore.CYAN + ' TO ' + Fore.WHITE + domains)
            config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
            write_file()
            halo = halo + domains + '\n'
        
        with open('UNCLEANED_DOMAINS.txt', 'r') as f:
            if domains in f.read():
                print(Fore.RED + '[-] ' + Fore.WHITE + domains + Fore.RED + ' Duplicated ' + Fore.WHITE)
            else:
                with open('UNCLEANED_DOMAINS.txt', 'a+') as save:
                    save.write(halo)
    except Exception:
        print('[' + Fore.YELLOW + '!' + Fore.WHITE + '] Server Is Not Connected!')
        sys.exit()
    except KeyboardInterrupt:
        print('[' + Fore.YELLOW + '!' + Fore.WHITE + '] Program Quiting!')
        sys.exit()


def ipregion(IPs, IPin, THREAD):
    """Get IP region/country information"""
    try:
        os.mkdir('result')
    except FileExistsError:
        pass
    
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
    }
    response = requests.get('https://ipwhois.app/json/' + IPs, headers=headers)
    region = re.findall(r'(?<="country_code":")[^"]*', response.text)
    country = re.findall(r'(?<="country":")[^"]*', response.text)
    
    if len(region[0]) > 1:
        print('[' + Fore.GREEN + region[0] + Fore.WHITE + '] ' + IPs)
        config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
        write_file()
        with open('result/' + country[0] + '.txt', 'a+') as save:
            save.write(IPs + '\n')
    else:
        print('[' + Fore.RED + 'UNKOWN' + Fore.WHITE + '] ' + IPs)
        config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
        write_file()
        with open('result/' + country[0] + '.txt', 'a+') as save:
            save.write(IPs + '\n')


def input_num(word):
    try:
        thread = int(input(word))
    except ValueError:
        print(Fore.YELLOW + 'Please insert only a number value' + Fore.WHITE)
        return input_num(word)
    
    if thread < 1 or thread > 10:
        print(Fore.RED + 'Insert number that not under ' + Fore.YELLOW + '1' + Fore.RED + ' and more than ' + Fore.YELLOW + '10' + Fore.RED + '.' + Fore.WHITE)
        return input_num(word)
    return thread


def input_num_domain2ip(word):
    try:
        thread = int(input(word))
    except ValueError:
        print(Fore.YELLOW + 'Please insert only a number value' + Fore.WHITE)
        return input_num_domain2ip(word)
    
    if thread < 1 or thread > 30:
        print(Fore.RED + 'Insert number that not under ' + Fore.YELLOW + '1' + Fore.RED + ' and more than ' + Fore.YELLOW + '30' + Fore.RED + '.' + Fore.WHITE)
        return input_num_domain2ip(word)
    return thread


def input_num_active(word):
    try:
        thread = int(input(word))
    except ValueError:
        print(Fore.YELLOW + 'Please insert only a number value' + Fore.WHITE)
        return input_num_active(word)
    
    if thread < 1 or thread > 50:
        print(Fore.RED + 'Insert number that not under ' + Fore.YELLOW + '1' + Fore.RED + ' and more than ' + Fore.YELLOW + '50' + Fore.RED + '.' + Fore.WHITE)
        return input_num_active(word)
    return thread


def genips(word):
    try:
        ipgen = int(input(word))
    except ValueError:
        print(Fore.YELLOW + 'Please insert only a number value' + Fore.WHITE)
        return genips(word)
    
    if ipgen < 1 or ipgen > 10000000:
        print(Fore.RED + 'Insert number that not under ' + Fore.YELLOW + '1' + Fore.RED + ' and more than ' + Fore.YELLOW + '10000000' + Fore.RED + '.' + Fore.WHITE)
        return genips(word)
    return ipgen


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


def reverse():
    """Reverse IP to Domains - Main function"""
    clearConsole()
    logo()
    print(Fore.WHITE + '[ ' + Fore.CYAN + 'Reversing IP to Domains' + Fore.WHITE + ' ]')
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
            print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'UNCLEANED_DOMAINS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates domain]')
            
            p = Pool(THREAD, init_worker)
            a = 0
            for i in IPs:
                if a != THREAD:
                    cleango = p.apply_async(pro, args=(i, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'REVERSE COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'UNCLEANED_DOMAINS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates domain]')
            time.sleep(3)
        else:
            filelist()
            IPin = input_file()
            with open(IPin, 'r') as f:
                IPs = list(dict.fromkeys(f.read().split()))
            THREAD = input_num(Fore.WHITE + 'Enter Your Thread [Max is 10]: ' + Fore.YELLOW)
            start_time = datetime.datetime.now()
            print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'UNCLEANED_DOMAINS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates domain]')
            
            p = Pool(THREAD, init_worker)
            a = 0
            for i in IPs:
                if a != THREAD:
                    cleango = p.apply_async(pro, args=(i, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'REVERSE COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'UNCLEANED_DOMAINS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates domain]')
            time.sleep(3)
    else:
        filelist()
        IPin = input_file()
        with open(IPin, 'r') as f:
            IPs = list(dict.fromkeys(f.read().split()))
        THREAD = input_num(Fore.WHITE + 'Enter Your Thread [Max is 10]: ' + Fore.YELLOW)
        start_time = datetime.datetime.now()
        print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'UNCLEANED_DOMAINS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates domain]')
        
        p = Pool(THREAD, init_worker)
        a = 0
        for i in IPs:
            if a != THREAD:
                cleango = p.apply_async(pro, args=(i, IPin, THREAD))
            else:
                a = 0
                time.sleep(THREAD)
        p.close()
        p.join()
        
        os.remove('.session')
        end_time = datetime.datetime.now()
        long = end_time - start_time
        pot = str(long).split('.')
        print(Fore.WHITE + 'REVERSE COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'UNCLEANED_DOMAINS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates domain]')
        time.sleep(3)


def domain2ip():
    """Convert Domain to IP - Main function"""
    clearConsole()
    logo()
    print(Fore.WHITE + '[ ' + Fore.CYAN + 'Domain to Ip' + Fore.WHITE + ' ]')
    print('')
    
    if os.path.exists(resume):
        print('[' + Fore.YELLOW + '+' + Fore.WHITE + '] We Found A Session!')
        con = input('[' + Fore.YELLOW + '+' + Fore.WHITE + '] Do you want to continue session ? [y/n] ')
        
        if 'Y' in con or 'y' in con:
            filelist()
            gen = config.get(token, 'list')
            fromlast = config.get(token, 'lastip')
            with open(gen) as f:
                gen_array = f.read().split(fromlast + '\n')[1].split()
            gen_array = list(set(gen_array))
            THREAD = int(config.get(token, 'thread'))
            start_time = datetime.datetime.now()
            print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'UNCLEANED_IPS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates ips]')
            
            p = Pool(THREAD, init_worker)
            a = 0
            for i in gen_array:
                if a != THREAD:
                    cleango = p.apply_async(con2ip, args=(i, gen, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'CONVERT COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'UNCLEANED_IPS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates ips]')
            time.sleep(3)
        else:
            filelist()
            gen = input_file()
            with open(gen, 'r') as f:
                gen_array = list(set(f.read().split()))
            THREAD = input_num_domain2ip(Fore.WHITE + 'Enter Your Thread [Max is 30]: ' + Fore.YELLOW)
            start_time = datetime.datetime.now()
            print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'UNCLEANED_IPS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates ips]')
            
            p = Pool(THREAD, init_worker)
            a = 0
            for i in gen_array:
                if a != THREAD:
                    cleango = p.apply_async(con2ip, args=(i, gen, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'CONVERT COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'UNCLEANED_IPS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates ips]')
            time.sleep(3)
    else:
        filelist()
        gen = input_file()
        with open(gen, 'r') as f:
            gen_array = list(set(f.read().split()))
        THREAD = input_num_domain2ip(Fore.WHITE + 'Enter Your Thread [Max is 30]: ' + Fore.YELLOW)
        start_time = datetime.datetime.now()
        print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'UNCLEANED_IPS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates ips]')
        
        p = Pool(THREAD, init_worker)
        a = 0
        for i in gen_array:
            if a != THREAD:
                cleango = p.apply_async(con2ip, args=(i, gen, THREAD))
            else:
                a = 0
                time.sleep(THREAD)
        p.close()
        p.join()
        
        os.remove('.session')
        end_time = datetime.datetime.now()
        long = end_time - start_time
        pot = str(long).split('.')
        print(Fore.WHITE + 'CONVERT COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'UNCLEANED_IPS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates ips]')
        time.sleep(3)


def active():
    """Check Active Domains - Main function"""
    clearConsole()
    logo()
    print(Fore.WHITE + '[ ' + Fore.CYAN + 'Check Active Domains' + Fore.WHITE + ' ]')
    print('')
    
    if os.path.exists(resume):
        print('[' + Fore.YELLOW + '+' + Fore.WHITE + '] We Found A Session!')
        con = input('[' + Fore.YELLOW + '+' + Fore.WHITE + '] Do you want to continue session ? [y/n] ')
        
        if 'Y' in con or 'y' in con:
            filelist()
            Domenin = config.get(token, 'list')
            fromlast = config.get(token, 'lastip')
            with open(Domenin) as f:
                Domen = f.read().split(fromlast + '\n')[1].split()
            Domen = list(set(Domen))
            THREAD = int(config.get(token, 'thread'))
            start_time = datetime.datetime.now()
            print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'UNCLEANED_ACTIVE_DOMAINS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates domain]')
            
            p = Pool(THREAD, init_worker)
            a = 0
            for i in Domen:
                if a != THREAD:
                    cleango = p.apply_async(actdo, args=(i, Domenin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'CHECK ACTIVE DOMAINS IS COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'UNCLEANED_ACTIVE_DOMAINS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates domain]')
            time.sleep(3)
        else:
            filelist()
            Domenin = input_file()
            with open(Domenin, 'r') as f:
                Domen = list(set(f.read().split()))
            THREAD = input_num_active(Fore.WHITE + 'Enter Your Thread [Max is 50]: ' + Fore.YELLOW)
            start_time = datetime.datetime.now()
            print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'UNCLEANED_ACTIVE_DOMAINS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates domain]')
            
            p = Pool(THREAD, init_worker)
            a = 0
            for i in Domen:
                if a != THREAD:
                    cleango = p.apply_async(actdo, args=(i, Domenin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'CHECK ACTIVE DOMAINS IS COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'UNCLEANED_ACTIVE_DOMAINS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates domain]')
            time.sleep(3)
    else:
        filelist()
        Domenin = input_file()
        with open(Domenin, 'r') as f:
            Domen = list(set(f.read().split()))
        THREAD = input_num_active(Fore.WHITE + 'Enter Your Thread [Max is 50]: ' + Fore.YELLOW)
        start_time = datetime.datetime.now()
        print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'UNCLEANED_ACTIVE_DOMAINS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates domain]')
        
        p = Pool(THREAD, init_worker)
        a = 0
        for i in Domen:
            if a != THREAD:
                cleango = p.apply_async(actdo, args=(i, Domenin, THREAD))
            else:
                a = 0
                time.sleep(THREAD)
        p.close()
        p.join()
        
        os.remove('.session')
        end_time = datetime.datetime.now()
        long = end_time - start_time
        pot = str(long).split('.')
        print(Fore.WHITE + 'CHECK ACTIVE DOMAINS IS COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'UNCLEANED_ACTIVE_DOMAINS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates domain]')
        time.sleep(3)


def ipregioncheck():
    """Check IP Region - Main function"""
    clearConsole()
    logo()
    print(Fore.WHITE + '[ ' + Fore.CYAN + 'Check IP Region' + Fore.WHITE + ' ]')
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
            print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'UNCLEANED_DOMAINS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates domain]')
            
            p = Pool(THREAD, init_worker)
            a = 0
            for i in IPs:
                if a != THREAD:
                    cleango = p.apply_async(ipregion, args=(i, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'REVERSE COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'UNCLEANED_DOMAINS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates domain]')
            time.sleep(3)
        else:
            filelist()
            IPin = input_file()
            with open(IPin, 'r') as f:
                IPs = list(dict.fromkeys(f.read().split()))
            THREAD = input_num_active(Fore.WHITE + 'Enter Your Thread [Max is 50]: ' + Fore.YELLOW)
            start_time = datetime.datetime.now()
            print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'UNCLEANED_DOMAINS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates domain]')
            
            p = Pool(THREAD, init_worker)
            a = 0
            for i in IPs:
                if a != THREAD:
                    cleango = p.apply_async(ipregion, args=(i, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'REVERSE COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'UNCLEANED_DOMAINS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates domain]')
            time.sleep(3)
    else:
        filelist()
        IPin = input_file()
        with open(IPin, 'r') as f:
            IPs = list(dict.fromkeys(f.read().split()))
        THREAD = input_num_active(Fore.WHITE + 'Enter Your Thread [Max is 50]: ' + Fore.YELLOW)
        start_time = datetime.datetime.now()
        print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'UNCLEANED_DOMAINS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates domain]')
        
        p = Pool(THREAD, init_worker)
        a = 0
        for i in IPs:
            if a != THREAD:
                cleango = p.apply_async(ipregion, args=(i, IPin, THREAD))
            else:
                a = 0
                time.sleep(THREAD)
        p.close()
        p.join()
        
        os.remove('.session')
        end_time = datetime.datetime.now()
        long = end_time - start_time
        pot = str(long).split('.')
        print(Fore.WHITE + 'REVERSE COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'UNCLEANED_DOMAINS.txt' + Fore.WHITE + ' [Use option 5 to Clean all duplicates domain]')
        time.sleep(3)


def ips():
    """Generate random IP addresses"""
    clearConsole()
    logo()
    print(Fore.WHITE + '[ ' + Fore.CYAN + 'Generate IPs' + Fore.WHITE + ' ]')
    filelist()
    result = input('Enter result filename: ' + Fore.YELLOW)
    gen = genips(Fore.WHITE + 'How much IPs you want to generate: ' + Fore.YELLOW)
    
    for x in range(int(gen)):
        ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xFFFFFFFF)))
        print(Fore.CYAN + 'Generate Ips > ' + Fore.WHITE + ip)
        with open(result, 'a+') as saveips:
            saveips.write(ip + '\n')
    
    print(Fore.WHITE + 'Generating ' + Fore.YELLOW + str(gen) + Fore.WHITE + ' IP is done! saved on ' + Fore.YELLOW + result + Fore.WHITE)
    time.sleep(3)
    main()


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
        
        with open(result, 'r') as fin:
            data = fin.read().splitlines(True)
        
        with open(result, 'w') as fout:
            fout.writelines(data[:40])
        
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
        with open('.shuf', 'w+') as f:
            pass
        
        clearConsole()
        logo()
        print(Fore.WHITE + '[ ' + Fore.CYAN + 'Cleaning duplicates ' + Fore.WHITE + ']')
        filelist()
        result = input(Fore.WHITE + 'Enter your result name: ' + Fore.YELLOW)
        files = input_file()
        
        os.system('cat ' + files + ' | sort > .1')
        os.system('cat .1 | uniq > .tempnya')
        os.system("sed '1,50d' .tempnya > .shuf")
        os.system('cat .shuf | shuf > ' + result)
        os.remove('.1')
        os.remove('.tempnya')
        os.remove('.shuf')
        os.remove(files)
        
        print(Fore.WHITE + 'Success deleting all duplicate domains and saved on ' + Fore.YELLOW + result + Fore.WHITE + '')
        time.sleep(3)


def main():
    try:
        while True:
            menu()
            option = input(Fore.WHITE + 'Enter Your Option: ' + Fore.YELLOW)
            
            if int(option) == 1:
                reverse()
            elif int(option) == 2:
                ips()
            elif int(option) == 3:
                domain2ip()
            elif int(option) == 4:
                active()
            elif int(option) == 5:
                ipregioncheck()
            elif int(option) == 6:
                cleaning()
            else:
                print(Fore.WHITE + '[ ' + Fore.RED + 'Please enter a valid option ' + Fore.WHITE + ']')
                time.sleep(3)
                main()
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