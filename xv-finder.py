import os
import requests
import urllib3
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style, Back, init

urllib3.disable_warnings()
init(autoreset=True)

def check_domain(domain, paths):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    for path in paths:
        url = f"{domain}{path}"
        try:
            response = requests.get(url, headers=headers, verify=False, timeout=10)
            keywords = [b'{Ninja-Shell}', b'drwxr-xr-x', b'drwxrwxrwx', b'-rw-r--r--', b'Backdoor Destroyer', b'Gel4y Mini Shell', b'Tiny File Manager', b'File manager', b'#0x2525', b'{Ninja-Shell}', b'./AlfaTeam', b'Mr.Combet', b'%PDF-0-1', b'nopebee7 [@] skullxploit', b'X0MB13', b'Gel4y Mini Shell', b'https://github.com/fluidicon.png', b'Madstore.sk! - Priv8 Sh3ll!']
            for keyword in keywords:
                if keyword in response.content:
                    print(f" - {domain} - {Fore.LIGHTGREEN_EX}{Style.DIM}{Style.BRIGHT}Vulnerable{Style.RESET_ALL}")
                    with open("Shells.txt", "a", encoding="latin-1") as samawi:
                        samawi.write(f"{url}\n")
                    break
            else:
                if b'"eval"' in response.content or b'"stat"' in response.content or b'"rrer","name"' in response.content or b"'eval'" in response.content or b'SeoOk' in response.content or b'"code":200400,"msg":"params decrypt fail' in response.content:
                    print(f" - {domain} - {Fore.LIGHTGREEN_EX}{Style.DIM}{Style.BRIGHT}Vulnerable{Style.RESET_ALL}")
                    with open("Shells.txt", "a", encoding="latin-1") as samawi:
                        samawi.write(f"{url}\n")
                    break
                else:
                    print(f" - {domain} - {Fore.LIGHTRED_EX}{Style.DIM}{Style.BRIGHT}Not Vulnerable {Style.RESET_ALL}")
        except Exception as e:
            print(f" - {domain} - {Fore.LIGHTRED_EX}{Style.DIM}{Style.BRIGHT}Not Vulnerable {Style.RESET_ALL}")

