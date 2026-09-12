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
    import requests
except ImportError:
    print("[!] Please install module requests : pip3 install requests")
    sys.exit()

try:
    import phonenumbers
    from phonenumbers import carrier
except ImportError:
    print("[!] Please install module phonenumbers : pip3 install phonenumbers")
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
from phonenumbers import geocoder

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
    if 'WPV' not in tok:
        print("[!] You cant use this token on this scanner! Recheck token.txt file then re run this tool.")
        sys.exit()

with open('token.txt', 'r') as f:
    token = f.readline().strip()


def logo():
    logo = f"""
{Fore.MAGENTA}$$\\      $$\\ $$$$$$$\\  $$\\    $$\\ 
{Fore.MAGENTA}$$ | $\\  $$ |$$  __$$\\ $$ |   $$ |
{Fore.MAGENTA}$$ |$$$\\ $$ |$$ |  $$ |$$ |   $$ |
{Fore.MAGENTA}$$ $$ $$\\$$ |$$$$$$$  |\\$$\\  $$  |
{Fore.MAGENTA}$$$$  _$$$$ |$$  ____/  \\$$\\$$  / 
{Fore.MAGENTA}$$$  / \\$$$ |$$ |        \\$$$  /  
{Fore.MAGENTA}$$  /   \\$$ |$$ |         \\$  /   
{Fore.MAGENTA}\\__/     \\__|\\__|          \\_/{Fore.WHITE} by {Fore.GREEN}W3LL.STORE\n"""
    for line in logo.split('\n'):
        print(line)
        time.sleep(0.15)


def menu():
    clearConsole()
    logo()
    print(Fore.WHITE)
    print(Fore.WHITE + '[' + Fore.CYAN + 'MENU' + Fore.WHITE + ']')
    print('')
    print('[' + Fore.YELLOW + '1' + Fore.WHITE + '] Validate Phone Number & Sort By Carrier')
    print('[' + Fore.YELLOW + '2' + Fore.WHITE + '] Validate Phone Number & Sort By Country')
    print('[' + Fore.YELLOW + '3' + Fore.WHITE + '] Generate Random Phone Numbers')
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


def random_phone_num_generator():
    region = str(random.randint(1, 988))
    first = str(random.randint(100, 999))
    second = str(random.randint(1, 888)).zfill(3)
    last = str(random.randint(1, 9998)).zfill(4)
    
    # Avoid pattern numbers
    while last in ('1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888'):
        last = str(random.randint(1, 9998)).zfill(4)
    
    return f'+{region}{first}{second}{last}'


def init_worker():
    signal.signal(signal.SIGINT, signal.SIG_IGN)


def nums(IPs, IPin, THREAD):
    try:
        my_number = phonenumbers.parse(IPs)
        isvalid = phonenumbers.is_valid_number(my_number)
        location = geocoder.description_for_number(my_number, 'en')
        savednya = phonenumbers.region_code_for_number(my_number)
        kariranjg = carrier.name_for_number(my_number, 'en')
        halo = ''
        
        if location == '':
            location = 'UNKOWN'
        if kariranjg == '':
            kariranjg = 'UNKOWN'
        
        if isvalid:
            print('[' + Fore.GREEN + 'VALID' + Fore.WHITE + '] ' + IPs + ' [ Country: ' + Fore.YELLOW + location + Fore.WHITE + ' ] [ Carrier: ' + Fore.YELLOW + kariranjg + Fore.WHITE + ' ]')
            halo = IPs + '\n'
        else:
            print('[' + Fore.RED + 'INVALID' + Fore.WHITE + '] ' + IPs)
        
        with open(f'result/{kariranjg}.txt', 'a+') as save:
            save.write(halo)
        
        config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
        write_file()
    
    except KeyboardInterrupt:
        print('[' + Fore.YELLOW + '!' + Fore.WHITE + '] Program Quiting!')
        sys.exit()


