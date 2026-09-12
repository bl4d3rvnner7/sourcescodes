import sys
import os
import time
import signal
import re
import requests
import datetime
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore


def logo():
    logo = '\n{}$$$$$$$\\  $$$$$$$\\   $$$$$$\\   $$$$$$\\  $$$$$$$$\\ $$\\   $$\\ \n{}$$  __$$\\ $$  __$$\\ $$  __$$\\ $$  __$$\\ $$  _____|$$ | $$  |\n{}$$ |  $$ |$$ |  $$ |$$ /  $$ |$$ /  \\__|$$ |      $$ |$$  / \n{}$$$$$$$  |$$$$$$$  |$$ |  $$ |$$ |      $$$$$\\    $$$$$  /  \n{}$$  ____/ $$  __$$< $$ |  $$ |$$ |      $$  __|   $$  $$<   \n{}$$ |      $$ |  $$ |$$ |  $$ |$$ |  $$\\ $$ |      $$ |\\$$\\  \n{}$$ |      $$ |  $$ | $$$$$$  |\\$$$$$$  |$$$$$$$$\\ $$ | \\$$\\ \n{}\\__|      \\__|  \\__| \\______/  \\______/ \\________|\\__|  \\__|{} by {}W3LL.STORE\n'.format(Fore.MAGENTA,Fore.MAGENTA,Fore.MAGENTA,Fore.MAGENTA,Fore.MAGENTA,Fore.MAGENTA,Fore.MAGENTA,Fore.MAGENTA,Fore.WHITE,Fore.GREEN)
    for line in logo.split('\n'):
        print(line)
        time.sleep(0.15)
        
def menu():
    clearConsole()
    logo()
    print(Fore.WHITE + '[' + Fore.CYAN + 'MENU' + Fore.WHITE + ']')
    print('')
    print(Fore.WHITE + '[' + Fore.YELLOW + '1' + Fore.WHITE + '] Check Live Proxy')
    print(Fore.WHITE + '[' + Fore.YELLOW + '2' + Fore.WHITE + '] Scrape Proxy')
    print('')
    print(Fore.WHITE + '[' + Fore.YELLOW + 'CTRL + C' + Fore.WHITE + '] Go Back To This Menu')
    print('')

def input_num(word):
    try:
        thread = int(word)
    except ValueError:
        raise ValueError(Fore.YELLOW + "Please insert only a number value" + Fore.WHITE)
    if thread < 1 or thread > 50:
        raise ValueError(Fore.RED + "Insert number that  under " + Fore.YELLOW + "1" + Fore.RED + "and more than " +Fore.YELLOW + "50" + Fore.RED + ".")
    return thread
    
def filelist():
    arr = os.listdir()
    print('')
    print(Fore.YELLOW + 'All files' + Fore.WHITE + '/' + Fore.YELLOW + 'directory' + Fore.WHITE + ':')
    print('')
    for alldir in arr:
        print(Fore.CYAN + alldir + Fore.WHITE)
    print('')
    
def init_worker():
    signal.signal(signal.SIGINT,signal.SIG_IGN)
    