def main():
    file_path = input(f"{Fore.LIGHTMAGENTA_EX}{Style.DIM}{Style.BRIGHT}Enter the file path:{Style.RESET_ALL} ")
    domain_list = []
    with open(file_path, "r", encoding="latin-1") as file:
        for line in file:
            domain_list.append(line.strip())
    paths = ['/wp-ver.php', '/inc.php', '/inputs.php', '/atomlib.php', '/simple.php?p=2f686f6d652f7074317464616379696b39722f7075626c69635f68746d6c&tod=75706c6f6164', '/qindex.php', '/wp-atom.php', '/unlockindex.php', '/lockindex.php', '/csv.php', '/atomlib.php', '/nf_tracking.php', '/alfanew.php7', '/wp-info.php', '/inputs.php', '/cong.php', '/style.php', '/wp-commentin.php?pass=f0aab4595a024d626315fb786dce8282', '/x.php?action=768776e296b6f286f26796e2a72607e2972647', '/about.php?p=2f686f6d652f726164696f736b792f7075626c69635f68746d6c&tod=75706c6f6164', '/wp-2019.php', '/wp-includes/style.php', '/wp-content/uploads/style.php', '/wp-content/style.php', '/wp-admin/style.php', '/wp-includes/js/jquery/jquery.js', '/wp-includes/js/admin-bar.js', '/wp-admin/js/user-suggest.js', '/wp-includes/rest-api/fields/cache/simple.php?p=2f686f6d652f7074317464616379696b39722f7075626c69635f68746d6c&tod=75706c6f6164', '/ALFA_DATA/alfacgiapi/?p=2f686f6d652f7074317464616379696b39722f7075626c69635f68746d6c&tod=75706c6f6164', '/admin.php?p=2f686f6d652f7074317464616379696b39722f7075626c69635f68746d6c&tod=75706c6f6164', '/shell.php?p=2f686f6d652f7074317464616379696b39722f7075626c69635f68746d6c&tod=75706c6f6164', '/wp-includes/js/tinymce/plugins/image/index.php?p=2f686f6d652f7074317464616379696b39722f7075626c69635f68746d6c&tod=75706c6f6164', '/classwithtostring.php?p=2f686f6d652f7074317464616379696b39722f7075626c69635f68746d6c&tod=75706c6f6164', '/wp-includes/SimplePie/index.php?p=2f686f6d652f7074317464616379696b39722f7075626c69635f68746d6c&tod=75706c6f6164', '/chosen.php?p=2f686f6d652f7074317464616379696b39722f7075626c69635f68746d6c&tod=75706c6f6164', '/wp-content/uploads/index.php?p=2f686f6d652f7074317464616379696b39722f7075626c69635f68746d6c&tod=75706c6f6164', '/ninja.php?p=2f686f6d652f7074317464616379696b39722f7075626c69635f68746d6c&tod=75706c6f6164', '/link.php?p=2f686f6d652f7074317464616379696b39722f7075626c69635f68746d6c&tod=75706c6f6164', '/dropdown.php', '/atomlib.php', '/styple.php', '/style.php?upload', '/wp-2019.php', '/about.php?upload', '/admin.php?p=&upload', '/admin.php', '/content.php', '/repeater.php', '/wp-activate.php', '/install.php', '/wp-login.php', '/ws.php', '/radio.php', '/doc.php', '/as.php', '/shell.php', '/themes.php', '/wp.php', '/upfile.php', '/.Wp-back.phP', '/moon.php', '/wp-content/themes/finley/min.php', '/css.php', '/wp-admin/css/index.php', '/dropdown.php', '/yanzshell.php', '/.well-known/', '/.well-known/acme-challenge/', '/ALFA_DATA//ALFA_DATA/alfacgiapi/', '/css/', '/wp-admin/css/colors/', '/wp-admin/css/colors/blue/', '/wp-admin/network/', '/wp-content/ALFA_DATA/alfacgiapi/', '/wp-content/', '/wp-content/patior/', '/wp-content/plugins/', '/wp-content/plugins/wp-help/', '/wp-content/uploads/', '/wp-content/uploads/2023/', '/wp-includes/Requests/Text/', '/wp-includes/SimplePie/', '/about.php', '/radio.php', '/content.php', '/lock360.php', '/admin.php', '/wp-login.php', '/wp-content/themes/pridmag/db.php?u', '/wp-content/plugins/linkpreview/db.php?u', '/wp-content/plugins/seoplugins/db.php?u', '/wp-content/themes/gaukingo/db.php?u', '/wp-content/themes/seotheme/db.php?u', '/chosen.php?upload', '/db.php?u', '/wp-content/outcms.php?up', '/wp-content/plugins/db/uploader.php?uploader', '/wp-content/plugins/seoplugin/db.php?u', '/wp-content/plugins/virr/uploader.php?uploader', '/wp-content/themes/jobart/db.php?u', '/wp-content/themes/noriumportfolio/db.php?u', '/wp-content/themes/rishi/db.php?u', '/wp-content/themes/skatepark/db.php?u', '/wp-content/themes/workart/db.php?u', '/wp-content/themes/twenty/twenty.php', '/about.php', '/ws.php', '/wso112233.php', '/css.php', '/wp-login.php', '/.well-known/acme-challenge/cloud.php', '/wp-includes/wp-class.php', '/404.php', '/wso.php', '/radio.php', '/wp-load.php', '/wp-class.php', '/cloud.php', '/revision.php', '/wp-content/style-css.php', '/fw.php', '/wp-cron.php', '/wso-x569.php', '/wp-admin/user/cloud.php']

    check_domains_with_threads(domain_list, paths)

def check_domains_with_threads(domain_list, paths):
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(check_domain, domain, paths) for domain in domain_list]
        for future in as_completed(futures):
            future.result()

if __name__ == '__main__':
    main()

file_path = 'Shells.txt'
with open(file_path, 'r', encoding='latin-1') as file:
    number_of_domains = sum(1 for _ in file)
    print(f"{Fore.LIGHTGREEN_EX}{Style.DIM}{Style.BRIGHT}\n    Report: \n    \n    Number Of Shells : {Fore.LIGHTWHITE_EX}{Back.RED}{number_of_domains}{Style.RESET_ALL}\n    \n                         Enter To Exit\n    ")
    input()