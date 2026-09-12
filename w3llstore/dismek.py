import os
import json
import sys
import time
import threading
import random
import itertools
import re
from os import path
import datetime
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

# List of context templates for disclaimer generation
contexts = [
    'Sensitive business information is enclosed within.',
    'Proprietary data is included for your review.',
    'Confidential company details are discussed herein.',
    'Privileged client information is the subject of this correspondence.',
    'Enclosed data is for the sole attention of the addressee.',
    'The message holds private information, potentially subject to legal privilege.',
    'The attached document, meant only for the addressee, contains privileged content.',
    'Information only intended for the eyes of the recipient is present.',
    'Recipient-only access is granted to the protected data in this transmission.',
    'The enclosed message bears proprietary details exclusive to our firm.',
    'Confidential material herein is not to be disclosed or distributed without authorization.',
    'Strictly confidential information is presented, intended for the direct addressee.',
    'Notification: the message contains sensitive content to be kept private.',
    'Exclusively enclosed is information for the individual to whom it is addressed.',
    "The attached document is for the addressee's use and contains sensitive material.",
    'The following information is legally privileged and intended for the recipient specified.',
    'This transmission includes specific private information and should be read only by the intended recipient.',
    "Confidential material for the intended recipient's use is contained within this email.",
    "The sender's views are expressed in this message and may not reflect the company's position.",
    'Information from the company, potentially privileged or confidential, is detailed here.'
]

# Read token
with open('token.txt') as f:
    lines = f.readlines()

if path.exists('token.txt') is False:
    print(Fore.WHITE + '[' + Fore.YELLOW + '!' + Fore.WHITE + ']' + Fore.WHITE + ' Recheck ' + Fore.YELLOW + 'token.txt' + Fore.WHITE + ' file ' + Fore.WHITE + 'then re run this tool.')
    sys.exit()

for tok in lines:
    if 'DISMEK' not in tok:
        print(Fore.WHITE + '[' + Fore.YELLOW + '!' + Fore.WHITE + ']' + Fore.WHITE + ' You cant use this token on this scanner! Recheck ' + Fore.YELLOW + 'token.txt' + Fore.WHITE + ' file ' + Fore.WHITE + 'then re run this tool.')
        sys.exit()

with open('token.txt', 'r') as f:
    token = f.readline().strip()


def logo():
    logo = f"""
{Fore.MAGENTA}$$$$$$$\\  $$$$$$\\  $$$$$$\\  $$\\      $$\\ $$$$$$$$\\ $$\\   $$\\ 
{Fore.MAGENTA}$$  __$$\\ \\_$$  _|$$  __$$\\ $$$\\    $$$ |$$  _____|$$ | $$  |
{Fore.MAGENTA}$$ |  $$ |  $$ |  $$ /  \\__|$$$$\\  $$$$ |$$ |      $$ |$$  / 
{Fore.MAGENTA}$$ |  $$ |  $$ |  \\$$$$$$\\  $$\\$$\\$$ $$ |$$$$$\\    $$$$$  /  
{Fore.MAGENTA}$$ |  $$ |  $$ |   \\____$$\\ $$ \\$$$  $$ |$$  __|   $$  $$<   
{Fore.MAGENTA}$$ |  $$ |  $$ |  $$\\   $$ |$$ |\\$  /$$ |$$ |      $$ |\\$$\\  
{Fore.MAGENTA}$$$$$$$  |$$$$$$\\ \\$$$$$$  |$$ | \\_/ $$ |$$$$$$$$\\ $$ | \\$$\\ 
{Fore.MAGENTA}\\_______/ \\______| \\______/ \\__|     \\__|\\________|\\__|  \\__|{Fore.WHITE} by {Fore.GREEN}W3LL.STORE\n"""
    for line in logo.split('\n'):
        print(line)
        time.sleep(0.15)


def wait_for_keypress():
    """Wait for user to press any key before exiting"""
    if os.name == 'nt':
        sys.stdout.write('\n[' + Fore.YELLOW + '!' + Fore.WHITE + '] Press any key to exit . . . ')
        sys.stdout.flush()
        os.system('pause >nul')