def validator(IPs):
    print(IPs)
    if not os.path.exists('results'):
        os.mkdir('result')
    try:
        proxies = {'http': 'socks5://' + IPs, 'https': 'socks5://'+ IPs}
        headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'en-US,en;q=0.8', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
        response = requests.get('https://ipwhois.app/json/',headers=headers, proxies=proxies,timeout=5)
        if 'ip' in response.text:
            country = re.findall('(?<="country":")[^"]*', response.text)[0]
            ip = re.findall('(?<="ip":")[^"]*', response.text)[0]
            print(Fore.WHITE + '[' + Fore.GREEN + 'SOCKS5' + Fore.WHITE + '] ' + ip + Fore.YELLOW + ' > ' + Fore.BLUE + country)
            with open('result/socks5.txt', 'a+') as save:
                save.write(IPs + '\n')
        else:
            print(Fore.WHITE + '[' + Fore.RED + 'DIE IP' + Fore.WHITE + ']' + IPs)
            with open('result/DIE.txt', 'a+') as save:
                save.write(IPs + '\n')
    except Exception as E:
        print(Fore.WHITE + '[' + Fore.RED + 'DIE IP' + Fore.WHITE + ']' + IPs + ' [SOCKS5] --> ' + str(E))
        pass
    try:
        proxies = {'http': 'socks4://' + IPs, 'https': 'socks4://'+ IPs}
        headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'en-US,en;q=0.8', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
        response = requests.get('https://ipwhois.app/json/',headers=headers, proxies=proxies,timeout=5)
        if 'ip' in response.text:
            country = re.findall('(?<="country":")[^"]*', response.text)[0]
            ip = re.findall('(?<="ip":")[^"]*', response.text)[0]
            print(Fore.WHITE + '[' + Fore.GREEN + 'SOCKS4' + Fore.WHITE + '] ' + ip + Fore.YELLOW + ' > ' + Fore.BLUE + country)
            with open('result/socks4.txt', 'a+') as save:
                save.write(IPs + '\n')
        else:
            print(Fore.WHITE + '[' + Fore.RED + 'DIE IP' + Fore.WHITE + ']' + IPs)
            with open('result/DIE.txt', 'a+') as save:
                save.write(IPs + '\n')
    except Exception as E:
        print(Fore.WHITE + '[' + Fore.RED + 'DIE IP' + Fore.WHITE + ']' + IPs + ' [SOCKS4] --> ' + str(E))
        pass
    try:
        proxies = {'http': 'http://' + IPs, 'https': 'http://'+ IPs}
        headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'en-US,en;q=0.8', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
        response = requests.get('https://ipwhois.app/json/',headers=headers, proxies=proxies,timeout=5)
        if 'ip' in response.text:
            country = re.findall('(?<="country":")[^"]*', response.text)[0]
            ip = re.findall('(?<="ip":")[^"]*', response.text)[0]
            print(Fore.WHITE + '[' + Fore.GREEN + 'HTTP' + Fore.WHITE + '] ' + ip + Fore.YELLOW + ' > ' + Fore.BLUE + country)
            with open('result/http.txt', 'a+') as save:
                save.write(IPs + '\n')
        else:
            print(Fore.WHITE + '[' + Fore.RED + 'DIE IP' + Fore.WHITE + ']' + IPs)
            with open('result/DIE.txt', 'a+') as save:
                save.write(IPs + '\n')
    except Exception as E:
        print(Fore.WHITE + '[' + Fore.RED + 'DIE IP' + Fore.WHITE + ']' + IPs + ' [HTTP] --> ' + str(E))
        pass
    try:
        proxies = {'http': 'https://' + IPs, 'https': 'https://'+ IPs}
        headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'en-US,en;q=0.8', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
        response = requests.get('https://ipwhois.app/json/',headers=headers, proxies=proxies,timeout=5)
        if 'ip' in response.text:
            country = re.findall('(?<="country":")[^"]*', response.text)[0]
            ip = re.findall('(?<="ip":")[^"]*', response.text)[0]
            print(Fore.WHITE + '[' + Fore.GREEN + 'HTTPS' + Fore.WHITE + '] ' + ip + Fore.YELLOW + ' > ' + Fore.BLUE + country)
            with open('result/https.txt', 'a+') as save:
                save.write(IPs + '\n')
        else:
            print(Fore.WHITE + '[' + Fore.RED + 'DIE IP' + Fore.WHITE + ']' + IPs)
            with open('result/DIE.txt', 'a+') as save:
                save.write(IPs + '\n')
    except Exception as E:
        print(Fore.WHITE + '[' + Fore.RED + 'DIE IP' + Fore.WHITE + ']' + IPs + ' [HTTPS] --> ' + str(E))
        pass
    