def nomornya(IPs, IPin, THREAD):
    try:
        my_number = phonenumbers.parse(IPs)
        isvalid = phonenumbers.is_valid_number(my_number)
        location = geocoder.description_for_number(my_number, 'en')
        savednya = phonenumbers.region_code_for_number(my_number)
        kariranjg = carrier.name_for_number(my_number, 'en')
        halo = ''
        
        if location == '':
            location = 'UNKOWN'
        if kariranjg == '':
            kariranjg = 'UNKOWN'
        
        if isvalid:
            print('[' + Fore.GREEN + 'VALID' + Fore.WHITE + '] ' + IPs + ' [ Country: ' + Fore.YELLOW + location + Fore.WHITE + ' ] [ Carrier: ' + Fore.YELLOW + kariranjg + Fore.WHITE + ' ]')
            halo = IPs + '\n'
        else:
            print('[' + Fore.RED + 'INVALID' + Fore.WHITE + '] ' + IPs)
        
        with open(f'result/{savednya}.txt', 'a+') as save:
            save.write(halo)
        
        config['token'] = {'list': IPin, 'thread': str(THREAD), 'lastip': IPs}
        write_file()
    
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


def gennum(word):
    try:
        ipgen = int(input(word))
    except ValueError:
        print(Fore.YELLOW + 'Please insert only a number value' + Fore.WHITE)
        return gennum(word)
    
    if ipgen < 1 or ipgen > 10000000:
        print(Fore.RED + 'Insert number that not under ' + Fore.YELLOW + '1' + Fore.RED + ' and more than ' + Fore.YELLOW + '10000000' + Fore.RED + '.' + Fore.WHITE)
        return gennum(word)
    
    return ipgen


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def wpv():
    clearConsole()
    logo()
    print(Fore.WHITE + '[ ' + Fore.CYAN + 'W3LL PHONE VALIDATOR SORT BY CARRIER' + Fore.WHITE + ' ]')
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
            print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'result' + Fore.WHITE + ' FOLDER')
            
            p = Pool(THREAD, init_worker)
            a = 0
            for i in IPs:
                if a != THREAD:
                    cleango = p.apply_async(nums, args=(i, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            # Clean up empty files
            for root, dirs, files in os.walk(os.getcwd()):
                for name in files:
                    filename = os.path.join(root, name)
                    if os.stat(filename).st_size == 0:
                        os.remove(filename)
            
            os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'EXTRACTING COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'result' + Fore.WHITE + ' FOLDER')
            time.sleep(3)
        else:
            filelist()
            IPin = input_file()
            with open(IPin, 'r') as f:
                IPs = list(set(f.read().split()))
            THREAD = input_num(Fore.WHITE + 'Enter Your Thread [Max is 50]: ' + Fore.YELLOW)
            start_time = datetime.datetime.now()
            print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'result' + Fore.WHITE + ' FOLDER')
            
            p = Pool(THREAD, init_worker)
            a = 0
            for i in IPs:
                if a != THREAD:
                    cleango = p.apply_async(nums, args=(i, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            for root, dirs, files in os.walk(os.getcwd()):
                for name in files:
                    filename = os.path.join(root, name)
                    if os.stat(filename).st_size == 0:
                        os.remove(filename)
            
            os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'NUMBER VALIDATING HAS COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'result' + Fore.WHITE + ' FOLDER')
            time.sleep(3)
    else:
        filelist()
        IPin = input_file()
        with open(IPin, 'r') as f:
            IPs = list(set(f.read().split()))
        THREAD = input_num(Fore.WHITE + 'Enter Your Thread [Max is 50]: ' + Fore.YELLOW)
        start_time = datetime.datetime.now()
        print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'result' + Fore.WHITE + ' FOLDER')
        
        p = Pool(THREAD, init_worker)
        a = 0
        for i in IPs:
            if a != THREAD:
                cleango = p.apply_async(nums, args=(i, IPin, THREAD))
            else:
                a = 0
                time.sleep(THREAD)
        p.close()
        p.join()
        
        for root, dirs, files in os.walk(os.getcwd()):
            for name in files:
                filename = os.path.join(root, name)
                if os.stat(filename).st_size == 0:
                    os.remove(filename)
        
        os.remove('.session')
        end_time = datetime.datetime.now()
        long = end_time - start_time
        pot = str(long).split('.')
        print(Fore.WHITE + 'NUMBER VALIDATING HAS COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'result' + Fore.WHITE + ' FOLDER')
        time.sleep(3)


def wpvcon():
    clearConsole()
    logo()
    print(Fore.WHITE + '[ ' + Fore.CYAN + 'W3LL PHONE VALIDATOR SORT BY COUNTRY' + Fore.WHITE + ' ]')
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
            print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'result' + Fore.WHITE + ' FOLDER')
            
            p = Pool(THREAD, init_worker)
            a = 0
            for i in IPs:
                if a != THREAD:
                    cleango = p.apply_async(nomornya, args=(i, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            for root, dirs, files in os.walk(os.getcwd()):
                for name in files:
                    filename = os.path.join(root, name)
                    if os.stat(filename).st_size == 0:
                        os.remove(filename)
            
            os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'EXTRACTING COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'result' + Fore.WHITE + ' FOLDER')
            time.sleep(3)
        else:
            filelist()
            IPin = input_file()
            with open(IPin, 'r') as f:
                IPs = list(set(f.read().split()))
            THREAD = input_num(Fore.WHITE + 'Enter Your Thread [Max is 50]: ' + Fore.YELLOW)
            start_time = datetime.datetime.now()
            print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'result' + Fore.WHITE + ' FOLDER')
            
            p = Pool(THREAD, init_worker)
            a = 0
            for i in IPs:
                if a != THREAD:
                    cleango = p.apply_async(nomornya, args=(i, IPin, THREAD))
                else:
                    a = 0
                    time.sleep(THREAD)
            p.close()
            p.join()
            
            for root, dirs, files in os.walk(os.getcwd()):
                for name in files:
                    filename = os.path.join(root, name)
                    if os.stat(filename).st_size == 0:
                        os.remove(filename)
            
            os.remove('.session')
            end_time = datetime.datetime.now()
            long = end_time - start_time
            pot = str(long).split('.')
            print(Fore.WHITE + 'NUMBER VALIDATING HAS COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'result' + Fore.WHITE + ' FOLDER')
            time.sleep(3)
    else:
        filelist()
        IPin = input_file()
        with open(IPin, 'r') as f:
            IPs = list(set(f.read().split()))
        THREAD = input_num(Fore.WHITE + 'Enter Your Thread [Max is 50]: ' + Fore.YELLOW)
        start_time = datetime.datetime.now()
        print(Fore.WHITE + 'All result will inserted on ' + Fore.YELLOW + 'result' + Fore.WHITE + ' FOLDER')
        
        p = Pool(THREAD, init_worker)
        a = 0
        for i in IPs:
            if a != THREAD:
                cleango = p.apply_async(nomornya, args=(i, IPin, THREAD))
            else:
                a = 0
                time.sleep(THREAD)
        p.close()
        p.join()
        
        for root, dirs, files in os.walk(os.getcwd()):
            for name in files:
                filename = os.path.join(root, name)
                if os.stat(filename).st_size == 0:
                    os.remove(filename)
        
        os.remove('.session')
        end_time = datetime.datetime.now()
        long = end_time - start_time
        pot = str(long).split('.')
        print(Fore.WHITE + 'NUMBER VALIDATING HAS COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'result' + Fore.WHITE + ' FOLDER')
        time.sleep(3)


def randnum():
    clearConsole()
    logo()
    print(Fore.WHITE + '[ ' + Fore.CYAN + 'Generate Numbers' + Fore.WHITE + ' ]')
    filelist()
    start_time = datetime.datetime.now()
    result = input('Enter result filename: ' + Fore.YELLOW)
    gen = gennum(Fore.WHITE + 'How much IPs you want to generate: ' + Fore.YELLOW)
    
    for x in range(int(gen)):
        nums = random_phone_num_generator()
        print(Fore.CYAN + 'Generate Numbers > ' + Fore.WHITE + nums)
        with open(result, 'a+') as saveips:
            saveips.write(nums + '\n')
    
    end_time = datetime.datetime.now()
    long = end_time - start_time
    pot = str(long).split('.')
    print(Fore.WHITE + 'GENERATING NUMBER HAS COMPLETED! WITH ' + pot[0] + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + result + Fore.WHITE + ' FILE')
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


def main():
    try:
        while True:
            menu()
            option = input(Fore.WHITE + 'Enter Your Option: ' + Fore.YELLOW)
            
            if int(option) == 1:
                wpv()
            elif int(option) == 2:
                wpvcon()
            elif int(option) == 3:
                randnum()
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