def prompt_for_count():
    """Prompt user for number of disclaimers to generate (max 100)"""
    try:
        count = int(input('[' + Fore.YELLOW + '!' + Fore.WHITE + '] How many disclaimers do you want to make (max 100)? '))
        if 1 <= count <= 100:
            return count
        else:
            print('[' + Fore.RED + '!' + Fore.WHITE + '] Please enter a number between 1 and 100.' + Fore.WHITE)
            return prompt_for_count()
    except ValueError:
        print('[' + Fore.RED + '!' + Fore.WHITE + '] Invalid input. Please enter a number.' + Fore.WHITE)
        return prompt_for_count()


def worker(context, results):
    """Worker function that generates a disclaimer for a given context"""
    disclaimer = generate_disclaimer(context)
    results.append(disclaimer)


# Global flag for loading animation
loading = True


def animated_loading():
    """Display an animated loading spinner while generating disclaimers"""
    global loading
    if loading:
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if not loading:
                break
            sys.stdout.write('\r[' + Fore.YELLOW + c + Fore.WHITE + '] Generating disclaimers...')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\r[' + Fore.YELLOW + '!' + Fore.WHITE + '] Done!                           \n\n')
    else:
        sys.stdout.write('\r[' + Fore.YELLOW + '!' + Fore.WHITE + '] Done!                           \n\n')


def generate_disclaimer(context):
    """Generate a disclaimer using OpenAI GPT-3.5 API"""
    terms = ['DISCLAIMER', 'NOTICE', 'IMPORTANT', 'ATTENTION', 'CAUTION', 'ADVISORY']
    selected_term = random.choice(terms)
    selected_context = random.choice(contexts)
    
    disclaimer_template = f"""
    Use {selected_term} infront of the email disclaimer with the context - '{context}', the following points must be included:
    1. Intended recipient notice
    2. Confidentiality note
    3. Legal advice disclaimer (if applicable)
    4. Non-liability for errors or omissions
    Do not include any salutations like 'Dear recipient' or closings like 'Sincerely'.
    """
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + os.getenv('OPENAI_API_KEY', '')
    }
    
    json_data = {
        'model': 'gpt-3.5-turbo-instruct',
        'prompt': disclaimer_template,
        'max_tokens': 2900,
        'temperature': 0.9,
        'top_p': 1,
        'n': 1
    }
    
    response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=json_data)
    
    if response.status_code == 200:
        try:
            answer = response.json()['choices'][0]['text'].strip()
            formatted_answer = answer.replace('\n', ' ').strip()
            
            # Clean up the formatted answer
            formatted_answer = re.sub(r'[-*]{2,}', '-', formatted_answer)
            formatted_answer = re.sub(r'^[^\w]+', '', formatted_answer)
            formatted_answer = re.sub(r'\s{2,}', ' ', formatted_answer)
            
            return formatted_answer
        except KeyError:
            pass
    
    return None


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


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
        clearConsole()
        logo()
        print(Fore.WHITE + '[ ' + Fore.CYAN + 'W3LL DISCLAIMER MAKER' + Fore.WHITE + ' ]')
        print('')
        
        num_disclaimers = prompt_for_count()
        save_to_file = input('[' + Fore.YELLOW + '!' + Fore.WHITE + '] Do you want to save it to a text file [Y/N]? ').lower()
        
        global loading
        loading = True
        anim_thread = threading.Thread(target=animated_loading)
        anim_thread.start()
        
        threads = []
        results = []
        results_lock = threading.Lock()
        
        for i in range(num_disclaimers):
            context = random.choice(contexts)
            t = threading.Thread(target=worker, args=(context, results))
            t.start()
            threads.append(t)
        
        for t in threads:
            t.join()
        
        loading = False
        anim_thread.join()
        
        with results_lock:
            for disclaimer in results:
                if disclaimer is not None:
                    # Truncate long disclaimers for display
                    if len(disclaimer) > 100:
                        display_disclaimer = disclaimer[:100] + '...'
                    else:
                        display_disclaimer = disclaimer
                    
                    print('[' + Fore.GREEN + '+' + Fore.WHITE + '] ' + display_disclaimer + Fore.WHITE)
                    
                    if save_to_file == 'y':
                        with open('disclaimers.txt', 'a') as file:
                            file.write(disclaimer + '\n\n')
        
        wait_for_keypress()
        sys.exit(0)
    except KeyboardInterrupt:
        main()
    sys.exit(0)


if __name__ == '__main__':
    #tokres = Check_token()
    #if 'DAYS LEFT' in tokres.text:
    main()
    #else:
    #    print('[' + Fore.RED + '!' + Fore.WHITE + '] YOUR TOKEN IS INVALID' + Fore.WHITE)
    #    time.sleep(3)