def gopro():
    try:
        start_time = datetime.datetime.now()
        proxies = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
            'TE': 'trailers'
        }

        response = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=all&country=all&ssl=all&anonymity=allt', headers=headers)
        proxies.extend(response.text.splitlines())

        response = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt', headers=headers)
        proxies.extend(response.text.splitlines())

        response = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt', headers=headers)
        proxies.extend(response.text.splitlines())

        response = requests.get('https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt', headers=headers)
        proxies.extend(response.text.splitlines())

        response = requests.get('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt', headers=headers)
        proxies.extend(response.text.splitlines())
        
        response = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt', headers=headers)
        proxies.extend(response.text.splitlines())

        params = {'type': 'socks4'}
        response = requests.get('https://www.proxy-list.download/api/v1/get', headers=headers, params=params)
        proxies.extend(response.text.splitlines())

        params = {'type': 'socks5'}
        response = requests.get('https://www.proxy-list.download/api/v1/get', headers=headers, params=params)
        proxies.extend(response.text.splitlines())
        
        response = requests.get('https://www.sslproxies.org/', headers=headers)
        regex = r'\d+\.\d+\.\d+\.\d+:\d{1,5}'
        proxy_list = re.findall(regex, response.text)
        proxies.extend(proxy_list)

        response = requests.get('https://free-proxy-list.net/uk-proxy.html', headers=headers)
        regex = r'\d+\.\d+\.\d+\.\d+:\d{1,5}'
        proxy_list = re.findall(regex, response.text)
        proxies.extend(proxy_list)

        params = {'type': 'http'}
        response = requests.get('https://www.proxy-list.download/api/v1/get', headers=headers, params=params)
        proxies.extend(response.text.splitlines())

        params = {'type': 'https'}
        response = requests.get('https://www.proxy-list.download/api/v1/get', headers=headers, params=params)
        proxies.extend(response.text.splitlines())
        
        response = requests.get('https://free-proxy-list.net/uk-proxy.html', headers=headers)
        regex = r'\d+\.\d+\.\d+\.\d+:\d{1,5}'
        proxy_list = re.findall(regex, response.text)
        proxies.extend(proxy_list)

        response = requests.get('https://free-proxy-list.net/anonymous-proxy.html', headers=headers)
        regex = r'\d+\.\d+\.\d+\.\d+:\d{1,5}'
        proxy_list = re.findall(regex, response.text)
        proxies.extend(proxy_list)
        
        response = requests.get('https://www.us-proxy.org/', headers=headers)
        regex = r'\d+\.\d+\.\d+\.\d+:\d{1,5}'
        proxy_list = re.findall(regex, response.text)
        proxies.extend(proxy_list)

        response = requests.get('https://spys.me/proxy.txt', headers=headers)
        regex = r'\d+\.\d+\.\d+\.\d+:\d{1,5}'
        proxy_list = re.findall(regex, response.text)
        proxies.extend(proxy_list)
        
        response = requests.get('https://www.socks-proxy.net/', headers=headers)
        regex = r'\d+\.\d+\.\d+\.\d+:\d{1,5}'
        proxy_list = re.findall(regex, response.text)
        proxies.extend(proxy_list)
        
        response = requests.get('https://free-proxy-list.net/', headers=headers)
        regex = r'\d+\.\d+\.\d+\.\d+:\d{1,5}'
        proxy_list = re.findall(regex, response.text)
        proxies.extend(proxy_list)
        print("")
        print(Fore.WHITE + '[' + Fore.YELLOW + '!' + Fore.WHITE + '] Removing Duplicates...')
        end_time = datetime.datetime.now()
        pot = (end_time - start_time).total_seconds()
        proxies = list(set([proxy for proxy in proxies if proxy is not None]))
        print("")
        savepro = open('proxy-gen.txt', 'a+')
        for proxy in proxies:
            savepro.write(proxy + '\n')
        savepro.close()
        print(Fore.WHITE + 'SCRAPED ' + Fore.GREEN + str(len(proxies)) + Fore.WHITE + ' PROXIES')
        print(Fore.WHITE + 'GENERATE PROXY HAS COMPLETED WITH ' + Fore.YELLOW + str(pot) + Fore.WHITE + ' TIME ELAPSED, ALL SAVED INSIDE ' + Fore.YELLOW + 'proxy-gen.txt' + Fore.WHITE)
        time.sleep(3)
    except Exception:
        print(Fore.WHITE + '[' + Fore.YELLOW + '!' + Fore.WHITE + '] Program Quiting!')
        sys.exit()
        
def clearConsole():
    cmd = 'clear'
    if os.name in ('nt', 'dos'):
        cmd = 'cls'
    os.system(cmd)
    
def runner():
    filelist()
    LIST = input(Fore.WHITE + 'Enter Your Proxy List(proxy-gen.txt): ' + Fore.YELLOW)
    if os.path.exists(LIST):
        IPS = open(LIST, 'r').read().splitlines()
        THREADS = input_num(int(input(Fore.WHITE + 'Enter Your Thread [Max is 50]: ' + Fore.YELLOW)))
        print('All result will inserted on ' + Fore.YELLOW + 'result' + Fore.WHITE + ' folder')
        with ThreadPoolExecutor(max_workers=THREADS) as executor:
            executor.map(validator, IPS)
    else:
        print(Fore.WHITE + '[' + Fore.RED + '!' + Fore.WHITE + '] This path does not exits : ' + Fore.RED + LIST + Fore.WHITE)
        time.sleep(5)
        sys.exit()
    
def main():
    menu()
    option = input(Fore.WHITE + 'Enter Your Option: ' + Fore.YELLOW)
    try:
        if option == "1":
            runner()
        elif option == "2":
            gopro()
        else:
            print(Fore.WHITE + '[' + Fore.RED + + 'Please enter a valid option ' + Fore.WHITE + ']')
            time.sleep(5)
            sys.exit()
    except Exception:
        print(Fore.WHITE + '[' + Fore.RED + + 'Please enter a valid option ' + Fore.WHITE + ']')
        time.sleep(5)
        sys.exit()
        
if __name__ == '__main__':
    main()